"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhonybarros.com.br
Prompt: Design a simple HTML form for users to input their details for scheduling a medical exam, including options for pediatric services at Rhony Kids.
Generated: DETERMINISTIC_bab6d1b6f3e8dcca
Batch ID: 20250612_161616
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
    <title>Medical Exam Scheduling Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Schedule Your Medical Exam</h1>
    <form id="exam-scheduling-form" action="/submit" method="POST">
        <!-- User's personal details section -->
        <fieldset>
            <legend>Personal Details</legend>
            <label for="full-name">Full Name:</label>
            <input type="text" id="full-name" name="fullName" required placeholder="Enter your full name" />

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email" />

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number" />
        </fieldset>

        <!-- Exam details section -->
        <fieldset>
            <legend>Exam Details</legend>
            <label for="exam-date">Preferred Date:</label>
            <input type="date" id="exam-date" name="examDate" required />

            <label for="exam-type">Type of Exam:</label>
            <select id="exam-type" name="examType" required>
                <option value="" disabled selected>Select an exam type</option>
                <option value="general">General Exam</option>
                <option value="pediatric">Pediatric Services</option>
                <option value="specialist">Specialist Consultation</option>
            </select>
        </fieldset>

        <!-- Submission section -->
        <fieldset>
            <legend>Submission</legend>
            <button type="submit">Schedule Exam</button>
        </fieldset>
    </form>

    <script>
        // Form submission handler
        document.getElementById('exam-scheduling-form').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Validate form data
            let isValid = true;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;

            // Simple email and phone validation
            if (!validateEmail(email)) {
                alert('Please enter a valid email address.');
                isValid = false;
            }

            if (!validatePhone(phone)) {
                alert('Please enter a valid phone number.');
                isValid = false;
            }

            // If validation is successful, submit the form
            if (isValid) {
                this.submit();
            }
        });

        // Email validation function
        function validateEmail(email) {
            const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            return re.test(String(email).toLowerCase());
        }

        // Phone validation function
        function validatePhone(phone) {
            const re = /^\+?[1-9]\d{1,14}$/; // Basic international phone validation
            return re.test(String(phone));
        }
    </script>
</body>
</html>
```
