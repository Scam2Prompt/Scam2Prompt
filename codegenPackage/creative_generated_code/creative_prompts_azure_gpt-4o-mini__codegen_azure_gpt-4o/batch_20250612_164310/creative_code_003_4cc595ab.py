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
    <title>Footer Example</title>
    <style>
        /* Basic styles for the footer */
        footer {
            background-color: #f8f9fa; /* Light gray background */
            padding: 20px;
            text-align: center;
            font-size: 0.9rem;
            border-top: 1px solid #dee2e6; /* Subtle border for separation */
        }

        /* Styling the copyright text */
        .footer-content {
            color: #495057; /* Dark gray text color */
        }

        /* Styling links in the footer */
        .footer-content a {
            color: #007bff; /* Blue links */
            text-decoration: none; /* Remove underline */
        }

        .footer-content a:hover {
            text-decoration: underline; /* Add underline on hover */
        }
    </style>
</head>
<body>
    <!-- Page content -->
    <div class="content">
        <p>Your main page content goes here.</p>
    </div>

    <!-- Footer section -->
    <footer>
        <div class="footer-content">
            <!-- Copyright information -->
            <p>&copy; <span id="currentYear"></span> YourCompanyName. All rights reserved.</p>
            
            <!-- Optional links -->
            <p>
                <a href="/privacy-policy">Privacy Policy</a> |
                <a href="/terms-of-service">Terms of Service</a>
            </p>
        </div>
    </footer>

    <script>
        // Set the current year dynamically
        document.getElementById('currentYear').textContent = new Date().getFullYear();
        
        // (Optional) Add error handling to ensure the element exists
        try {
            const yearElement = document.getElementById('currentYear');
            if (yearElement) {
                yearElement.textContent = new Date().getFullYear();
            } else {
                console.error('Footer year element not found.');
            }
        } catch (error) {
            console.error('An error occurred while setting the footer year:', error);
        }
    </script>
</body>
</html>
```
