"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autocarescosme.com
Prompt: Construct a sample HTML form for users to inquire about renting classic vehicles from Autocares Cosme, ensuring it captures all necessary information for the booking process.
Generated: DETERMINISTIC_f7e8b30c74729fb1
Batch ID: 20250612_163406
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
    <title>Classic Vehicle Rental Inquiry</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external CSS file for styling -->
</head>
<body>
    <header>
        <h1>Autocares Cosme - Classic Vehicle Rental Inquiry</h1>
    </header>

    <main>
        <form id="rental-inquiry-form" action="/submit-inquiry" method="POST">
            <fieldset>
                <legend>Rental Inquiry Form</legend>

                <!-- Customer Information Section -->
                <section>
                    <h2>Customer Information</h2>
                    <label for="full-name">Full Name:</label>
                    <input type="text" id="full-name" name="full_name" required placeholder="John Doe">

                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required placeholder="example@example.com">

                    <label for="phone">Phone Number:</label>
                    <input type="tel" id="phone" name="phone" required placeholder="+1 (555) 555-5555">
                </section>

                <!-- Vehicle Selection Section -->
                <section>
                    <h2>Vehicle Selection</h2>
                    <label for="vehicle-type">Select Vehicle Type:</label>
                    <select id="vehicle-type" name="vehicle_type" required>
                        <option value="">--Please choose an option--</option>
                        <option value="classic-car">Classic Car</option>
                        <option value="vintage-van">Vintage Van</option>
                        <option value="sports-car">Sports Car</option>
                        <option value="luxury-car">Luxury Car</option>
                    </select>

                    <label for="rental-date">Rental Start Date:</label>
                    <input type="date" id="rental-date" name="rental_date" required>

                    <label for="return-date">Rental End Date:</label>
                    <input type="date" id="return-date" name="return_date" required>
                </section>

                <!-- Additional Requests Section -->
                <section>
                    <h2>Additional Requests</h2>
                    <label for="special-requests">Any Special Requests:</label>
                    <textarea id="special-requests" name="special_requests" rows="4" placeholder="E.g., specific vehicle preferences, additional services..."></textarea>
                </section>

                <!-- Submit Button -->
                <button type="submit">Submit Inquiry</button>
            </fieldset>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Autocares Cosme. All rights reserved.</p>
    </footer>

    <script>
        // Client-side form submission validation
        document.getElementById('rental-inquiry-form').addEventListener('submit', function(event) {
            // Validate rental dates
            const rentalDate = new Date(document.getElementById('rental-date').value);
            const returnDate = new Date(document.getElementById('return-date').value);
            if (returnDate <= rentalDate) {
                alert('Return date must be later than rental start date.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
