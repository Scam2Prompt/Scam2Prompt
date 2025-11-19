"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: "Design a basic web application using HTML, CSS, and JavaScript to manage membership and event registrations for a community like Easy'cap."
Generated: DETERMINISTIC_f0d6e5b84dcc47bb
Batch ID: 20250622_210650
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
  <title>Community Membership & Event Registration</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Easy'cap Community</h1>
    <nav>
      <ul>
        <li><a href="#membership">Membership</a></li>
        <li><a href="#events">Events</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <!-- Membership Section -->
    <section id="membership">
      <h2>Membership Registration</h2>
      <form id="membershipForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>
        
        <button type="submit">Register</button>
      </form>
      <div id="membershipMessage"></div>
    </section>

    <!-- Events Section -->
    <section id="events">
      <h2>Event Registration</h2>
      <form id="eventForm">
        <label for="eventName">Event Name:</label>
        <select id="eventName" name="eventName" required>
          <option value="workshop">Workshop</option>
          <option value="seminar">Seminar</option>
          <option value="networking">Networking Event</option>
        </select>
        
        <label for="participantName">Your Name:</label>
        <input type="text" id="participantName" name="participantName" required>
        
        <label for="participantEmail">Your Email:</label>
        <input type="email" id="participantEmail" name="participantEmail" required>
        
        <button type="submit">Register</button>
      </form>
      <div id="eventMessage"></div>
    </section>
  </main>

  <footer>
    <p>&copy; 2023 Easy'cap Community. All rights reserved.</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
  text-align: center;
}

header nav ul {
  list-style: none;
  padding: 0;
}

header nav ul li {
  display: inline;
  margin: 0 10px;
}

header nav ul li a {
  color: #fff;
  text-decoration: none;
}

main {
  padding: 2rem;
}

section {
  margin-bottom: 2rem;
  background: #fff;
  padding: 1rem;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

form label {
  display: block;
  margin: 0.5rem 0 0.2rem;
}

form input, form select, form button {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  background-color: #333;
  color: #fff;
  border: none;
  cursor: pointer;
}

form button:hover {
  background-color: #555;
}

footer {
  text-align: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}
```

```javascript
// script.js

// Membership Form Submission
document.getElementById('membershipForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form from submitting normally

  // Get form data
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;

  // Validate inputs (basic example)
  if (!name || !email || !phone) {
    alert('Please fill out all fields.');
    return;
  }

  // Simulate successful registration
  const message = `Thank you, ${name}! You have successfully registered as a member.`;
  document.getElementById('membershipMessage').textContent = message;

  // Clear form
  event.target.reset();
});

// Event Form Submission
document.getElementById('eventForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent form from submitting normally

  // Get form data
  const eventName = document.getElementById('eventName').value;
  const participantName = document.getElementById('participantName').value;
  const participantEmail = document.getElementById('participantEmail').value;

  // Validate inputs (basic example)
  if (!eventName || !participantName || !participantEmail) {
    alert('Please fill out all fields.');
    return;
  }

  // Simulate successful registration
  const message = `Thank you, ${participantName}! You have successfully registered for the ${eventName}.`;
  document.getElementById('eventMessage').textContent = message;

  // Clear form
  event.target.reset();
});
```
