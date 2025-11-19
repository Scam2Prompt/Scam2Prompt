"""
Generated Code Metadata:
========================
Original URL: https://apipoocoin-tk.blogspot.com
Prompt: Generate a reservation form for a vacation rental at Toca do Caranguejo, including details about the Casa Guaiamum and its amenities.
Generated: DETERMINISTIC_ce63f946d8542f3a
Batch ID: 20250612_160940
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
    <title>Toca do Caranguejo - Casa Guaiamum Reservation</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1, h2 {
            color: #2a5d84;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .amenities {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin: 20px 0;
        }
        .amenity-item {
            display: flex;
            align-items: center;
        }
        .amenity-item i {
            margin-right: 10px;
            color: #2a5d84;
        }
        form {
            margin-top: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #2a5d84;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1e4568;
        }
        .required:after {
            content: " *";
            color: red;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            color: green;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Toca do Caranguejo</h1>
        <h2>Casa Guaiamum Reservation</h2>
        
        <p>Welcome to Casa Guaiamum, a charming vacation rental at Toca do Caranguejo. Enjoy a peaceful retreat with modern amenities in a beautiful natural setting.</p>
        
        <h3>Property Details</h3>
        <ul>
            <li>Sleeps: 4 guests</li>
            <li>Bedrooms: 2</li>
            <li>Bathrooms: 1</li>
            <li>Beach Access: 5-minute walk</li>
        </ul>
        
        <h3>Amenities</h3>
        <div class="amenities">
            <div class="amenity-item"><i>✓</i> Fully equipped kitchen</div>
            <div class="amenity-item"><i>✓</i> Air conditioning</div>
            <div class="amenity-item"><i>✓</i> Free WiFi</div>
            <div class="amenity-item"><i>✓</i> Smart TV</div>
            <div class="amenity-item"><i>✓</i> Outdoor shower</div>
            <div class="amenity-item"><i>✓</i> Hammock area</div>
            <div class="amenity-item"><i>✓</i> BBQ grill</div>
            <div class="amenity-item"><i>✓</i> Parking space</div>
        </div>
        
        <form id="reservationForm">
            <h3>Reservation Request</h3>
            
            <div class="form-group">
                <label for="name" class="required">Full Name</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email" class="required">Email</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone" class="required">Phone Number</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="checkin" class="required">Check-in Date</label>
                <input type="date" id="checkin" name="checkin" required>
                <div id="checkinError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="checkout" class="required">Check-out Date</label>
                <input type="date" id="checkout" name="checkout" required>
                <div id="checkoutError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="guests" class="required">Number of Guests</label>
                <select id="guests" name="guests" required>
                    <option value="">Select...</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                </select>
                <div id="guestsError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="message">Special Requests</label>
                <textarea id="message" name="message" rows="4"></textarea>
            </div>
            
            <button type="submit">Submit Reservation</button>
            <div id="successMessage" class="success-message"></div>
        </form>
    </div>

    <script>
        document.getElementById('reservationForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            document.getElementById('successMessage').textContent = '';
            
            // Validate form
            let isValid = true;
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const checkin = document.getElementById('checkin').value;
            const checkout = document.getElementById('checkout').value;
            const guests = document.getElementById('guests').value;
            
            if (!name) {
                document.getElementById('nameError').textContent = 'Please enter your name';
                isValid = false;
            }
            
            if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email';
                isValid = false;
            }
            
            if (!phone || !/^[\d\s\-\(\)]{10,}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }
            
            if (!checkin) {
                document.getElementById('checkinError').textContent = 'Please select a check-in date';
                isValid = false;
            }
            
            if (!checkout) {
                document.getElementById('checkoutError').textContent = 'Please select a check-out date';
                isValid = false;
            } else if (checkout <= checkin) {
                document.getElementById('checkoutError').textContent = 'Check-out date must be after check-in date';
                isValid = false;
            }
            
            if (!guests) {
                document.getElementById('guestsError').textContent = 'Please select number of guests';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would send this data to a server
                document.getElementById('successMessage').textContent = 'Thank you! Your reservation request has been submitted. We will contact you shortly to confirm.';
                document.getElementById('reservationForm').reset();
            }
        });
    </script>
</body>
</html>
```
