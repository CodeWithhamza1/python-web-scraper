# Web Scraping with ♥️ Flask

The tool you've been working on is a web scraping application built using Flask, Selenium, and BeautifulSoup. It allows users to input a URL, specify HTML elements (tags) and/or CSS classes to scrape, and set a limit on the number of results to retrieve. After scraping, the application can format the data and offer it for download in CSV format.

## Features

Here's a breakdown of the main components and features of this web scraping tool:

1. **Flask Web Application**: The tool is implemented as a web application using Flask, a popular Python web framework. Flask provides a simple way to create a web interface and handle user interactions.

2. **Selenium WebDriver**: Selenium is used for web automation and browser control. The tool employs the Selenium WebDriver to load and interact with web pages, allowing it to dynamically fetch content from websites. The tool can navigate web pages and locate HTML elements using both class names and tag names specified by the user.

3. **BeautifulSoup**: BeautifulSoup is used for parsing and extracting information from HTML and XML documents. The tool utilizes BeautifulSoup to extract text from HTML elements found on web pages.

4. **Scraping Options**: Users can specify the URL of the web page they want to scrape. They can also provide a list of HTML elements (e.g., div, span) and CSS class names to target specific content. A limit option allows users to control how many results they want to scrape.

5. **Data Cleaning**: The application can clean and format the scraped data. While the tool doesn't perform complex data cleaning, it provides a foundation for further data manipulation.

6. **CSV Export**: Once the data is scraped, the tool can export it to a CSV file. This CSV file can be downloaded by the user for further analysis or storage.

7. **Error Handling**: The tool has built-in error handling to manage various scenarios, such as invalid URLs, scraping failures, or situations where no data is found. Users receive informative error messages.

8. **User Interface (HTML)**: The front end of the tool is created with HTML and Bootstrap. Users can enter the URL, specify elements and classes, set a limit, and initiate the scraping process. Progress is displayed with a loading bar.

9. **Content Limitations**: Due to web page content restrictions, some websites may not be accessible for scraping or may require user authentication. Additionally, web scraping might be subject to legal and ethical considerations, and users should respect website terms of service.

## Getting Started

To run this application, follow these steps:

### 1. Install Required Libraries

First, install all the necessary libraries using the following command:

```bash
pip install -r requirements.txt
```

### 2. Launch the app using following command:
```bash
python app.py
```