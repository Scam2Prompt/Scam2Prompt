"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Create code to set up a cookie-based system for analyzing website traffic and optimizing user experience, as described in the uuip-hualdlugeen services.
Generated: DETERMINISTIC_1aa6a6d75590de82
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
from datetime import datetime, timedelta
from flask import Flask, request, make_response, jsonify
import json
import uuid
import sqlite3
from typing import Dict, Optional, Tuple

app = Flask(__name__)

# Database configuration
DATABASE = 'analytics.db'

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create user_sessions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_sessions (
            session_id TEXT PRIMARY KEY,
            user_id TEXT,
            first_visit TIMESTAMP,
            last_activity TIMESTAMP,
            page_views INTEGER DEFAULT 0,
            referrer TEXT,
            user_agent TEXT,
            ip_address TEXT
        )
    ''')
    
    # Create page_events table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS page_events (
            event_id TEXT PRIMARY KEY,
            session_id TEXT,
            page_url TEXT,
            event_type TEXT,
            event_time TIMESTAMP,
            FOREIGN KEY (session_id) REFERENCES user_sessions (session_id)
        )
    ''')
    
    # Create user_preferences table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_preferences (
            user_id TEXT PRIMARY KEY,
            theme TEXT DEFAULT 'light',
            language TEXT DEFAULT 'en',
            font_size INTEGER DEFAULT 14,
            last_updated TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def generate_user_id(ip_address: str, user_agent: str) -> str:
    """Generate a unique but consistent user ID based on IP and User Agent."""
    unique_string = f"{ip_address}-{user_agent}"
    return hashlib.sha256(unique_string.encode()).hexdigest()

def get_or_create_session() -> Tuple[Dict, bool]:
    """Get existing session from cookie or create a new one."""
    session_id = request.cookies.get('session_id')
    user_id = request.cookies.get('user_id')
    new_session = False
    
    if not session_id:
        # Create new session
        session_id = str(uuid.uuid4())
        user_id = user_id or generate_user_id(request.remote_addr, request.user_agent.string)
        new_session = True
        
        # Store session in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO user_sessions (
                session_id, user_id, first_visit, last_activity, 
                referrer, user_agent, ip_address
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            session_id, user_id, datetime.now(), datetime.now(),
            request.referrer, request.user_agent.string, request.remote_addr
        ))
        conn.commit()
        conn.close()
    
    return {
        'session_id': session_id,
        'user_id': user_id,
        'new_session': new_session
    }, new_session

def update_session_activity(session_id: str):
    """Update the last activity time for a session."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE user_sessions 
        SET last_activity = ?, page_views = page_views + 1 
        WHERE session_id = ?
    ''', (datetime.now(), session_id))
    conn.commit()
    conn.close()

def track_page_event(session_id: str, page_url: str, event_type: str = 'pageview'):
    """Track a page view or other event."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO page_events (
            event_id, session_id, page_url, event_type, event_time
        ) VALUES (?, ?, ?, ?, ?)
    ''', (str(uuid.uuid4()), session_id, page_url, event_type, datetime.now()))
    conn.commit()
    conn.close()

def get_user_preferences(user_id: str) -> Optional[Dict]:
    """Retrieve user preferences from database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_preferences WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return dict(result)
    return None

def update_user_preferences(user_id: str, preferences: Dict):
    """Update or create user preferences."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if preferences exist
    existing = get_user_preferences(user_id)
    
    if existing:
        # Update existing preferences
        cursor.execute('''
            UPDATE user_preferences 
            SET theme = ?, language = ?, font_size = ?, last_updated = ?
            WHERE user_id = ?
        ''', (
            preferences.get('theme', existing['theme']),
            preferences.get('language', existing['language']),
            preferences.get('font_size', existing['font_size']),
            datetime.now(),
            user_id
        ))
    else:
        # Create new preferences
        cursor.execute('''
            INSERT INTO user_preferences (
                user_id, theme, language, font_size, last_updated
            ) VALUES (?, ?, ?, ?, ?)
        ''', (
            user_id,
            preferences.get('theme', 'light'),
            preferences.get('language', 'en'),
            preferences.get('font_size', 14),
            datetime.now()
        ))
    
    conn.commit()
    conn.close()

@app.before_request
def before_request():
    """Handle session tracking before each request."""
    session_data, is_new = get_or_create_session()
    request.session = session_data
    
    # Update session activity
    update_session_activity(session_data['session_id'])
    
    # Track page view
    track_page_event(session_data['session_id'], request.path)

@app.after_request
def after_request(response):
    """Set cookies after each request if needed."""
    if hasattr(request, 'session') and request.session.get('new_session', False):
        # Set cookies for new session
        response.set_cookie(
            'session_id',
            value=request.session['session_id'],
            max_age=timedelta(days=30).total_seconds(),
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        response.set_cookie(
            'user_id',
            value=request.session['user_id'],
            max_age=timedelta(days=365).total_seconds(),
            httponly=True,
            secure=True,
            samesite='Lax'
        )
    return response

@app.route('/api/preferences', methods=['GET'])
def get_preferences():
    """Endpoint to get user preferences."""
    if not hasattr(request, 'session'):
        return jsonify({'error': 'Session not found'}), 400
    
    preferences = get_user_preferences(request.session['user_id'])
    return jsonify(preferences or {})

@app.route('/api/preferences', methods=['POST'])
def update_preferences():
    """Endpoint to update user preferences."""
    if not hasattr(request, 'session'):
        return jsonify({'error': 'Session not found'}), 400
    
    try:
        preferences = request.get_json()
        update_user_preferences(request.session['user_id'], preferences)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/analytics/summary', methods=['GET'])
def get_analytics_summary():
    """Endpoint to get basic analytics summary."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get total sessions
    cursor.execute('SELECT COUNT(*) FROM user_sessions')
    total_sessions = cursor.fetchone()[0]
    
    # Get active sessions (last 30 minutes)
    active_time = datetime.now() - timedelta(minutes=30)
    cursor.execute('SELECT COUNT(*) FROM user_sessions WHERE last_activity > ?', (active_time,))
    active_sessions = cursor.fetchone()[0]
    
    # Get popular pages
    cursor.execute('''
        SELECT page_url, COUNT(*) as views 
        FROM page_events 
        WHERE event_type = 'pageview'
        GROUP BY page_url 
        ORDER BY views DESC 
        LIMIT 5
    ''')
    popular_pages = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({
        'total_sessions': total_sessions,
        'active_sessions': active_sessions,
        'popular_pages': popular_pages
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```
