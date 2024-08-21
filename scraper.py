import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import schedule
import time
import sqlite3

def run_scraper():
    url = 'https://techcrunch.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('h2', 
                         class_ ="has-link-color wp-block-post-title has-h-5-font-size wp-elements-565fa7bab0152bfdca0217543865c205"
                         )


    data = []

    for article in articles:
        a_tag = article.find('a')
        if a_tag:
            title = a_tag.get_text(strip = True)
            link = a_tag['href']
            data.append({'Title': title, 'Link': link})
    

    conn = sqlite3.connect('scraped_data.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS articles
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT UNIQUE,
              link TEXT UNIQUE) ''')
    
    for title, link in data:
        try:
            c.execute("INSERT INTO articles (title, link) VALUES (?,?)", (title, link))
        except sqlite3.IntegrityError:
            print(f"Duplicate found: {title}")

    conn.commit()

    conn.close()


    print('Scraping completed and data saved to database.')
    
    df = pd.DataFrame(data)
    df.to_csv('scraped_data.csv', index = False)

    print('Data successfully scraped and added to csv')

def schedule_scraper():
    schedule.every().day.at("09:00").do(run_scraper)


    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    print('Starting scraper with automation')
    schedule_scraper()
