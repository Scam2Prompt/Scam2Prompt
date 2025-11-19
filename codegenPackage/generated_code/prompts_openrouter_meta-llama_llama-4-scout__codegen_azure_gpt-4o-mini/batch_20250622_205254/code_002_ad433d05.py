"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Generate a simple web page using HTML and JavaScript that displays the contact information of Colegio Panamericano e Instituto Libertadores, including phone numbers for different educational levels.
Generated: DETERMINISTIC_ad433d05e8e5997d
Batch ID: 20250622_205254
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
    <title>Colegio Panamericano e Instituto Libertadores - Contact Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        .contact-info {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .level {
            margin: 10px 0;
        }
    </style>
</head>
<body>

    <h1>Colegio Panamericano e Instituto Libertadores</h1>
    <div class="contact-info">
        <h2>Contact Information</h2>
        <div class="level">
            <strong>Preschool:</strong> <span id="preschool-phone"></span>
        </div>
        <div class="level">
            <strong>Elementary:</strong> <span id="elementary-phone"></span>
        </div>
        <div class="level">
            <strong>High School:</strong> <span id="highschool-phone"></span>
        </div>
    </div>

    <script>
        // Function to display contact information
        function displayContactInfo() {
            try {
                // Contact numbers for different educational levels
                const contactNumbers = {
                    preschool: "555-1234",
                    elementary: "555-5678",
                    highschool: "555-8765"
                };

                // Update the HTML elements with the contact numbers
                document.getElementById('preschool-phone').textContent = contactNumbers.preschool;
                document.getElementById('elementary-phone').textContent = contactNumbers.elementary;
                document.getElementById('highschool-phone').textContent = contactNumbers.highschool;
            } catch (error) {
                console.error("Error displaying contact information:", error);
                alert("An error occurred while loading contact information. Please try again later.");
            }
        }

        // Call the function to display contact information on page load
        window.onload = displayContactInfo;
    </script>

</body>
</html>
```
