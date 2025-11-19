"""
Generated Code Metadata:
========================
Original URL: https://foundation-lido.org
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display information about a recent sports event or tournament.
Generated: DETERMINISTIC_6e94625d4156d580
Batch ID: 20250622_211850
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
  <meta name="description" content="Sports Event Information">
  <title>Sports Event</title>
  <!-- Link to external CSS -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header section -->
  <header>
    <h1>Recent Sports Event: Championship Finals</h1>
  </header>

  <!-- Main content section -->
  <main>
    <section id="event-details">
      <h2>Event Details</h2>
      <p>Date: <span id="event-date"></span></p>
      <p>Location: <span id="event-location"></span></p>
      <p>Winner: <span id="event-winner"></span></p>
    </section>

    <!-- Button to fetch event details -->
    <button id="fetch-details">Get Event Details</button>
  </main>

  <!-- Footer section -->
  <footer>
    <p>&copy; 2023 Sports Event Info</p>
  </footer>

  <!-- Link to external JavaScript -->
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
  color: #333;
}

/* Header styles */
header {
  background-color: #007bff;
  color: white;
  padding: 20px;
  text-align: center;
}

/* Main content styles */
main {
  padding: 20px;
}

section {
  background: white;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

/* Footer styles */
footer {
  text-align: center;
  padding: 10px;
  background-color: #007bff;
  color: white;
  position: fixed;
  bottom: 0;
  width: 100%;
}
```

```javascript
// script.js

// Event details (mock data)
const eventData = {
  date: "October 15, 2023",
  location: "National Stadium, Cityville",
  winner: "Team A"
};

// Function to populate event details
function populateEventDetails() {
  try {
    // Get elements by ID
    const dateElement = document.getElementById("event-date");
    const locationElement = document.getElementById("event-location");
    const winnerElement = document.getElementById("event-winner");

    // Populate elements with data
    dateElement.textContent = eventData.date;
    locationElement.textContent = eventData.location;
    winnerElement.textContent = eventData.winner;
  } catch (error) {
    console.error("Error populating event details:", error);
    alert("An error occurred while fetching event details.");
  }
}

// Add event listener to button
document.getElementById("fetch-details").addEventListener("click", populateEventDetails);
```
