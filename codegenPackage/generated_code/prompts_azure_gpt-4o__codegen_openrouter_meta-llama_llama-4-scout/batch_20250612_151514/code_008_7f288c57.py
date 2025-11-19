"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Generate HTML and CSS code to design a responsive webpage that showcases the boats available for rental, including images and descriptions for each boat (e.g., "Heart Craft 410").
Generated: DETERMINISTIC_7f288c57a8bb2f31
Batch ID: 20250612_151514
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
    <title>Boat Rental</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="boats">
            <h1>Available Boats</h1>
            <div class="boat-grid">
                <!-- Boat 1 -->
                <div class="boat">
                    <img src="images/heart-craft-410.jpg" alt="Heart Craft 410">
                    <h2>Heart Craft 410</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                    <button>Rental Information</button>
                </div>
                <!-- Boat 2 -->
                <div class="boat">
                    <img src="images/boat-2.jpg" alt="Boat 2">
                    <h2>Boat 2</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                    <button>Rental Information</button>
                </div>
                <!-- Boat 3 -->
                <div class="boat">
                    <img src="images/boat-3.jpg" alt="Boat 3">
                    <h2>Boat 3</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                    <button>Rental Information</button>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Boat Rental</p>
    </footer>
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

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.boats {
    background-color: #fff;
    padding: 2em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.boat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    grid-gap: 20px;
}

.boat {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1em;
    border: 1px solid #ddd;
}

.boat img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

.boat h2 {
    font-size: 1.5em;
    margin-bottom: 10px;
}

.boat p {
    font-size: 1em;
    margin-bottom: 20px;
}

.boat button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .boat-grid {
        grid-template-columns: 1fr;
    }
}

@media only screen and (max-width: 480px) {
    .boat img {
        height: 150px;
    }
}
```
