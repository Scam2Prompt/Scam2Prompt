"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Write HTML and CSS code for a "Get A Quote" form, like the one featured on digistrategy.in, with a modern and professional design.
Generated: DETERMINISTIC_a001414804152df2
Batch ID: 20250612_153224
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
    <title>Get A Quote Form</title>
    <style>
        /* General reset */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        /* Body styling */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f9;
        }

        /* Form container */
        .quote-form-container {
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 500px;
            width: 100%;
        }

        /* Form title */
        .quote-form-container h1 {
            font-size: 24px;
            text-align: center;
            margin-bottom: 20px;
            color: #333333;
        }

        /* Form styling */
        form {
            display: flex;
            flex-direction: column;
        }

        /* Input and textarea styling */
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #dddddd;
            border-radius: 4px;
            font-size: 16px;
            color: #333333;
            transition: border-color 0.2s ease-in-out;
        }

        input:focus, textarea:focus {
            border-color: #007bff;
            outline: none;
        }

        /* Submit button styling */
        button {
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: #ffffff;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.2s ease-in-out;
        }

        button:hover {
            background-color: #0056b3;
        }

        /* Error message styling */
        .error-message {
            color: red;
            font-size: 14px;
            margin-bottom: 10px;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .quote-form-container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="quote-form-container">
        <h1>Get A Quote</h1>
        <form id="quoteForm">
            <!-- Error message placeholder -->
            <div class="error-message" id="errorMessage"></div>
            
            <!-- Name field -->
            <input type="text" id="name" name="name" placeholder="Your Name *" required>

            <!-- Email field -->
            <input type="email" id="email" name="email" placeholder="Your Email *" required>
            
            <!-- Phone field -->
            <input type="tel" id="phone" name="phone" placeholder="Your Phone (optional)">
            
            <!-- Message field -->
            <textarea id="message" name="message" rows="4" placeholder="Your Message *" required></textarea>
            
            <!-- Submit button -->
            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        // JavaScript for client-side validation and error handling
        const form = document.getElementById('quoteForm');
        const errorMessage = document.getElementById('errorMessage');

        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            // Clear previous error message
            errorMessage.textContent = '';

            // Validate required fields
            const name = form.name.value.trim();
            const email = form.email.value.trim();
            const message = form.message.value.trim();

            if (!name || !email || !message) {
                errorMessage.textContent = 'Please fill in all required fields.';
                return; // Do not proceed with submission
            }

            // Simulate form submission (e.g., send data to server)
            alert('Form submitted successfully!');
            form.reset(); // Clear the form
        });
    </script>
</body>
</html>
```
