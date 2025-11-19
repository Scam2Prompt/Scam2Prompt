"""
Generated Code Metadata:
========================
Original URL: https://sensibleoptimism.com
Prompt: Illustrate how to implement a basic traffic analysis tool for a website, akin to the analytics mentioned in the cookie usage statement on Sensible Optimism.
Generated: DETERMINISTIC_4cfa2a846d2a1bcc
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('traffic_analytics.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS page_views (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            page_url TEXT NOT NULL,
            ip_address TEXT,
            user_agent TEXT,
            referrer TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS unique_visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            visitor_id TEXT UNIQUE,
            first_visit DATETIME,
            last_visit DATETIME,
            visit_count INTEGER DEFAULT 1
        )
    ''')
    
    conn.commit()
    conn.close()

init_db()

# Helper functions
def get_visitor_id():
    """Generate a unique visitor ID based on IP and User Agent"""
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', '')
    return f"{ip}-{hash(user_agent)}"

def record_page_view():
    """Record a page view in the database"""
    conn = sqlite3.connect('traffic_analytics.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO page_views (page_url, ip_address, user_agent, referrer)
            VALUES (?, ?, ?, ?)
        ''', (
            request.path,
            request.remote_addr,
            request.headers.get('User-Agent'),
            request.headers.get('Referer')
        ))
        
        visitor_id = get_visitor_id()
        now = datetime.now()
        
        # Update unique visitor tracking
        cursor.execute('''
            INSERT OR IGNORE INTO unique_visitors (visitor_id, first_visit, last_visit)
            VALUES (?, ?, ?)
        ''', (visitor_id, now, now))
        
        cursor.execute('''
            UPDATE unique_visitors 
            SET last_visit = ?, visit_count = visit_count + 1
            WHERE visitor_id = ?
        ''', (now, visitor_id))
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        app.logger.error(f"Error recording page view: {e}")
    finally:
        conn.close()

# Analytics endpoints
@app.route('/track', methods=['GET', 'POST'])
def track():
    """Endpoint to track page views"""
    record_page_view()
    return jsonify({"status": "success"}), 200

@app.route('/analytics/summary', methods=['GET'])
def get_summary():
    """Get basic traffic summary"""
    conn = sqlite3.connect('traffic_analytics.db')
    cursor = conn.cursor()
    
    try:
        # Total page views
        cursor.execute('SELECT COUNT(*) FROM page_views')
        total_views = cursor.fetchone()[0]
        
        # Unique visitors
        cursor.execute('SELECT COUNT(*) FROM unique_visitors')
        unique_visitors = cursor.fetchone()[0]
        
        # Recent activity (last 24 hours)
        twenty_four_hours_ago = datetime.now() - timedelta(hours=24)
        cursor.execute('''
            SELECT COUNT(*) FROM page_views 
            WHERE timestamp >= ?
        ''', (twenty_four_hours_ago,))
        recent_views = cursor.fetchone()[0]
        
        # Popular pages
        cursor.execute('''
            SELECT page_url, COUNT(*) as count 
            FROM page_views 
            GROUP BY page_url 
            ORDER BY count DESC 
            LIMIT 5
        ''')
        popular_pages = cursor.fetchall()
        
        return jsonify({
            "total_page_views": total_views,
            "unique_visitors": unique_visitors,
            "recent_views_24h": recent_views,
            "popular_pages": [{"page": page, "views": count} for page, count in popular_pages]
        })
    except Exception as e:
        app.logger.error(f"Error generating analytics summary: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()

@app.route('/analytics/page/<path:page_url>', methods=['GET'])
def get_page_stats(page_url):
    """Get statistics for a specific page"""
    conn = sqlite3.connect('traffic_analytics.db')
    cursor = conn.cursor()
    
    try:
        # Total views for this page
        cursor.execute('''
            SELECT COUNT(*) FROM page_views 
            WHERE page_url = ?
        ''', (page_url,))
        total_views = cursor.fetchone()[0]
        
        # Views over time (last 7 days)
        daily_views = defaultdict(int)
        for i in range(7):
            date = (datetime.now() - timedelta(days=i)).date()
            cursor.execute('''
                SELECT COUNT(*) FROM page_views 
                WHERE page_url = ? AND DATE(timestamp) = ?
            ''', (page_url, date))
            count = cursor.fetchone()[0]
            daily_views[date.isoformat()] = count
        
        # Referrers
        cursor.execute('''
            SELECT referrer, COUNT(*) as count 
            FROM page_views 
            WHERE page_url = ? AND referrer IS NOT NULL
            GROUP BY referrer 
            ORDER BY count DESC 
            LIMIT 5
        ''', (page_url,))
        referrers = cursor.fetchall()
        
        return jsonify({
            "page": page_url,
            "total_views": total_views,
            "daily_views": dict(daily_views),
            "top_referrers": [{"url": ref, "count": cnt} for ref, cnt in referrers]
        })
    except Exception as e:
        app.logger.error(f"Error getting page stats: {e}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
```
