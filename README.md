**Installation Guide Web Scraping using beautifulsoup and CSV Creation for each step in the installation guide**

This Python script automates the process of scraping installation guides from a list of URLs and saving the relevant content to CSV files. It is particularly useful for extracting structured data from web pages with headings, sub-headings, and code snippets.

aspects of the code:
-> Scrapes installation guides from specified URLs and saves each step as a seperate csv file.
-> Extracts headings, sub-headings, and code snippets.
-> Skips the csv creation for the urls which does not contain headings, sub-headings and code snippets.
-> Organizes extracted data into CSV files for easy analysis and reference.

Before running the script, ensure you have the following dependencies installed:
-> Python
-> Requests
-> BeautifulSoup4

You can install the required libraries using pip:
-> pip install requests beautifulsoup4

Clone the repository:
-> git clone https://github.com/your-username/your-repository.git

Navigate to the project directory:
-> cd the-target-repository

Run the script:
-> python3 crawler.py

View the generated CSV files in the results directory.
