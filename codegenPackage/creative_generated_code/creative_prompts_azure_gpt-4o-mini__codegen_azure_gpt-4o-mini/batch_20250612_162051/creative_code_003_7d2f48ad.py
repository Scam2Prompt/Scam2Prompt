"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.albertozofrea.it
Prompt: Develop a simple web form in HTML for users to book a Shiatsu appointment, referencing the opening hours listed on the Alberto Zofrea website.
Generated: DETERMINISTIC_7d2f48adb11c6001
Batch ID: 20250612_162051
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
    <title>Shiatsu Appointment Booking</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Shiatsu Appointment Booking</h1>
    </header>
    
    <main>
        <form id="appointment-form" action="submit_appointment.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <label for="date">Preferred Date:</label>
            <input type="date" id="date" name="date" required>

            <label for="time">Preferred Time:</label>
            <input type="time" id="time" name="time" required>

            <p>Opening Hours:</p>
            <ul>
                <li>Monday - Friday: 9:00 AM - 7:00 PM</li>
                <li>Saturday: 10:00 AM - 5:00 PM</li>
                <li>Sunday: Closed</li>
            </ul>

            <input type="submit" value="Book Appointment">
        </form>
    </main>
    
    <footer>
        <p>&copy; 2023 Shiatsu Booking by Alberto Zofrea. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler for additional client-side validation
        document.getElementById('appointment-form').addEventListener('submit', function(event) {
            const dateInput = document.getElementById('date').value;
            const timeInput = document.getElementById('time').value;
            const appointmentDateTime = new Date(`${dateInput}T${timeInput}`);

            // Check if the appointment is during opening hours
            const openingHoursStart = new Date(appointmentDateTime);
            openingHoursStart.setHours(9, 0, 0); // Set to 9:00 AM

            const openingHoursEnd = new Date(appointmentDateTime);
            openingHoursEnd.setHours(19, 0, 0); // Set to 7:00 PM

            // Validate that the appointment is in the established hours
            if (appointmentDateTime < openingHoursStart || appointmentDateTime > openingHoursEnd) {
                alert("Please select a time within our opening hours.");
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
