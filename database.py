from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import ScrapedData, Base

engine = create_engine("sqlite:///scraper.db")
Session = sessionmaker(bind=engine)
session = Session()

def create_db():
    """Create tables and insert sample data only if the table is empty."""
    Base.metadata.create_all(engine)
    if not session.query(ScrapedData).first():  # Check if the table is empty
        sample_data = [
            ScrapedData(title="Example Domain", url="https://example.com"),
            ScrapedData(title="Google", url="https://www.google.com"),
        ]
        session.add_all(sample_data)
        session.commit()
        print("✅ Sample data inserted successfully!")
    else:
        print("⚠️ Sample data already exists, skipping insertion.")
