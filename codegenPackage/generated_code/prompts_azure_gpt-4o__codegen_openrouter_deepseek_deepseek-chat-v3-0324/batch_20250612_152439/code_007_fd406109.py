"""
Generated Code Metadata:
========================
Original URL: https://tech-xpet.pages.dev
Prompt: Write code to implement cache clearing functionality for a web-based blockchain game platform like xPet.tech.
Generated: DETERMINISTIC_fd406109aab59d8f
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import redis
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# Configuration
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_DB = int(os.getenv('REDIS_DB', 0))
API_KEY = os.getenv('API_KEY', 'default-secret-key')

# Initialize Redis client
redis_client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=REDIS_DB,
    decode_responses=True
)

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if api_key != API_KEY:
            return jsonify({'error': 'Invalid API key'}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/cache/clear', methods=['POST'])
@require_api_key
def clear_cache():
    """
    Clear the entire Redis cache or specific keys.
    Accepts JSON payload with optional 'keys' array to clear specific keys.
    """
    try:
        data = request.get_json()
        
        if data and 'keys' in data:
            keys = data['keys']
            if not isinstance(keys, list):
                return jsonify({'error': 'Keys must be an array'}), 400
                
            if not keys:
                return jsonify({'error': 'Empty keys array provided'}), 400
                
            redis_client.delete(*keys)
            return jsonify({
                'status': 'success',
                'message': f'Cleared {len(keys)} specified cache keys'
            })
        else:
            redis_client.flushdb()
            return jsonify({
                'status': 'success',
                'message': 'Cleared entire cache'
            })
            
    except redis.RedisError as e:
        return jsonify({'error': f'Redis error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/api/cache/health', methods=['GET'])
def health_check():
    """Endpoint to check if cache service is healthy"""
    try:
        if redis_client.ping():
            return jsonify({'status': 'healthy'})
    except redis.RedisError:
        return jsonify({'status': 'unhealthy'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
