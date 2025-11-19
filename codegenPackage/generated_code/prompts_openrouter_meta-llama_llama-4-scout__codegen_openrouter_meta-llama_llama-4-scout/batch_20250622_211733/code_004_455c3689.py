"""
Generated Code Metadata:
========================
Original URL: https://starplumbingelectrical.com
Prompt: "Create a plumbing services website using HTML, CSS, and JavaScript, incorporating features and services from Certified Plumbers Graham, TX."
Generated: DETERMINISTIC_455c3689fa7a7d73
Batch ID: 20250622_211733
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
    <title>Certified Plumbers Graham, TX</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="home">
            <h1>Welcome to Certified Plumbers Graham, TX</h1>
            <p>We offer a wide range of plumbing services to residents and businesses in Graham, TX.</p>
            <button>Learn More</button>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Emergency Plumbing Repairs</li>
                <li>Drain Cleaning</li>
                <li>Water Heater Installation</li>
                <li>Toilet Installation</li>
                <li>Kitchen and Bathroom Fixtures</li>
            </ul>
        </section>
        <section id="about">
            <h2>About Us</h2>
            <p>Our team of certified plumbers has years of experience serving the Graham, TX community. We pride ourselves on providing excellent customer service and quality workmanship.</p>
        </section>
        <section id="contact">
            <h2>Get in Touch</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br><br>
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone"><br><br>
                <label for="message">Message:</label>
                <textarea id="message" name="message"></textarea><br><br>
                <button id="submit-btn">Send</button>
            </form>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
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

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

#contact-form {
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}
```

**script.js**
```javascript
// Get the contact form element
const contactForm = document.getElementById('contact-form');

// Add event listener to the submit button
document.getElementById('submit-btn').addEventListener('click', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    // Validate form data
    if (name === '' || email === '' || phone === '' || message === '') {
        alert('Please fill out all fields.');
        return;
    }

    // Send form data to server or email
    try {
        // Use fetch API to send data to server
        fetch('/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name,
                email,
                phone,
                message
            })
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                alert('Message sent successfully!');
                contactForm.reset();
            } else {
                alert('Error sending message. Please try again.');
            }
        })
        .catch((error) => {
            console.error(error);
            alert('Error sending message. Please try again.');
        });
    } catch (error) {
        console.error(error);
        alert('Error sending message. Please try again.');
    }
});
```

**server.js** (optional, for sending form data to server)
```javascript
const express = require('express');
const app = express();
const nodemailer = require('nodemailer');

app.use(express.json());

app.post('/contact', (req, res) => {
    const { name, email, phone, message } = req.body;

    // Set up nodemailer transporter
    const transporter = nodemailer.createTransport({
        host: 'smtp.example.com',
        port: 587,
        auth: {
            user: 'your-email@example.com',
            pass: 'your-password'
        }
    });

    // Send email
    const mailOptions = {
        from: email,
        to: 'your-email@example.com',
        subject: `Message from ${name}`,
        text: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nMessage: ${message}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            res.json({ success: false });
        } else {
            console.log(`Email sent: ${info.response}`);
            res.json({ success: true });
        }
    });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
