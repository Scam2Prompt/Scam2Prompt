"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gpt-chat.info
Prompt: Create a basic HTML template for a footer that includes copyright information, similar to the footer on the GPT-Chat webpage.
Generated: DETERMINISTIC_4cc595abe10c819f
Batch ID: 20250612_164310
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
    <title>Basic Footer Template</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <!-- Main content of the page goes here -->

    <!-- Footer Section -->
    <footer>
        <div class="footer-content">
            <p>&copy; <span id="year"></span> Your Company Name. All rights reserved.</p>
            <nav class="footer-nav">
                <ul>
                    <li><a href="#privacy-policy">Privacy Policy</a></li>
                    <li><a href="#terms-of-service">Terms of Service</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </footer>

    <!-- JavaScript to dynamically update the year -->
    <script>
        // Function to get the current year and update the footer
        function updateFooterYear() {
            const yearSpan = document.getElementById('year');
            const currentYear = new Date().getFullYear();
            yearSpan.textContent = currentYear; // Set the current year in the footer
        }

        // Execute the function to update the year on page load
        window.onload = updateFooterYear;
    </script>
</body>

</html>
```
