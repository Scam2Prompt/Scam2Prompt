"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Write code in JavaScript to display business hours dynamically on a webpage, including weekdays (9:00–17:00) and a message to contact a specific phone number for weekends and public holidays.
Generated: DETERMINISTIC_edf14487001e54cf
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to dynamically display business hours on a webpage

// Function to determine if the day is a weekend or public holiday
function isWeekendOrHoliday(date) {
  // Weekend check: Saturday (6) or Sunday (0)
  const day = date.getDay();
  if (day === 0 || day === 6) {
    return true;
  }

  // Public holidays (example: list of fixed holidays)
  const publicHolidays = [
    '01-01', // New Year's Day
    '12-25', // Christmas Day
    '07-04', // Independence Day (example for U.S.)
  ];

  const formattedDate = `${String(date.getMonth() + 1).padStart(2, '0')}-${String(
    date.getDate()
  ).padStart(2, '0')}`;

  return publicHolidays.includes(formattedDate);
}

// Function to display business hours or contact message
function displayBusinessHours() {
  const now = new Date();
  const businessHoursElement = document.getElementById('business-hours');

  if (isWeekendOrHoliday(now)) {
    // Display weekend/public holiday message
    businessHoursElement.innerHTML =
      'Our offices are closed today. Please contact us at <strong>(123) 456-7890</strong>.';
  } else {
    // Display weekday business hours
    businessHoursElement.innerHTML =
      'Our business hours are <strong>9:00 AM – 5:00 PM</strong>.';
  }
}

// Ensure the DOM is fully loaded before running code
document.addEventListener('DOMContentLoaded', () => {
  try {
    displayBusinessHours();
  } catch (error) {
    console.error('Error displaying business hours:', error);
    const businessHoursElement = document.getElementById('business-hours');
    if (businessHoursElement) {
      businessHoursElement.innerHTML =
        'An error occurred while displaying business hours. Please try again later.';
    }
  }
});
```

```html
<!-- Example HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Business Hours</title>
</head>
<body>
  <div id="business-hours"></div>
  <script src="business-hours.js"></script>
</body>
</html>
```
