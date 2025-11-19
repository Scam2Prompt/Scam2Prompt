"""
Generated Code Metadata:
========================
Original URL: https://berang.vercel.app
Prompt: Generate HTML and CSS code for a basic layout of a parts catalog webpage, inspired by Beerang Parts.
Generated: DETERMINISTIC_c1568273e2aa6bfb
Batch ID: 20250622_211011
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/150": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
    <title>Parts Catalog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#all-parts">All Parts</a></li>
                <li><a href="#search-parts">Search Parts</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Welcome to our Parts Catalog</h1>
            <p>Find the parts you need quickly and easily</p>
            <button>Search Parts</button>
        </section>
        <section id="all-parts">
            <h2>All Parts</h2>
            <div class="parts-grid">
                <!-- parts will be generated dynamically -->
                <div class="part-card">
                    <img src="https://via.placeholder.com/150" alt="Part Image">
                    <h3>Part Name</h3>
                    <p>Part Description</p>
                    <p>Part Number: <span>ABC123</span></p>
                </div>
                <div class="part-card">
                    <img src="https://via.placeholder.com/150" alt="Part Image">
                    <h3>Part Name</h3>
                    <p>Part Description</p>
                    <p>Part Number: <span>DEF456</span></p>
                </div>
            </div>
        </section>
        <section id="search-parts">
            <h2>Search Parts</h2>
            <form>
                <input type="text" placeholder="Search by part number or name">
                <button>Search</button>
            </form>
            <div class="search-results">
                <!-- search results will be generated dynamically -->
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Parts Catalog</p>
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

section {
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#hero {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 5em;
    text-align: center;
}

#hero button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.parts-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.part-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 1em;
}

.part-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.part-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
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
    .parts-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media only screen and (max-width: 480px) {
    .parts-grid {
        grid-template-columns: 1fr;
    }
}
```
