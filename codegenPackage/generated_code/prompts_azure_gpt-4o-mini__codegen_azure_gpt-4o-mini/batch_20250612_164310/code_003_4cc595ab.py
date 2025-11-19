"""
Generated Code Metadata:
========================
Original URL: https://www.gpt-chat.info
Prompt: Create a basic HTML template for a footer that includes copyright information, similar to the footer on the GPT-Chat webpage.
Generated: DETERMINISTIC_4cc595abe10c819f
Batch ID: 20250612_164310
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
    <title>Footer Example</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>

    <!-- Main content of the page goes here -->

    <footer>
        <div class="footer-content">
            <p>&copy; <span id="current-year"></span> Your Company Name. All rights reserved.</p>
            <nav class="footer-nav">
                <ul>
                    <li><a href="#privacy-policy">Privacy Policy</a></li>
                    <li><a href="#terms-of-service">Terms of Service</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </footer>

    <script>
        // Function to set the current year in the footer
        function setCurrentYear() {
            const yearElement = document.getElementById('current-year');
            if (yearElement) {
                const currentYear = new Date().getFullYear();
                yearElement.textContent = currentYear; // Set the current year
            } else {
                console.error('Year element not found'); // Error handling if element is missing
            }
        }

        // Call the function to set the current year on page load
        document.addEventListener('DOMContentLoaded', setCurrentYear);
    </script>

    <style>
        /* Basic styles for the footer */
        footer {
            background-color: #f8f9fa; /* Light background color */
            padding: 20px; /* Padding around the footer */
            text-align: center; /* Centered text */
            border-top: 1px solid #dee2e6; /* Top border for separation */
        }

        .footer-nav ul {
            list-style-type: none; /* Remove bullet points */
            padding: 0; /* Remove padding */
        }

        .footer-nav li {
            display: inline; /* Inline list items */
            margin: 0 15px; /* Spacing between items */
        }

        .footer-nav a {
            text-decoration: none; /* Remove underline from links */
            color: #007bff; /* Link color */
        }

        .footer-nav a:hover {
            text-decoration: underline; /* Underline on hover */
        }
    </style>

</body>
</html>
```
