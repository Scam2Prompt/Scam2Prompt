"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Create a JavaScript function to display the operating hours of RAVIOLI HOUSE, including Tuesday to Sunday from 17:00 to 21:30 and Saturday from 12:00 to 21:30.
Generated: DETERMINISTIC_b28c86b8ec35a241
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
 * Returns the operating hours of RAVIOLI HOUSE based on the current day.
 * @returns {string} The operating hours message for the current day or a closed message.
 */
function getRavioliHouseHours() {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const today = new Date();
    const currentDay = today.getDay();
    const currentHour = today.getHours();
    const currentMinute = today.getMinutes();

    // Operating hours configuration
    const operatingHours = {
        Tuesday: { open: 17, close: 21.5 },
        Wednesday: { open: 17, close: 21.5 },
        Thursday: { open: 17, close: 21.5 },
        Friday: { open: 17, close: 21.5 },
        Saturday: { open: 12, close: 21.5 },
        Sunday: { open: 17, close: 21.5 }
    };

    const dayName = days[currentDay];
    const hoursToday = operatingHours[dayName];

    if (!hoursToday) {
        return 'RAVIOLI HOUSE is closed today (Monday).';
    }

    const currentTime = currentHour + (currentMinute / 60);
    const isOpen = currentTime >= hoursToday.open && currentTime < hoursToday.close;

    if (isOpen) {
        const closingTime = hoursToday.close === 21.5 ? '21:30' : `${Math.floor(hoursToday.close)}:00`;
        return `RAVIOLI HOUSE is open today (${dayName}) until ${closingTime}.`;
    } else {
        const openingTime = hoursToday.open === 12 ? '12:00' : '17:00';
        return `RAVIOLI HOUSE is closed now. Today's (${dayName}) hours: ${openingTime} - 21:30.`;
    }
}

// Example usage:
console.log(getRavioliHouseHours());
```
