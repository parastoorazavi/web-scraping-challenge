# web-scraping-challenge

Web Scraping is a useful technique to extract large amounts of data from variety websites and saved them to a local file in your computer or to a database in table format. In this project, a web application is built that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## 📝 Table of Contents

- [About](#about)
- [Step 1 - Scraping](#scraping)
- [Step 2 - MongoDB and Flask Application](#flask_application)

## 🧐 About <a name = "about"></a>
Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


## ✂️ Step 1 - Scraping <a name = "scraping"></a>

**NASA Mars News:** <br>
- Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
- Assign the text to variables that you can reference later.

**JPL Mars Space Images - Featured Image:** <br>
-	Visit the url for JPL Featured Space Image here.
-	Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called "featured_image_url".
- Make sure to find the image url to the full size .jpg image.
- Make sure to save a complete url string for this image.

**Mars Facts:** <br>
- Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Use Pandas to convert the data to a HTML table string.

**Mars Hemispheres:** <br>
- Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
- You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
- Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys "img_url" and "title".
- Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## 💻 Step 2 - MongoDB and Flask Application. <a name = "flask_application"></a>

- Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
- Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
- Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
- Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


 
