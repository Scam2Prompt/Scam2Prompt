"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Develop a sample HTML form for clients to submit their event details, including venue, date, and preferred DJ package, based on the services offered by Central Oregon DJs.
Generated: DETERMINISTIC_e6bb5fd548154f1f
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Submission Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Event Submission Form</h1>
    <form id="eventForm" action="/submit-event" method="POST">
        <!-- Venue Input -->
        <label for="venue">Venue:</label>
        <input type="text" id="venue" name="venue" required placeholder="Enter the venue name">
        
        <!-- Date Input -->
        <label for="date">Event Date:</label>
        <input type="date" id="date" name="date" required>
        
        <!-- DJ Package Selection -->
        <label for="djPackage">Preferred DJ Package:</label>
        <select id="djPackage" name="djPackage" required>
            <option value="" disabled selected>Select a package</option>
            <option value="basic">Basic Package</option>
            <option value="premium">Premium Package</option>
            <option value="deluxe">Deluxe Package</option>
        </select>
        
        <!-- Additional Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Any additional details or requests"></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Submit Event Details</button>
    </form>

    <script>
        // Form submission event listener
        document.getElementById('eventForm').addEventListener('submit', function(event) {
            // Validate form data before submission
            const venue = document.getElementById('venue').value;
            const date = document.getElementById('date').value;
            const djPackage = document.getElementById('djPackage').value;

            if (!venue || !date || !djPackage) {
                alert('Please fill in all required fields.');
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });
    </script>
</body>
</html>
```
