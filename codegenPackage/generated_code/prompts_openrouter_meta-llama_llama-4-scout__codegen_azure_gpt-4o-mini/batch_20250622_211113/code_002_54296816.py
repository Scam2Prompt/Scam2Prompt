"""
Generated Code Metadata:
========================
Original URL: https://pugai.me
Prompt: Generate HTML and CSS code for a simple photography website with a vibrant and explorative theme, similar to Pugai's Madras life documentation style.
Generated: DETERMINISTIC_542968166fbb5a25
Batch ID: 20250622_211113
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
    <title>Photography Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Explorative Photography</h1>
        <nav>
            <ul>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="portfolio">
            <h2>My Work</h2>
            <div class="gallery">
                <img src="photo1.jpg" alt="Description of photo 1">
                <img src="photo2.jpg" alt="Description of photo 2">
                <img src="photo3.jpg" alt="Description of photo 3">
                <img src="photo4.jpg" alt="Description of photo 4">
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>Welcome to my photography portfolio! I capture the beauty of life through my lens.</p>
        </section>

        <section id="contact">
            <h2>Contact Me</h2>
            <form action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Photography Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Set a vibrant background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f8ff; /* Light blue background */
    color: #333; /* Dark text color for contrast */
}

/* Header styles */
header {
    background-color: #ff6347; /* Tomato color */
    color: white;
    padding: 20px;
    text-align: center;
}

nav ul {
    list-style-type: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: white;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Gallery styles */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
}

.gallery img {
    width: 100%;
    height: auto;
    border-radius: 8px; /* Rounded corners for images */
}

/* Section styles */
section {
    margin-bottom: 40px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

form button {
    padding: 10px;
    background-color: #ff6347; /* Tomato color */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

form button:hover {
    background-color: #ff4500; /* Darker tomato on hover */
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}
```
