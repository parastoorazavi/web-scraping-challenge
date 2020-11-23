# web-scraping-challenge

Web Scraping is a useful technique to extract large amounts of data from variety websites and saved them to a local file in your computer or to a database in table format. In this project, a web application is built that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## 📝 Table of Contents

- [About](#about)
- [Step 1 - Scraping](#scraping)
- [Step 2 - MongoDB and Flask Application](#flask_application)

## 🧐 About <a name = "about"></a>
There are some plots of Latitude - Latitude Analysis which in this project they are going to use in building of visualization dashboard website. For this project we are donig:
1.	Create a website with 7 pages for different devices.
2.	Create a table in html.
3.	Deploy the website to GitHub pages.


## 🏁 Step 1 - Scraping <a name = "scraping"></a>

**Landing page:** <br>
- An explanation of the project.
- Links to each visualizations page. There should be a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.

**Four visualization pages:** <br>
-	A descriptive title and heading tag. 
-	The plot/visualization itself for the selected comparison.
- A paragraph describing the plot and its significance.

**Comparisons page:** <br>
- Contains all of the visualizations on the same page so we can easily visually compare them.
- Uses a Bootstrap grid for the visualizations.
- The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.

**Data page:** <br>
- Displays a responsive table containing the data used in the visualizations.
- The table must be a bootstrap table component.
- The data must come from exporting the .csv file as HTML, or converting it to HTML.

## :doughnut:Step 2 - MongoDB and Flask Application. <a name = "flask_application"></a>

- The website must, at the top of every page, have a navigation menu.
- Has the name of the site on the left of the nav which allows users to return to the landing page from any page.
- Contains a dropdown menu on the right of the navbar named "Plots" that provides a link to each individual visualization page.
- Provides two more text links on the right: "Comparisons," which links to the comparisons page, and "Data," which links to the data page.
- Is responsive (using media queries). The nav must have similar behavior as the screenshots "Navigation Menu" section (notice the background color change).

- Finally, the website must be deployed to GitHub pages.

 
