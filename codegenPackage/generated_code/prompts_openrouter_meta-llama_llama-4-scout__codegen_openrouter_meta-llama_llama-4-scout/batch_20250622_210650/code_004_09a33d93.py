"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Create a basic webpage layout using HTML and CSS for a dental rehabilitation center, inspired by Tiziano Testori's website design and content organization.
Generated: DETERMINISTIC_09a33d935c1943b8
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
    <title>Dental Rehabilitation Center</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to Dental Rehabilitation Center</h1>
        <p>Providing comprehensive dental care for a healthier smile</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>Our team of experts is dedicated to providing personalized dental care</p>
        <img src="team.jpg" alt="Our Team">
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <ul>
            <li>
                <h3>Implantology</h3>
                <p>State-of-the-art implant solutions for missing teeth</p>
            </li>
            <li>
                <h3>Restorative Dentistry</h3>
                <p>Comprehensive restorative care for damaged or decayed teeth</p>
            </li>
            <li>
                <h3>Periodontics</h3>
                <p>Advanced treatment for gum disease and gum health</p>
            </li>
        </ul>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Contact us to schedule an appointment or learn more about our services</p>
        <form>
            <input type="text" placeholder="Name">
            <input type="email" placeholder="Email">
            <textarea placeholder="Message"></textarea>
            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Dental Rehabilitation Center</p>
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
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#home h1 {
    font-size: 48px;
}

/* About Styles */
#about {
    padding: 2em;
}

#about img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

/* Services Styles */
#services {
    padding: 2em;
}

#services ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

#services li {
    margin-bottom: 20px;
}

#services h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Contact Styles */
#contact {
    padding: 2em;
}

#contact form {
    max-width: 500px;
    margin: 0 auto;
}

#contact input, #contact textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#contact button {
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
