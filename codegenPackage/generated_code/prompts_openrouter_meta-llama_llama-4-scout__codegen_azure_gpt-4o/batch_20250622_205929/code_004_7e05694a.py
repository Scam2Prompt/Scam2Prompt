"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Write a JavaScript code snippet for creating a simple event calendar that displays upcoming events for Celestia, including event titles, dates, and locations.
Generated: DETERMINISTIC_7e05694aa2b2c89c
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Event Calendar for Celestia
// This script creates a simple event calendar that displays upcoming events with titles, dates, and locations.

// Sample event data
const events = [
  { title: "Celestia Community Meetup", date: "2023-11-15", location: "San Francisco, CA" },
  { title: "Celestia Developer Workshop", date: "2023-12-01", location: "New York, NY" },
  { title: "Celestia Hackathon", date: "2024-01-20", location: "Austin, TX" },
];

// Function to format the date in a readable format
function formatDate(dateString) {
  try {
    const options = { year: "numeric", month: "long", day: "numeric" };
    const date = new Date(dateString);
    return date.toLocaleDateString(undefined, options);
  } catch (error) {
    console.error("Error formatting date:", error);
    return "Invalid Date";
  }
}

// Function to render the event calendar
function renderEventCalendar(events) {
  // Create a container for the calendar
  const calendarContainer = document.createElement("div");
  calendarContainer.id = "event-calendar";
  calendarContainer.style.border = "1px solid #ccc";
  calendarContainer.style.padding = "20px";
  calendarContainer.style.borderRadius = "8px";
  calendarContainer.style.maxWidth = "400px";
  calendarContainer.style.margin = "20px auto";
  calendarContainer.style.fontFamily = "Arial, sans-serif";

  // Add a title to the calendar
  const calendarTitle = document.createElement("h2");
  calendarTitle.textContent = "Celestia Event Calendar";
  calendarTitle.style.textAlign = "center";
  calendarContainer.appendChild(calendarTitle);

  // Check if there are events
  if (events.length === 0) {
    const noEventsMessage = document.createElement("p");
    noEventsMessage.textContent = "No upcoming events.";
    noEventsMessage.style.textAlign = "center";
    calendarContainer.appendChild(noEventsMessage);
  } else {
    // Create a list for the events
    const eventList = document.createElement("ul");
    eventList.style.listStyleType = "none";
    eventList.style.padding = "0";

    // Loop through the events and add them to the list
    events.forEach((event) => {
      const eventItem = document.createElement("li");
      eventItem.style.marginBottom = "15px";
      eventItem.style.padding = "10px";
      eventItem.style.border = "1px solid #ddd";
      eventItem.style.borderRadius = "5px";
      eventItem.style.backgroundColor = "#f9f9f9";

      const eventTitle = document.createElement("h3");
      eventTitle.textContent = event.title;
      eventTitle.style.margin = "0 0 5px 0";

      const eventDate = document.createElement("p");
      eventDate.textContent = `Date: ${formatDate(event.date)}`;
      eventDate.style.margin = "0";

      const eventLocation = document.createElement("p");
      eventLocation.textContent = `Location: ${event.location}`;
      eventLocation.style.margin = "0";

      eventItem.appendChild(eventTitle);
      eventItem.appendChild(eventDate);
      eventItem.appendChild(eventLocation);
      eventList.appendChild(eventItem);
    });

    calendarContainer.appendChild(eventList);
  }

  // Append the calendar to the body of the document
  document.body.appendChild(calendarContainer);
}

// Render the event calendar on page load
document.addEventListener("DOMContentLoaded", () => {
  try {
    renderEventCalendar(events);
  } catch (error) {
    console.error("Error rendering event calendar:", error);
  }
});
```
