"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Generate a code snippet to create a simple web page for quoting and reserving outdoor advertising locations, similar to the functionality provided by WOW MEDIA."
Generated: DETERMINISTIC_3cf70e4eacb4a121
Batch ID: 20250622_211633
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
  <title>Outdoor Advertising Reservation</title>
  <link rel="stylesheet" href="styles.css">
  <script src="script.js" defer></script>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Outdoor Advertising Reservation</h1>
    <p>Find and reserve the perfect location for your advertisement.</p>
  </header>

  <!-- Main Content Section -->
  <main>
    <!-- Form for Quoting and Reserving Locations -->
    <section id="reservation-form">
      <h2>Get a Quote & Reserve</h2>
      <form id="quoteForm">
        <!-- Location Selection -->
        <label for="location">Select Location:</label>
        <select id="location" name="location" required>
          <option value="">-- Choose a Location --</option>
          <option value="downtown">Downtown</option>
          <option value="highway">Highway</option>
          <option value="suburbs">Suburbs</option>
        </select>

        <!-- Date Selection -->
        <label for="startDate">Start Date:</label>
        <input type="date" id="startDate" name="startDate" required>

        <label for="endDate">End Date:</label>
        <input type="date" id="endDate" name="endDate" required>

        <!-- Budget Input -->
        <label for="budget">Budget ($):</label>
        <input type="number" id="budget" name="budget" min="100" required>

        <!-- Submit Button -->
        <button type="submit">Get Quote</button>
      </form>
    </section>

    <!-- Quote Display Section -->
    <section id="quoteDisplay" style="display: none;">
      <h2>Your Quote</h2>
      <p id="quoteDetails"></p>
      <button id="reserveButton">Reserve Now</button>
    </section>
  </main>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Outdoor Advertising Co. All rights reserved.</p>
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
  background-color: #f4f4f4;
}

header {
  background-color: #333;
  color: #fff;
  padding: 20px;
  text-align: center;
}

main {
  padding: 20px;
}

footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
  position: fixed;
  bottom: 0;
  width: 100%;
}

/* Form Styles */
form {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin: 10px 0 5px;
}

input, select, button {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  background-color: #333;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #555;
}
```

```javascript
// script.js

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  const quoteForm = document.getElementById('quoteForm');
  const quoteDisplay = document.getElementById('quoteDisplay');
  const quoteDetails = document.getElementById('quoteDetails');
  const reserveButton = document.getElementById('reserveButton');

  // Handle form submission
  quoteForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form from refreshing the page

    // Gather form data
    const location = document.getElementById('location').value;
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const budget = document.getElementById('budget').value;

    // Validate inputs
    if (!location || !startDate || !endDate || !budget) {
      alert('Please fill out all fields.');
      return;
    }

    // Generate a quote (mock calculation for demonstration purposes)
    const quote = `Location: ${location}, Start Date: ${startDate}, End Date: ${endDate}, Budget: $${budget}`;

    // Display the quote
    quoteDetails.textContent = quote;
    quoteDisplay.style.display = 'block';
  });

  // Handle reservation button click
  reserveButton.addEventListener('click', () => {
    alert('Reservation successful! Thank you for choosing us.');
    quoteDisplay.style.display = 'none';
    quoteForm.reset();
  });
});
```
