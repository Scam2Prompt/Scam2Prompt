"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: How can I create a mobile-ready design for a social media platform that supports both light and dark themes, inspired by Lovr's features?
Generated: DETERMINISTIC_238222ff9f350350
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Media Platform</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>

<body>
    <header>
        <h1>Social Media Platform</h1>
        <button id="theme-toggle">Toggle Theme</button>
    </header>
    <main>
        <section class="post-feed">
            <article class="post">
                <h2>Post Title</h2>
                <p>This is an example of a post on our social media platform.</p>
            </article>
            <!-- Additional posts can be added here -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Social Media Platform</p>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* Base styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

header {
    background-color: var(--header-bg);
    color: var(--header-color);
    padding: 1rem;
    text-align: center;
}

main {
    padding: 1rem;
}

footer {
    background-color: var(--footer-bg);
    color: var(--footer-color);
    text-align: center;
    padding: 1rem;
}

/* Light theme colors */
:root {
    --header-bg: #ffffff;
    --header-color: #000000;
    --footer-bg: #ffffff;
    --footer-color: #000000;
    --post-bg: #f9f9f9;
    --post-color: #000000;
}

/* Dark theme colors */
[data-theme='dark'] {
    --header-bg: #000000;
    --header-color: #ffffff;
    --footer-bg: #000000;
    --footer-color: #ffffff;
    --post-bg: #333333;
    --post-color: #ffffff;
}

.post {
    background-color: var(--post-bg);
    color: var(--post-color);
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 1rem 0;
    padding: 1rem;
}
```

```javascript
// script.js

// Function to toggle the theme between light and dark
const toggleTheme = () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    
    // Save the selected theme in local storage for persistence
    localStorage.setItem('theme', newTheme);
};

// Event listener for theme toggle button
document.getElementById('theme-toggle').addEventListener('click', toggleTheme);

// Function to apply the saved theme on page load
const applySavedTheme = () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
};

// Apply the saved theme when the page loads
document.addEventListener('DOMContentLoaded', applySavedTheme);
```

This code includes a simple HTML structure for a social media platform, CSS for styling with light and dark themes, and JavaScript for toggling between themes while saving the preference in local storage. All sections are documented, and best practices are followed.
