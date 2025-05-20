from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up headless Chrome
options = Options()
# options.add_argument("--headless")  # Optional: comment this out to see browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# URL to scrape
url = 'https://www.listcorp.com/asx/gmg/goodman-group'
driver.get(url)

# Wait for JavaScript to render (adjust as needed)
time.sleep(5)

# Get rendered HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(html)
# Example: Extract company name
company_name = soup.find('h1', class_="CompanyPage2CompanyPageHero__header-name")
print("Company Name:", company_name.text.strip() if company_name else "Not found")


#
table_div = soup.find('div', class_= "CompanyPage2CompanyPageReports__table")

# Close browser
driver.quit()
