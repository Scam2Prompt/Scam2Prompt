"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Generate a code snippet in JavaScript and HTML5 for a simple web application that showcases a company's services, similar to those offered by dionlineaja.id.
Generated: DETERMINISTIC_8f864add791305fc
Batch ID: 20250622_210316
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
    <title>Company Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="services">
            <h1>Our Services</h1>
            <div class="service-cards">
                <!-- Services will be rendered here -->
            </div>
        </section>
        <section id="about">
            <h1>About Us</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        </section>
        <section id="contact">
            <h1>Get in Touch</h1>
            <form id="contact-form">
                <input type="text" name="name" placeholder="Name">
                <input type="email" name="email" placeholder="Email">
                <textarea name="message" placeholder="Message"></textarea>
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

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.service-card {
    background-color: #f7f7f7;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 1em;
    margin: 1em;
    width: 200px;
}

.service-card h2 {
    margin-top: 0;
}

#contact-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#contact-form input, #contact-form textarea {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#contact-form button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#contact-form button[type="submit"]:hover {
    background-color: #444;
}
```

**script.js**
```javascript
// Define services data
const services = [
    { id: 1, title: "Service 1", description: "This is service 1" },
    { id: 2, title: "Service 2", description: "This is service 2" },
    { id: 3, title: "Service 3", description: "This is service 3" },
];

// Render services
const serviceCardsContainer = document.querySelector(".service-cards");
services.forEach((service) => {
    const serviceCard = document.createElement("div");
    serviceCard.classList.add("service-card");
    serviceCard.innerHTML = `
        <h2>${service.title}</h2>
        <p>${service.description}</p>
    `;
    serviceCardsContainer.appendChild(serviceCard);
});

// Handle contact form submission
const contactForm = document.getElementById("contact-form");
contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.querySelector("input[name='name']").value;
    const email = document.querySelector("input[name='email']").value;
    const message = document.querySelector("textarea[name='message']").value;

    // Basic validation
    if (!name || !email || !message) {
        alert("Please fill in all fields");
        return;
    }

    // Send data to server or handle as needed
    console.log("Form submitted:", { name, email, message });
    contactForm.reset();
});
```
