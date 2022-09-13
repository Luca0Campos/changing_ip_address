import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

for driver in range(2):

    PROXY = '20.206.106.192:80'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument(f'--proxy-server={PROXY}')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options)
    driver.get('https://www.myip.com/')
    time.sleep(5)
    driver.close()

