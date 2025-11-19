"""
Generated Code Metadata:
========================
Original URL: https://sei.land
Prompt: Generate HTML and CSS code for a simple website footer that includes a copyright notice for 2025 and a link to a privacy policy page.
Generated: DETERMINISTIC_a0f4d34be12a019e
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Website Footer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <footer class="footer">
        <div class="footer-content">
            <p class="copyright">&copy; 2025 Simple Website. All rights reserved.</p>
            <ul class="footer-links">
                <li><a href="privacy-policy.html">Privacy Policy</a></li>
            </ul>
        </div>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Footer Styles */
.footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

.footer-content {
    max-width: 800px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.copyright {
    font-size: 0.8em;
    margin-right: 1em;
}

.footer-links {
    list-style: none;
    margin: 0;
    padding: 0;
}

.footer-links li {
    display: inline-block;
    margin-left: 20px;
}

.footer-links a {
    color: #fff;
    text-decoration: none;
}

.footer-links a:hover {
    text-decoration: underline;
}

/* Responsive Design */
@media only screen and (max-width: 600px) {
    .footer-content {
        flex-direction: column;
    }
    
    .copyright {
        margin-bottom: 10px;
    }
    
    .footer-links li {
        margin-left: 0;
    }
}
```
