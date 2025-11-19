"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Create a simple HTML/CSS template for a wedding dress online store that offers appointment scheduling and showcases various dress styles, similar to Berny Novias."
Generated: DETERMINISTIC_6dc83fbcd96426bb
Batch ID: 20250622_210703
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
    <title>Wedding Dresses - Berny Novias Inspired</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#dresses">Dresses</a></li>
                <li><a href="#appointments">Appointments</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Wedding Dress Boutique</h1>
        <p>Discover your dream dress with us</p>
        <button>Explore Dresses</button>
    </section>

    <!-- Dresses Section -->
    <section id="dresses">
        <h2>Our Beautiful Wedding Dresses</h2>
        <div class="dress-grid">
            <div class="dress-card">
                <img src="dress1.jpg" alt="Wedding Dress 1">
                <h3>Classic Elegance</h3>
                <p>$2,500</p>
            </div>
            <div class="dress-card">
                <img src="dress2.jpg" alt="Wedding Dress 2">
                <h3>Romantic Whimsy</h3>
                <p>$3,000</p>
            </div>
            <div class="dress-card">
                <img src="dress3.jpg" alt="Wedding Dress 3">
                <h3>Modern Sophisticate</h3>
                <p>$2,800</p>
            </div>
        </div>
    </section>

    <!-- Appointments Section -->
    <section id="appointments">
        <h2>Schedule an Appointment</h2>
        <form id="appointment-form">
            <label for="name">Name:</label>
            <input type="text" id="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" required>
            <label for="date">Date:</label>
            <input type="date" id="date" required>
            <label for="time">Time:</label>
            <input type="time" id="time" required>
            <button>Schedule Appointment</button>
        </form>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>We are a team of passionate wedding dress designers and consultants dedicated to helping you find your dream dress.</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Wedding Dress Boutique</p>
    </footer>

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

/* Header Styles */
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

/* Hero Styles */
.hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #333;
}

.hero h1 {
    font-size: 48px;
}

/* Dresses Styles */
#dresses {
    padding: 2em;
}

.dress-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.dress-card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.dress-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.dress-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Appointments Styles */
#appointments {
    padding: 2em;
}

#appointment-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#appointment-form label {
    display: block;
    margin-bottom: 10px;
}

#appointment-form input {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

#appointment-form button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

**script.js**
```javascript
// Get the appointment form
const appointmentForm = document.getElementById('appointment-form');

// Add event listener to form submission
appointmentForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Validate form data
    if (name && email && date && time) {
        // Send appointment request to server (replace with actual API endpoint)
        fetch('/appointments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name,
                email,
                date,
                time
            })
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.error(error));

        // Display success message
        alert('Appointment scheduled successfully!');
    } else {
        alert('Please fill out all fields.');
    }
});
```
