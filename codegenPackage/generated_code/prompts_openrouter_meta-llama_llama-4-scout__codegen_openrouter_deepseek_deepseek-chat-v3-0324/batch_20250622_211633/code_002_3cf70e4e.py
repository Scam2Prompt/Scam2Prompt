"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Generate a code snippet to create a simple web page for quoting and reserving outdoor advertising locations, similar to the functionality provided by WOW MEDIA."
Generated: DETERMINISTIC_3cf70e4eacb4a121
Batch ID: 20250622_211633
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
    <title>Outdoor Advertising Reservation System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #35424a;
            color: white;
            padding: 20px 0;
            text-align: center;
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
        }
        button {
            background: #35424a;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 4px;
        }
        button:hover {
            background: #4e5d6c;
        }
        .quote-result {
            margin-top: 20px;
            padding: 20px;
            background: #f4f4f4;
            border-radius: 4px;
            display: none;
        }
        footer {
            text-align: center;
            padding: 20px 0;
            background: #35424a;
            color: white;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Outdoor Advertising Reservation</h1>
            <p>Book premium outdoor advertising locations with ease</p>
        </div>
    </header>

    <div class="container">
        <form id="reservationForm">
            <div class="form-group">
                <label for="location">Select Location:</label>
                <select id="location" required>
                    <option value="">-- Select a location --</option>
                    <option value="times-square">Times Square, NYC</option>
                    <option value="la-billboard">Los Angeles Billboard</option>
                    <option value="chicago-l-train">Chicago L-Train</option>
                    <option value="miami-beach">Miami Beach</option>
                </select>
            </div>

            <div class="form-group">
                <label for="adType">Advertising Type:</label>
                <select id="adType" required>
                    <option value="">-- Select ad type --</option>
                    <option value="billboard">Billboard</option>
                    <option value="digital-screen">Digital Screen</option>
                    <option value="transit-ad">Transit Ad</option>
                    <option value="street-furniture">Street Furniture</option>
                </select>
            </div>

            <div class="form-group">
                <label for="duration">Duration (weeks):</label>
                <input type="number" id="duration" min="1" max="52" required>
            </div>

            <div class="form-group">
                <label for="startDate">Start Date:</label>
                <input type="date" id="startDate" required>
            </div>

            <div class="form-group">
                <label for="contactEmail">Contact Email:</label>
                <input type="email" id="contactEmail" required>
            </div>

            <div class="form-group">
                <label for="specialRequests">Special Requests:</label>
                <textarea id="specialRequests" rows="4"></textarea>
            </div>

            <button type="button" onclick="calculateQuote()">Get Quote</button>
        </form>

        <div id="quoteResult" class="quote-result">
            <h3>Your Quote</h3>
            <p id="quoteDetails"></p>
            <button type="button" onclick="confirmReservation()">Confirm Reservation</button>
        </div>
    </div>

    <footer>
        <div class="container">
            <p>&copy; 2023 Outdoor Advertising Reservation System</p>
        </div>
    </footer>

    <script>
        // Price mapping based on location and ad type
        const priceMap = {
            'times-square': {
                'billboard': 5000,
                'digital-screen': 7000,
                'transit-ad': 3000,
                'street-furniture': 2000
            },
            'la-billboard': {
                'billboard': 4000,
                'digital-screen': 6000,
                'transit-ad': 2500,
                'street-furniture': 1800
            },
            'chicago-l-train': {
                'billboard': 3500,
                'digital-screen': 5000,
                'transit-ad': 2000,
                'street-furniture': 1500
            },
            'miami-beach': {
                'billboard': 4500,
                'digital-screen': 6500,
                'transit-ad': 2800,
                'street-furniture': 1900
            }
        };

        /**
         * Calculates the quote based on user selections
         */
        function calculateQuote() {
            try {
                const location = document.getElementById('location').value;
                const adType = document.getElementById('adType').value;
                const duration = parseInt(document.getElementById('duration').value);
                const startDate = document.getElementById('startDate').value;

                // Validate inputs
                if (!location || !adType || !duration || !startDate) {
                    alert('Please fill in all required fields');
                    return;
                }

                // Calculate total price
                const weeklyPrice = priceMap[location][adType];
                const totalPrice = weeklyPrice * duration;

                // Display quote
                document.getElementById('quoteDetails').innerHTML = `
                    <strong>Location:</strong> ${document.getElementById('location').options[document.getElementById('location').selectedIndex].text}<br>
                    <strong>Ad Type:</strong> ${document.getElementById('adType').options[document.getElementById('adType').selectedIndex].text}<br>
                    <strong>Duration:</strong> ${duration} weeks<br>
                    <strong>Start Date:</strong> ${startDate}<br>
                    <strong>Weekly Price:</strong> $${weeklyPrice.toLocaleString()}<br>
                    <strong>Total Price:</strong> $${totalPrice.toLocaleString()}
                `;

                document.getElementById('quoteResult').style.display = 'block';
            } catch (error) {
                console.error('Error calculating quote:', error);
                alert('An error occurred while calculating your quote. Please try again.');
            }
        }

        /**
         * Confirms the reservation (simulated)
         */
        function confirmReservation() {
            try {
                const email = document.getElementById('contactEmail').value;
                if (!email) {
                    alert('Please provide your contact email');
                    return;
                }

                // In a real application, this would send data to a server
                alert(`Thank you! Your reservation request has been received. We'll contact you at ${email} shortly.`);
                document.getElementById('reservationForm').reset();
                document.getElementById('quoteResult').style.display = 'none';
            } catch (error) {
                console.error('Error confirming reservation:', error);
                alert('An error occurred while processing your reservation. Please try again.');
            }
        }

        // Set minimum date to today
        document.getElementById('startDate').min = new Date().toISOString().split('T')[0];
    </script>
</body>
</html>
```
