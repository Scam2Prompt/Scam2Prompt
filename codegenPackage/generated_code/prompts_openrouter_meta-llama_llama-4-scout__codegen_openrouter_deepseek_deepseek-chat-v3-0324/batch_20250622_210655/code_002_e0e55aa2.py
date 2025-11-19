"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Generate a sample code for a travel concierge website's contact form, including fields for client information, travel preferences, and message, similar to the one on Rapala.tc.
Generated: DETERMINISTIC_e0e55aa2b2cb907f
Batch ID: 20250622_210655
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
    <title>Travel Concierge - Contact Us</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 150px;
        }
        .form-row {
            display: flex;
            gap: 20px;
        }
        .form-row .form-group {
            flex: 1;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            width: 100%;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            background: #2ecc71;
            color: white;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            text-align: center;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Travel Concierge Service</h1>
        <div id="success-message" class="success-message">
            Thank you for your inquiry! We'll get back to you soon.
        </div>
        <form id="contact-form">
            <div class="form-row">
                <div class="form-group">
                    <label for="first-name">First Name*</label>
                    <input type="text" id="first-name" name="first-name" required>
                    <div id="first-name-error" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="last-name">Last Name*</label>
                    <input type="text" id="last-name" name="last-name" required>
                    <div id="last-name-error" class="error"></div>
                </div>
            </div>

            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
                <div id="email-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
            </div>

            <div class="form-group">
                <label for="destination">Destination of Interest</label>
                <select id="destination" name="destination">
                    <option value="">Select a destination</option>
                    <option value="europe">Europe</option>
                    <option value="asia">Asia</option>
                    <option value="africa">Africa</option>
                    <option value="americas">Americas</option>
                    <option value="middle-east">Middle East</option>
                    <option value="oceania">Oceania</option>
                </select>
            </div>

            <div class="form-group">
                <label for="travel-dates">Preferred Travel Dates</label>
                <input type="text" id="travel-dates" name="travel-dates" placeholder="MM/DD/YYYY - MM/DD/YYYY">
            </div>

            <div class="form-group">
                <label for="travel-type">Type of Travel</label>
                <select id="travel-type" name="travel-type">
                    <option value="">Select travel type</option>
                    <option value="leisure">Leisure</option>
                    <option value="business">Business</option>
                    <option value="family">Family</option>
                    <option value="honeymoon">Honeymoon</option>
                    <option value="adventure">Adventure</option>
                </select>
            </div>

            <div class="form-group">
                <label for="budget">Approximate Budget (per person)</label>
                <select id="budget" name="budget">
                    <option value="">Select budget range</option>
                    <option value="under-1000">Under $1,000</option>
                    <option value="1000-3000">$1,000 - $3,000</option>
                    <option value="3000-5000">$3,000 - $5,000</option>
                    <option value="5000-10000">$5,000 - $10,000</option>
                    <option value="over-10000">Over $10,000</option>
                </select>
            </div>

            <div class="form-group">
                <label for="message">Your Travel Preferences & Message*</label>
                <textarea id="message" name="message" required placeholder="Tell us about your travel preferences, special requests, or any other details..."></textarea>
                <div id="message-error" class="error"></div>
            </div>

            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate form
            let isValid = true;
            const firstName = document.getElementById('first-name').value.trim();
            const lastName = document.getElementById('last-name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            if (!firstName) {
                document.getElementById('first-name-error').textContent = 'First name is required';
                isValid = false;
            }
            
            if (!lastName) {
                document.getElementById('last-name-error').textContent = 'Last name is required';
                isValid = false;
            }
            
            if (!email) {
                document.getElementById('email-error').textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('email-error').textContent = 'Please enter a valid email';
                isValid = false;
            }
            
            if (!message) {
                document.getElementById('message-error').textContent = 'Message is required';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would send the form data to the server here
                // For demonstration, we'll just show a success message
                document.getElementById('success-message').style.display = 'block';
                document.getElementById('contact-form').reset();
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    document.getElementById('success-message').style.display = 'none';
                }, 5000);
            }
        });
    </script>
</body>
</html>
```
