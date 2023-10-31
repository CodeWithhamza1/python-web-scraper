import os
import csv
from flask import Flask, render_template, request, Response, send_file, jsonify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

app = Flask(__name__, static_url_path='/static')

app = Flask(__name__)

# List of proxies
proxies = [
    "http://144.126.212.251:3128",
    "http://125.212.192.238:8888",
    "http://64.225.4.17:10005",
    "http://191.243.46.162:43241",
    "http://101.231.64.89:8443",
    "http://103.9.206.186:10008",
    "http://136.243.37.28:8888",
    "http://109.107.177.89:3128",
    "http://27.79.56.106:10008"
]

# Custom headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.form.get("url")
    classes = request.form.get("classes")
    elements = request.form.get("elements")
    limit = int(request.form.get("limit", 10000))

    if not url:
        return jsonify({"error": "URL cannot be empty"})

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        scraped_data = set()  # Use a set to avoid duplicates

        if classes:
            for class_name in classes.split(","):
                class_elements = driver.find_elements(By.CLASS_NAME, class_name.strip())
                for element in class_elements:
                    if limit > 0 and len(scraped_data) >= limit:
                        break
                    scraped_data.add((class_name.strip(), element.text))

        if elements:
            for element_name in elements.split(","):
                element_elements = driver.find_elements(By.TAG_NAME, element_name.strip())
                for element in element_elements:
                    if limit > 0 and len(scraped_data) >= limit:
                        break
                    scraped_data.add((element_name.strip(), element.text))

        driver.quit()

        if not scraped_data:
            return jsonify({"error": "No elements or data found on the page"})

        scraped_data = list(scraped_data)  # Convert the set to a list for further processing

        return jsonify({"data": scraped_data})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    classes = request.args.get("classes")
    elements = request.args.get("elements")
    limit = int(request.args.get("limit", 0))

    if not url:
        return jsonify({"error": "URL cannot be empty"})

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        scraped_data = set()  # Use a set to avoid duplicates

        if classes:
            for class_name in classes.split(","):
                class_elements = driver.find_elements(By.CLASS_NAME, class_name.strip())
                for element in class_elements:
                    if limit > 0 and len(scraped_data) >= limit:
                        break
                    scraped_data.add((class_name.strip(), element.text))

        if elements:
            for element_name in elements.split(","):
                element_elements = driver.find_elements(By.TAG_NAME, element_name.strip())
                for element in element_elements:
                    if limit > 0 and len(scraped_data) >= limit:
                        break
                    scraped_data.add((element_name.strip(), element.text))

        driver.quit()

        if not scraped_data:
            return jsonify({"error": "No elements or data found on the page"})

        scraped_data = list(scraped_data)  # Convert the set to a list for further processing

        if len(scraped_data) > 0:
            # Create a DataFrame for advanced cleaning
            data = pd.DataFrame(scraped_data, columns=["Element/Class", "Scraped Text"])

            # Perform data cleaning and manipulation here (e.g., removing duplicates, further formatting)

            # Save the cleaned data to a CSV file
            csv_filename = "formatted_data.csv"
            data.to_csv(csv_filename, index=False)

            return send_file(csv_filename, as_attachment=True)
        else:
            return jsonify({"error": "No elements or data found on the page"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
