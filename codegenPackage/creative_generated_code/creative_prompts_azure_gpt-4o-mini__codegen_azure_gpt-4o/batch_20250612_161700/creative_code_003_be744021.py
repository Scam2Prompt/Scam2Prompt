"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villapanorea.com
Prompt: Develop a web form using HTML and JavaScript for users to request a personal discount offer for their stay at Villa Panorea.
Generated: DETERMINISTIC_be744021b5d411da
Batch ID: 20250612_161700
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
    <title>Villa Panorea - Discount Request Form</title>
    <style>
        /* Simple styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 15px;
            background-color: #f9f9f9;
        }
        .form-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin: 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #5cb85c;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
        .error-message {
            color: red;
            margin-top: 10px;
        }
        .success-message {
            color: green;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Request a Personal Discount</h1>
        <form id="discount-form">
            <!-- Name Input -->
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" placeholder="Enter your full name" required>
            </div>

            <!-- Email Input -->
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
            </div>

            <!-- Stay Dates Input -->
            <div class="form-group">
                <label for="dates">Dates of Stay</label>
                <input type="text" id="dates" name="dates" placeholder="e.g., June 15 - June 20, 2024" required>
            </div>

            <!-- Message Input -->
            <div class="form-group">
                <label for="message">Additional Information</label>
                <textarea id="message" name="message" placeholder="Write any additional details here..." rows="4"></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit">Submit Request</button>
            
            <!-- Feedback Messages -->
            <p id="feedback-message" class="error-message" style="display: none;"></p>
            <p id="success-message" class="success-message" style="display: none;">Your request has been submitted successfully!</p>
        </form>
    </div>

    <script>
        // Error handling and form submission logic
        document.getElementById('discount-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Clear previous feedback messages
            const errorMessage = document.getElementById('feedback-message');
            const successMessage = document.getElementById('success-message');
            errorMessage.style.display = 'none';
            successMessage.style.display = 'none';

            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const dates = document.getElementById('dates').value.trim();
            const message = document.getElementById('message').value.trim();

            // Simple validation
            if (!name || !email || !dates) {
                errorMessage.textContent = 'Please fill in all required fields.';
                errorMessage.style.display = 'block';
                return;
            }

            // Simulate form submission (replace with actual backend logic)
            try {
                // Normally, you'd send this data to a server using fetch() or XMLHttpRequest
                const formData = {
                    name: name,
                    email: email,
                    dates: dates,
                    message: message
                };

                console.log('Form Submitted Successfully:', formData);

                // Display success message
                successMessage.style.display = 'block';

                // Reset form
                document.getElementById('discount-form').reset();
            } catch (error) {
                // Handle any unexpected errors
                errorMessage.textContent = 'An error occurred while submitting your request. Please try again later.';
                errorMessage.style.display = 'block';
                console.error('Form Submission Error:', error);
            }
        });
    </script>
</body>
</html>
```
