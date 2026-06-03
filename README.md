# News-Scraper-Task-3
A simple Python script that scrapes news headlines from a website and saves them to a text file using Requests and BeautifulSoup.

## Features

* Fetches HTML content from a news website.
* Extracts headlines from `<h2>` and `<h3>` tags.
* Saves scraped headlines to a text file.
* Basic error handling for network and parsing issues.
* Easy to customize for different websites.

## Requirements

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Project Structure

```text
.
├── news_scraper.py
├── headlines.txt      # Generated after running the script
└── README.md
```

## Usage

Run the script:

```bash
python news_scraper.py
```

By default, the script scrapes headlines from:

```python
https://www.bbc.com/news
```

and saves them to:

```text
headlines.txt
```

## Example Code

```python
from news_scraper import scrape_headlines

scrape_headlines(
    url="https://www.bbc.com/news",
    output_file="bbc_headlines.txt"
)
```

## Sample Output

```text
World News Headlines
Latest Updates from Europe
Technology Trends in 2025
Breaking News Around the Globe
```

## How It Works

1. Sends an HTTP request to the target website.
2. Parses the HTML content using BeautifulSoup.
3. Finds all `<h2>` and `<h3>` tags.
4. Extracts the text from each headline.
5. Saves the headlines into a text file.

## Customization

To scrape a different website, change the URL in the script:

```python
url = "https://example-news-site.com"
scrape_headlines(url)
```

You can also modify the tags being searched:

```python
for tag in soup.find_all(["h1", "h2", "h3"]):
```

## Notes

* Website structures vary, so some sites may use different HTML tags for headlines.
* Some websites load content dynamically with JavaScript; this script works best with static HTML pages.
* Always review and comply with the website's Terms of Service and robots.txt before scraping.

## Error Handling

The script catches common exceptions such as:

* Network connection errors
* Invalid URLs
* HTTP request failures
* Parsing-related issues

Example:

```text
❌ Error: 404 Client Error: Not Found
```

## Future Improvements

* Export headlines to CSV or JSON.
* Add headline timestamps and links.
* Support multiple news websites.
* Schedule automated scraping.
* Filter duplicate headlines.

## License

This project is open source and available for educational and learning purposes.
