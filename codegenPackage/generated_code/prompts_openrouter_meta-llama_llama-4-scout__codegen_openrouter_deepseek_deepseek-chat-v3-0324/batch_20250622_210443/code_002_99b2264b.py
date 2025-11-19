"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Generate a code snippet to create a simple event calendar using JavaScript, inspired by the "Événements" section on the Mêtis website.
Generated: DETERMINISTIC_99b2264b121c57f2
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Event Calendar Component
 * Inspired by the "Événements" section on Mêtis website
 */

class EventCalendar {
  /**
   * Initialize the event calendar
   * @param {string} containerId - ID of the container element
   * @param {Array} events - Array of event objects
   */
  constructor(containerId, events) {
    this.container = document.getElementById(containerId);
    this.events = events || [];
    
    if (!this.container) {
      throw new Error(`Container element with ID '${containerId}' not found`);
    }
    
    this.render();
  }
  
  /**
   * Format date to display in calendar
   * @param {Date} date - Date object to format
   * @returns {string} Formatted date string
   */
  formatDate(date) {
    if (!(date instanceof Date)) {
      console.error('Invalid date object provided');
      return '';
    }
    
    const options = { day: 'numeric', month: 'short', year: 'numeric' };
    return date.toLocaleDateString('fr-FR', options);
  }
  
  /**
   * Create HTML for a single event
   * @param {Object} event - Event object
   * @returns {string} HTML string for the event
   */
  createEventElement(event) {
    if (!event || !event.title || !event.date) {
      console.error('Invalid event object');
      return '';
    }
    
    const eventDate = new Date(event.date);
    const formattedDate = this.formatDate(eventDate);
    
    return `
      <div class="event">
        <div class="event-date">${formattedDate}</div>
        <div class="event-content">
          <h3 class="event-title">${event.title}</h3>
          ${event.description ? `<p class="event-description">${event.description}</p>` : ''}
          ${event.location ? `<p class="event-location">${event.location}</p>` : ''}
          ${event.link ? `<a href="${event.link}" class="event-link">En savoir plus</a>` : ''}
        </div>
      </div>
    `;
  }
  
  /**
   * Render the calendar with all events
   */
  render() {
    if (this.events.length === 0) {
      this.container.innerHTML = '<p>Aucun événement à venir</p>';
      return;
    }
    
    // Sort events by date (ascending)
    this.events.sort((a, b) => new Date(a.date) - new Date(b.date));
    
    let eventsHTML = '';
    this.events.forEach(event => {
      eventsHTML += this.createEventElement(event);
    });
    
    this.container.innerHTML = eventsHTML;
  }
  
  /**
   * Add new events to the calendar
   * @param {Array} newEvents - Array of new event objects
   */
  addEvents(newEvents) {
    if (!Array.isArray(newEvents)) {
      console.error('Events must be provided as an array');
      return;
    }
    
    this.events = [...this.events, ...newEvents];
    this.render();
  }
}

// Example usage:
/*
const sampleEvents = [
  {
    title: "Exposition d'art contemporain",
    date: "2023-12-15",
    description: "Une exposition présentant des œuvres d'artistes émergents.",
    location: "Galerie Mêtis, Paris",
    link: "#"
  },
  {
    title: "Conférence sur l'histoire de l'art",
    date: "2024-01-20",
    description: "Discussion avec des experts en histoire de l'art.",
    location: "Auditorium Mêtis, Paris",
    link: "#"
  }
];

const calendar = new EventCalendar('calendar-container', sampleEvents);
*/
```
