"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blasterturismo.com
Prompt: Design a user interface layout for a travel package selection page that features the unique itineraries offered by Blaster Turismo in Ametista do Sul.
Generated: DETERMINISTIC_8967df8989fd7fd3
Batch ID: 20250612_162050
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
    <title>Travel Package Selection - Blaster Turismo</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file for styles -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript file for functionality -->
</head>
<body>
    <header>
        <h1>Blaster Turismo - Ametista do Sul</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#packages">Packages</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section id="packages">
            <h2>Unique Itineraries</h2>
            <div class="package-container">
                <!-- Package Item -->
                <div class="package-item">
                    <img src="package1.jpg" alt="Package 1 Image" class="package-image">
                    <h3>Adventure in Ametista</h3>
                    <p>Explore the breathtaking landscapes of Ametista do Sul with our adventure package!</p>
                    <span class="price">$499</span>
                    <button class="select-button">Select Package</button>
                </div>
                <!-- Package Item -->
                <div class="package-item">
                    <img src="package2.jpg" alt="Package 2 Image" class="package-image">
                    <h3>Cultural Exploration</h3>
                    <p>Immerse yourself in the rich culture and traditions of Ametista do Sul.</p>
                    <span class="price">$399</span>
                    <button class="select-button">Select Package</button>
                </div>
                <!-- Package Item -->
                <div class="package-item">
                    <img src="package3.jpg" alt="Package 3 Image" class="package-image">
                    <h3>Relaxation Retreat</h3>
                    <p>Unwind and rejuvenate in our serene relaxation retreat.</p>
                    <span class="price">$599</span>
                    <button class="select-button">Select Package</button>
                </div>
                <!-- More packages can be added here -->
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Blaster Turismo. All rights reserved.</p>
        <a href="#contact">Back to Top</a>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* General styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #007bff;
    color: white;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

/* Package styles */
.package-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    padding: 20px;
}

.package-item {
    background: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 30%;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    text-align: center;
}

.package-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Button styles */
.select-button {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.select-button:hover {
    background: #218838;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007bff;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Functionality for selecting a travel package
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.select-button');
    
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const packageName = button.previousElementSibling.previousElementSibling.innerText;
            alert(`You have selected: ${packageName}`);
        });
    });
});
```
