"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Design a simple HTML form that collects user information for a digital course on architecture and interior design offered by Nyiku Design.
Generated: DETERMINISTIC_7c4dd61781cbf8d6
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
    <meta name="description" content="Register for Nyiku Design's digital course on architecture and interior design.">
    <title>Nyiku Design Course Registration</title>
    <style>
        /* Simple styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        form {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #333;
        }
        label {
            font-weight: bold;
            margin-bottom: 5px;
            display: block;
        }
        input, select, textarea, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            cursor: pointer;
            border: none;
        }
        button:hover {
            background-color: #45a049;
        }
        .error-message {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <!-- Course registration form -->
    <form id="course-registration-form">
        <h1>Course Registration</h1>
        <!-- User name input -->
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
        <span class="error-message" id="name-error"></span>

        <!-- Email input -->
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <span class="error-message" id="email-error"></span>

        <!-- Phone number input -->
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
        <span class="error-message" id="phone-error"></span>

        <!-- Course selection -->
        <label for="course">Select Course</label>
        <select id="course" name="course" required>
            <option value="" disabled selected>Please select a course</option>
            <option value="architecture">Architecture</option>
            <option value="interior-design">Interior Design</option>
        </select>
        <span class="error-message" id="course-error"></span>

        <!-- Additional comments -->
        <label for="comments">Additional Comments (Optional)</label>
        <textarea id="comments" name="comments" rows="4" placeholder="If you have any comments or questions, write them here."></textarea>

        <!-- Submit button -->
        <button type="submit">Register</button>
    </form>

    <script>
        // Basic client-side form validation
        document.getElementById('course-registration-form').addEventListener('submit', function(event) {
            let isValid = true;

            // Clear previous error messages
            document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

            // Validate Full Name
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('name-error').textContent = 'Full Name is required.';
                isValid = false;
            }

            // Validate Email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('email-error').textContent = 'Email is required.';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('email-error').textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // Validate Phone Number
            const phone = document.getElementById('phone').value.trim();
            if (!phone) {
                document.getElementById('phone-error').textContent = 'Phone Number is required.';
                isValid = false;
            }

            // Validate Course Selection
            const course = document.getElementById('course').value;
            if (!course) {
                document.getElementById('course-error').textContent = 'Please select a course.';
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
