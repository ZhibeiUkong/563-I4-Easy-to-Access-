import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO


def access_json_api():
    """
    Information structure: JSON
    Access technology: API connection over HTTP

    Pros:
    - Data is structured and easy to parse with Python.
    - API access can be automated and updated without manual downloads.

    Cons:
    - Requires internet access.
    - API limits, endpoint changes, or server errors may break the code.

    Run instruction:
    - No API key is required for this sample.
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

    Pros:
    - Useful when data is published as a webpage rather than an API.
    - Can extract tables or page text from existing public websites.

    Cons:
    - HTML structure may change and break the scraper.
    - Web scraping is less stable than using an official API.

    Run instruction:
    - Requires beautifulsoup4 and requests.
    """
    url = "https://en.wikipedia.org/wiki/Food_safety"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").get_text(strip=True)
    first_paragraph = soup.find("p").get_text(strip=True)

    print("\n--- HTML Sample: Wikipedia Food Safety Page ---")
    print("Title:", title)
    print("First paragraph sample:", first_paragraph[:300])


def access_local_csv():
    """
    Information structure: CSV
    Access technology: Manual file download/read locally

    Pros:
    - Simple and reliable after the file is downloaded.
    - Good for reproducible class projects because the local file does not change unexpectedly.

    Cons:
    - Manual download adds extra work.
    - Local files may become outdated if the original data source changes.

    Run instruction:
    - This sample creates a small local CSV automatically for easy testing.
    - In a real project, replace sample_food_data.csv with a manually downloaded CSV file.
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
