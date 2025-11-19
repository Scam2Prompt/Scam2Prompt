"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Design a simple HTML form for users to submit inquiries about tailored horse riding tours at Chile Horse Riding, ensuring it captures essential details like the desired tour and number of participants.
Generated: DETERMINISTIC_f33a334ffee5b248
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
    <title>Chile Horse Riding Inquiry Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            background-color: #f9f9f9;
        }

        .form-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input, select, textarea, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            color: #fff;
            background-color: #007BFF;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>

<body>
    <div class="form-container">
        <h1>Chile Horse Riding Inquiry</h1>
        <!-- Inquiry form starts here -->
        <form id="inquiryForm">
            <!-- Full name field -->
            <label for="fullName">Full Name</label>
            <input type="text" id="fullName" name="fullName" required placeholder="Enter your full name">
            <span class="error" id="fullNameError"></span>

            <!-- Email field -->
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">
            <span class="error" id="emailError"></span>

            <!-- Desired tour field -->
            <label for="tour">Desired Tour</label>
            <select id="tour" name="tour" required>
                <option value="">Select a tour...</option>
                <option value="coastal">Coastal Exploration</option>
                <option value="mountain">Mountain Adventure</option>
                <option value="desert">Desert Trail</option>
            </select>
            <span class="error" id="tourError"></span>

            <!-- Number of participants field -->
            <label for="participants">Number of Participants</label>
            <input type="number" id="participants" name="participants" min="1" required placeholder="Enter number of participants">
            <span class="error" id="participantsError"></span>

            <!-- Additional notes field -->
            <label for="notes">Additional Notes (Optional)</label>
            <textarea id="notes" name="notes" rows="4" placeholder="Add any specific requirements or details..."></textarea>

            <!-- Submit button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        // Basic client-side validation script
        const form = document.getElementById('inquiryForm');

        // Error messages for form fields
        const fullNameError = document.getElementById('fullNameError');
        const emailError = document.getElementById('emailError');
        const tourError = document.getElementById('tourError');
        const participantsError = document.getElementById('participantsError');

        // Form submission event listener
        form.addEventListener('submit', function (event) {
            // Clear previous error messages
            fullNameError.textContent = '';
            emailError.textContent = '';
            tourError.textContent = '';
            participantsError.textContent = '';

            let isValid = true;

            // Validate full name
            const fullName = form.fullName.value.trim();
            if (fullName === '') {
                fullNameError.textContent = 'Full Name is required.';
                isValid = false;
            }

            // Validate email
            const email = form.email.value.trim();
            if (email === '') {
                emailError.textContent = 'Email is required.';
                isValid = false;
            } else if (!email.includes('@')) {
                emailError.textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // Validate desired tour
            const tour = form.tour.value;
            if (tour === '') {
                tourError.textContent = 'Please select a tour.';
                isValid = false;
            }

            // Validate number of participants
            const participants = form.participants.value;
            if (participants === '' || participants <= 0) {
                participantsError.textContent = 'Please enter a valid number of participants.';
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>

</html>
```
