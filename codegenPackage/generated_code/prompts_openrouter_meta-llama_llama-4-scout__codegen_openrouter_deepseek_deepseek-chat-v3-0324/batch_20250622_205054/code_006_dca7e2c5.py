"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-website.vercel.app
Prompt: What are the requirements for deploying a custom bridge server for WalletConnect, and how does it differ from using WalletConnect Labs' public bridge server?
Generated: DETERMINISTIC_dca7e2c5b9cf3caa
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# walletconnect_bridge_server.py

import os
import json
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from redis import Redis
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Redis configuration
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_DB = int(os.getenv('REDIS_DB', 0))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)

try:
    redis_client = Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    redis_client.ping()  # Test connection
    logger.info("Successfully connected to Redis")
except Exception as e:
    logger.error(f"Failed to connect to Redis: {e}")
    raise

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Subscribe to a topic"""
    try:
        data = request.get_json()
        topic = data.get('topic')
        client_id = data.get('clientId')
        
        if not topic or not client_id:
            return jsonify({'error': 'Missing required parameters'}), 400
            
        redis_client.sadd(f'subscribers:{topic}', client_id)
        return jsonify({'success': True}), 200
    except Exception as e:
        logger.error(f"Subscribe error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/publish', methods=['POST'])
def publish():
    """Publish a message to a topic"""
    try:
        data = request.get_json()
        topic = data.get('topic')
        message = data.get('message')
        
        if not topic or not message:
            return jsonify({'error': 'Missing required parameters'}), 400
            
        # Store message in Redis
        redis_client.set(f'message:{topic}', json.dumps(message))
        
        # Notify subscribers
        subscribers = redis_client.smembers(f'subscribers:{topic}')
        for sub in subscribers:
            redis_client.publish(f'notifications:{sub}', topic)
            
        return jsonify({'success': True}), 200
    except Exception as e:
        logger.error(f"Publish error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/fetch', methods=['POST'])
def fetch():
    """Fetch messages for a topic"""
    try:
        data = request.get_json()
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'Missing topic parameter'}), 400
            
        message = redis_client.get(f'message:{topic}')
        if not message:
            return jsonify({'message': None}), 200
            
        return jsonify({'message': json.loads(message)}), 200
    except Exception as e:
        logger.error(f"Fetch error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('DEBUG', 'false').lower() == 'true'
    )
```

```dockerfile
# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=walletconnect_bridge_server.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "walletconnect_bridge_server:app"]
```

```text
# requirements.txt

flask==2.0.1
flask-cors==3.0.10
redis==4.1.0
python-dotenv==0.19.0
gunicorn==20.1.0
```

```text
# .env.example

# Redis configuration
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=

# Server configuration
HOST=0.0.0.0
PORT=5000
DEBUG=false
```

```yaml
# docker-compose.yml

version: '3.8'

services:
  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped

  bridge:
    build: .
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
    depends_on:
      - redis
    restart: unless-stopped

volumes:
  redis_data:
```
