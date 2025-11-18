"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dionlineaja.id
Prompt: Write JavaScript code to create an interactive portfolio section for a website, showcasing "Projects," "Clients," and "Cooperations," as seen on dionlineaja.id.
Generated: DETERMINISTIC_c12d2936c07de810
Batch ID: 20250612_152739
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
    <title>Interactive Portfolio Section</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="portfolio">
        <nav>
            <button class="tab-button" data-tab="projects">Projects</button>
            <button class="tab-button" data-tab="clients">Clients</button>
            <button class="tab-button" data-tab="cooperations">Cooperations</button>
        </nav>
        <div id="tab-content">
            <div class="tab" id="projects" data-active="true">
                <h2>Projects</h2>
                <ul>
                    <li>Project 1</li>
                    <li>Project 2</li>
                    <li>Project 3</li>
                </ul>
            </div>
            <div class="tab" id="clients">
                <h2>Clients</h2>
                <ul>
                    <li>Client A</li>
                    <li>Client B</li>
                    <li>Client C</li>
                </ul>
            </div>
            <div class="tab" id="cooperations">
                <h2>Cooperations</h2>
                <ul>
                    <li>Cooperation X</li>
                    <li>Cooperation Y</li>
                    <li>Cooperation Z</li>
                </ul>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
body, h2, ul {
    margin: 0;
    padding: 0;
}

/* Portfolio section styling */
#portfolio {
    margin: 20px;
    font-family: Arial, sans-serif;
}

nav {
    margin-bottom: 10px;
}

.tab-button {
    padding: 10px;
    border: none;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    margin-right: 5px;
}

.tab-button:hover {
    background-color: #0056b3;
}

.tab {
    display: none; /* Hide all tabs by default */
}

.tab[data-active="true"] {
    display: block; /* Show active tab */
}
```

```javascript
// script.js

// Function to handle tab switching
function switchTab(event) {
    try {
        // Get the tab to show
        const selectedTabId = event.target.getAttribute('data-tab');
        
        // Hide all tabs
        const tabs = document.querySelectorAll('.tab');
        tabs.forEach(tab => {
            tab.setAttribute('data-active', 'false');
        });

        // Show the selected tab
        const selectedTab = document.getElementById(selectedTabId);
        selectedTab.setAttribute('data-active', 'true');
    } catch (error) {
        console.error("Error switching tabs: ", error);
    }
}

// Initialize event listeners for tab buttons
function init() {
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.addEventListener('click', switchTab);
    });
}

// Wait for the DOM to load before initializing
document.addEventListener('DOMContentLoaded', init);
```
