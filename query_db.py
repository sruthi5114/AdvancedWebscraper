from database import session, ScrapedData

data = session.query(ScrapedData).all()

for item in data:
    print(f"{item.id}: {item.title} ({item.url})")
