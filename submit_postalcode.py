from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import exceptions
import logging,sys

logger = logging.getLogger(__name__)

def populate_recommendation_postcode(URL, postal_code):
    """
    URL: "https://www.postnl.nl/"
    postal_code: Valid The Netherlands Postal Code
    return: dictionary
    Function will search user provided Valid Code and fetches the recommendation from the dynamic URL.
    It returns dictionary with URL, List of Landmarks, List of time required to reach and List of destinations.
    """
    options = webdriver.ChromeOptions()

    # User-Agent
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')

    # Cookies
    cookie_var = 'Language=nl; ARRAffinity=c7ac3993c5f78615110fddbd6c5d75fb6506753c3ebddfa3b3be06389d9e4c10; bm_sz=70DE1575AA0B8BD399D7E94A025A6D4B~YAAQNDZ8aKtax5dzAQAA4sFXtAhAQ9m35pW5ACyU0OdrkxZGnYIvy6IuUD/H6Z8OplpScKWQ/UurTIz5MMBxDY0UjRhcefgqAaBZVYlgMf50YuQg725arL+izHf2C3ScGQ/0IQ+rGTXqdlFWmch4qjaRZG2XNdrZu6sYe3kzI87D+fSfjovn2Z64M0AaTUw=; ai_user=e7SA9|2020-08-03T12:42:17.343Z; _abck=961F6E999CD5BB584D677C78B1BC6644~0~YAAQNDZ8aK5ax5dzAQAAesdXtAQnf49oHdWd5Vk3a5ePTZXn+8m9eT+ekxQfg2WEkkC/VlteOH+JLi7Xphc2YrOZpoY95mKK47klubY9XTp6qtCeUCx3NVM5LJ/tzFVtf0AWrZqIINon9dpEsJ1YIm+Oy6BlhbXYhrMZk+adoJexJYZpp1HlJsTbRhP/Ppa9wEwddVVeFGzJjH31Un/33m+RJmKtIbneIhAFsi+be8QZ8MIyWhKzt/s8/t6iGNH9gwvySaawNLj87vzcoao2v06QGTBSbexhnvGGxMTvu+gvfNOEceN3B6p5tj5sCbyTGPOUoX3B~-1~-1~-1; ak_bmsc=2BACE3ABE0C2B35E6094F337A96A6AC8687C3634184D00001406285FB7B7BD5E~pl1qPUpc5qvILF/+ciq656tN9Ip0eVjehwtSvpnwZ8SIK+ptK6HPdAaAG1y8rw6QMSu5q40qiA5y4kcH2D6C8ZcxFEGLNdjEoXNzA9Z3UtwqBK2MFD55EON/N76MoKonkoII2c12zf2mc2LP8gbB2dgcZcev7vM9UEeRb2YZhssjgiDt8S4DzsUdbXyqQGvPdPXejjHTXc2lSdVYnKoa020ObH/FlA1+Ecm0aLoQUqqkoIPmspg9eB/b/BRim5yEChP37p9AO5+s86e4D21CS4pPYSVIDPZcBh2Ym/NGtqGIk=; bm_sv=F68B55FD55C77CDB81B141EADD0F7877~tMRLRJbuynsjr5zywNcuYI7cgS18jSPwCc3zLc/wj/y8y0QEUORZ0EbOBh5TJEzkoU2bPl0UDjDbtEouzMDJYwkPr5oT5loKbrYXWGFvud0v3VOakuSDulhiBeXDiJ3ZpDJsDTdUnVvbG/6RfpoQRbo+7+oKhD7/A88yOWQSQMs=; ai_user=e7SA9|2020-08-03T12:42:17.343Z; ai_session=vxpPF|1596458538316.915|1596458538316.915; CookiePermissionInfo=%7B%22LastModifiedDate%22%3A%22%5C%2FDate(1596458544537)%5C%2F%22%2C%22ExpirationDate%22%3A%22%5C%2FDate(1627994544537)%5C%2F%22%2C%22Allow%22%3Atrue%2C%22CategoryPermission%22%3A%5B%7B%22Category%22%3A%22Cat.8%22%2C%22Permission%22%3Atrue%7D%2C%7B%22Category%22%3A%22Cat.9%22%2C%22Permission%22%3Atrue%7D%2C%7B%22Category%22%3A%22Cat.10%22%2C%22Permission%22%3Atrue%7D%2C%7B%22Category%22%3A%22Cat.11%22%2C%22Permission%22%3Atrue%7D%2C%7B%22Category%22%3A%22Cat.12%22%2C%22Permission%22%3Atrue%7D%5D%7D; ai_session=vxpPF|1596458538316|1596458594096.67; Ely_vID=tscdb2wrworrtmm263vgb3x3reuedjwr; ely_cc_answ=%7B%22privacy-control-analytics%22%3A1%2C%22privacy-control-usabilla%22%3A1%2C%22default%22%3A1%2C%22privacy-control-rtb%22%3A1%7D; prevpages=Lzo6; elytis=157563%2C177570%2C152449; elytil=157379; _fbp=fb.1.1596458594882.255094481; _gcl_au=1.1.1397857157.1596458595; ABTasty=uid=938t54v7as4w3g87&fst=1596458545814&pst=-1&cst=1596458545814&ns=1&pvt=3&pvis=3&th=; ABTastySession=mrasn=&lp=https://www.postnl.nl/&sen=4'
    options.add_argument(f'cookie={cookie_var}')

    # Selenium Headless
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-logging')
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
    logger.debug("Starting Driverless Selenium driver session..")
    driver.get(URL)
    driver.maximize_window()
    WebDriverWait(driver, 10)

    # Accepting the cookie permission
    try:
        permission = "//div[@class='cookie__footer__content']//button[@id='grantPermissionButton']"
        driver.find_element_by_xpath(permission).click()
    except exceptions.NoSuchElementException as e:
        logger.error("Not able to locate cookie permission page")
        logger.error("Please try again..")
        sys.exit(1)

    # Selecting PostNl Point
    postnl_point = "//div[contains(@class,'location-tool')]//h2[@class='title']"
    wl_pnp = driver.find_element_by_xpath(postnl_point).click()

    # Input Postal Code
    post_code = "//form[contains(@class,'locationpicker-killerapp')]//span[@class='field']//input[@id='address']"
    we_pc = driver.find_element_by_xpath(post_code)
    driver.execute_script("arguments[0].value='" + postal_code + "';", we_pc)

    # Clicking Search Button
    search = "//form[contains(@class,'locationpicker-killerapp')]//div[contains(@class,'submit-buttons')]//button[@class='button']"
    driver.find_element_by_xpath(search).click()
    driver.refresh()
    driver.refresh()
    WebDriverWait(driver, 60)

    # Fetching the Dynamic URl after recommendation populated
    dynamic_URL = driver.current_url
    logger.debug(
        "Dynamic URL %s generated for postal code %s after populating the recommendations.", dynamic_URL,postal_code)

    results = {}
    landmarks, times, destinations = [], [], []

    # Landmarks
    we_lm = driver.find_elements_by_xpath(
        "//app-results//div[contains(@class,'lp-list--interactive')]//div[contains(@class,'lp-list-item-body')]//strong")
    for landmark in we_lm:
        landmarks.append(landmark.text)
    logger.debug("Landmarks populated %s", landmarks)
    logger.debug("Total Landmarks %s", len(landmarks))

    # Time required to reach the Destination
    we_times = driver.find_elements_by_xpath(
        "//app-results//div[contains(@class,'lp-list--interactive')]//div[contains(@class,'lp-list-item-body')]//span[contains(@class,'text-muted')]")
    for time in we_times:
        times.append(time.text)

    logger.debug("Time required to reach the destination %s", times)
    logger.debug("Total List of times %s", len(times))

    # Destinations
    we_des = driver.find_elements_by_xpath("//app-results//div[contains(@class,'lp-list--interactive')]//div[contains(@class,'lp-list-item-body')]//span[@class='d-block']")
    for destination in we_des:
        destinations.append(destination.text)
    logger.debug("Destinations populated %s", destinations)
    logger.debug("Total Destinations %s", len(destinations))

    results = {
        'url': dynamic_URL,
        'landmark': landmarks,
        'time': times,
        'destination': destinations
    }

    return results
