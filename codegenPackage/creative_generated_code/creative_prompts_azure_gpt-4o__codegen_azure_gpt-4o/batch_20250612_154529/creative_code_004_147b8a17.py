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
  <title>Tripocost Flight Booking</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="form-container">
    <form id="flight-booking-form">
      <!-- Flight Type Selection -->
      <div class="form-group">
        <label for="flight-type">Flight Type</label>
        <select id="flight-type" name="flight-type" required>
          <option value="one-way">One Way</option>
          <option value="round-trip">Round Trip</option>
          <option value="multi-city">Multi-City</option>
        </select>
      </div>

      <!-- Departure Airport -->
      <div class="form-group">
        <label for="departure-airport">Departure Airport</label>
        <select id="departure-airport" name="departure-airport" required>
          <option value="">Select Airport</option>
          <option value="JFK">John F. Kennedy International Airport (JFK)</option>
          <option value="SFO">San Francisco International Airport (SFO)</option>
          <option value="LAX">Los Angeles International Airport (LAX)</option>
          <!-- Add more airport codes as needed -->
        </select>
      </div>

      <!-- Destination Airport -->
      <div class="form-group">
        <label for="destination-airport">Destination Airport</label>
        <select id="destination-airport" name="destination-airport" required>
          <option value="">Select Airport</option>
          <option value="ORD">O'Hare International Airport (ORD)</option>
          <option value="ATL">Hartsfield-Jackson Atlanta International Airport (ATL)</option>
          <option value="DFW">Dallas/Fort Worth International Airport (DFW)</option>
          <!-- Add more airport codes as needed -->
        </select>
      </div>

      <!-- Departure Date -->
      <div class="form-group">
        <label for="departure-date">Departure Date</label>
        <input type="date" id="departure-date" name="departure-date" required>
      </div>

      <!-- Return Date -->
      <div class="form-group return-date-group">
        <label for="return-date">Return Date</label>
        <input type="date" id="return-date" name="return-date">
      </div>

      <!-- Passenger Details -->
      <div class="form-group">
        <label for="passengers">Passengers</label>
        <input type="number" id="passengers" name="passengers" min="1" max="20" value="1" required>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit" id="submit-button">Search Flights</button>
      </div>
    </form>
  </div>
</body>
</html>

<style>
/* styles.css */

/* Reset styles */
body, h1, h2, h3, p, ul, ol, li, form, input, select, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body styling */
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

/* Form container styling */
.form-container {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 100%;
  max-width: 400px;
}

/* Form group styling */
.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group select,
.form-group button {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* Button styling */
button {
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

/* Responsive Design */
@media (max-width: 768px) {
  .form-container {
    padding: 15px;
  }
}
</style>
```
