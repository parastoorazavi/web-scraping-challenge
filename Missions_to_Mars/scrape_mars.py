from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_dict ={}

    # Visit mars.nasa.gov
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)

    # Scrape page into Soup
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Get the articles, title and paragraph
    articles = news_soup.find_all('ul', class_='item_list')
    for article in articles:
        news_title = article.find('div', class_='content_title').text
        news_p = article.find('div', class_='article_teaser_body').text



    # Visit jpl.nasa.gov
    main_jpl_url = 'https://www.jpl.nasa.gov'
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    # Scrape page into Soup
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    # Get the featured Image
    image = image_soup.find_all('img')[3]['src']
    featured_image_url = main_jpl_url + image



    # Visit space-facts.com
    fact_url = 'https://space-facts.com/mars/'

    # Scrape page to get table
    tables = pd.read_html(fact_url)
    df = tables[0]
    df.columns = ['description','value']
    df = df.set_index("description")
    html_table = df.to_html()
    html_table.replace('\n', '')


    # Visit astrogeology.usgs.gov
    main_hemisphere_url = 'https://astrogeology.usgs.gov'
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
    browser.visit(hemisphere_url)

    # Scrape page into Soup
    html = browser.html
    hemisphere_soup = BeautifulSoup(html, 'html.parser')


    # Get the featured Image
    results = hemisphere_soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    for result in results:
        title = result.find('div', class_="description").h3.text
        link = result.find('div', class_="description").a['href']
        browser.visit(main_hemisphere_url+link)
        html = browser.html
        hemisphere_image_soup = BeautifulSoup(html, 'html.parser')
        new_results = hemisphere_image_soup.find('div', class_='downloads')
        img_url = new_results.find('li').a['href']

        # Store data in a dictionary
        img_dict = {}
        img_dict['title'] = title
        img_dict['img_url'] = img_url
        hemisphere_image_urls.append(img_dict)

    # Close the browser after scraping
    browser.quit()

    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": str(html_table),
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Return results
    return mars_dict