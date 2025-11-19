"""
Generated Code Metadata:
========================
Original URL: https://getin.co.il
Prompt: Generate HTML and JavaScript code to display a warning message when JavaScript is disabled, ensuring the message is styled and localized for Hebrew users like on https://getin.co.il.
Generated: DETERMINISTIC_78c51e65e73c5886
Batch ID: 20250612_150417
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
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Warning</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <noscript>
        <div class="js-disabled-warning">
            <p dir="rtl">אזהרה: JavaScript מושבת בדפדפן שלך</p>
            <p dir="rtl">אנא הפעל JavaScript כדי להשתמש באתר זה</p>
        </div>
    </noscript>
    <script src="script.js" defer></script>
</body>
</html>
```

**styles.css**
```css
.js-disabled-warning {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #FFC080;
    color: #666;
    padding: 1em;
    text-align: center;
    direction: rtl;
}

.js-disabled-warning p {
    margin-bottom: 0.5em;
}
```

**script.js**
```javascript
// No JavaScript code needed for this specific request,
// as the warning message is displayed using the <noscript> tag.
```
