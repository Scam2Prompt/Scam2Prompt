"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: "Write a code snippet to create a simple event management system using JavaScript, inspired by Jam UAE's services for corporate events and festivals."
Generated: DETERMINISTIC_8663cf8d8a07f5e0
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Event Management System
 * Inspired by Jam UAE's corporate events and festivals services
 */

class Event {
  /**
   * @param {string} name - Event name
   * @param {string} type - Event type (corporate, festival, etc.)
   * @param {Date} date - Event date
   * @param {string} location - Event location
   * @param {number} capacity - Maximum attendees
   */
  constructor(name, type, date, location, capacity) {
    this.name = name;
    this.type = type;
    this.date = date;
    this.location = location;
    this.capacity = capacity;
    this.attendees = [];
    this.status = 'planned'; // planned, active, completed, cancelled
  }

  /**
   * Add attendee to the event
   * @param {string} attendeeName - Name of the attendee
   * @throws {Error} If event is at capacity or not in planned/active state
   */
  addAttendee(attendeeName) {
    if (this.attendees.length >= this.capacity) {
      throw new Error('Event is at full capacity');
    }
    if (!['planned', 'active'].includes(this.status)) {
      throw new Error('Cannot add attendees to this event in its current state');
    }
    this.attendees.push(attendeeName);
  }

  /**
   * Update event status
   * @param {string} newStatus - New status for the event
   * @throws {Error} If invalid status transition
   */
  updateStatus(newStatus) {
    const validStatuses = ['planned', 'active', 'completed', 'cancelled'];
    if (!validStatuses.includes(newStatus)) {
      throw new Error('Invalid status provided');
    }

    // Validate status transitions
    if (this.status === 'completed' || this.status === 'cancelled') {
      throw new Error(`Cannot change status from ${this.status}`);
    }

    this.status = newStatus;
  }

  /**
   * Get event details
   * @returns {object} Event information
   */
  getDetails() {
    return {
      name: this.name,
      type: this.type,
      date: this.date.toISOString().split('T')[0],
      location: this.location,
      capacity: this.capacity,
      attendees: this.attendees,
      status: this.status,
      availableSpots: this.capacity - this.attendees.length
    };
  }
}

class EventManager {
  constructor() {
    this.events = [];
  }

  /**
   * Create a new event
   * @param {string} name - Event name
   * @param {string} type - Event type
   * @param {Date} date - Event date
   * @param {string} location - Event location
   * @param {number} capacity - Maximum attendees
   * @returns {Event} The created event
   * @throws {Error} If date is in the past or capacity is invalid
   */
  createEvent(name, type, date, location, capacity) {
    if (date < new Date()) {
      throw new Error('Event date cannot be in the past');
    }
    if (capacity <= 0) {
      throw new Error('Capacity must be greater than 0');
    }

    const event = new Event(name, type, date, location, capacity);
    this.events.push(event);
    return event;
  }

  /**
   * Find events by type
   * @param {string} type - Event type to filter by
   * @returns {Array} Array of matching events
   */
  findEventsByType(type) {
    return this.events.filter(event => event.type === type);
  }

  /**
   * Get upcoming events
   * @returns {Array} Array of upcoming events
   */
  getUpcomingEvents() {
    const now = new Date();
    return this.events.filter(event => 
      event.date >= now && event.status !== 'cancelled'
    );
  }

  /**
   * Cancel an event
   * @param {string} eventName - Name of the event to cancel
   * @throws {Error} If event not found or already completed/cancelled
   */
  cancelEvent(eventName) {
    const event = this.events.find(e => e.name === eventName);
    if (!event) {
      throw new Error('Event not found');
    }
    event.updateStatus('cancelled');
  }

  /**
   * Get all events
   * @returns {Array} Array of all events
   */
  getAllEvents() {
    return this.events.map(event => event.getDetails());
  }
}

// Example usage
try {
  const manager = new EventManager();
  
  // Create corporate event
  const corporateDate = new Date();
  corporateDate.setDate(corporateDate.getDate() + 30);
  const corporateEvent = manager.createEvent(
    'Tech Conference 2023',
    'corporate',
    corporateDate,
    'Dubai World Trade Centre',
    500
  );
  
  // Create festival event
  const festivalDate = new Date();
  festivalDate.setDate(festivalDate.getDate() + 60);
  const festivalEvent = manager.createEvent(
    'Dubai Food Festival',
    'festival',
    festivalDate,
    'Downtown Dubai',
    10000
  );
  
  // Add attendees
  corporateEvent.addAttendee('John Smith');
  corporateEvent.addAttendee('Sarah Johnson');
  
  festivalEvent.addAttendee('Ahmed Al Maktoum');
  
  // Update status
  corporateEvent.updateStatus('active');
  
  // Get all events
  console.log('All Events:', manager.getAllEvents());
  
  // Get upcoming events
  console.log('Upcoming Events:', manager.getUpcomingEvents());
  
  // Find corporate events
  console.log('Corporate Events:', manager.findEventsByType('corporate'));
  
} catch (error) {
  console.error('Event Management Error:', error.message);
}
```
