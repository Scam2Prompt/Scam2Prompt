"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Design a layout for a corporate website that incorporates a news feed, photo gallery, and contact form, using Ra-Don's services.
Generated: DETERMINISTIC_293754a8e11a8c0e
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**corporate_website.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corporate Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#news">News</a></li>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="news">
            <h1>News Feed</h1>
            <div class="news-container">
                <!-- News feed will be populated dynamically -->
            </div>
        </section>
        <section id="gallery">
            <h1>Photo Gallery</h1>
            <div class="gallery-container">
                <!-- Gallery will be populated dynamically -->
            </div>
        </section>
        <section id="contact">
            <h1>Contact Us</h1>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                <button type="submit">Send</button>
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

h1 {
    margin-top: 0;
}

.news-container, .gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.news-item, .gallery-item {
    margin: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#contact-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 10px;
}

input, textarea {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #444;
}
```

**script.js**
```javascript
// News feed data
const newsFeed = [
    { title: 'News Item 1', description: 'This is a news item' },
    { title: 'News Item 2', description: 'This is another news item' },
    // Add more news items here
];

// Gallery data
const gallery = [
    { image: 'image1.jpg', description: 'This is an image' },
    { image: 'image2.jpg', description: 'This is another image' },
    // Add more gallery items here
];

// Populate news feed
const newsContainer = document.querySelector('.news-container');
newsFeed.forEach((newsItem) => {
    const newsElement = document.createElement('div');
    newsElement.classList.add('news-item');
    newsElement.innerHTML = `
        <h2>${newsItem.title}</h2>
        <p>${newsItem.description}</p>
    `;
    newsContainer.appendChild(newsElement);
});

// Populate gallery
const galleryContainer = document.querySelector('.gallery-container');
gallery.forEach((galleryItem) => {
    const galleryElement = document.createElement('div');
    galleryElement.classList.add('gallery-item');
    galleryElement.innerHTML = `
        <img src="${galleryItem.image}" alt="${galleryItem.description}">
        <p>${galleryItem.description}</p>
    `;
    galleryContainer.appendChild(galleryElement);
});

// Contact form submission handler
const contactForm = document.getElementById('contact-form');
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Send data to server using fetch API
    fetch('/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, message })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Contact form submission handler
app.post('/contact', (req, res) => {
    const { name, email, message } = req.body;
    console.log(`Received contact form submission from ${name} (${email}): ${message}`);
    res.json({ message: 'Form submitted successfully' });
});

// Serve static files
app.use(express.static('public'));

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
