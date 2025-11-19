"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Design a simple web page using HTML, CSS, and JavaScript to promote the Pro Integration Future Asia event, including sections for event details, registration, and exhibitor information.
Generated: DETERMINISTIC_622376f3c7a7d828
Batch ID: 20250622_212850
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
    <title>Pro Integration Future Asia</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#event-details">Event Details</a></li>
                <li><a href="#registration">Registration</a></li>
                <li><a href="#exhibitor-information">Exhibitor Information</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="event-details">
            <h1>Pro Integration Future Asia</h1>
            <h2>Event Details</h2>
            <p>Join us for the Pro Integration Future Asia event, taking place on <span id="event-date">March 15-16, 2024</span> at the <span id="event-location">Singapore Expo</span>.</p>
            <p>Discover the latest trends and innovations in integration technology, and network with industry experts and peers.</p>
        </section>
        <section id="registration">
            <h2>Registration</h2>
            <form id="registration-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="company">Company:</label>
                <input type="text" id="company" name="company" required>
                <button id="register-btn">Register Now</button>
            </form>
            <div id="registration-response"></div>
        </section>
        <section id="exhibitor-information">
            <h2>Exhibitor Information</h2>
            <p>We have a range of exhibitors showcasing their latest products and services, including:</p>
            <ul id="exhibitors">
                <!-- Exhibitor list will be populated dynamically -->
            </ul>
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

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

#registration-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#registration-form label {
    margin-bottom: 10px;
}

#registration-form input {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#register-btn {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#register-btn:hover {
    background-color: #444;
}

#exhibitors {
    list-style: none;
    margin: 0;
    padding: 0;
}

#exhibitors li {
    margin-bottom: 10px;
}
```

**script.js**
```javascript
// Populate exhibitor list dynamically
const exhibitors = [
    { name: 'Company A', description: 'Description of Company A' },
    { name: 'Company B', description: 'Description of Company B' },
    { name: 'Company C', description: 'Description of Company C' },
];

const exhibitorList = document.getElementById('exhibitors');
exhibitors.forEach((exhibitor) => {
    const listItem = document.createElement('li');
    listItem.textContent = `${exhibitor.name} - ${exhibitor.description}`;
    exhibitorList.appendChild(listItem);
});

// Handle registration form submission
const registrationForm = document.getElementById('registration-form');
const registrationResponse = document.getElementById('registration-response');

registrationForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const company = document.getElementById('company').value;

    // Simulate registration API call
    try {
        // Replace with actual API call
        console.log(`Registering ${name} from ${company} with email ${email}`);
        registrationResponse.textContent = 'Registration successful!';
        registrationResponse.style.color = 'green';
    } catch (error) {
        registrationResponse.textContent = 'Error registering. Please try again.';
        registrationResponse.style.color = 'red';
        console.error(error);
    }
});
```
