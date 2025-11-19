"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Create a function in JavaScript that formats and displays family history events, like those mentioned on Apperley.ca, in a user-friendly timeline.
Generated: DETERMINISTIC_57ef9621d28558df
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Formats and displays family history events in a user-friendly timeline.
 * @param {Array} events - Array of event objects with properties: year, title, description, location
 * @param {string} containerId - The ID of the DOM element to render the timeline
 * @throws {Error} If events is not an array or containerId is invalid
 */
function displayFamilyTimeline(events, containerId) {
    // Input validation
    if (!Array.isArray(events)) {
        throw new Error('Events must be an array');
    }
    
    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container element with ID '${containerId}' not found`);
    }

    // Sort events by year (ascending)
    const sortedEvents = [...events].sort((a, b) => a.year - b.year);

    // Create timeline HTML
    let timelineHTML = `
        <div class="timeline">
            <div class="timeline__line"></div>
            <div class="timeline__events">
    `;

    sortedEvents.forEach(event => {
        if (!event.year || !event.title) {
            console.warn('Event missing required properties (year or title)', event);
            return;
        }

        timelineHTML += `
            <div class="timeline__event">
                <div class="timeline__event-year">${event.year}</div>
                <div class="timeline__event-content">
                    <h3 class="timeline__event-title">${event.title}</h3>
                    ${event.description ? `<p class="timeline__event-description">${event.description}</p>` : ''}
                    ${event.location ? `<p class="timeline__event-location">📍 ${event.location}</p>` : ''}
                </div>
            </div>
        `;
    });

    timelineHTML += `
            </div>
        </div>
    `;

    // Add CSS if not already present
    if (!document.getElementById('timeline-styles')) {
        const style = document.createElement('style');
        style.id = 'timeline-styles';
        style.textContent = `
            .timeline {
                position: relative;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px 0;
            }
            .timeline__line {
                position: absolute;
                left: 50%;
                top: 0;
                bottom: 0;
                width: 2px;
                background: #ddd;
                transform: translateX(-50%);
            }
            .timeline__events {
                position: relative;
            }
            .timeline__event {
                display: flex;
                margin-bottom: 30px;
                position: relative;
            }
            .timeline__event:last-child {
                margin-bottom: 0;
            }
            .timeline__event-year {
                width: 100px;
                text-align: center;
                padding: 5px 10px;
                background: #4a6fa5;
                color: white;
                border-radius: 20px;
                font-weight: bold;
                margin: 0 20px;
                z-index: 1;
            }
            .timeline__event-content {
                flex: 1;
                padding: 15px;
                background: #f9f9f9;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .timeline__event-title {
                margin: 0 0 10px 0;
                color: #333;
            }
            .timeline__event-description {
                margin: 0 0 5px 0;
                color: #666;
            }
            .timeline__event-location {
                margin: 0;
                font-size: 0.9em;
                color: #888;
            }
            @media (max-width: 600px) {
                .timeline__line {
                    left: 30px;
                }
                .timeline__event {
                    flex-direction: column;
                }
                .timeline__event-year {
                    margin: 0 0 10px 0;
                    align-self: flex-start;
                }
            }
        `;
        document.head.appendChild(style);
    }

    // Render timeline
    container.innerHTML = timelineHTML;
}
```
