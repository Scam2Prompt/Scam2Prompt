"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okayvc.com
Prompt: Generate a code snippet for a website that effectively showcases branding and graphic design services, similar to the offerings of Okay Visual Creations.
Generated: DETERMINISTIC_410042bdefcfd513
Batch ID: 20250612_135906
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
    <title>Branding & Graphic Design Services</title>
    <link rel="stylesheet" href="styles.css"> <!-- Linking to external CSS for styling -->
</head>

<body>
    <header>
        <div class="container">
            <h1>Okay Visual Creations</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <div class="service">
                <h3>Brand Identity</h3>
                <p>Creating a unique and visually stunning brand identity that resonates with your target audience.</p>
            </div>
            <div class="service">
                <h3>Graphic Design</h3>
                <p>Providing high-quality graphic design services tailored to your business needs.</p>
            </div>
            <div class="service">
                <h3>Web Design</h3>
                <p>Designing user-friendly and visually appealing websites that enhance user engagement.</p>
            </div>
        </section>

        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1" />
                <h4>Project Title 1</h4>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2" />
                <h4>Project Title 2</h4>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3" />
                <h4>Project Title 3</h4>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" method="POST" action="submit_form.php">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>

                <button type="submit">Submit</button>
            </form>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Okay Visual Creations. All rights reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script> <!-- Linking to external JavaScript for interactivity -->
</body>

</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Set body font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

.header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin-left: 20px;
}

/* Main content styling */
main {
    padding: 20px;
}

section {
    margin-bottom: 40px;
}

.service {
    background: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
}

/* Portfolio item styling */
.portfolio-item {
    display: inline-block;
    margin-right: 20px;
}

/* Footer styling */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```

```javascript
// script.js

document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent default form submission

    // Collect form data
    const formData = new FormData(this);

    // Send data to the server using Fetch API
    fetch(this.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // Assuming server responds with JSON
    })
    .then(data => {
        console.log('Success:', data);
        alert('Your message has been sent successfully!');
        this.reset(); // Reset the form
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error sending your message. Please try again.');
    });
});
```
