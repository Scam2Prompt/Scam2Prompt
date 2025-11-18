"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Generate HTML and JavaScript code for a contact form that allows users to book electrostimulation training sessions, with validation for email and phone number fields.
Generated: DETERMINISTIC_673d2772b9811d1d
Batch ID: 20250612_151040
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
    <title>Electrostimulation Training Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .contact-form {
            max-width: 400px;
            margin: auto;
            background: #fff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .contact-form h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-field {
            margin-bottom: 15px;
        }
        .form-field label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .form-field input {
            width: 100%;
            padding: 8px;
            font-size: 1em;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-field input:invalid {
            border-color: red;
        }
        .form-field input:valid {
            border-color: green;
        }
        .submit-btn {
            display: block;
            width: 100%;
            padding: 10px;
            font-size: 1em;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h2>Book a Training Session</h2>
        <form id="bookingForm">
            <div class="form-field">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-field">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-field">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" pattern="^\+?\d{10,15}$" required title="Please enter a valid phone number (e.g., +1234567890 or 1234567890)">
            </div>
            <div class="form-field">
                <label for="date">Preferred Date</label>
                <input type="date" id="date" name="date" required>
            </div>
            <button type="submit" class="submit-btn">Submit</button>
        </form>
    </div>

    <script>
        // Wait for the DOM to fully load
        document.addEventListener('DOMContentLoaded', () => {
            // Reference to the form element
            const form = document.getElementById('bookingForm');

            // Add event listener to handle form submission
            form.addEventListener('submit', (event) => {
                event.preventDefault(); // Prevent form from submitting normally

                // Collect form data
                const formData = {
                    name: form.name.value.trim(),
                    email: form.email.value.trim(),
                    phone: form.phone.value.trim(),
                    date: form.date.value.trim()
                };

                // Validate form data
                if (!formData.email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
                    alert('Please enter a valid email address.');
                    return;
                }

                if (!formData.phone.match(/^\+?\d{10,15}$/)) {
                    alert('Please enter a valid phone number.');
                    return;
                }

                // Simulate form submission (replace this with actual backend API call)
                console.log('Form submitted successfully!', formData);
                alert('Your booking request has been submitted successfully.');

                // Optionally, reset the form
                form.reset();
            });
        });
    </script>
</body>
</html>
```
