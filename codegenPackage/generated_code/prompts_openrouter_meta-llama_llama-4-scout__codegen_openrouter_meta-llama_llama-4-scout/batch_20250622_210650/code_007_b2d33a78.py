"""
Generated Code Metadata:
========================
Original URL: https://samional.com
Prompt: "Generate code for a responsive web design that adapts to different screen sizes and devices, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_b2d33a78decfff5d
Batch ID: 20250622_210650
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
    <title>Responsive Web Design</title>
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
            <h2>Features</h2>
            <ul>
                <li>
                    <h3>Feature 1</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </li>
                <li>
                    <h3>Feature 2</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </li>
                <li>
                    <h3>Feature 3</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                </li>
            </ul>
        </section>
    </main>
    <script src="script.js"></script>
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

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.features {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.features h2 {
    margin-top: 0;
}

.features ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.features li {
    margin-bottom: 20px;
}

.features h3 {
    margin-top: 0;
}

/* Responsive Design */

/* Mobile Devices */
@media only screen and (max-width: 768px) {
    .hero {
        height: 50vh;
    }
    .hero h1 {
        font-size: 24px;
    }
}

/* Tablet Devices */
@media only screen and (min-width: 769px) and (max-width: 1024px) {
    .hero {
        height: 75vh;
    }
    .hero h1 {
        font-size: 36px;
    }
}

/* Desktop Devices */
@media only screen and (min-width: 1025px) {
    .hero {
        height: 100vh;
    }
    .hero h1 {
        font-size: 48px;
    }
}
```

**script.js**
```javascript
// Get the navigation links
const navLinks = document.querySelectorAll('header nav a');

// Add event listener to each link
navLinks.forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        // Get the target section
        const targetId = link.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        // Scroll to the target section
        targetSection.scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Get the hero section
const heroSection = document.querySelector('.hero');

// Add event listener to the learn more button
const learnMoreButton = heroSection.querySelector('button');
learnMoreButton.addEventListener('click', () => {
    // Scroll to the features section
    const featuresSection = document.querySelector('.features');
    featuresSection.scrollIntoView({
        behavior: 'smooth'
    });
});

// Handle errors
try {
    // No errors to handle
} catch (error) {
    console.error('An error occurred:', error);
}
```
