"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inkawasiollague.cl
Prompt: Develop a simple web form for users to submit their contact information and comments when reserving a room at a hostel in Ollagüe.
Generated: DETERMINISTIC_a583d1c59d28c7ba
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
    <title>Hostel Reservation Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 10px;
            font-weight: bold;
        }
        input, textarea, button {
            margin-top: 8px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            margin-top: 20px;
            background-color: #007BFF;
            color: #fff;
            cursor: pointer;
            border: none;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error {
            color: red;
            font-size: 12px;
        }
        .success {
            color: green;
            font-size: 14px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hostel Reservation Form</h1>
        <!-- Success message placeholder -->
        <p id="successMessage" class="success" hidden>Thank you! Your reservation has been submitted.</p>
        <!-- Contact information and comments form -->
        <form id="reservationForm">
            <!-- Name field -->
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
            <span id="errorName" class="error" hidden>Please enter your name.</span>

            <!-- Email field -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="Enter your email" required>
            <span id="errorEmail" class="error" hidden>Please enter a valid email.</span>

            <!-- Phone number field -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" placeholder="Enter your phone number">

            <!-- Comments field -->
            <label for="comments">Comments:</label>
            <textarea id="comments" name="comments" rows="4" placeholder="Add any comments or special requests"></textarea>

            <!-- Submit button -->
            <button type="submit">Submit Reservation</button>
        </form>
    </div>

    <!-- JavaScript for form validation and submission -->
    <script>
        // Form submission handler
        document.getElementById('reservationForm').addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent default form submission
            
            // Grab input values
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            
            // Clear previous error messages
            document.getElementById('errorName').hidden = true;
            document.getElementById('errorEmail').hidden = true;

            let formIsValid = true;

            // Validate full name
            if (!fullName) {
                document.getElementById('errorName').hidden = false;
                formIsValid = false;
            }

            // Validate email
            if (!email || !/^\S+@\S+\.\S+$/.test(email)) {
                document.getElementById('errorEmail').hidden = false;
                formIsValid = false;
            }

            // If form is valid, simulate submission
            if (formIsValid) {
                document.getElementById('successMessage').hidden = false; // Show success message
                document.getElementById('reservationForm').reset(); // Reset form
            }
        });
    </script>
</body>
</html>
```
