"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Design a simple ticket booking form with fields for number of tickets, ticket type, and preferred communication method using HTML and CSS.
Generated: DETERMINISTIC_7a3ef8cef76e4936
Batch ID: 20250622_212001
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket Booking Form</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        /* Form container */
        .booking-form {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 500px;
        }

        /* Form header */
        .form-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .form-header h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 10px;
        }

        /* Form fields */
        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }

        .form-control {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        select.form-control {
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 10px center;
            background-size: 1em;
        }

        /* Radio button group */
        .radio-group {
            display: flex;
            gap: 15px;
        }

        .radio-option {
            display: flex;
            align-items: center;
        }

        .radio-option input {
            margin-right: 8px;
        }

        /* Submit button */
        .submit-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #45a049;
        }

        /* Responsive adjustments */
        @media (max-width: 600px) {
            .booking-form {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <form class="booking-form">
        <div class="form-header">
            <h1>Ticket Booking</h1>
        </div>

        <div class="form-group">
            <label for="ticket-count">Number of Tickets</label>
            <input type="number" id="ticket-count" class="form-control" min="1" max="10" required>
        </div>

        <div class="form-group">
            <label for="ticket-type">Ticket Type</label>
            <select id="ticket-type" class="form-control" required>
                <option value="" disabled selected>Select ticket type</option>
                <option value="standard">Standard ($20)</option>
                <option value="vip">VIP ($50)</option>
                <option value="premium">Premium ($100)</option>
            </select>
        </div>

        <div class="form-group">
            <label>Preferred Communication Method</label>
            <div class="radio-group">
                <div class="radio-option">
                    <input type="radio" id="email" name="communication" value="email" checked>
                    <label for="email">Email</label>
                </div>
                <div class="radio-option">
                    <input type="radio" id="sms" name="communication" value="sms">
                    <label for="sms">SMS</label>
                </div>
                <div class="radio-option">
                    <input type="radio" id="phone" name="communication" value="phone">
                    <label for="phone">Phone Call</label>
                </div>
            </div>
        </div>

        <button type="submit" class="submit-btn">Book Tickets</button>
    </form>
</body>
</html>
```
