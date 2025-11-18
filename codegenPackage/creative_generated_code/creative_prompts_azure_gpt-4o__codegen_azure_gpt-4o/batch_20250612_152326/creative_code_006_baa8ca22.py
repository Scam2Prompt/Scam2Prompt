"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Create HTML and CSS code for a festival webpage that highlights the celestial theme, featuring sections for event descriptions, ticket purchasing, and application forms.
Generated: DETERMINISTIC_baa8ca222cb8fffa
Batch ID: 20250612_152326
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
  <title>Celestial Festival</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <h1>Celestial Festival 2023</h1>
    <p>Celebrate the stars, the cosmos, and the celestial wonders!</p>
  </header>

  <!-- Event Description Section -->
  <section class="event-description">
    <h2>About the Festival</h2>
    <p>
      The Celestial Festival is an annual event dedicated to exploring the beauty of the cosmos. 
      Join us for stargazing, astronomy workshops, art exhibits, and more!
    </p>
  </section>

  <!-- Ticket Purchasing Section -->
  <section class="tickets">
    <h2>Get Your Tickets</h2>
    <p>Reserve your spot today and be part of the celestial magic.</p>
    <button onclick="alert('Tickets purchased successfully!')">Buy Tickets</button>
  </section>

  <!-- Application Form Section -->
  <section class="application-form">
    <h2>Volunteer Application</h2>
    <form id="volunteerForm" action="/submit" method="POST">
      <!-- Name Field -->
      <label for="name">Name:</label>
      <input type="text" id="name" name="name" required>
      
      <!-- Email Field -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" required>
      
      <!-- Role Selection -->
      <label for="role">Preferred Volunteer Role:</label>
      <select id="role" name="role" required>
        <option value="stargazing">Stargazing Assistant</option>
        <option value="workshop">Workshop Coordinator</option>
        <option value="art">Art Exhibit Helper</option>
        <option value="general">General Volunteer</option>
      </select>
      
      <!-- Submit Button -->
      <button type="submit">Apply</button>
    </form>
  </section>

  <!-- Footer Section -->
  <footer class="footer">
    <p>© 2023 Celestial Festival. All rights reserved.</p>
  </footer>
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
  background-color: #121212;
  color: #f0f0f0;
  line-height: 1.6;
}

/* Header Section */
.header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(to bottom, #000428, #004e92); /* Celestial-themed gradient */
  color: white;
}

.header h1 {
  font-size: 2.5em;
}

.header p {
  font-size: 1.2em;
}

/* Event Description Section */
.event-description {
  padding: 20px;
  margin: 20px auto;
  max-width: 800px;
  text-align: center;
}

.event-description h2 {
  font-size: 2em;
  margin-bottom: 10px;
}

/* Ticket Purchasing Section */
.tickets {
  padding: 20px;
  text-align: center;
}

.tickets h2 {
  font-size: 2em;
  margin-bottom: 10px;
}

.tickets button {
  background-color: #00c6ff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 1em;
}

.tickets button:hover {
  background-color: #007acc;
}

/* Application Form Section */
.application-form {
  padding: 20px;
  margin: 20px auto;
  max-width: 800px;
}

.application-form h2 {
  font-size: 2em;
  margin-bottom: 10px;
}

.application-form label {
  display: block;
  margin: 10px 0 5px;
}

.application-form input, .application-form select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.application-form button {
  background-color: #00c6ff;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 1em;
}

.application-form button:hover {
  background-color: #007acc;
}

/* Footer Section */
.footer {
  text-align: center;
  padding: 20px;
  background-color: #000428;
  color: white;
}
```
