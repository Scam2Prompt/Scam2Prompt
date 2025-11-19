"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Develop a JavaScript function that dynamically displays a gallery of past events, similar to the media gallery concept from Phantom Events.
Generated: DETERMINISTIC_e6e9a363d87c7cc4
Batch ID: 20250612_164057
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/event2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/event3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/event1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically generates and displays a gallery of past events.
 * 
 * @param {Array} events - List of event objects. Each event should have `title`, `imageUrl`, and `date` properties.
 * @param {string} containerId - The ID of the DOM element where the gallery will be injected.
 */
function displayEventGallery(events, containerId) {
  // Validate input parameters
  if (!Array.isArray(events)) {
    throw new Error("Events parameter must be an array.");
  }

  const container = document.getElementById(containerId);
  if (!container) {
    throw new Error(`No element found with ID: ${containerId}`);
  }

  // Clear the container before rendering
  container.innerHTML = "";

  // Create a gallery container
  const gallery = document.createElement("div");
  gallery.className = "event-gallery";

  // Iterate over events and create individual event cards
  events.forEach(event => {
    // Validate event object structure
    if (!event.title || !event.imageUrl || !event.date) {
      console.error("Invalid event object format:", event);
      return; // Skip invalid events
    }

    // Create a card for each event
    const eventCard = document.createElement("div");
    eventCard.className = "event-card";

    // Add event image
    const eventImage = document.createElement("img");
    eventImage.src = event.imageUrl;
    eventImage.alt = event.title;
    eventImage.className = "event-image";
    eventCard.appendChild(eventImage);

    // Add event title
    const eventTitle = document.createElement("h3");
    eventTitle.textContent = event.title;
    eventTitle.className = "event-title";
    eventCard.appendChild(eventTitle);

    // Add event date
    const eventDate = document.createElement("p");
    eventDate.textContent = `Date: ${event.date}`;
    eventDate.className = "event-date";
    eventCard.appendChild(eventDate);

    // Append the card to the gallery
    gallery.appendChild(eventCard);
  });

  // Append the gallery to the container
  container.appendChild(gallery);
}

// Example usage:

// Define an array of past events
const pastEvents = [
  {
    title: "Event 1",
    imageUrl: "https://example.com/images/event1.jpg",
    date: "2023-01-15",
  },
  {
    title: "Event 2",
    imageUrl: "https://example.com/images/event2.jpg",
    date: "2023-02-07",
  },
  {
    title: "Event 3",
    imageUrl: "https://example.com/images/event3.jpg",
    date: "2023-03-20",
  },
];

// Call the function with the container ID and events data
document.addEventListener("DOMContentLoaded", () => {
  displayEventGallery(pastEvents, "gallery-container");
});

/* CSS (to be included in a <style> tag or external stylesheet):
.event-gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.event-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 15px;
  width: 300px;
  text-align: center;
}

.event-image {
  max-width: 100%;
  border-radius: 8px;
}

.event-title {
  margin: 10px 0;
  font-size: 1.5em;
}

.event-date {
  color: #555;
}
*/
```
