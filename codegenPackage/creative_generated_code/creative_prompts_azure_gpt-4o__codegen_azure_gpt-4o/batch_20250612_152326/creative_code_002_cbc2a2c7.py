"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Generate JavaScript code for a webpage that dynamically displays upcoming events with details like date, location, and theme, similar to the "Road to Celestia" event list.
Generated: DETERMINISTIC_cbc2a2c7d8d6c0d0
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the webpage
document.body.innerHTML = `
  <header>
    <h1>Upcoming Events</h1>
  </header>
  <main>
    <section id="event-list"></section>
  </main>
  <footer>
    <p>&copy; 2023 Event Manager</p>
  </footer>
`;

// JavaScript to dynamically generate and display events

// Event data (can be replaced with fetched data from an API)
const events = [
  {
    name: "Road to Celestia",
    date: "2023-11-15",
    location: "New York, NY",
    theme: "Adventure & Exploration",
  },
  {
    name: "Tech Fusion Conference",
    date: "2023-12-05",
    location: "San Francisco, CA",
    theme: "Innovation in Technology",
  },
  {
    name: "Art & Soul Festival",
    date: "2024-01-20",
    location: "Austin, TX",
    theme: "Creativity & Expression",
  },
];

// Function to format the event date
function formatDate(dateString) {
  try {
    const options = { year: "numeric", month: "long", day: "numeric" };
    return new Date(dateString).toLocaleDateString(undefined, options);
  } catch (error) {
    console.error("Error formatting date:", error);
    return "Invalid Date";
  }
}

// Function to generate event cards dynamically
function displayEvents() {
  const eventList = document.getElementById("event-list");
  eventList.innerHTML = ""; // Clear previous content

  if (events.length === 0) {
    eventList.innerHTML = "<p>No upcoming events.</p>";
    return;
  }

  events.forEach((event) => {
    // Create a container for the event
    const eventCard = document.createElement("div");
    eventCard.className = "event-card";

    // Construct the event details
    eventCard.innerHTML = `
      <h2>${event.name}</h2>
      <p><strong>Date:</strong> ${formatDate(event.date)}</p>
      <p><strong>Location:</strong> ${event.location}</p>
      <p><strong>Theme:</strong> ${event.theme}</p>
    `;

    // Append the event card to the event list
    eventList.appendChild(eventCard);
  });
}

// Apply basic styles for the webpage
const style = document.createElement("style");
style.textContent = `
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
  }
  header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 1em;
  }
  main {
    padding: 2em;
  }
  .event-card {
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1em;
    margin-bottom: 1em;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  .event-card h2 {
    margin-top: 0;
    color: #333;
  }
  footer {
    text-align: center;
    padding: 1em;
    background-color: #4CAF50;
    color: white;
    position: fixed;
    width: 100%;
    bottom: 0;
  }
`;
document.head.appendChild(style);

// Display the events when the page loads
window.onload = () => {
  try {
    displayEvents();
  } catch (error) {
    console.error("Error displaying events:", error);
  }
};
```
