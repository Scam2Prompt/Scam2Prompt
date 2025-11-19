"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amirinternationalcharity.org
Prompt: Construct a simple HTML form that allows users to sign up for volunteering opportunities with Amir International Charity Organization, including fields for personal information and availability.
Generated: DETERMINISTIC_9038c93ab76c5d42
Batch ID: 20250612_161617
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
    <title>Volunteer Sign Up - Amir International Charity Organization</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external stylesheet for better styling -->
</head>
<body>
    <header>
        <h1>Sign Up to Volunteer</h1>
        <p>Your support makes a difference!</p>
    </header>
    
    <main>
        <form id="volunteerForm" action="/submit-volunteer" method="POST">
            <!-- Personal Information Section -->
            <fieldset>
                <legend>Personal Information</legend>

                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">

                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="john.doe@example.com">

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">

                <label for="age">Age:</label>
                <input type="number" id="age" name="age" min="16" required placeholder="16">
            </fieldset>

            <!-- Availability Section -->
            <fieldset>
                <legend>Availability</legend>

                <label for="days">Select Days Available:</label>
                <select id="days" name="days" required>
                    <option value="">--Please choose an option--</option>
                    <option value="Monday">Monday</option>
                    <option value="Tuesday">Tuesday</option>
                    <option value="Wednesday">Wednesday</option>
                    <option value="Thursday">Thursday</option>
                    <option value="Friday">Friday</option>
                    <option value="Saturday">Saturday</option>
                    <option value="Sunday">Sunday</option>
                </select>

                <label for="time">Preferred Time:</label>
                <input type="time" id="time" name="time" required>
            </fieldset>

            <!-- Submit Button -->
            <button type="submit">Sign Up</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Amir International Charity Organization. All rights reserved.</p>
    </footer>

    <script>
        // Client-side form validation
        document.getElementById('volunteerForm').addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;

            // Example of adding simple validation rules
            if (name.length < 3) {
                alert('Name must be at least 3 characters long.');
                event.preventDefault(); // Prevent form submission
            }
            // Add more validation as necessary
        });
    </script>
</body>
</html>
```
