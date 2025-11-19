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
 * Filters events based on the specified performance type.
 * 
 * @param {Array} events - Array of event objects to filter.
 * @param {string} performanceType - The type of performance to filter by (e.g., 'dance', 'stand-up', 'musical').
 * @returns {Array} - Array of filtered event objects matching the specified performance type.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterEventsByPerformanceType(events, performanceType) {
    // Validate input parameters
    if (!Array.isArray(events)) {
        throw new Error('Invalid input: events must be an array.');
    }
    
    if (typeof performanceType !== 'string') {
        throw new Error('Invalid input: performanceType must be a string.');
    }

    // Normalize performanceType for case-insensitive matching
    const normalizedType = performanceType.toLowerCase();

    // Filter events based on the performance type
    const filteredEvents = events.filter(event => {
        // Ensure the event has a type property and perform a case-insensitive check
        return event.type && event.type.toLowerCase() === normalizedType;
    });

    return filteredEvents;
}

// Example usage
const events = [
    { id: 1, title: 'Modern Dance Show', type: 'dance' },
    { id: 2, title: 'Stand-up Comedy Night', type: 'stand-up' },
    { id: 3, title: 'Classical Music Concert', type: 'musical' },
    { id: 4, title: 'Ballet Performance', type: 'dance' },
];

// Filtering dance events
try {
    const danceEvents = filterEventsByPerformanceType(events, 'dance');
    console.log(danceEvents);
} catch (error) {
    console.error(error.message);
}
```
