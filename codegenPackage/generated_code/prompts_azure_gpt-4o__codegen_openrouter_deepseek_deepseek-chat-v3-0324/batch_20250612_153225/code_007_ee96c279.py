"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Create a JavaScript function to dynamically display sports class schedules by day, similar to the weekly schedule format used on the Batıkent Tofaş Spor Klübü website.
Generated: DETERMINISTIC_ee96c279fb18d3bb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays sports class schedules by day in a weekly format.
 * @param {Object} scheduleData - The schedule data organized by day.
 * @param {string} containerId - The ID of the container to render the schedule.
 */
function displayWeeklySchedule(scheduleData, containerId) {
    // Validate input parameters
    if (!scheduleData || typeof scheduleData !== 'object') {
        console.error('Invalid schedule data provided.');
        return;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        console.error(`Container with ID '${containerId}' not found.`);
        return;
    }

    // Clear previous content
    container.innerHTML = '';

    // Create the schedule table
    const table = document.createElement('table');
    table.className = 'schedule-table';

    // Create table header with days of the week
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    headerRow.innerHTML = `
        <th>Time</th>
        <th>Monday</th>
        <th>Tuesday</th>
        <th>Wednesday</th>
        <th>Thursday</th>
        <th>Friday</th>
        <th>Saturday</th>
        <th>Sunday</th>
    `;
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');

    // Get all unique time slots from all days
    const allTimes = new Set();
    Object.values(scheduleData).forEach(daySchedule => {
        Object.keys(daySchedule).forEach(time => allTimes.add(time));
    });
    const sortedTimes = Array.from(allTimes).sort();

    // Create a row for each time slot
    sortedTimes.forEach(time => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${time}</td>`;

        // Add cells for each day of the week
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].forEach(day => {
            const cell = document.createElement('td');
            const classes = scheduleData[day] && scheduleData[day][time];
            
            if (classes && classes.length > 0) {
                cell.innerHTML = classes.map(cls => `
                    <div class="class-entry">
                        <strong>${cls.name}</strong><br>
                        <span>${cls.coach}</span><br>
                        <span>${cls.location}</span>
                    </div>
                `).join('');
            } else {
                cell.innerHTML = '-';
            }

            row.appendChild(cell);
        });

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    container.appendChild(table);

    // Add basic styling if no CSS is present
    if (!document.querySelector('style.schedule-styles')) {
        const style = document.createElement('style');
        style.className = 'schedule-styles';
        style.textContent = `
            .schedule-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-family: Arial, sans-serif;
            }
            .schedule-table th, .schedule-table td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }
            .schedule-table th {
                background-color: #f2f2f2;
                font-weight: bold;
            }
            .schedule-table tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            .class-entry {
                margin: 5px 0;
                padding: 5px;
                background-color: #e6f7ff;
                border-radius: 4px;
            }
            .class-entry strong {
                color: #0056b3;
            }
        `;
        document.head.appendChild(style);
    }
}

// Example usage:
/*
const sampleSchedule = {
    Monday: {
        '09:00': [
            { name: 'Basketball', coach: 'Coach Ali', location: 'Court 1' },
            { name: 'Yoga', coach: 'Coach Zeynep', location: 'Studio A' }
        ],
        '14:00': [
            { name: 'Swimming', coach: 'Coach Mehmet', location: 'Pool' }
        ]
    },
    Tuesday: {
        '10:00': [
            { name: 'Pilates', coach: 'Coach Ayşe', location: 'Studio B' }
        ]
    },
    // ... other days
};

displayWeeklySchedule(sampleSchedule, 'schedule-container');
*/
```
