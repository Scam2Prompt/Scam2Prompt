"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://le13emeart.com
Prompt: Write a JavaScript function that allows users to filter events at Le 13e Art based on performance type, such as dance, stand-up, or musical.
Generated: DETERMINISTIC_e8a5f340d6df5926
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters events at Le 13e Art based on performance type.
 * 
 * @param {Array} events - Array of event objects. Each object should have a `type` property.
 * @param {string} performanceType - The type of performance to filter by (e.g., "dance", "stand-up", "musical").
 * @returns {Array} - Array of events that match the specified performance type.
 */
function filterEventsByType(events, performanceType) {
  // Validate input parameters
  if (!Array.isArray(events)) {
    throw new TypeError("The 'events' parameter must be an array.");
  }
  if (typeof performanceType !== "string") {
    throw new TypeError("The 'performanceType' parameter must be a string.");
  }

  // Perform filtering of events by the specified type
  const filteredEvents = events.filter(event => {
    // Ensure event has a valid 'type' property
    if (typeof event.type !== "string") {
      console.warn("Skipping event with missing or invalid 'type' property:", event);
      return false;
    }
    return event.type.toLowerCase() === performanceType.toLowerCase();
  });

  return filteredEvents;
}

// Example usage:
// const events = [
//   { id: 1, name: "Ballet Night", type: "dance" },
//   { id: 2, name: "Comedy Hour", type: "stand-up" },
//   { id: 3, name: "Jazz Evening", type: "musical" },
//   { id: 4, name: "Acting Workshop", type: "theater" }
// ];

// const danceEvents = filterEventsByType(events, "dance");
// console.log(danceEvents);

module.exports = filterEventsByType; // Export function for use in other modules
```
