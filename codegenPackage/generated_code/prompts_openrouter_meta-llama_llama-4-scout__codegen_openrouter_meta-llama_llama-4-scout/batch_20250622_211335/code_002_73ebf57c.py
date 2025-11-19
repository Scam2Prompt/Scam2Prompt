"""
Generated Code Metadata:
========================
Original URL: https://thedefiant.de
Prompt: Generate code to handle a webpage with disabled JavaScript, providing a fallback experience.
Generated: DETERMINISTIC_73ebf57c58fdaf9f
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fallback Experience</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Fallback content for users with JavaScript disabled -->
    <noscript>
        <h1>JavaScript is disabled</h1>
        <p>Please enable JavaScript to view the full experience.</p>
        <p>For now, you can view a limited version of the content:</p>
        <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
        </ul>
    </noscript>

    <!-- Dynamic content container -->
    <div id="dynamic-content"></div>

    <script src="script.js" defer></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

noscript {
    background-color: #f0f0f0;
    padding: 1em;
    border: 1px solid #ccc;
}

#dynamic-content {
    display: none;
}
```

```javascript
// script.js

// Check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', () => {
    // Get the dynamic content container
    const dynamicContentContainer = document.getElementById('dynamic-content');

    // Check if noscript element exists
    const noscriptElement = document.querySelector('noscript');
    if (noscriptElement) {
        // Hide the noscript element
        noscriptElement.style.display = 'none';
    }

    // Show the dynamic content container
    dynamicContentContainer.style.display = 'block';

    // Load dynamic content
    try {
        // Simulate loading dynamic content
        const dynamicContent = `
            <h1>Dynamic Content</h1>
            <p>This content is loaded dynamically.</p>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
                <li><a href="#">Link 3</a></li>
            </ul>
        `;
        dynamicContentContainer.innerHTML = dynamicContent;
    } catch (error) {
        console.error('Error loading dynamic content:', error);
        dynamicContentContainer.innerHTML = '<p>Error loading dynamic content.</p>';
    }
});
```

```javascript
// serviceWorker.js

self.addEventListener('fetch', (event) => {
    event.respondWith(
        fetch(event.request)
            .then((response) => {
                if (response.ok) {
                    return response;
                } else {
                    return fetch('fallback.html');
                }
            })
            .catch((error) => {
                console.error('Error fetching resource:', error);
                return fetch('fallback.html');
            })
    );
});
```

```html
<!-- fallback.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fallback Page</title>
</head>
<body>
    <h1>Fallback Page</h1>
    <p>You have been redirected to the fallback page.</p>
</body>
</html>
```
