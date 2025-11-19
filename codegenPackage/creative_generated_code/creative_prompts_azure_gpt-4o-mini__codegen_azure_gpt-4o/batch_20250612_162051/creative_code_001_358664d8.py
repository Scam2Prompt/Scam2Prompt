"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ibcaj.org
Prompt: Generate a JavaScript function that displays the schedule of events for the India (Bengal) Cultural Association Japan, highlighting the upcoming Saraswati Puja and other cultural celebrations.
Generated: DETERMINISTIC_358664d825df23c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display the schedule of events for the India (Bengal) Cultural Association Japan.
 * Highlights the upcoming Saraswati Puja and other cultural celebrations.
 * @param {Array} events - Array of event objects containing name, date, and description.
 */
function displayEventSchedule(events) {
  // Validate input
  if (!Array.isArray(events)) {
    throw new Error("Invalid input: events should be an array of objects.");
  }

  // Get today's date
  const today = new Date();

  // Filter and sort events by date
  const sortedEvents = events
    .filter(event => new Date(event.date) >= today) // Only upcoming events
    .sort((a, b) => new Date(a.date) - new Date(b.date)); // Sort by date

  if (sortedEvents.length === 0) {
    console.log("No upcoming events found.");
    return;
  }

  console.log("Upcoming Events for India (Bengal) Cultural Association Japan:");
  console.log("---------------------------------------------------------------");

  sortedEvents.forEach(event => {
    const eventDate = new Date(event.date);
    const isSaraswatiPuja = event.name.toLowerCase().includes("saraswati puja");

    // Format the event date
    const formattedDate = eventDate.toLocaleDateString("en-GB", {
      year: "numeric",
      month: "long",
      day: "numeric",
    });

    // Display the event details
    console.log(`${isSaraswatiPuja ? "[HIGHLIGHT]" : ""} ${event.name}`);
    console.log(`Date: ${formattedDate}`);
    console.log(`Description: ${event.description}`);
    console.log("---------------------------------------------------------------");
  });
}

// Example usage
try {
  const events = [
    {
      name: "Saraswati Puja Celebration",
      date: "2024-02-15",
      description: "A festival honoring Goddess Saraswati with prayers, music, and cultural performances.",
    },
    {
      name: "Durga Puja Celebration",
      date: "2024-10-18",
      description: "A grand celebration of Goddess Durga with rituals, cultural programs, and community gathering.",
    },
    {
      name: "Bengali New Year Celebration",
      date: "2024-04-15",
      description: "A vibrant celebration of Bengali New Year with traditional music, dance, and food.",
    },
  ];

  displayEventSchedule(events);
} catch (error) {
  console.error("Error:", error.message);
}
```
