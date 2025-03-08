# config.py

# MongoDB connection settings
MONGO_URI = "mongodb://localhost:27017"  # Update this if using cloud MongoDB
DB_NAME = "web_scraper"
COLLECTION_NAME = "scraped_data"

# Target website URL for scraping
SCRAPE_URL = "https://www.bbc.com/news"  # You can change this URL as needed

# Logging settings
LOG_FILE = "logs/scraper.log"
LOG_LEVEL = "INFO"
