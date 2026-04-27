import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for package in ["requests", "pandas", "beautifulsoup4"]:
    install(package)

import requests
import pandas as pd
from bs4 import BeautifulSoup


def access_json_api():
    """
    Information structure: JSON
    Access technology: API connection over HTTP

    Pros: Structured, easy to parse, and can be updated automatically.
    Cons: Requires internet access and may fail if the API changes or has limits.
    """
    url = "https://api.fda.gov/food/enforcement.json?limit=3"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("\n--- JSON API Sample: openFDA Food Enforcement ---")
    for item in data["results"]:
        print({
            "product_description": item.get("product_description"),
            "reason_for_recall": item.get("reason_for_recall"),
            "recalling_firm": item.get("recalling_firm")
        })


def access_html_over_http():
    """
    Information structure: HTML
    Access technology: Code library reads HTML over HTTP

    Pros: Useful for extracting data from public webpages.
    Cons: Less stable than APIs because webpage structure may change.
    """
    url = "https://en.wikipedia.org/wiki/Food_safety"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").get_text(strip=True)
    paragraph = soup.find("p").get_text(strip=True)

    print("\n--- HTML Sample: Wikipedia Food Safety Page ---")
    print("Title:", title)
    print("First paragraph sample:", paragraph[:300])


def access_local_csv():
    """
    Information structure: CSV
    Access technology: Manual/local file download and read locally

    Pros: Simple, stable, and easy to reproduce.
    Cons: Manual files can become outdated and require extra download steps.
    """
    csv_data = """food_id,food_name,category,safety_status
1,Apple,Fruit,Safe
2,Chicken Breast,Meat,Needs Temperature Control
3,Spinach,Vegetable,Wash Before Eating
"""

    file_name = "sample_food_data.csv"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(csv_data)

    df = pd.read_csv(file_name)

    print("\n--- Local CSV Sample ---")
    print(df.head())


def main():
    access_json_api()
    access_html_over_http()
    access_local_csv()


if __name__ == "__main__":
    main()
