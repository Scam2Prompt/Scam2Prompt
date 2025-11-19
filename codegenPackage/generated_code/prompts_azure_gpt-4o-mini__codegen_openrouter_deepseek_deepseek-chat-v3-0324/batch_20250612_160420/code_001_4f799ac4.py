"""
Generated Code Metadata:
========================
Original URL: https://totalwineusinc.com
Prompt: How can I implement a custom error page for a website that is currently unavailable, similar to the message shown on totalwineusinc.com?
Generated: DETERMINISTIC_4f799ac4cc765d11
Batch ID: 20250612_160420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website Temporarily Unavailable</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .container {
            max-width: 600px;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #d32f2f;
            margin-bottom: 20px;
        }
        p {
            margin-bottom: 20px;
            line-height: 1.6;
        }
        .logo {
            max-width: 200px;
            margin-bottom: 20px;
        }
        .contact {
            margin-top: 30px;
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Replace with your company logo -->
        <img src="your-logo.png" alt="Company Logo" class="logo">
        
        <h1>Website Temporarily Unavailable</h1>
        
        <p>We're currently performing scheduled maintenance to improve your experience. The website will be back online shortly.</p>
        
        <p>We apologize for any inconvenience and appreciate your patience.</p>
        
        <div class="contact">
            <p>If you need immediate assistance, please contact us at:</p>
            <p><strong>Email:</strong> support@yourcompany.com</p>
            <p><strong>Phone:</strong> 1-800-YOUR-COMPANY</p>
        </div>
    </div>

    <!-- Optional: Auto-refresh to check if site is back up -->
    <script>
        // Check every 5 minutes if the site is back up
        setTimeout(function() {
            window.location.reload();
        }, 300000);
    </script>
</body>
</html>
```

```nginx
# Nginx configuration for custom error page
server {
    listen 80;
    server_name yourdomain.com;
    
    # Serve maintenance page for all requests
    location / {
        root /path/to/maintenance/page;
        try_files /maintenance.html =503;
    }
    
    error_page 503 @maintenance;
    location @maintenance {
        root /path/to/maintenance/page;
        rewrite ^(.*)$ /maintenance.html break;
    }
}
```

```apache
# Apache .htaccess configuration for custom error page
RewriteEngine On

# Serve maintenance page for all requests
RewriteCond %{REQUEST_URI} !^/maintenance\.html$
RewriteRule ^(.*)$ /maintenance.html [R=503,L]

ErrorDocument 503 /maintenance.html
```
