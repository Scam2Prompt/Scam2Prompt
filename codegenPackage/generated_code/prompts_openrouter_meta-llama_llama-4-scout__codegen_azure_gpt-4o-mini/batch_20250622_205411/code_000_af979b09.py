"""
Generated Code Metadata:
========================
Original URL: https://celsi-us-network.com
Prompt: Generate HTML and CSS code for a basic webpage that displays copyright information and links to a privacy policy.
Generated: DETERMINISTIC_af979b09c046c818
Batch ID: 20250622_205411
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
    <title>Basic Webpage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <footer>
        <div class="footer-content">
            <p>&copy; 2023 Your Company Name. All rights reserved.</p>
            <p>
                <a href="privacy-policy.html" class="privacy-link">Privacy Policy</a>
            </p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, p {
    margin: 0;
    padding: 0;
}

/* Style for the footer */
footer {
    background-color: #f8f9fa; /* Light background color */
    padding: 20px; /* Padding around the footer */
    text-align: center; /* Center text alignment */
    position: relative; /* Positioning context for child elements */
}

/* Style for the footer content */
.footer-content {
    max-width: 800px; /* Maximum width for the content */
    margin: 0 auto; /* Center the content */
}

/* Style for the privacy policy link */
.privacy-link {
    color: #007bff; /* Link color */
    text-decoration: none; /* Remove underline from link */
}

.privacy-link:hover {
    text-decoration: underline; /* Underline on hover for better UX */
}
```
