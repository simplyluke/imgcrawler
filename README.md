# Usage

Install scrapy

`sudo pip install scrapy`

Modify imgcrawler/main_spider.py to use the websites you want to crawl.

Run the script with output as json (can be many other types of data, look at http://doc.scrapy.org/en/latest/topics/feed-exports.html)

`$ scrapy crawl main -o output.json -t json`
