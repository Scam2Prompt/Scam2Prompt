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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebbCode Ltd - UI/UX Design & Development</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to WebbCode Ltd</h1>
        <p>We specialize in UI/UX design and tailored solutions for clients.</p>
        <button>Discover More</button>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="card">
                <h3>UI/UX Design</h3>
                <p>We craft intuitive and visually appealing interfaces.</p>
            </div>
            <div class="card">
                <h3>Web Development</h3>
                <p>Our team builds scalable and efficient web applications.</p>
            </div>
            <div class="card">
                <h3>Digital Marketing</h3>
                <p>We help you reach your target audience and grow your business.</p>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio">
        <h2>Our Portfolio</h2>
        <div class="portfolio-grid">
            <div class="project">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project 1</h3>
                <p>A brief description of project 1.</p>
            </div>
            <div class="project">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project 2</h3>
                <p>A brief description of project 2.</p>
            </div>
            <div class="project">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project 3</h3>
                <p>A brief description of project 3.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message"></textarea><br><br>
            <input type="submit" value="Send">
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 WebbCode Ltd. All rights reserved.</p>
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

/* Header Styles */
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

/* Hero Styles */
#home {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 5em;
    text-align: center;
}

#home h1 {
    font-size: 36px;
}

#home button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

/* Services Styles */
#services {
    padding: 5em;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #fff;
    padding: 20px;
    margin: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: calc(33.33% - 20px);
}

.card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Portfolio Styles */
#portfolio {
    padding: 5em;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Contact Styles */
#contact {
    padding: 5em;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
