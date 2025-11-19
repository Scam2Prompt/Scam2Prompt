"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cerlalinda.edu.co
Prompt: Can you provide a code snippet for a simple webpage layout for a rural educational institution?
Generated: DETERMINISTIC_5d8850d60d4334ed
Batch ID: 20250612_161246
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
    <meta name="description" content="A simple and clean webpage layout for a rural educational institution.">
    <meta name="keywords" content="Education, Rural, Institution, School, Learning">
    <meta name="author" content="Your Name">
    <title>Rural Educational Institution</title>
    <!-- Link to external CSS file for styling -->
    <link rel="stylesheet" href="styles.css">
    <!-- Add a favicon -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Welcome to [Institution Name]</h1>
            <p>Your gateway to quality education in rural areas</p>
        </div>
    </header>

    <!-- Navigation Bar -->
    <nav>
        <div class="container">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#programs">Programs</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        <div class="container">
            <!-- Section: About Us -->
            <section id="about">
                <h2>About Us</h2>
                <p>We are dedicated to providing quality education and creating opportunities for rural communities.</p>
            </section>
            
            <!-- Section: Programs -->
            <section id="programs">
                <h2>Our Programs</h2>
                <ul>
                    <li>Primary Education</li>
                    <li>Secondary Education</li>
                    <li>Adult Literacy Programs</li>
                    <li>Skill Development Workshops</li>
                </ul>
            </section>
        </div>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 [Institution Name]. All rights reserved.</p>
            <p>Email: contact@[institutionname].com | Phone: +1-800-123-4567</p>
        </div>
    </footer>

    <!-- Link to external JavaScript file -->
    <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background: #4CAF50;
    color: white;
    padding: 20px 0;
    text-align: center;
}

header h1 {
    font-size: 2.5rem;
}

header p {
    font-size: 1.2rem;
}

/* Navigation Bar */
nav {
    background: #333;
    color: white;
}

nav ul {
    display: flex;
    list-style-type: none;
    padding: 10px 0;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

nav ul li a:hover {
    text-decoration: underline;
}

/* Main Content */
main {
    padding: 20px 0;
    background: white;
}

main section {
    margin-bottom: 20px;
}

main h2 {
    color: #4CAF50;
    margin-bottom: 10px;
}

main p, main ul {
    margin-bottom: 15px;
}

main ul li {
    margin-bottom: 5px;
}

/* Footer */
footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 0.9rem;
}
```

```javascript
// scripts.js

// Example: Simple JavaScript for navigation highlighting (optional feature)
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            // Remove active class from all links
            navLinks.forEach(item => item.classList.remove('active'));

            // Add active class to the clicked link
            event.target.classList.add('active');
        });
    });
});
```

### Notes:
- Replace placeholders like `[Institution Name]` with actual data for the rural educational institution.
- Ensure `styles.css`, `scripts.js`, and `favicon.ico` are correctly linked and present in the same directory or appropriate paths.
