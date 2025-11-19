"""
Generated Code Metadata:
========================
Original URL: https://tokenpocketn.shop
Prompt: Generate code to create a responsive webpage layout using HTML and CSS, ensuring it adheres to SEO mobile-friendliness standards.
Generated: DETERMINISTIC_61cb9259f0682f7c
Batch ID: 20250612_151509
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
    <title>Responsive Webpage Layout</title>
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
        <section class="hero">
            <h1>Welcome to our website</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            <button>Learn More</button>
        </section>
        <section class="features">
            <h2>Our Features</h2>
            <div class="feature-cards">
                <div class="feature-card">
                    <h3>Feature 1</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </div>
                <div class="feature-card">
                    <h3>Feature 2</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </div>
                <div class="feature-card">
                    <h3>Feature 3</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Responsive Webpage Layout</p>
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

/* Mobile-Friendly Navigation */
nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    text-decoration: none;
    color: #337ab7;
}

nav a:hover {
    color: #23527c;
}

/* Hero Section */
.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    padding: 50px;
    text-align: center;
}

.hero h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

.hero p {
    margin-bottom: 20px;
}

.hero button {
    background-color: #337ab7;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.hero button:hover {
    background-color: #23527c;
}

/* Features Section */
.features {
    padding: 50px;
}

.features h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.feature-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.feature-card {
    background-color: #fff;
    padding: 20px;
    margin: 20px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.feature-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Footer */
footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
    clear: both;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .feature-card {
        width: calc(50% - 20px);
    }
}

@media only screen and (max-width: 480px) {
    .feature-card {
        width: 100%;
        margin: 10px 0;
    }
    
    .hero {
        padding: 20px;
    }
    
    .hero h1 {
        font-size: 24px;
    }
}
```
