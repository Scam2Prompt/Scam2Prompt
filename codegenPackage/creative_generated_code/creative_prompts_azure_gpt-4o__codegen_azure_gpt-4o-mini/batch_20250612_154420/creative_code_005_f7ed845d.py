"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Develop code for a web form that allows customers to submit service requests for HVAC repairs or tune-ups, including fields for contact information, service type (e.g., air conditioning repair, duct cleaning), and preferred appointment time.
Generated: DETERMINISTIC_f7ed845dbfd557dd
Batch ID: 20250612_154420
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
    <title>HVAC Service Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to a CSS file for styling -->
</head>
<body>
    <h1>HVAC Service Request Form</h1>
    <form id="serviceRequestForm" action="/submit-request" method="POST">
        <!-- Contact Information Section -->
        <fieldset>
            <legend>Contact Information</legend>
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="johndoe@example.com">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">
        </fieldset>

        <!-- Service Type Section -->
        <fieldset>
            <legend>Service Type</legend>
            <label for="serviceType">Select Service:</label>
            <select id="serviceType" name="serviceType" required>
                <option value="" disabled selected>Select a service</option>
                <option value="air_conditioning_repair">Air Conditioning Repair</option>
                <option value="furnace_repair">Furnace Repair</option>
                <option value="duct_cleaning">Duct Cleaning</option>
                <option value="tune_up">Tune-Up</option>
            </select>
        </fieldset>

        <!-- Preferred Appointment Time Section -->
        <fieldset>
            <legend>Preferred Appointment Time</legend>
            <label for="appointmentDate">Date:</label>
            <input type="date" id="appointmentDate" name="appointmentDate" required>

            <label for="appointmentTime">Time:</label>
            <input type="time" id="appointmentTime" name="appointmentTime" required>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Handle form submission
        document.getElementById('serviceRequestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission behavior

            // Gather form data
            const formData = new FormData(this);

            // Send data to the server
            fetch('/submit-request', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert('Request submitted successfully: ' + JSON.stringify(data));
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your request. Please try again.');
            });
        });
    </script>
</body>
</html>
```

### Notes:
- This code provides a complete HTML form for submitting HVAC service requests, including error handling during form submission.
- The `<form>` element uses the POST method to submit data to the server.
- Basic frontend validation is handled using HTML5 attributes like `required`.
- JavaScript is used to manage form submission asynchronously and handle responses properly.
