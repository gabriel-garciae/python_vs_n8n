# 🕷️ Web Scraping Project with Python

## 📋 Project Objective

This project demonstrates how to perform **web scraping** on Mercado Livre to monitor product prices in real time. The goal is to automatically collect price data and create a complete monitoring system with notifications and visualization.

## 🎯 Learning Objectives

### Fundamental Concepts
- **Web Scraping**: Techniques to extract data from websites
- **HTTP Requests**: How to make requests to web pages
- **HTML Parsing**: Interpret and extract information from HTML
- **Automation**: Create scripts that perform repetitive tasks

### Technologies Used
- **Python**: Main language of the project
- **Requests**: Library to make HTTP requests
- **BeautifulSoup**: HTML parser to extract data
- **CSV**: For saving and analyzing price history

## 📁 Project Structure

### Example Scripts

#### **code.py** - Save Page HTML
- Makes an HTTP request to the product page and saves the raw HTML to a timestamped file in the `htmls/` folder.
- Useful for capturing the page content for later analysis or debugging.

#### **code2.py** - Simple Price Extraction
- Fetches the product page and uses BeautifulSoup to extract the product price from the HTML.
- Prints the captured price to the terminal.

#### **code3.py** - Save Price to CSV
- Scrapes the product price and saves the data (timestamp, product name, price, URL, source) to a CSV file (`price_history.csv`).
- Enables building a price history for future analysis.

#### **code4.py** - Continuous Price Monitoring
- Runs the scraping process in an infinite loop, saving the price to the CSV every minute (with a random interval to simulate human behavior).
- Ideal for automatic and continuous monitoring of price changes.

### Data Files
- **price_history.csv**: Real collected price data
- **htmls/**: Folder containing saved HTML files from the product page

## Implemented Features

### Data Collection
- HTTP requests with browser-like headers
- HTML parsing with BeautifulSoup
- Price extraction using CSS selectors
- Saving to CSV files

### Automatic Monitoring
- Continuous execution loop
- Random delays to avoid detection
- Basic error handling
- Execution logs

## 🛠️ How to Use

### Prerequisites

- **Python 3.8+** installed on your system.
- (Recommended) Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  ```
- Install the required libraries:
  ```bash
  pip install requests beautifulsoup4 pandas
  ```

### Running the Scripts

- **Save the HTML of the product page:**
  ```bash
  python src/code.py
  ```
  The HTML file will be saved in the `src/htmls/` folder.

- **Extract and print the product price:**
  ```bash
  python src/code2.py
  ```

- **Extract the price and save it to a CSV file:**
  ```bash
  python src/code3.py
  ```
  The data will be appended to `src/price_history.csv`.

- **Continuous price monitoring and CSV logging:**
  ```bash
  python src/code4.py
  ```
  The script will run indefinitely, saving new price entries every minute.

### Viewing the Results

- The HTML files are saved in `src/htmls/`.
- The price history is saved in `src/price_history.csv`, which you can open with Excel, LibreOffice, or any text editor.

Feel free to adapt and expand these scripts for your own web scraping and monitoring needs!
