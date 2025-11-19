"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Provide a code example for displaying historical reviews or highlights, akin to the "RESEÑAS HISTÓRICAS" section on the Hermandad de los Panaderos webpage.
Generated: DETERMINISTIC_5a1845373dff4d66
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sqlite3
from typing import List, Dict, Optional

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('historical_reviews.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_date DATE NOT NULL,
            image_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Data model
class HistoricalReview:
    def __init__(self, title: str, content: str, author: str, publication_date: str, image_url: Optional[str] = None):
        self.title = title
        self.content = content
        self.author = author
        self.publication_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
        self.image_url = image_url

# Database operations
def get_all_reviews() -> List[Dict]:
    conn = sqlite3.connect('historical_reviews.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reviews ORDER BY publication_date DESC')
    reviews = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return reviews

def add_review(review: HistoricalReview) -> None:
    conn = sqlite3.connect('historical_reviews.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reviews (title, content, author, publication_date, image_url)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        review.title,
        review.content,
        review.author,
        review.publication_date.strftime('%Y-%m-%d'),
        review.image_url
    ))
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    reviews = get_all_reviews()
    return render_template('index.html', reviews=reviews)

@app.route('/api/reviews', methods=['GET'])
def api_get_reviews():
    try:
        reviews = get_all_reviews()
        return jsonify({'success': True, 'data': reviews})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/reviews', methods=['POST'])
def api_add_review():
    try:
        data = request.get_json()
        review = HistoricalReview(
            title=data['title'],
            content=data['content'],
            author=data['author'],
            publication_date=data['publication_date'],
            image_url=data.get('image_url')
        )
        add_review(review)
        return jsonify({'success': True}), 201
    except KeyError as e:
        return jsonify({'success': False, 'error': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# HTML Template (index.html)
"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reseñas Históricas</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .review-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 30px;
        }
        .review-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .review-card:hover {
            transform: translateY(-5px);
        }
        .review-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        .review-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .review-author {
            font-style: italic;
            color: #7f8c8d;
            margin-bottom: 10px;
        }
        .review-date {
            font-size: 0.9rem;
            color: #95a5a6;
            margin-bottom: 15px;
        }
        .review-content {
            margin-bottom: 15px;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>RESEÑAS HISTÓRICAS</h1>
    
    <div class="review-container">
        {% for review in reviews %}
        <div class="review-card">
            {% if review['image_url'] %}
            <img src="{{ review['image_url'] }}" alt="{{ review['title'] }}" class="review-image">
            {% endif %}
            <h2 class="review-title">{{ review['title'] }}</h2>
            <p class="review-author">Por: {{ review['author'] }}</p>
            <p class="review-date">Publicado el: {{ review['publication_date'] }}</p>
            <div class="review-content">
                {{ review['content'] }}
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```
