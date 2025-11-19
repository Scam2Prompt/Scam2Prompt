"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: "Create a template for a company's about page that highlights their mission, vision, and team expertise in web design, development, and marketing."
Generated: DETERMINISTIC_1cc95f19a3b12c49
Batch ID: 20250622_210655
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
    <title>About Us</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#mission">Mission</a></li>
                <li><a href="#vision">Vision</a></li>
                <li><a href="#team">Team</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="mission">
            <h1>Our Mission</h1>
            <p>At [Company Name], our mission is to deliver innovative web solutions that exceed our clients' expectations. We strive to build long-lasting relationships with our clients, providing them with the tools and expertise needed to succeed in the digital landscape.</p>
        </section>
        <section id="vision">
            <h1>Our Vision</h1>
            <p>Our vision is to be a leading provider of web design, development, and marketing services. We aim to stay at the forefront of industry trends, leveraging the latest technologies to drive business growth and success for our clients.</p>
        </section>
        <section id="team">
            <h1>Meet Our Team</h1>
            <div class="team-members">
                <div class="team-member">
                    <img src="team-member-1.jpg" alt="Team Member 1">
                    <h2>John Doe</h2>
                    <p>Web Design Lead</p>
                    <p>With 5+ years of experience in web design, John leads our design team in creating visually stunning and user-friendly interfaces.</p>
                </div>
                <div class="team-member">
                    <img src="team-member-2.jpg" alt="Team Member 2">
                    <h2>Jane Smith</h2>
                    <p>Web Development Lead</p>
                    <p>Jane has 8+ years of experience in web development, leading our development team in building scalable and efficient web applications.</p>
                </div>
                <div class="team-member">
                    <img src="team-member-3.jpg" alt="Team Member 3">
                    <h2>Bob Johnson</h2>
                    <p>Marketing Lead</p>
                    <p>With a background in marketing, Bob leads our marketing team in developing and executing strategies to drive business growth and engagement.</p>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; [Company Name] 2023</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
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
}

header nav ul li {
    display: inline-block;
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
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-top: 0;
}

.team-members {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.team-member {
    margin: 20px;
    width: calc(33.33% - 20px);
    text-align: center;
}

.team-member img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to navigation links
document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll('header nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            targetSection.scrollIntoView({ behavior: 'smooth' });
        });
    });
});
```
