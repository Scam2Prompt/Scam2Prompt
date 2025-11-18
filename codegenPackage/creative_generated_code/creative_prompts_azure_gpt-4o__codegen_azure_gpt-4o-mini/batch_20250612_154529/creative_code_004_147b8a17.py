"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Generate HTML and CSS code for a responsive form that replicates Tripocost's flight booking interface, including dropdowns for airport codes, date pickers, and passenger details.
Generated: DETERMINISTIC_147b8a170e45cb8d
Batch ID: 20250612_154529
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
    <title>Flight Booking Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Flight Booking</h1>
        <form id="bookingForm">
            <div class="form-group">
                <label for="departureAirport">Departure Airport</label>
                <select id="departureAirport" name="departureAirport" required>
                    <option value="" disabled selected>Select Airport</option>
                    <option value="JFK">John F. Kennedy International Airport (JFK)</option>
                    <option value="LAX">Los Angeles International Airport (LAX)</option>
                    <option value="ORD">O'Hare International Airport (ORD)</option>
                    <option value="DFW">Dallas/Fort Worth International Airport (DFW)</option>
                </select>
            </div>

            <div class="form-group">
                <label for="arrivalAirport">Arrival Airport</label>
                <select id="arrivalAirport" name="arrivalAirport" required>
                    <option value="" disabled selected>Select Airport</option>
                    <option value="SFO">San Francisco International Airport (SFO)</option>
                    <option value="SEA">Seattle-Tacoma International Airport (SEA)</option>
                    <option value="MIA">Miami International Airport (MIA)</option>
                    <option value="LAS">McCarran International Airport (LAS)</option>
                </select>
            </div>

            <div class="form-group">
                <label for="departureDate">Departure Date</label>
                <input type="date" id="departureDate" name="departureDate" required>
            </div>

            <div class="form-group">
                <label for="returnDate">Return Date</label>
                <input type="date" id="returnDate" name="returnDate" required>
            </div>

            <div class="form-group">
                <label for="passengers">Number of Passengers</label>
                <select id="passengers" name="passengers" required>
                    <option value="" disabled selected>Select Number</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
            </div>

            <button type="submit" class="submit-btn">Book Flight</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Container for the form */
.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f8f9fa;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Style for header */
h1 {
    text-align: center;
    margin-bottom: 20px;
}

/* Form group styles */
.form-group {
    margin-bottom: 15px;
}

/* Label styles */
label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

/* Input and select styles */
input[type="date"],
select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ced4da;
    border-radius: 4px;
}

/* Button styles */
.submit-btn {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
}

/* Button hover effect */
.submit-btn:hover {
    background-color: #0056b3;
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .container {
        padding: 15px;
    }
}
```

```javascript
// script.js

// Adding an event listener on form submission
document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Form validation can be done here if needed

    // Collecting form data
    const formData = {
        departureAirport: this.departureAirport.value,
        arrivalAirport: this.arrivalAirport.value,
        departureDate: this.departureDate.value,
        returnDate: this.returnDate.value,
        passengers: this.passengers.value
    };

    // At this point, you could send the data to the server
    // Example: fetch('/api/booking', { method: 'POST', body: JSON.stringify(formData) })
    
    // For demonstration purposes, we'll just log the data
    console.log('Form submitted', formData);
});
```
