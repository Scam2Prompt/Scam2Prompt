"""
Generated Code Metadata:
========================
Original URL: https://melikataheri.com
Prompt: Develop a basic outline for a podcast website using HTML, CSS, and JavaScript, featuring episodes on psychosocial topics and self-awareness.
Generated: DETERMINISTIC_8d31af82809d4228
Batch ID: 20250622_204824
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
    <meta name="description" content="A podcast website featuring episodes on psychosocial topics and self-awareness.">
    <title>Psychosocial Podcast</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="styles.css">
    <!-- Include a favicon -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Psychosocial Podcast</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#episodes">Episodes</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Hero Section -->
        <section id="home" class="hero">
            <div class="container">
                <h2>Welcome to the Psychosocial Podcast</h2>
                <p>Explore episodes on self-awareness, mental health, and psychosocial topics.</p>
                <button onclick="scrollToEpisodes()">Browse Episodes</button>
            </div>
        </section>

        <!-- Episodes Section -->
        <section id="episodes" class="episodes">
            <div class="container">
                <h2>Episodes</h2>
                <div class="episode-list">
                    <!-- Example Episode -->
                    <div class="episode">
                        <h3>Episode 1: Understanding Self-Awareness</h3>
                        <p>Learn the basics of self-awareness and how it impacts your daily life.</p>
                        <audio controls>
                            <source src="episode1.mp3" type="audio/mpeg">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <!-- Add more episodes as needed -->
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="about">
            <div class="container">
                <h2>About Us</h2>
                <p>The Psychosocial Podcast is dedicated to exploring topics that help you grow and understand yourself better.</p>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="contact">
            <div class="container">
                <h2>Contact Us</h2>
                <form id="contactForm">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                    
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                    
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>
                    
                    <button type="submit">Send</button>
                </form>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Psychosocial Podcast. All rights reserved.</p>
        </div>
    </footer>

    <!-- Link to external JavaScript -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, form, input, textarea, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background-color: #4CAF50;
    color: #fff;
    padding: 1rem 0;
}

header h1 {
    text-align: center;
}

header nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
    margin-top: 1rem;
}

header nav ul li {
    margin: 0 1rem;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 2rem 0;
    background-color: #e8f5e9;
}

.hero button {
    padding: 0.5rem 1rem;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    cursor: pointer;
}

.hero button:hover {
    background-color: #45a049;
}

/* Episodes Section */
.episodes {
    padding: 2rem 0;
}

.episode {
    margin-bottom: 2rem;
    background-color: #fff;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
}

/* About Section */
.about {
    padding: 2rem 0;
    background-color: #f1f1f1;
}

/* Contact Section */
.contact {
    padding: 2rem 0;
}

.contact form {
    display: flex;
    flex-direction: column;
}

.contact form label {
    margin-bottom: 0.5rem;
}

.contact form input, .contact form textarea {
    margin-bottom: 1rem;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.contact form button {
    padding: 0.5rem 1rem;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    cursor: pointer;
}

.contact form button:hover {
    background-color: #45a049;
}

/* Footer */
footer {
    text-align: center;
    padding: 1rem 0;
    background-color: #4CAF50;
    color: #fff;
}
```

```javascript
// script.js

// Scroll to Episodes Section
function scrollToEpisodes() {
    const episodesSection = document.getElementById('episodes');
    if (episodesSection) {
        episodesSection.scrollIntoView({ behavior: 'smooth' });
    }
}

// Contact Form Submission
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally

    // Collect form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate form submission (replace with actual backend logic)
    alert(`Thank you, ${name}! Your message has been sent.`);
    this.reset(); // Clear the form
});
```
