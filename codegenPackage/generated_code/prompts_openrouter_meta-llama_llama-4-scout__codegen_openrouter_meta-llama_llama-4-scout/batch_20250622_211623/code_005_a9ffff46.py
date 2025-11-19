"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Create a basic webpage template for a psychology clinic that provides information on services like psychology, neuropsychology, speech pathology, and occupational therapy.
Generated: DETERMINISTIC_a9ffff4602695f87
Batch ID: 20250622_211623
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
    <title>Psychology Clinic</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#psychology">Psychology</a></li>
                <li><a href="#neuropsychology">Neuropsychology</a></li>
                <li><a href="#speech-pathology">Speech Pathology</a></li>
                <li><a href="#occupational-therapy">Occupational Therapy</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to Our Psychology Clinic</h1>
        <p>We provide comprehensive mental health services to support your well-being.</p>
        <button>Learn More</button>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="card">
                <h3>Psychology</h3>
                <p>Our psychologists provide evidence-based therapies to address a range of mental health concerns.</p>
            </div>
            <div class="card">
                <h3>Neuropsychology</h3>
                <p>Our neuropsychologists specialize in the assessment and treatment of brain-related disorders.</p>
            </div>
            <div class="card">
                <h3>Speech Pathology</h3>
                <p>Our speech pathologists help individuals with communication and swallowing disorders.</p>
            </div>
            <div class="card">
                <h3>Occupational Therapy</h3>
                <p>Our occupational therapists support individuals in achieving independence in daily activities.</p>
            </div>
        </div>
    </section>

    <!-- Service Details Section -->
    <section id="psychology">
        <h2>Psychology Services</h2>
        <p>Our psychology services include:</p>
        <ul>
            <li>Cognitive-behavioral therapy</li>
            <li>Psychodynamic therapy</li>
            <li>Family therapy</li>
        </ul>
    </section>

    <section id="neuropsychology">
        <h2>Neuropsychology Services</h2>
        <p>Our neuropsychology services include:</p>
        <ul>
            <li>Comprehensive neuropsychological assessments</li>
            <li>Cognitive rehabilitation</li>
            <li>Memory and attention training</li>
        </ul>
    </section>

    <section id="speech-pathology">
        <h2>Speech Pathology Services</h2>
        <p>Our speech pathology services include:</p>
        <ul>
            <li>Speech and language assessments</li>
            <li>Communication therapy</li>
            <li>Swallowing assessments and therapy</li>
        </ul>
    </section>

    <section id="occupational-therapy">
        <h2>Occupational Therapy Services</h2>
        <p>Our occupational therapy services include:</p>
        <ul>
            <li>Daily living skills training</li>
            <li>Fine motor skills training</li>
            <li>Cognitive training</li>
        </ul>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Contact us to schedule an appointment or learn more about our services.</p>
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
        <p>&copy; 2023 Psychology Clinic</p>
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
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
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

#services {
    padding: 5em;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #f7f7f7;
    margin: 20px;
    padding: 20px;
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.card h3 {
    margin-top: 0;
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

// Add event listener to form submission
document.querySelector('#contact form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;

    // Basic form validation
    if (name === '' || email === '' || message === '') {
        alert('Please fill out all fields.');
        return;
    }

    // Send form data to server or handle as needed
    console.log('Form submitted:', { name, email, message });
});
```
