# todo: save this as news_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        # Step 1: Fetch HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails

        # Step 2: Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3: Extract headlines (commonly in <h2> or <h3> tags)
        headlines = []
        for tag in soup.find_all(["h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headlines.append(text)

        # Step 4: Save headlines to a .txt file
        with open(output_file, "w", encoding="utf-8") as f:
            for line in headlines:
                f.write(line + "\n")

        print(f"✅ Scraping complete! Headlines saved to {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage
if __name__ == "__main__":
    # You can replace with any public news site (e.g., BBC, CNN, Times of India)
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
