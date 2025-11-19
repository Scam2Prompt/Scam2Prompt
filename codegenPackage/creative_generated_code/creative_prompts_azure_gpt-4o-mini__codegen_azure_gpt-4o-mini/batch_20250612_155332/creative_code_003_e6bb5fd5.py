"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-djs.com
Prompt: Develop a sample HTML form for clients to submit their event details, including venue, date, and preferred DJ package, based on the services offered by Central Oregon DJs.
Generated: DETERMINISTIC_e6bb5fd548154f1f
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Details Submission</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Submit Your Event Details</h1>
    <form id="event-form" action="/submit-event" method="POST">
        <!-- Venue input -->
        <label for="venue">Venue:</label>
        <input type="text" id="venue" name="venue" required placeholder="Enter venue name">
        
        <!-- Date input -->
        <label for="date">Event Date:</label>
        <input type="date" id="date" name="date" required>
        
        <!-- Preferred DJ Package selection -->
        <label for="dj-package">Preferred DJ Package:</label>
        <select id="dj-package" name="dj_package" required>
            <option value="" disabled selected>Select a DJ Package</option>
            <option value="basic">Basic Package</option>
            <option value="premium">Premium Package</option>
            <option value="deluxe">Deluxe Package</option>
        </select>
        
        <!-- Additional Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Any additional information..."></textarea>
        
        <!-- Submit button -->
        <button type="submit">Submit Event Details</button>
    </form>

    <!-- JavaScript for form validation -->
    <script>
        document.getElementById('event-form').addEventListener('submit', function(event) {
            // Client-side validation
            const venue = document.getElementById('venue').value;
            const date = document.getElementById('date').value;
            const djPackage = document.getElementById('dj-package').value;

            if (!venue || !date || !djPackage) {
                alert('Please fill in all required fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
