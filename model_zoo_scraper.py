import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(style="darkgrid")

URL = "https://modelzoo.co/"


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome("./chromedriver", chrome_options=chrome_options)


def read_website(browser):
    browser.get(URL)
    time.sleep(10)
    return browser.page_source


def get_models(soup):
    return soup.find_all("a", {"class": "model-detail-div box-shadow w-100"})


def parse_span(model, class_name):
    span = model.find("span", {"class", class_name})
    if span and span.contents:
        span = span.contents
    return span


def get_stars(model):
    stars = parse_span(model, "model-stars")
    stars = int(stars[1]) if stars else 0
    return stars


def parse_models(models_html):
    data = {
        "name": [],
        "stars": [],
        "description": [],
        "framework": [],
        "categories": [],
    }

    for model in models_html:
        data["name"].append(model.find("h2", {"class", "title"}).string)
        data["stars"].append(get_stars(model))
        data["framework"].append(parse_span(model, "btn btn-primary nohover")[0])
        data["categories"].append(
            parse_span(model, "btn btn-category btn-category-detail nohover")
        )
        data["description"].append(model.find("p", {"class", "description"}).string)

    return pd.DataFrame(data=data)


def add_to_cats(x, cats):
    if x:
        cats += x


def plot_framework(df):
    sns.countplot(x="framework", data=df).set(title="Frameworks")
    plt.tight_layout()
    plt.savefig("plots/framework.png")
    plt.clf()


def plot_stars(df):
    sns.displot(data=df, x="stars", kind="kde").set(title="Star Distribution")
    plt.tight_layout()
    plt.savefig("plots/stars.png")
    plt.clf()


def plot_categories(df):
    cats = []
    df["categories"].apply(lambda x: add_to_cats(x, cats))
    cat_df = pd.DataFrame(data={"categories": cats})

    sns.countplot(data=cat_df, x="categories").set(title="Categories")
    plt.tight_layout()
    plt.savefig("plots/categories.png")
    plt.clf()


# Create browser
browser = get_browser()

# Read the website
html = read_website(browser)

# Create Soup
soup = BeautifulSoup(html, "lxml")

# Find models
models_html = get_models(soup)

# Create the dataset
df = parse_models(models_html)

# plots
plot_framework(df)
plot_stars(df)
plot_categories(df)
