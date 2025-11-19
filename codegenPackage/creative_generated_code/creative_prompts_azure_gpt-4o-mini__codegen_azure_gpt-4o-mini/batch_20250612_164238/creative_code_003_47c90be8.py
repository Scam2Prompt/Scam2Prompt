"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Develop a sample HTML form for booking a boat rental at Coastal Boat Rentals, ensuring it includes fields for boat selection, rental duration, and customer contact information.
Generated: DETERMINISTIC_47c90be8926fdd7b
Batch ID: 20250612_164238
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
    <title>Coastal Boat Rentals - Booking Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Coastal Boat Rentals</h1>
        <h2>Book Your Boat Rental</h2>
    </header>

    <main>
        <form id="boatRentalForm" action="/submit" method="POST">
            <fieldset>
                <legend>Boat Selection</legend>
                <label for="boatType">Choose your boat:</label>
                <select id="boatType" name="boatType" required>
                    <option value="" disabled selected>Select a boat</option>
                    <option value="sailboat">Sailboat</option>
                    <option value="motorboat">Motorboat</option>
                    <option value="kayak">Kayak</option>
                    <option value="paddleboard">Paddleboard</option>
                </select>
            </fieldset>

            <fieldset>
                <legend>Rental Duration</legend>
                <label for="rentalDays">Number of days:</label>
                <input type="number" id="rentalDays" name="rentalDays" min="1" required>
            </fieldset>

            <fieldset>
                <legend>Contact Information</legend>
                <label for="customerName">Full Name:</label>
                <input type="text" id="customerName" name="customerName" required>
                
                <label for="customerEmail">Email Address:</label>
                <input type="email" id="customerEmail" name="customerEmail" required>
                
                <label for="customerPhone">Phone Number:</label>
                <input type="tel" id="customerPhone" name="customerPhone" required>
            </fieldset>

            <button type="submit">Submit Booking</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Coastal Boat Rentals. All rights reserved.</p>
    </footer>

    <script>
        // Client-side form validation before submission
        document.getElementById('boatRentalForm').addEventListener('submit', function(event) {
            // Implement additional validation if necessary
            const rentalDays = document.getElementById('rentalDays').value;
            if (rentalDays < 1) {
                alert('Please select at least one day for rental.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
