import scrapy
import json
class CompaniesSpider(scrapy.Spider):
    name = 'companies'
    code = ''
    start_urls = [
        'https://www.listcorp.com/_api/services/discovery/get-all-companies?offset=0&sortBy=market_capitalisation&descending=true&exchange=ASX&recentlyListedCompanies=false&etf=false'
    ]
    
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        data = response.json()
        companies = data.get('data', [])
        # with open('companies.json', 'w', encoding='utf-8') as f:
        #     json.dump(companies, f, ensure_ascii=False, indent=4)
        for company in companies:
            yield {
                'company_name': company.get('company_name', 'N/A'),
                'campany_link': company.get('url', 'N/A'),
            }
        print(len(companies))
    
    


