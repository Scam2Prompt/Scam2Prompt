"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Generate a code snippet for a construction company's website, including sections for about, sectors, and contact us, with a focus on groundworks solutions and health and safety."
Generated: DETERMINISTIC_1b0f18ede2a347f5
Batch ID: 20250622_205955
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
    <title>Groundworks Solutions | Construction Company</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#sectors">Sectors</a></li>
                <li><a href="#contact-us">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Groundworks Solutions</h1>
        <p>Expert construction services for a solid foundation</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <h2>About Us</h2>
        <p>At Groundworks Solutions, we pride ourselves on delivering high-quality construction services with a focus on groundworks solutions. Our team of experts has years of experience in the industry, ensuring that every project is completed to the highest standard.</p>
        <p>We are committed to providing exceptional customer service, ensuring that our clients are satisfied with our work. Our goal is to build long-term relationships with our clients, providing them with reliable and efficient construction solutions.</p>
    </section>

    <!-- Sectors Section -->
    <section id="sectors" class="sectors">
        <h2>Sectors We Serve</h2>
        <ul>
            <li>Residential</li>
            <li>Commercial</li>
            <li>Industrial</li>
            <li>Infrastructure</li>
        </ul>
        <p>Our team has extensive experience working in various sectors, providing groundworks solutions for a wide range of projects. From residential developments to large-scale infrastructure projects, we have the expertise and equipment to deliver high-quality results.</p>
    </section>

    <!-- Health and Safety Section -->
    <section class="health-and-safety">
        <h2>Health and Safety</h2>
        <p>At Groundworks Solutions, we take health and safety seriously. Our team is trained to identify and mitigate potential hazards on site, ensuring that every project is completed safely and efficiently.</p>
        <p>We are committed to complying with all relevant health and safety regulations, ensuring that our workers and clients are protected at all times.</p>
    </section>

    <!-- Contact Us Section -->
    <section id="contact-us" class="contact-us">
        <h2>Get in Touch</h2>
        <p>Contact us today to learn more about our groundworks solutions and how we can help with your construction project.</p>
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
        <p>&copy; 2023 Groundworks Solutions. All rights reserved.</p>
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

.about {
    padding: 2em;
}

.sectors {
    padding: 2em;
}

.health-and-safety {
    padding: 2em;
}

.contact-us {
    padding: 2em;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

form {
    margin-top: 20px;
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
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #555;
}
```

```javascript
// script.js

// Get the form element
const form = document.querySelector('form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Validate form data
    if (name === '' || email === '' || message === '') {
        alert('Please fill out all fields.');
        return;
    }

    // Send the form data to the server
    fetch('/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name,
            email,
            message
        })
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        alert('Message sent successfully!');
        form.reset();
    })
    .catch((error) => {
        console.error(error);
        alert('Error sending message. Please try again.');
    });
});
```

```python
# server.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Save the message to a database or send an email
    print(f"Name: {name}, Email: {email}, Message: {message}")

    return jsonify({'message': 'Message sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
```
