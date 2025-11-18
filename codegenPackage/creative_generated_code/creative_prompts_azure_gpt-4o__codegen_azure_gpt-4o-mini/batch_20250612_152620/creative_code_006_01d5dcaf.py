"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Create a CSS template for a real estate photography portfolio page that includes sections for testimonials, a gallery, and contact information, inspired by Perth Real Estate Photography's website design.
Generated: DETERMINISTIC_01d5dcafce5f6c70
Batch ID: 20250612_152620
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
    <title>Real Estate Photography Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <h1>Real Estate Photography Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="gallery">
        <h2>Gallery</h2>
        <div class="gallery-container">
            <img src="image1.jpg" alt="Property Image 1">
            <img src="image2.jpg" alt="Property Image 2">
            <img src="image3.jpg" alt="Property Image 3">
            <img src="image4.jpg" alt="Property Image 4">
            <!-- Add more images as needed -->
        </div>
    </section>

    <section id="testimonials">
        <h2>Testimonials</h2>
        <div class="testimonial-container">
            <blockquote>
                <p>"The photos transformed our listing and helped us sell our home quickly!"</p>
                <footer>- Happy Client</footer>
            </blockquote>
            <blockquote>
                <p>"Incredible work! The photographer was professional and the results were stunning."</p>
                <footer>- Satisfied Customer</footer>
            </blockquote>
            <!-- Add more testimonials as needed -->
        </div>
    </section>

    <section id="contact">
        <h2>Contact</h2>
        <form action="submit_form.php" method="POST" id="contact-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2023 Real Estate Photography. All Rights Reserved.</p>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* Basic resets for consistent styling across browsers */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

header h1 {
    margin-bottom: 10px;
}

/* Navigation styling */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
    font-weight: bold;
}

/* Section styling */
section {
    padding: 20px;
    margin: 20px 0;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Gallery styling */
.gallery-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 10px;
}

.gallery-container img {
    width: 100%;
    border-radius: 5px;
}

/* Testimonial styling */
.testimonial-container {
    margin-top: 20px;
}

.testimonial-container blockquote {
    border-left: 4px solid #35424a;
    margin: 10px 0;
    padding-left: 20px;
    font-style: italic;
}

/* Contact form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    margin-top: 10px;
    padding: 10px;
    border: none;
    background: #35424a;
    color: #ffffff;
    cursor: pointer;
    border-radius: 5px;
}

form button:hover {
    background: #2c3e50;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
    margin-top: 20px;
}
```
