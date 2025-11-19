"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Generate JavaScript code for a webpage that dynamically displays upcoming events with details like date, location, and theme, similar to the "Road to Celestia" event list.
Generated: DETERMINISTIC_cbc2a2c7d8d6c0d0
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Event class representing an upcoming event
class Event {
  /**
   * @param {string} date - Event date in 'YYYY-MM-DD' format
   * @param {string} location - Event location
   * @param {string} theme - Event theme
   */
  constructor(date, location, theme) {
    this.date = date;
    this.location = location;
    this.theme = theme;
  }
}

// EventList class to manage and display events
class EventList {
  constructor() {
    this.events = [];
  }

  /**
   * Add an event to the list
   * @param {Event} event - Event to add
   */
  addEvent(event) {
    this.events.push(event);
  }

  /**
   * Render the event list on the webpage
   * @param {HTMLElement} container - Container element to render the list in
   */
  renderEventList(container) {
    // Clear existing event list
    container.innerHTML = '';

    // Sort events by date
    this.events.sort((a, b) => new Date(a.date) - new Date(b.date));

    // Create event list elements
    this.events.forEach((event) => {
      const eventElement = document.createElement('div');
      eventElement.classList.add('event');

      const dateElement = document.createElement('p');
      dateElement.textContent = `Date: ${event.date}`;
      eventElement.appendChild(dateElement);

      const locationElement = document.createElement('p');
      locationElement.textContent = `Location: ${event.location}`;
      eventElement.appendChild(locationElement);

      const themeElement = document.createElement('p');
      themeElement.textContent = `Theme: ${event.theme}`;
      eventElement.appendChild(themeElement);

      container.appendChild(eventElement);
    });
  }
}

// Initialize event list and container element
const eventList = new EventList();
const eventContainer = document.getElementById('event-container');

// Example events
try {
  eventList.addEvent(new Event('2024-10-15', 'New York', 'Celestia Launch'));
  eventList.addEvent(new Event('2024-11-01', 'Los Angeles', 'Celestia Community Meetup'));
  eventList.addEvent(new Event('2024-12-20', 'Online', 'Celestia Holiday Party'));

  // Render event list
  eventList.renderEventList(eventContainer);
} catch (error) {
  console.error('Error rendering event list:', error);
  const errorElement = document.createElement('p');
  errorElement.textContent = 'Error loading events.';
  eventContainer.appendChild(errorElement);
}
```

```css
/* Add this CSS to your stylesheet */
.event {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.event p {
  margin: 0;
  padding: 5px;
}
```

```html
<!-- Add this HTML to your webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Upcoming Events</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Upcoming Events</h1>
  <div id="event-container"></div>
  <script src="script.js"></script>
</body>
</html>
```
