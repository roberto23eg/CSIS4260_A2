https://roberto23eg-csis4260-a2-app-sn7u1f.streamlit.app

# CSIS 4260 - Special Topics in Data Analytics

### Assignment 2 - Learning web scrapping and text analysis

## Name: Roberto Escalante Gafau

## ID: 300383075

> Included are the csv files with the results of the test comparison between BeautifulSoup and Playwright. There is also the csv file with the 100 articles scraped and the csv file with the summary and sentiment analysis for those 100 articles.

### Part 1: Web Scraping

I choose to scrape the articles from `https://apnews.com/`.
After the test with BeautifulSoup and Playwright I noticed that I can scrape the articles using just BeautifulSoup, meaning that the website is fully compatible with this tool and not needed to deep in dynamic websites.
For my case I found BeautifulSoup more efficient and easier to use, with this tool I didn't need to launch a browser. Also the test results for BeautifulSoup are articles more clear than the ones with Playwright.

### Part 2: Text Analysis

For the second part I used nltk for the sentiment analysis and transformers for the summarization. I choosed those tools because they seem easier to use and gave me good results, also they work well with news.
