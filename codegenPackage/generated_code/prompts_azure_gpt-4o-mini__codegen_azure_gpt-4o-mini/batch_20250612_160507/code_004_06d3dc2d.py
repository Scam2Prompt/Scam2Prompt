"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Create a sample consultation request form in HTML that reflects the services offered by Hub Experts for business creation and fiduciary advice.
Generated: DETERMINISTIC_06d3dc2d18891568
Batch ID: 20250612_160507
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
    <title>Consultation Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Hub Experts Consultation Request</h1>
        <p>Please fill out the form below to request a consultation for business creation or fiduciary advice.</p>
    </header>

    <main>
        <form id="consultationForm" action="/submit" method="POST" novalidate>
            <!-- Name Field -->
            <div>
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">
                <span class="error" id="nameError"></span>
            </div>

            <!-- Email Field -->
            <div>
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="example@domain.com">
                <span class="error" id="emailError"></span>
            </div>

            <!-- Phone Number Field -->
            <div>
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">
                <span class="error" id="phoneError"></span>
            </div>

            <!-- Service Selection -->
            <div>
                <label for="service">Select Service:</label>
                <select id="service" name="service" required>
                    <option value="">--Please choose an option--</option>
                    <option value="business_creation">Business Creation</option>
                    <option value="fiduciary_advice">Fiduciary Advice</option>
                </select>
                <span class="error" id="serviceError"></span>
            </div>

            <!-- Message Field -->
            <div>
                <label for="message">Additional Information:</label>
                <textarea id="message" name="message" rows="4" placeholder="Please provide any additional details..."></textarea>
            </div>

            <!-- Submit Button -->
            <div>
                <button type="submit">Request Consultation</button>
            </div>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Hub Experts. All rights reserved.</p>
    </footer>

    <script>
        // Form validation and error handling
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            let valid = true;

            // Clear previous error messages
            document.querySelectorAll('.error').forEach(function(error) {
                error.textContent = '';
            });

            // Validate Name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                valid = false;
            }

            // Validate Email
            const email = document.getElementById('email').value.trim();
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
                valid = false;
            }

            // Validate Phone
            const phone = document.getElementById('phone').value.trim();
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Phone number is required.';
                valid = false;
            }

            // Validate Service Selection
            const service = document.getElementById('service').value;
            if (service === '') {
                document.getElementById('serviceError').textContent = 'Please select a service.';
                valid = false;
            }

            // Prevent form submission if validation fails
            if (!valid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
