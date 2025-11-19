"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: "Design a graphic design portfolio for a client in Addis Ababa, Ethiopia, showcasing their brand message and trustworthiness."
Generated: DETERMINISTIC_82fae1576cefc750
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
    <title>Addis Ababa Graphic Design Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to Our Graphic Design Portfolio</h1>
        <p>Based in Addis Ababa, Ethiopia, we create stunning designs that showcase your brand message and trustworthiness.</p>
        <button>Discover More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>We are a team of experienced graphic designers dedicated to delivering high-quality designs that exceed our clients' expectations.</p>
        <p>Our mission is to help businesses in Addis Ababa and beyond establish a strong brand identity that resonates with their target audience.</p>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio">
        <h2>Our Portfolio</h2>
        <div class="portfolio-grid">
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project 1: Brand Identity for Ethiopian Coffee Shop</h3>
                <p>Created a unique brand identity for a local coffee shop in Addis Ababa, including logo design, business cards, and menu design.</p>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project 2: Marketing Materials for Ethiopian Fashion Brand</h3>
                <p>Designed a range of marketing materials, including brochures, flyers, and social media graphics, for a fashion brand based in Addis Ababa.</p>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project 3: Website Design for Ethiopian Non-Profit Organization</h3>
                <p>Created a user-friendly website for a non-profit organization in Addis Ababa, including custom graphics and a responsive design.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Have a project in mind? We'd love to hear from you!</p>
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
        <p>&copy; 2023 Addis Ababa Graphic Design Portfolio</p>
    </footer>

    <script src="script.js"></script>
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

#home {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    padding: 5em;
    text-align: center;
}

#home button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#about {
    padding: 5em;
}

#portfolio {
    padding: 5em;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.portfolio-item {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
}

.portfolio-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

#contact {
    padding: 5em;
}

form {
    max-width: 500px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 20px;
    padding: 10px;
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

// Add event listener to the button in the hero section
document.querySelector('#home button').addEventListener('click', () => {
    // Scroll to the portfolio section
    document.querySelector('#portfolio').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to the form submission
document.querySelector('#contact form').addEventListener('submit', (e) => {
    e.preventDefault();
    // Get the form data
    const formData = new FormData(e.target);
    // Send the form data to the server using fetch API
    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```
