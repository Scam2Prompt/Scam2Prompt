"""
Generated Code Metadata:
========================
Original URL: https://www.azrvservices.com
Prompt: Construct a sample HTML form for users to submit requests for RV inspections, including fields for service type and contact information.
Generated: DETERMINISTIC_9e3b7aa97b97fbb5
Batch ID: 20250612_163350
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
    <title>RV Inspection Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Request an RV Inspection</h1>
    <form id="inspectionRequestForm" action="/submit-inspection-request" method="POST">
        <!-- Service Type Selection -->
        <label for="serviceType">Select Service Type:</label>
        <select id="serviceType" name="serviceType" required>
            <option value="" disabled selected>Select a service</option>
            <option value="pre-purchase">Pre-Purchase Inspection</option>
            <option value="routine">Routine Maintenance Inspection</option>
            <option value="post-repair">Post-Repair Inspection</option>
        </select>

        <!-- Contact Information -->
        <fieldset>
            <legend>Contact Information</legend>
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required placeholder="John Doe">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="example@example.com">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">
        </fieldset>

        <!-- Additional Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Any specific requests or notes..."></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('inspectionRequestForm').addEventListener('submit', function(event) {
            // Perform client-side validation if necessary
            // For example, check if all required fields are filled
            const serviceType = document.getElementById('serviceType').value;
            if (!serviceType) {
                alert('Please select a service type.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
