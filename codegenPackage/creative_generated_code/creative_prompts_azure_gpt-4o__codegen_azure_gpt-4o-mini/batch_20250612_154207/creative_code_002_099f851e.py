"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Generate HTML and CSS code for a photography portfolio website with a "Gallery" section showcasing wedding, maternity, and family photos, inspired by Yaisa Tangwell's services.
Generated: DETERMINISTIC_099f851ee0af8432
Batch ID: 20250612_154207
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
    <title>Photography Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Yaisa Tangwell Photography</h1>
        <nav>
            <ul>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="gallery">
            <h2>Gallery</h2>
            <div class="gallery-container">
                <div class="gallery-category" id="weddings">
                    <h3>Weddings</h3>
                    <img src="images/wedding1.jpg" alt="Wedding Photo 1">
                    <img src="images/wedding2.jpg" alt="Wedding Photo 2">
                    <img src="images/wedding3.jpg" alt="Wedding Photo 3">
                </div>
                <div class="gallery-category" id="maternity">
                    <h3>Maternity</h3>
                    <img src="images/maternity1.jpg" alt="Maternity Photo 1">
                    <img src="images/maternity2.jpg" alt="Maternity Photo 2">
                    <img src="images/maternity3.jpg" alt="Maternity Photo 3">
                </div>
                <div class="gallery-category" id="family">
                    <h3>Family</h3>
                    <img src="images/family1.jpg" alt="Family Photo 1">
                    <img src="images/family2.jpg" alt="Family Photo 2">
                    <img src="images/family3.jpg" alt="Family Photo 3">
                </div>
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>Welcome to my photography portfolio! I specialize in capturing beautiful moments for weddings, maternity, and families.</p>
        </section>

        <section id="contact">
            <h2>Contact Me</h2>
            <form action="submit_form.php" method="post">
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
        <p>&copy; 2023 Yaisa Tangwell Photography. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f8f8;
}

/* Header styles */
header {
    background: #35424a;
    color: white;
    text-align: center;
    padding: 1rem 0;
}

header h1 {
    margin-bottom: 0.5rem;
}

nav ul {
    list-style: none;
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
.gallery-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.gallery-category {
    border: 1px solid #ddd;
    padding: 10px;
    background: white;
}

.gallery-category img {
    width: 100%;
    height: auto;
    margin-bottom: 10px;
}

/* About section styles */
#about {
    background: #e2e2e2;
    padding: 20px;
    margin-top: 20px;
}

/* Contact form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    padding: 10px;
    background: #35424a;
    color: white;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #2c353e;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background: #35424a;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
