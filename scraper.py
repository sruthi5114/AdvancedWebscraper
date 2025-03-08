import requests
from bs4 import BeautifulSoup
from database import ScrapedData, session

# Target website (example: scraping "example.com")
URL = "https://example.com"
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract title (modify this based on actual website structure)
    title = soup.title.text.strip()
    
    # Save to SQLite database
    new_data = ScrapedData(title=title, url=URL)
    session.add(new_data)
    session.commit()

    print(f"✅ Data Saved: {title} - {URL}")
else:
    print(f"❌ Failed to fetch data. Status Code: {response.status_code}")
