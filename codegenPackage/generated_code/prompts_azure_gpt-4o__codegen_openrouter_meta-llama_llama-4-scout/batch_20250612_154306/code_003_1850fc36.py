"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Generate code for a landing page that displays a "JavaScript required" message when JavaScript is disabled, as seen on the Step App domain page.
Generated: DETERMINISTIC_1850fc366c57a499
Batch ID: 20250612_154306
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
    <title>JavaScript Required</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <noscript>
        <div class="noscript-container">
            <h1>JavaScript Required</h1>
            <p>Please enable JavaScript in your browser to view this page.</p>
        </div>
    </noscript>
    <script src="script.js" defer></script>
</body>
</html>
```

**styles.css**
```css
.noscript-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.noscript-container h1 {
    font-size: 36px;
    margin-bottom: 16px;
}

.noscript-container p {
    font-size: 18px;
    color: #666;
}
```

**script.js**
```javascript
// Check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', () => {
    const noscriptContainer = document.querySelector('noscript');
    if (noscriptContainer) {
        noscriptContainer.style.display = 'none';
    }
});
```
