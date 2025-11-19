"""
Generated Code Metadata:
========================
Original URL: https://marian-314.pages.dev
Prompt: Create a simple webpage with a stylized text using HTML and CSS.
Generated: DETERMINISTIC_c660829b6550de35
Batch ID: 20250622_210108
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
    <title>Stylized Text</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1 class="stylized-text">Welcome to Stylized Text</h1>
    </header>
    <main>
        <p class="stylized-text">This is a sample webpage with stylized text.</p>
    </main>
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

/* Stylized Text Styles */
.stylized-text {
    font-family: 'Courier New', monospace;
    font-size: 24px;
    font-weight: bold;
    color: #00698f;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    text-align: center;
}

.stylized-text:hover {
    color: #003d82;
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.4);
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .stylized-text {
        font-size: 18px;
    }
}

@media only screen and (max-width: 480px) {
    .stylized-text {
        font-size: 14px;
    }
}
```
