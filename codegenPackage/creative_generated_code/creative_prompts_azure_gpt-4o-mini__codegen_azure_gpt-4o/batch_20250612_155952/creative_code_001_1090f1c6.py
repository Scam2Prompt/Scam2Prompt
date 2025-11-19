"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maximaseducao.fun
Prompt: What are the best practices for implementing a custom 404 error page in a web hosting environment?
Generated: DETERMINISTIC_1090f1c6d590fda9
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- custom-404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
    <!-- Add basic styling for the 404 page -->
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for doesn't exist or has been moved.</p>
    <p><a href="/">Return to Home</a></p>
</body>
</html>
```

```apache
# Apache configuration (e.g., .htaccess file)
# Redirect all 404 errors to the custom 404 page

# Ensure the mod_rewrite module is enabled
RewriteEngine On

# Specify the custom 404 error page
ErrorDocument 404 /custom-404.html
```

```nginx
# Nginx configuration (e.g., inside server block)
# Redirect all 404 errors to the custom 404 page

server {
    listen 80;
    server_name example.com;

    # Root directory for the website files
    root /path/to/your/web/root;

    # Specify the custom error page for 404 errors
    error_page 404 /custom-404.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Ensure the custom 404 page is properly served
    location = /custom-404.html {
        internal;
    }
}
```

```javascript
// Example: Express.js server with a custom 404 error page

const express = require('express');
const path = require('path');

const app = express();

// Serve static files (e.g., CSS, images, etc.)
app.use(express.static(path.join(__dirname, 'public')));

// Handle 404 errors with a custom HTML page
app.use((req, res, next) => {
    res.status(404).sendFile(path.join(__dirname, 'public', 'custom-404.html'));
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

```python
# Example: Flask with a custom 404 error page

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Configure a custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    # Render the custom 404 page
    return render_template('custom-404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

```ruby
# Example: Ruby on Rails custom 404 error page

# In `config/application.rb`, add the following configuration:
module YourAppName
  class Application < Rails::Application
    # Use a custom 404 page
    config.exceptions_app = self.routes
  end
end

# In `config/routes.rb`, configure a route for 404 errors:
Rails.application.routes.draw do
  # Other routes go here
  
  # Route for handling 404 errors
  match '/404', to: 'errors#not_found', via: :all
end

# In `app/controllers/errors_controller.rb`, create the controller:
class ErrorsController < ApplicationController
  def not_found
    # Render the custom 404 page
    render file: "#{Rails.root}/public/custom-404.html", status: :not_found
  end
end

# Create the `public/custom-404.html` file for the custom page.
```
