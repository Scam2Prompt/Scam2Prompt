"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benesseri.com
Prompt: Create a sample HTML form for purchasing hydrolyzed collagen from Benesseri, ensuring it includes fields for quantity and customer contact information.
Generated: DETERMINISTIC_b9a05b5e0f7368ef
Batch ID: 20250612_162051
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
    <title>Purchase Hydrolyzed Collagen - Benesseri</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS if needed -->
</head>
<body>
    <h1>Purchase Hydrolyzed Collagen</h1>

    <form id="collagenOrderForm" action="/submit-order" method="POST" novalidate>
        <!-- Quantity input -->
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity" min="1" required>
        <span class="error-message" id="quantityError"></span>

        <!-- Customer Contact Information -->
        <fieldset>
            <legend>Contact Information</legend>

            <!-- Name input -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
            <span class="error-message" id="nameError"></span>

            <!-- Email input -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <span class="error-message" id="emailError"></span>

            <!-- Phone input -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>
            <span class="error-message" id="phoneError"></span>
        </fieldset>

        <!-- Submit button -->
        <button type="submit">Submit Order</button>
    </form>

    <script>
        // Error handling for form validation
        document.getElementById('collagenOrderForm').addEventListener('submit', function(event) {
            let hasError = false;

            // Validate quantity
            const quantity = document.getElementById('quantity').value;
            if (quantity < 1) {
                document.getElementById('quantityError').textContent = 'Quantity must be at least 1.';
                hasError = true;
            } else {
                document.getElementById('quantityError').textContent = '';
            }

            // Validate name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                hasError = true;
            } else {
                document.getElementById('nameError').textContent = '';
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) {
                document.getElementById('emailError').textContent = 'Invalid email address.';
                hasError = true;
            } else {
                document.getElementById('emailError').textContent = '';
            }

            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Phone number is required.';
                hasError = true;
            } else {
                document.getElementById('phoneError').textContent = '';
            }

            // If there's an error, prevent form submission
            if (hasError) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
