"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.insectshieldzoro.com
Prompt: Write JavaScript code to implement a contact form that dynamically updates based on user queries about products like UPVC mosquito nets or stainless steel mesh, as described on the Insect Shield ZORO website.
Generated: DETERMINISTIC_f224359890f47be9
Batch ID: 20250612_151329
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
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .hidden {
            display: none;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

<h1>Contact Us</h1>
<form id="contactForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required><br><br>

    <label for="productQuery">Product Query:</label>
    <select id="productQuery" name="productQuery" required>
        <option value="">Select a product</option>
        <option value="UPVC mosquito nets">UPVC Mosquito Nets</option>
        <option value="stainless steel mesh">Stainless Steel Mesh</option>
    </select><br><br>

    <div id="additionalInfo" class="hidden">
        <label for="info">Additional Information:</label>
        <textarea id="info" name="info" rows="4" cols="50" placeholder="Please provide additional information..."></textarea>
    </div>

    <span id="errorMessage" class="error hidden"></span><br><br>

    <button type="submit">Submit</button>
</form>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const productQuery = document.getElementById('productQuery');
        const additionalInfo = document.getElementById('additionalInfo');
        const errorMessage = document.getElementById('errorMessage');
        const contactForm = document.getElementById('contactForm');

        // Event listener to show/hide additional information based on product selection
        productQuery.addEventListener('change', () => {
            if (productQuery.value) {
                additionalInfo.classList.remove('hidden');
            } else {
                additionalInfo.classList.add('hidden');
            }
        });

        // Form submission event handler
        contactForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent default form submission
            errorMessage.classList.add('hidden'); // Hide previous errors

            // Form validation
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const product = productQuery.value;
            const additional = document.getElementById('info').value.trim();

            if (!name || !email || !product) {
                errorMessage.textContent = "Please fill in all required fields.";
                errorMessage.classList.remove('hidden');
                return;
            }

            // Simple email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                errorMessage.textContent = "Please enter a valid email address.";
                errorMessage.classList.remove('hidden');
                return;
            }

            // Simulating a successful form submission
            // In a real-world scenario, you would send the data to a server here
            console.log("Form submitted successfully!");
            console.log({ name, email, product, additional });

            // Reset form after successful submission
            contactForm.reset();
            additionalInfo.classList.add('hidden');
        });
    });
</script>

</body>
</html>
```
