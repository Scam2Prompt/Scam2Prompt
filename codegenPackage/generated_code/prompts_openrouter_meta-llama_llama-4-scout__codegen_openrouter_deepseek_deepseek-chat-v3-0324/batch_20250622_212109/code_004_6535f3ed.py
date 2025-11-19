"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Create a JavaScript function to display upcoming events, like the ones listed on the Museo Vasca Votiva di Noceto website, in a dynamic and visually appealing way on a webpage.
Generated: DETERMINISTIC_6535f3ed207517fd
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and displays upcoming events in a visually appealing way.
 * @param {string} containerId - The ID of the container where events will be rendered.
 * @param {string} apiEndpoint - The URL to fetch events data from.
 */
function displayUpcomingEvents(containerId, apiEndpoint) {
    // Validate input parameters
    if (!containerId || !apiEndpoint) {
        console.error('Container ID and API endpoint are required');
        return;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container with ID '${containerId}' not found`);
        return;
    }

    // Show loading state
    container.innerHTML = '<div class="loading">Loading events...</div>';

    // Fetch events from API
    fetch(apiEndpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(events => {
            if (!events || events.length === 0) {
                container.innerHTML = '<div class="no-events">No upcoming events scheduled</div>';
                return;
            }

            // Clear loading state
            container.innerHTML = '';

            // Create and append event cards
            events.forEach(event => {
                const eventCard = document.createElement('div');
                eventCard.className = 'event-card';

                const eventDate = new Date(event.date);
                const formattedDate = eventDate.toLocaleDateString('en-US', {
                    weekday: 'long',
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                });

                eventCard.innerHTML = `
                    <div class="event-date">${formattedDate}</div>
                    <h3 class="event-title">${event.title}</h3>
                    <p class="event-description">${event.description}</p>
                    ${event.image ? `<img src="${event.image}" alt="${event.title}" class="event-image">` : ''}
                    ${event.link ? `<a href="${event.link}" class="event-link">More Info</a>` : ''}
                `;

                container.appendChild(eventCard);
            });
        })
        .catch(error => {
            console.error('Error fetching events:', error);
            container.innerHTML = '<div class="error">Failed to load events. Please try again later.</div>';
        });
}

// Example CSS (should be in a separate stylesheet)
/*
.event-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}

.event-card:hover {
    transform: translateY(-5px);
}

.event-date {
    color: #666;
    font-size: 0.9em;
    margin-bottom: 10px;
}

.event-title {
    margin: 0 0 10px 0;
    color: #333;
}

.event-description {
    margin: 0 0 15px 0;
    color: #555;
}

.event-image {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    margin-bottom: 15px;
}

.event-link {
    display: inline-block;
    padding: 8px 16px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.event-link:hover {
    background-color: #0056b3;
}

.loading, .no-events, .error {
    padding: 20px;
    text-align: center;
    color: #666;
}

.error {
    color: #dc3545;
}
*/
```
