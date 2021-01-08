# Webscraping Hackathon

## Why Webscraping

Data is not always available in a wel organized database or a flat CSV file.
Somethimes the data is available only on a website. We can 'scrape' this
website to extract the data we want and put that in a database or file
ourselfs. If there is a lot of data or the data updates the data we want quite
often, a script to extract the data can be written.

## Packages

- `requests`: perform http requests that will return the raw html of a webpage
- `beautifulsoup4`: interpret the html and extract the information of interest
- `pandas`: dataframes are handy to work with

## Challenge

Scrape the website [modelzoo.co](https://modelzoo.co/) and create a dataframe
containing the information on all models. Visualize the distributions found in
the data and other interesting features.
