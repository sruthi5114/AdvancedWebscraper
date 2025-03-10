from flask import Flask, jsonify
from database import session, ScrapedData

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Scraper API! Use /data to fetch results."})

@app.route('/data', methods=['GET'])
def get_data():
    """Fetch all scraped data from SQLite and return as JSON."""
    data = session.query(ScrapedData).all()
    result = [{"id": d.id, "title": d.title, "url": d.url} for d in data]
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 Starting Flask API...")
    app.run(debug=True)
