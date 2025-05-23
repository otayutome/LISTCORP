import scrapy
import json
class CompanyInfo(scrapy.Spider):
    name = 'companyinfo'
    code = "ASX:GMG"
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        api_article = "https://www.listcorp.com/_api/services/company/get-documents?code={self.code}&types=1"
        api_info = "https://www.listcorp.com/_api/services/company/get-related-links?code={self.code}"
        yield scrapy.Request(url=api_article,headers=headers, callback=self.parse_api_article)
        yield scrapy.Request(url=api_info,headers=headers, callback=self.parse_api_info)


    def parse_api_article(self, response):
        data = response.json()
        articles = data.get('data', [])
        # with open('companies.json', 'w', encoding='utf-8') as f:
        #     json.dump(companies, f, ensure_ascii=False, indent=4)
        for article in articles:
            yield {
                'article_title': article.get('article', []).get("title", 'N/A'),
                'article_url': article.get('article', []).get("url", 'N/A')
            }
        print(len(articles))
    
    def parse_api_info(self, response):
        data = response.json()
        companyInfos = data.get('data', [])
        # with open('companies.json', 'w', encoding='utf-8') as f:
        #     json.dump(companies, f, ensure_ascii=False, indent=4)
        for companyInfo in companyInfos:
            yield {
                'company_name': companyInfo.get('title', 'N/A'),
                'campany_link': companyInfo.get('url', 'N/A'),
            }
        print(len(companyInfos))


