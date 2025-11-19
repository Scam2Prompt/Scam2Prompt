"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://20000.paperplane.io
Prompt: Can you provide code examples for implementing a 301 redirect in a web server configuration?
Generated: DETERMINISTIC_b6a0c319a19bcdac
Batch ID: 20250612_160600
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://new-domain.com{request.path": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/new-page;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com${req.originalUrl}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com$request_uri;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/new-page": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here are examples for implementing a 301 redirect in various web server configurations:

---

### **Apache (HTTPD)**
```apache
# Redirecting a specific page to another URL
Redirect 301 /old-page https://example.com/new-page

# Redirecting the entire site to a new domain
<VirtualHost *:80>
    ServerName old-domain.com
    Redirect permanent / https://new-domain.com/
</VirtualHost>
```

---

### **Nginx**
```nginx
# Redirecting a specific page to another URL
server {
    listen 80;
    server_name example.com;
    location /old-page {
        return 301 https://example.com/new-page;
    }
}

# Redirecting the entire site to a new domain
server {
    listen 80;
    server_name old-domain.com;
    return 301 https://new-domain.com$request_uri;
}
```

---

### **Node.js (Express.js Framework)**
```javascript
const express = require('express');
const app = express();

// Redirecting a specific route to another URL
app.get('/old-page', (req, res) => {
    res.redirect(301, 'https://example.com/new-page');
});

// Redirecting the entire site to a new domain
app.use((req, res) => {
    res.redirect(301, `https://new-domain.com${req.originalUrl}`);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

---

### **Python (Flask Framework)**
```python
from flask import Flask, redirect

app = Flask(__name__)

# Redirecting a specific route to another URL
@app.route('/old-page')
def redirect_old_page():
    return redirect("https://example.com/new-page", code=301)

# Redirecting the entire site to a new domain
@app.before_request
def redirect_to_new_domain():
    new_domain = "https://new-domain.com"
    return redirect(new_domain + request.path, code=301)

if __name__ == "__main__":
    app.run(port=5000)
```

---

### **IIS (Web.config)**
```xml
<configuration>
    <system.webServer>
        <httpRedirect enabled="true" destination="https://new-domain.com" httpResponseStatus="Permanent" />
    </system.webServer>
</configuration>
```

---

### **Django**
```python
from django.http import HttpResponsePermanentRedirect

def redirect_old_page(request):
    return HttpResponsePermanentRedirect('https://example.com/new-page')

def redirect_entire_site(request):
    return HttpResponsePermanentRedirect(f'https://new-domain.com{request.path}')
```

---

### **PHP**
```php
<?php
// Redirecting a specific page to another URL
if ($_SERVER['REQUEST_URI'] == '/old-page') {
    header("Location: https://example.com/new-page", true, 301);
    exit();
}

// Redirecting the entire site to a new domain
header("Location: https://new-domain.com" . $_SERVER['REQUEST_URI'], true, 301);
exit();
?>
```
