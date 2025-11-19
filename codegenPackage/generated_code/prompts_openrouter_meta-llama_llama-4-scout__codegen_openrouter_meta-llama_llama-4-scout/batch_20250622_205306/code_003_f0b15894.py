"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Create a JavaScript function to filter and display upcoming events at The Second City based on location, date, and show type.
Generated: DETERMINISTIC_f0b158940bcbf7d7
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * EventFilter class to filter and display upcoming events at The Second City.
 */
class EventFilter {
  /**
   * Constructor to initialize events data.
   * @param {Object[]} events - Array of event objects.
   */
  constructor(events) {
    this.events = events;
  }

  /**
   * Filter events by location.
   * @param {string} location - Location to filter by.
   * @returns {Object[]} Filtered events.
   */
  filterByLocation(location) {
    return this.events.filter(event => event.location.toLowerCase().includes(location.toLowerCase()));
  }

  /**
   * Filter events by date.
   * @param {Date} date - Date to filter by.
   * @returns {Object[]} Filtered events.
   */
  filterByDate(date) {
    return this.events.filter(event => new Date(event.date) >= date);
  }

  /**
   * Filter events by show type.
   * @param {string} showType - Show type to filter by.
   * @returns {Object[]} Filtered events.
   */
  filterByShowType(showType) {
    return this.events.filter(event => event.showType.toLowerCase().includes(showType.toLowerCase()));
  }

  /**
   * Display upcoming events.
   * @param {string} [location] - Location to filter by.
   * @param {Date} [date] - Date to filter by.
   * @param {string} [showType] - Show type to filter by.
   */
  displayUpcomingEvents(location, date, showType) {
    let filteredEvents = this.events;

    if (location) {
      filteredEvents = this.filterByLocation(location);
    }

    if (date) {
      filteredEvents = this.filterByDate(date);
    }

    if (showType) {
      filteredEvents = this.filterByShowType(showType);
    }

    if (filteredEvents.length === 0) {
      console.log('No upcoming events found.');
      return;
    }

    console.log('Upcoming Events:');
    filteredEvents.forEach(event => {
      console.log(`Date: ${event.date}, Location: ${event.location}, Show Type: ${event.showType}`);
    });
  }
}

// Example usage:
const events = [
  { date: '2024-09-20', location: 'The Second City, Chicago', showType: 'Comedy' },
  { date: '2024-09-22', location: 'The Second City, Toronto', showType: 'Improv' },
  { date: '2024-09-25', location: 'The Second City, Chicago', showType: 'Drama' },
  { date: '2024-09-28', location: 'The Second City, New York', showType: 'Comedy' },
];

const eventFilter = new EventFilter(events);

// Test cases:
eventFilter.displayUpcomingEvents('Chicago');
eventFilter.displayUpcomingEvents(null, new Date('2024-09-24'));
eventFilter.displayUpcomingEvents(null, null, 'Comedy');
eventFilter.displayUpcomingEvents('Invalid Location');
```
