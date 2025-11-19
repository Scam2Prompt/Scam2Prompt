"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Create a JavaScript function to display a list of upcoming events for a sports club, including events like cross-country running and TEES Events, with filtering by date and event type.
Generated: DETERMINISTIC_7fbf9d154f21bf6a
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * EventManager - A class to manage and display upcoming events for a sports club.
 */
class EventManager {
    /**
     * @param {Array} events - Array of event objects
     * @param {Object} options - Configuration options
     */
    constructor(events = [], options = {}) {
        this.events = this._validateEvents(events);
        this.defaultOptions = {
            dateFormat: 'YYYY-MM-DD',
            displayContainer: '#events-container',
            filterForm: '#events-filter'
        };
        this.options = { ...this.defaultOptions, ...options };
    }

    /**
     * Validates the events array structure
     * @private
     * @param {Array} events - Array of event objects
     * @returns {Array} Validated events array
     * @throws {Error} If events structure is invalid
     */
    _validateEvents(events) {
        if (!Array.isArray(events)) {
            throw new Error('Events must be an array');
        }

        return events.map(event => {
            if (!event.id || !event.name || !event.date || !event.type) {
                throw new Error('Event must have id, name, date, and type properties');
            }

            if (isNaN(new Date(event.date).getTime())) {
                throw new Error(`Invalid date format for event ${event.id}`);
            }

            return {
                id: event.id,
                name: event.name,
                date: new Date(event.date),
                type: event.type,
                description: event.description || '',
                location: event.location || ''
            };
        });
    }

    /**
     * Filters events based on criteria
     * @param {Object} filters - Filter criteria
     * @returns {Array} Filtered events
     */
    filterEvents(filters = {}) {
        return this.events.filter(event => {
            let match = true;

            if (filters.startDate && event.date < new Date(filters.startDate)) {
                match = false;
            }

            if (filters.endDate && event.date > new Date(filters.endDate)) {
                match = false;
            }

            if (filters.type && event.type !== filters.type) {
                match = false;
            }

            return match;
        });
    }

    /**
     * Formats date according to options
     * @private
     * @param {Date} date - Date to format
     * @returns {String} Formatted date string
     */
    _formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');

        if (this.options.dateFormat === 'YYYY-MM-DD') {
            return `${year}-${month}-${day}`;
        } else {
            return `${day}/${month}/${year}`;
        }
    }

    /**
     * Renders events to the DOM
     * @param {Array} events - Events to render
     */
    renderEvents(events) {
        const container = document.querySelector(this.options.displayContainer);
        if (!container) {
            console.error('Display container not found');
            return;
        }

        if (events.length === 0) {
            container.innerHTML = '<p>No events found matching your criteria.</p>';
            return;
        }

        const eventList = document.createElement('ul');
        eventList.className = 'event-list';

        events.forEach(event => {
            const eventItem = document.createElement('li');
            eventItem.className = 'event-item';
            eventItem.innerHTML = `
                <h3>${event.name}</h3>
                <div class="event-date">${this._formatDate(event.date)}</div>
                <div class="event-type">Type: ${event.type}</div>
                ${event.description ? `<p class="event-description">${event.description}</p>` : ''}
                ${event.location ? `<div class="event-location">Location: ${event.location}</div>` : ''}
            `;
            eventList.appendChild(eventItem);
        });

        container.innerHTML = '';
        container.appendChild(eventList);
    }

    /**
     * Initializes event filters and rendering
     */
    init() {
        const filterForm = document.querySelector(this.options.filterForm);
        if (filterForm) {
            filterForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const formData = new FormData(filterForm);
                const filters = {
                    startDate: formData.get('startDate'),
                    endDate: formData.get('endDate'),
                    type: formData.get('type')
                };
                const filteredEvents = this.filterEvents(filters);
                this.renderEvents(filteredEvents);
            });
        }

        // Initial render with all events
        this.renderEvents(this.events);
    }
}

// Example usage:
/*
const events = [
    {
        id: 1,
        name: 'Cross-Country Running Championship',
        date: '2023-12-15',
        type: 'cross-country',
        description: 'Annual cross-country running competition',
        location: 'Central Park'
    },
    {
        id: 2,
        name: 'TEES Summer Event',
        date: '2023-07-22',
        type: 'tees',
        description: 'Summer social event for TEES members',
        location: 'Club House'
    },
    {
        id: 3,
        name: 'Winter Marathon',
        date: '2024-01-10',
        type: 'cross-country',
        description: 'Winter marathon through scenic routes',
        location: 'Mountain Trails'
    }
];

const eventManager = new EventManager(events);
eventManager.init();
*/
```
