from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create SQLite database
DATABASE_URL = "sqlite:///scraper_data.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create a Base class
Base = declarative_base()

# Define a table/model
class ScrapedData(Base):
    __tablename__ = "scraped_data"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)

# Create a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Create database tables
Base.metadata.create_all(engine)

print("✅ Database and tables created successfully!")
