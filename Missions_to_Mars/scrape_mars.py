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
    mars_data ={}

    # Visit mars.nasa.gov
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)

    # Scrape page into Soup
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Get the articles, title and paragraph
    articles = news_soup.find('ul', class_='item_list')
    news_title = articles.find_all('div', class_='content_title')[0].text
    news_p = articles.find_all('div', class_='article_teaser_body')[0].text



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
    df = pd.read_html(fact_url)[0]
    df.columns = ['description','value']
    df = df.set_index("description")
    html_table = df.to_html()

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
        hemisphere = result.find('div', class_="description")
        title = hemisphere.h3.text
        link = hemisphere.a['href']
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

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "hemisphere_images": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data