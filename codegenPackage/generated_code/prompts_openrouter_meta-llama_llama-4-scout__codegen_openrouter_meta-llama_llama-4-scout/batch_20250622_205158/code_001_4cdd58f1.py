"""
Generated Code Metadata:
========================
Original URL: https://linearlive.co.uk
Prompt: Generate a terms of service and privacy policy page using HTML, CSS, and JavaScript, similar to Linear Live Limited's website.
Generated: DETERMINISTIC_4cdd58f1106ca399
Batch ID: 20250622_205158
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
    <title>Terms of Service and Privacy Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Terms of Service and Privacy Policy</h1>
        <div class="tabbed-content">
            <button class="tab-button active" onclick="openTab(event, 'terms')">Terms of Service</button>
            <button class="tab-button" onclick="openTab(event, 'privacy')">Privacy Policy</button>
            <div id="terms" class="tab-content active">
                <h2>Terms of Service</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </div>
            <div id="privacy" class="tab-content">
                <h2>Privacy Policy</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.tabbed-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.tab-button {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.tab-button.active {
    background-color: #3e8e41;
}

.tab-content {
    display: none;
    padding: 20px;
}

.tab-content.active {
    display: block;
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

p {
    margin-bottom: 20px;
}
```

**script.js**
```javascript
// Function to open a tab
function openTab(event, tabId) {
    // Get all tab buttons and contents
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    // Remove active class from all tab buttons and contents
    tabButtons.forEach(button => button.classList.remove('active'));
    tabContents.forEach(content => content.classList.remove('active'));

    // Add active class to the selected tab button and content
    event.target.classList.add('active');
    document.getElementById(tabId).classList.add('active');
}

// Set the active tab to Terms of Service by default
document.addEventListener('DOMContentLoaded', () => {
    openTab({ target: document.querySelector('.tab-button:first-child') }, 'terms');
});

// Error handling for any uncaught exceptions
window.addEventListener('error', (event) => {
    console.error('Error occurred:', event.error);
});
```
