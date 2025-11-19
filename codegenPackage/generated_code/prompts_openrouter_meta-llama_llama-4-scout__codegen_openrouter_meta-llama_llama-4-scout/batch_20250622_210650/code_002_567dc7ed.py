"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Generate a sample HTML and CSS code for a lawyer's website, incorporating features like a gallery section, similar to fachriahyani.com, and a responsive design for various devices.
Generated: DETERMINISTIC_567dc7ed96f46c6c
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
    <title>Lawyer's Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to Our Law Firm</h1>
        <p>Providing expert legal services for over 10 years.</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
    </section>

    <!-- Gallery Section -->
    <section id="gallery">
        <h2>Our Gallery</h2>
        <div class="gallery-container">
            <div class="gallery-item">
                <img src="image1.jpg" alt="Image 1">
                <p>Image 1 Description</p>
            </div>
            <div class="gallery-item">
                <img src="image2.jpg" alt="Image 2">
                <p>Image 2 Description</p>
            </div>
            <div class="gallery-item">
                <img src="image3.jpg" alt="Image 3">
                <p>Image 3 Description</p>
            </div>
            <!-- Add more gallery items here -->
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <form>
            <input type="text" placeholder="Name">
            <input type="email" placeholder="Email">
            <textarea placeholder="Message"></textarea>
            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Lawyer's Website</p>
    </footer>

    <!-- Script Section -->
    <script src="script.js"></script>
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

header nav a:hover {
    color: #ccc;
}

/* Hero Section Styles */
#home {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#home h1 {
    font-size: 48px;
}

#home p {
    font-size: 18px;
}

#home button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

#home button:hover {
    background-color: #555;
}

/* About Section Styles */
#about {
    padding: 2em;
}

#about h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

#about p {
    font-size: 16px;
}

/* Gallery Section Styles */
#gallery {
    padding: 2em;
}

#gallery h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery-item {
    margin: 10px;
    width: calc(33.33% - 20px);
}

.gallery-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.gallery-item p {
    font-size: 14px;
    margin-top: 10px;
}

/* Contact Section Styles */
#contact {
    padding: 2em;
}

#contact h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

#contact p {
    font-size: 16px;
}

#contact form {
    display: flex;
    flex-direction: column;
    align-items: center;
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
    font-size: 18px;
    cursor: pointer;
}

#contact button:hover {
    background-color: #555;
}

/* Footer Section Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .gallery-item {
        width: calc(50% - 20px);
    }
}

@media only screen and (max-width: 480px) {
    .gallery-item {
        width: 100%;
    }
    #home h1 {
        font-size: 36px;
    }
    #home p {
        font-size: 14px;
    }
}
```

**script.js**
```javascript
// Add event listener to gallery images
const galleryItems = document.querySelectorAll('.gallery-item');

galleryItems.forEach((item) => {
    item.addEventListener('mouseover', () => {
        item.style.transform = 'scale(1.1)';
    });

    item.addEventListener('mouseout', () => {
        item.style.transform = 'scale(1)';
    });
});

// Add event listener to contact form submission
const contactForm = document.querySelector('#contact form');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // Add form submission logic here
    console.log('Form submitted');
});
```
