import argparse, logging, textwrap, sys
from extract_postalcode import extract_postalcode
from submit_postalcode import populate_recommendation_postcode

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='location_scrape_main',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Location Scrape Utility
            a) Requires Valid The Netherlands Postal Code
            b) It Returns dictionary having postal code as key
            and values as:
            Dynamic URL generated containing recommendation
            List of all the Nearby Landmarks
            List of all the time required to reach those Landmarks
            List of all the nearby Destination/Lanes
            '''))

    requiredNamed = parser.add_argument_group('Required Named Argument.')
    requiredNamed.add_argument('-p', '--p', dest='postal_code',
                               help='Please enter Valid The Netherlands Postal Code',
                               nargs='+',
                               required=True)
    args = parser.parse_args()

    # Logger
    logger = logging.getLogger()
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')
    fileHandler = logging.FileHandler(filename='app.log', mode='w+')  # Relative Path
    fileHandler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    logger.info(f"The Netherlands Postal Code entered by user: {args.postal_code}")

    # Fetch all the Valid The Netherlands Postal Code
    postalcode_URL = "http://www.geonames.org/postalcode-search.html?q=&country=NL"
    postal_code = extract_postalcode(postalcode_URL)
    logger.debug(f"Valid The Netherlands Postal Code: {postal_code}")
    if postal_code is None:
        logger.warning(f"Failed to establish a connection from URL: {postalcode_URL}")
        logger.warning("Please try again..")
        sys.exit(1)

    # Validation check for the valid Netherlands postal Code
    for code in args.postal_code:
        if code not in postal_code:
            logger.error("Code %s is not valid The Netherlands Postal Code", code)
            logger.error(f"Exiting...")
            sys.exit(1)

    # Fetch recommendations populated for each postal code
    recommendation_results = []
    URL="https://www.postnl.nl/"
    for code in args.postal_code:
        recommendation_results.append(populate_recommendation_postcode(URL,code))

    logger.info("Results populated for Postal Codes: %s", args.postal_code)
    logger.info(recommendation_results)