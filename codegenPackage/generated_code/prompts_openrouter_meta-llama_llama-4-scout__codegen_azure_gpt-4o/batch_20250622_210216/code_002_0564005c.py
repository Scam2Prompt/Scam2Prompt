"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Generate HTML code for a hotel room booking form, inspired by the design of Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_0564005cc282411e
Batch ID: 20250622_210216
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
    <meta name="description" content="Hotel Room Booking Form for Hostal Koltin Suchitoto">
    <title>Hotel Room Booking Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }

        .booking-form-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            color: #555555;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            font-size: 14px;
        }

        input:focus, select:focus, textarea:focus {
            border-color: #007BFF;
            outline: none;
        }

        .form-group textarea {
            resize: vertical;
        }

        .submit-btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }

        .submit-btn:hover {
            background-color: #0056b3;
        }

        .error-message {
            color: red;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="booking-form-container">
        <h1>Book Your Stay</h1>
        <form id="bookingForm" action="/submit-booking" method="POST">
            <!-- Full Name -->
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
                <span class="error-message" id="fullNameError"></span>
            </div>

            <!-- Email -->
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <span class="error-message" id="emailError"></span>
            </div>

            <!-- Phone Number -->
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" required>
                <span class="error-message" id="phoneError"></span>
            </div>

            <!-- Check-in Date -->
            <div class="form-group">
                <label for="checkInDate">Check-in Date</label>
                <input type="date" id="checkInDate" name="checkInDate" required>
                <span class="error-message" id="checkInDateError"></span>
            </div>

            <!-- Check-out Date -->
            <div class="form-group">
                <label for="checkOutDate">Check-out Date</label>
                <input type="date" id="checkOutDate" name="checkOutDate" required>
                <span class="error-message" id="checkOutDateError"></span>
            </div>

            <!-- Room Type -->
            <div class="form-group">
                <label for="roomType">Room Type</label>
                <select id="roomType" name="roomType" required>
                    <option value="">Select a room type</option>
                    <option value="single">Single Room</option>
                    <option value="double">Double Room</option>
                    <option value="suite">Suite</option>
                </select>
                <span class="error-message" id="roomTypeError"></span>
            </div>

            <!-- Special Requests -->
            <div class="form-group">
                <label for="specialRequests">Special Requests</label>
                <textarea id="specialRequests" name="specialRequests" rows="4"></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit" class="submit-btn">Submit Booking</button>
        </form>
    </div>

    <script>
        // Basic client-side validation
        document.getElementById('bookingForm').addEventListener('submit', function(event) {
            let isValid = true;

            // Clear previous error messages
            document.querySelectorAll('.error-message').forEach(function(el) {
                el.textContent = '';
            });

            // Validate Full Name
            const fullName = document.getElementById('fullName').value.trim();
            if (fullName === '') {
                document.getElementById('fullNameError').textContent = 'Full Name is required.';
                isValid = false;
            }

            // Validate Email
            const email = document.getElementById('email').value.trim();
            if (email === '') {
                document.getElementById('emailError').textContent = 'Email is required.';
                isValid = false;
            } else if (!/\S+@\S+\.\S+/.test(email)) {
                document.getElementById('emailError').textContent = 'Invalid email format.';
                isValid = false;
            }

            // Validate Phone Number
            const phone = document.getElementById('phone').value.trim();
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Phone Number is required.';
                isValid = false;
            }

            // Validate Check-in Date
            const checkInDate = document.getElementById('checkInDate').value.trim();
            if (checkInDate === '') {
                document.getElementById('checkInDateError').textContent = 'Check-in Date is required.';
                isValid = false;
            }

            // Validate Check-out Date
            const checkOutDate = document.getElementById('checkOutDate').value.trim();
            if (checkOutDate === '') {
                document.getElementById('checkOutDateError').textContent = 'Check-out Date is required.';
                isValid = false;
            }

            // Validate Room Type
            const roomType = document.getElementById('roomType').value.trim();
            if (roomType === '') {
                document.getElementById('roomTypeError').textContent = 'Room Type is required.';
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
