# Webscraping Hackathon

## Why Webscraping

Data is not always available in a well organized database or a flat CSV file.
Somethimes the data is available only on a website. We can 'scrape' this
website to extract the data we want and put that in a database or file
ourselfs. If there is a lot of data or the data is updated quite often, a
script to extract the data can be written.

## Packages

- `requests`: perform http requests that will return the raw html of a webpage
- `beautifulsoup4`: interpret the html and extract the information of interest
- `pandas`: dataframes are handy to work with
- `lxml`: library that allows pandas to interpret an html table

## Challenge

Scrape the website [modelzoo.co](https://modelzoo.co/) and create a dataframe
containing the information on all models. Visualize the distributions found in
the data and other interesting features.

## Running the examples

First install the required packages:

```
pip install -r requirements.txt
```

To run the exampels we run our own website:

```
cd tst_html
python -m http.server
```

Then run each example:

```
python examples/01_get_html.py
```
