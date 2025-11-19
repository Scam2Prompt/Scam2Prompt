"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Write HTML5 and CSS3 code for a corporate design webpage that includes sections for "About Us," "Clients," and "Contact," similar to the structure described on dionlineaja.id.
Generated: DETERMINISTIC_58a3ff9fb18d919e
Batch ID: 20250612_152739
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
    <title>Corporate Design</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#clients">Clients</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Corporate Design</h1>
        <p>We create innovative solutions for our clients.</p>
        <button>Learn More</button>
    </section>

    <!-- About Us Section -->
    <section id="about" class="about">
        <h2>About Us</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <div class="team">
            <div class="team-member">
                <img src="team-member-1.jpg" alt="Team Member 1">
                <h3>John Doe</h3>
                <p>CEO & Founder</p>
            </div>
            <div class="team-member">
                <img src="team-member-2.jpg" alt="Team Member 2">
                <h3>Jane Doe</h3>
                <p>Creative Director</p>
            </div>
        </div>
    </section>

    <!-- Clients Section -->
    <section id="clients" class="clients">
        <h2>Our Clients</h2>
        <ul>
            <li><img src="client-1.png" alt="Client 1"></li>
            <li><img src="client-2.png" alt="Client 2"></li>
            <li><img src="client-3.png" alt="Client 3"></li>
        </ul>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Get in Touch</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <form>
            <input type="text" name="name" placeholder="Name">
            <input type="email" name="email" placeholder="Email">
            <textarea name="message" placeholder="Message"></textarea>
            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Corporate Design</p>
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

/* About Us Styles */
.about {
    padding: 2em;
}

.about h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.team {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.team-member {
    margin: 20px;
    width: calc(50% - 20px);
    text-align: center;
}

.team-member img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

/* Clients Styles */
.clients {
    padding: 2em;
    background-color: #fff;
}

.clients h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.clients ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.clients li {
    margin: 20px;
}

/* Contact Styles */
.contact {
    padding: 2em;
    background-color: #f7f7f7;
}

.contact h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.contact form {
    max-width: 500px;
    margin: 0 auto;
}

.contact input, .contact textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

.contact button {
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
