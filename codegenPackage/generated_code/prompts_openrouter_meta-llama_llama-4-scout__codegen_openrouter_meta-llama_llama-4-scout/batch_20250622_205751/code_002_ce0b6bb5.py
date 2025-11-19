"""
Generated Code Metadata:
========================
Original URL: https://bafybeih2wl3ewsfuyky6vpzrkjfownqie7loq3mglk5wqoqifgmwyzrwre.ipfs.dweb.link
Prompt: Generate HTML/CSS code for a simple webpage that promotes an event with a registration deadline, similar to the content on this page.
Generated: DETERMINISTIC_ce0b6bb576f80024
Batch ID: 20250622_205751
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
    <title>Event Promotion</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Event Promotion</h1>
    </header>
    <main>
        <section class="event-details">
            <h2>Event Name: Conference 2024</h2>
            <p>Date: March 15-16, 2024</p>
            <p>Location: Downtown Convention Center</p>
        </section>
        <section class="registration">
            <h2>Register Now!</h2>
            <p>Don't miss out! Register by <span id="deadline">February 28, 2024</span> to secure your spot.</p>
            <form id="registration-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <button type="submit">Register</button>
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.event-details {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.registration {
    background-color: #f7f7f7;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#registration-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 0.5em;
}

input[type="text"], input[type="email"] {
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 0.5em 1em;
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
// Get the registration form and deadline elements
const registrationForm = document.getElementById('registration-form');
const deadlineElement = document.getElementById('deadline');

// Set the deadline date
const deadlineDate = new Date('2024-02-28');

// Add event listener to the registration form
registrationForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // Basic validation
    if (name && email) {
        // Send registration data to server or handle as needed
        console.log(`Registration submitted: ${name}, ${email}`);
        alert('Registration submitted successfully!');
        registrationForm.reset();
    } else {
        alert('Please fill out all fields.');
    }
});

// Update the deadline element with a formatted date
deadlineElement.textContent = deadlineDate.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
});

// Check if the deadline has passed
const today = new Date();
if (today > deadlineDate) {
    const registrationSection = document.querySelector('.registration');
    registrationSection.innerHTML = '<p>Registration deadline has passed.</p>';
}
```
