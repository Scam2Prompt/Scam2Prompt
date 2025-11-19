"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seandahealthcare.co.za
Prompt: Develop a simple HTML form for healthcare professionals to register with Seanda Healthcare, including fields for name, qualifications, and contact information.
Generated: DETERMINISTIC_6474446305b26aff
Batch ID: 20250612_155732
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
    <title>Seanda Healthcare Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="email"], input[type="tel"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <h1>Healthcare Professional Registration</h1>
    <form id="registrationForm" action="/submit-registration" method="POST">
        <div class="form-group">
            <label for="name">Full Name</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">
        </div>
        <div class="form-group">
            <label for="qualifications">Qualifications</label>
            <input type="text" id="qualifications" name="qualifications" required placeholder="Enter your qualifications">
        </div>
        <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">
        </div>
        <div class="form-group">
            <label for="phone">Contact Number</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your contact number">
        </div>
        <button type="submit">Register</button>
    </form>

    <script>
        // Form submission handling
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Perform client-side validation (if needed)

            // Gather form data
            const formData = new FormData(this);

            // Example of sending data via Fetch API
            fetch(this.action, {
                method: this.method,
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Handle success, e.g., show a success message
                alert('Registration successful!');
            })
            .catch(error => {
                // Handle error, e.g., show an error message
                console.error('There was a problem with the fetch operation:', error);
                alert('Registration failed. Please try again.');
            });
        });
    </script>

</body>
</html>
```
