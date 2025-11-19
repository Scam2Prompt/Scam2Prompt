"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Write a Python script to implement an IPTV streaming service with multiple package options, including TV channels, movies, and series, with a focus on stability and reliability.
Generated: DETERMINISTIC_ebcc9b1d1860c94b
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
import threading
import logging
from flask import Flask, request, jsonify, Response, abort
from werkzeug.utils import secure_filename
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('iptv_service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Constants
CONFIG_FILE = 'config.json'
ALLOWED_EXTENSIONS = {'m3u', 'json'}
DEFAULT_CONFIG = {
    "packages": {
        "basic": {
            "name": "Basic Package",
            "price": 9.99,
            "channels": [],
            "movies": [],
            "series": []
        },
        "standard": {
            "name": "Standard Package",
            "price": 19.99,
            "channels": [],
            "movies": [],
            "series": []
        },
        "premium": {
            "name": "Premium Package",
            "price": 29.99,
            "channels": [],
            "movies": [],
            "series": []
        }
    },
    "users": {},
    "stream_settings": {
        "buffer_size": 8192,
        "timeout": 30
    }
}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

class IPTVService:
    def __init__(self):
        self.config = self._load_config()
        self.lock = threading.Lock()
        self.stream_cache = {}
        self.stream_cache_lock = threading.Lock()
        self._initialize_directories()

    def _initialize_directories(self):
        """Ensure required directories exist."""
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    def _load_config(self) -> Dict:
        """Load configuration from file or create default."""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
            return DEFAULT_CONFIG.copy()
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return DEFAULT_CONFIG.copy()

    def _save_config(self):
        """Save current configuration to file."""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            logger.error(f"Error saving config: {e}")

    def add_content(self, package: str, content_type: str, content: Dict) -> bool:
        """Add content to a package."""
        with self.lock:
            if package not in self.config['packages']:
                logger.error(f"Package {package} not found")
                return False
            
            if content_type not in ['channels', 'movies', 'series']:
                logger.error(f"Invalid content type: {content_type}")
                return False
            
            self.config['packages'][package][content_type].append(content)
            self._save_config()
            return True

    def remove_content(self, package: str, content_type: str, content_id: str) -> bool:
        """Remove content from a package."""
        with self.lock:
            if package not in self.config['packages']:
                logger.error(f"Package {package} not found")
                return False
            
            if content_type not in ['channels', 'movies', 'series']:
                logger.error(f"Invalid content type: {content_type}")
                return False
            
            content_list = self.config['packages'][package][content_type]
            self.config['packages'][package][content_type] = [
                item for item in content_list if item.get('id') != content_id
            ]
            self._save_config()
            return True

    def get_package_content(self, package: str) -> Optional[Dict]:
        """Get all content for a package."""
        return self.config['packages'].get(package)

    def register_user(self, username: str, password: str, package: str) -> bool:
        """Register a new user."""
        with self.lock:
            if username in self.config['users']:
                logger.error(f"User {username} already exists")
                return False
            
            if package not in self.config['packages']:
                logger.error(f"Package {package} not found")
                return False
            
            self.config['users'][username] = {
                'password': password,
                'package': package,
                'active': True
            }
            self._save_config()
            return True

    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate a user."""
        user = self.config['users'].get(username)
        if not user or user['password'] != password or not user['active']:
            return False
        return True

    def get_user_package(self, username: str) -> Optional[str]:
        """Get package for a user."""
        user = self.config['users'].get(username)
        if not user:
            return None
        return user['package']

    def stream_content(self, content_url: str) -> Response:
        """Stream content from URL with proper buffering."""
        try:
            import requests
            from requests.exceptions import RequestException

            with self.stream_cache_lock:
                if content_url in self.stream_cache:
                    return self.stream_cache[content_url]

            settings = self.config['stream_settings']
            session = requests.Session()
            response = session.get(
                content_url,
                stream=True,
                timeout=settings['timeout']
            )

            if response.status_code != 200:
                abort(response.status_code)

            def generate():
                try:
                    for chunk in response.iter_content(chunk_size=settings['buffer_size']):
                        if chunk:
                            yield chunk
                except RequestException as e:
                    logger.error(f"Streaming error: {e}")
                    abort(500)
                finally:
                    response.close()
                    session.close()

            streaming_response = Response(
                generate(),
                content_type=response.headers.get('content-type', 'video/mp4')
            )

            with self.stream_cache_lock:
                self.stream_cache[content_url] = streaming_response

            return streaming_response

        except Exception as e:
            logger.error(f"Error streaming content: {e}")
            abort(500)

def allowed_file(filename: str) -> bool:
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data or 'package' not in data:
        abort(400, description="Missing required fields")

    if iptv_service.register_user(data['username'], data['password'], data['package']):
        return jsonify({"status": "success"}), 201
    return jsonify({"status": "error", "message": "Registration failed"}), 400

@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate user."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        abort(400, description="Missing required fields")

    if iptv_service.authenticate_user(data['username'], data['password']):
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route('/api/package/<package_name>', methods=['GET'])
def get_package(package_name: str):
    """Get package details."""
    package = iptv_service.get_package_content(package_name)
    if not package:
        abort(404, description="Package not found")
    return jsonify(package), 200

@app.route('/api/stream', methods=['GET'])
def stream():
    """Stream content."""
    if 'url' not in request.args:
        abort(400, description="Missing URL parameter")

    username = request.headers.get('X-Username')
    password = request.headers.get('X-Password')

    if not username or not password or not iptv_service.authenticate_user(username, password):
        abort(401, description="Unauthorized")

    return iptv_service.stream_content(request.args['url'])

@app.route('/api/admin/add_content', methods=['POST'])
def add_content():
    """Admin endpoint to add content."""
    if 'admin_key' not in request.headers or request.headers['admin_key'] != 'SECRET_ADMIN_KEY':
        abort(403, description="Forbidden")

    data = request.get_json()
    if not data or 'package' not in data or 'type' not in data or 'content' not in data:
        abort(400, description="Missing required fields")

    if iptv_service.add_content(data['package'], data['type'], data['content']):
