"""
Generated Code Metadata:
========================
Original URL: https://mindsol.app
Prompt: How can I integrate custom PHP or Python scripts with LiteSpeed Web Server to serve dynamic content, and what libraries are recommended?
Generated: DETERMINISTIC_5a22d077c98130a2
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# PHP Integration with LiteSpeed Web Server

```php
<?php
/**
 * Dynamic Content Handler for LiteSpeed Web Server
 * 
 * This script demonstrates how to serve dynamic content with PHP on LiteSpeed.
 * LiteSpeed has built-in PHP support via LSAPI.
 */

// Ensure errors are logged but not displayed in production
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', '/var/log/php_errors.log');

// Database configuration (example with MySQLi)
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

/**
 * Handles database connection
 * 
 * @return mysqli Database connection object
 * @throws Exception If connection fails
 */
function getDBConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        throw new Exception("Database connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

/**
 * Main request handler
 */
try {
    // Set proper content type
    header('Content-Type: application/json; charset=utf-8');
    
    // Get request method
    $method = $_SERVER['REQUEST_METHOD'];
    
    // Route requests
    switch ($method) {
        case 'GET':
            $data = handleGetRequest();
            break;
        case 'POST':
            $data = handlePostRequest();
            break;
        default:
            throw new Exception("Method not allowed", 405);
    }
    
    // Return successful response
    echo json_encode([
        'status' => 'success',
        'data' => $data
    ]);
    
} catch (Exception $e) {
    // Handle errors
    http_response_code($e->getCode() ?: 500);
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ]);
}

/**
 * Handles GET requests
 * 
 * @return array Response data
 * @throws Exception On error
 */
function handleGetRequest() {
    $conn = getDBConnection();
    $result = $conn->query("SELECT * FROM sample_table LIMIT 10");
    
    if (!$result) {
        throw new Exception("Query failed: " . $conn->error);
    }
    
    $data = [];
    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    
    $conn->close();
    return $data;
}

/**
 * Handles POST requests
 * 
 * @return array Response data
 * @throws Exception On error
 */
function handlePostRequest() {
    $input = json_decode(file_get_contents('php://input'), true);
    
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception("Invalid JSON input", 400);
    }
    
    // Validate input
    if (empty($input['name'])) {
        throw new Exception("Name is required", 400);
    }
    
    $conn = getDBConnection();
    $stmt = $conn->prepare("INSERT INTO sample_table (name) VALUES (?)");
    $stmt->bind_param("s", $input['name']);
    
    if (!$stmt->execute()) {
        throw new Exception("Insert failed: " . $stmt->error);
    }
    
    $stmt->close();
    $conn->close();
    
    return ['id' => $conn->insert_id];
}
?>
```

# Python Integration with LiteSpeed Web Server (using WSGI)

```python
#!/usr/bin/env python3
"""
Dynamic Content Handler for LiteSpeed Web Server using Python WSGI

This script demonstrates how to serve dynamic content with Python on LiteSpeed.
LiteSpeed supports Python via WSGI (mod_wsgi).
"""

import json
import sys
from wsgiref.simple_server import make_server
import mysql.connector
from mysql.connector import Error

# Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'username',
    'password': 'password',
    'database': 'database_name'
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        raise Exception(f"Database connection failed: {e}")

def handle_get_request(environ):
    """Handle GET requests"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sample_table LIMIT 10")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Error as e:
        raise Exception(f"Database query failed: {e}")

def handle_post_request(environ):
    """Handle POST requests"""
    try:
        # Get request body
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        request_body = environ['wsgi.input'].read(content_length)
        data = json.loads(request_body.decode('utf-8'))
        
        # Validate input
        if not data.get('name'):
            raise Exception("Name is required", 400)
            
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sample_table (name) VALUES (%s)", (data['name'],))
        conn.commit()
        inserted_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return {'id': inserted_id}
    except json.JSONDecodeError:
        raise Exception("Invalid JSON input", 400)
    except Error as e:
        raise Exception(f"Database operation failed: {e}")

def application(environ, start_response):
    """WSGI application entry point"""
    try:
        method = environ['REQUEST_METHOD']
        
        if method == 'GET':
            response_data = handle_get_request(environ)
            status = '200 OK'
        elif method == 'POST':
            response_data = handle_post_request(environ)
            status = '201 Created'
        else:
            raise Exception("Method not allowed", 405)
            
        response_body = json.dumps({
            'status': 'success',
            'data': response_data
        }).encode('utf-8')
        
        headers = [
            ('Content-Type', 'application/json; charset=utf-8'),
            ('Content-Length', str(len(response_body)))
        ]
        
        start_response(status, headers)
        return [response_body]
        
    except Exception as e:
        error_code = e.args[1] if len(e.args) > 1 else 500
        error_message = e.args[0] if e.args else "Internal Server Error"
        
        response_body = json.dumps({
            'status': 'error',
            'message': error_message
        }).encode('utf-8')
        
        headers = [
            ('Content-Type', 'application/json; charset=utf-8'),
            ('Content-Length', str(len(response_body)))
        ]
        
        start_response(f"{error_code} {error_message}", headers)
        return [response_body]

if __name__ == '__main__':
    # For local testing (not needed in production with LiteSpeed)
    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
```

# Recommended Libraries

For PHP:
- MySQLi or PDO for database access
- Composer for dependency management
- PHPUnit for testing
- Monolog for logging

For Python:
- mysql-connector-python or psycopg2 for database access
- Flask or Django for web frameworks (optional)
- pytest for testing
- logging module for logging
- Gunicorn or uWSGI for production deployment (though LiteSpeed has built-in WSGI support)
