"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Generate a JavaScript code to create a simple webpage that showcases Infusión's different mixes, including their ingredients and benefits, using a responsive design.
Generated: DETERMINISTIC_0fdafebe28586d60
Batch ID: 20250622_205045
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
    <title>Infusión Mixes Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Infusión Mixes</h1>
        <p>Explore our different mixes, their ingredients, and benefits.</p>
    </header>
    <main>
        <section id="mixes">
            <article class="mix">
                <h2>Herbal Bliss</h2>
                <ul>
                    <li>Ingredients: Chamomile, Lavender, Lemon Balm</li>
                    <li>Benefits: Calming, Sleep Aid, Stress Relief</li>
                </ul>
            </article>
            <article class="mix">
                <h2>Energy Boost</h2>
                <ul>
                    <li>Ingredients: Green Tea, Ginseng, Mint</li>
                    <li>Benefits: Increased Energy, Focus, Antioxidants</li>
                </ul>
            </article>
            <article class="mix">
                <h2>Detox Delight</h2>
                <ul>
                    <li>Ingredients: Dandelion, Ginger, Lemon</li>
                    <li>Benefits: Detoxification, Digestion Aid, Anti-inflammatory</li>
                </ul>
            </article>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Infusión. All rights reserved.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling for body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Mix article styling */
.mix {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px 0;
    padding: 15px;
}

/* Responsive design */
@media (max-width: 600px) {
    header, main, footer {
        padding: 10px;
    }

    .mix {
        padding: 10px;
    }
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px;
    background: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// This script can be expanded for future interactivity
document.addEventListener('DOMContentLoaded', () => {
    console.log("Infusión Mixes Showcase Loaded");
    // Future functionality can be added here
});
```
