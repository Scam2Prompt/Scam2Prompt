"""
Generated Code Metadata:
========================
Original URL: https://webbcode.com
Prompt: Create a website design template in HTML and CSS that aligns with WebbCode Ltd's focus on UI/UX design and tailored solutions for clients.
Generated: DETERMINISTIC_6f7fd9024ae88429
Batch ID: 20250612_153225
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
    <title>WebbCode Ltd - UI/UX Design Solutions</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>WebbCode Ltd</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="hero">
            <div class="container">
                <h2>Your Partner in UI/UX Design</h2>
                <p>Tailored solutions for your business needs.</p>
                <a href="#contact" class="cta-button">Get Started</a>
            </div>
        </section>

        <section id="services">
            <div class="container">
                <h2>Our Services</h2>
                <div class="service">
                    <h3>UI Design</h3>
                    <p>Creating intuitive and engaging user interfaces.</p>
                </div>
                <div class="service">
                    <h3>UX Research</h3>
                    <p>Understanding user needs to enhance experience.</p>
                </div>
                <div class="service">
                    <h3>Web Development</h3>
                    <p>Building responsive and functional websites.</p>
                </div>
            </div>
        </section>

        <section id="portfolio">
            <div class="container">
                <h2>Our Portfolio</h2>
                <p>Check out some of our recent projects.</p>
                <div class="portfolio-item">
                    <img src="project1.jpg" alt="Project 1">
                    <h3>Project Title 1</h3>
                </div>
                <div class="portfolio-item">
                    <img src="project2.jpg" alt="Project 2">
                    <h3>Project Title 2</h3>
                </div>
                <div class="portfolio-item">
                    <img src="project3.jpg" alt="Project 3">
                    <h3>Project Title 3</h3>
                </div>
            </div>
        </section>

        <section id="about">
            <div class="container">
                <h2>About Us</h2>
                <p>We are a team of passionate designers and developers dedicated to creating exceptional user experiences.</p>
            </div>
        </section>

        <section id="contact">
            <div class="container">
                <h2>Contact Us</h2>
                <form id="contact-form" action="submit_form.php" method="POST">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                    
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                    
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>
                    
                    <button type="submit">Send Message</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 WebbCode Ltd. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Container for layout */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Hero section styles */
#hero {
    background: #f4f4f4;
    padding: 50px 0;
    text-align: center;
}

.cta-button {
    background: #007BFF;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* Services section styles */
#services {
    padding: 20px 0;
    text-align: center;
}

.service {
    margin: 20px 0;
}

/* Portfolio section styles */
#portfolio {
    padding: 20px 0;
    text-align: center;
}

.portfolio-item {
    display: inline-block;
    margin: 10px;
}

/* About section styles */
#about {
    padding: 20px 0;
    text-align: center;
}

/* Contact section styles */
#contact {
    padding: 20px 0;
    text-align: center;
}

form {
    max-width: 600px;
    margin: auto;
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
}

form button {
    background: #007BFF;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
}

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```
