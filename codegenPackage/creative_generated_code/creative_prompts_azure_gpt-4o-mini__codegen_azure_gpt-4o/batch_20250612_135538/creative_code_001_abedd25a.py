"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://questsmisten.site
Prompt: How can I implement a copyright notice in the footer of my website using HTML and CSS?
Generated: DETERMINISTIC_abedd25a7e362a36
Batch ID: 20250612_135538
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
    <title>Website with Footer</title>
    <style>
        /* Footer styles */
        footer {
            background-color: #f8f9fa; /* Light background color for contrast */
            text-align: center; /* Center-align text */
            padding: 10px 0; /* Add some spacing */
            font-size: 0.9em; /* Slightly smaller font size */
            color: #6c757d; /* Muted text color */
            border-top: 1px solid #dee2e6; /* Optional border for separation */
        }

        /* Responsive design: Ensure footer adapts to smaller screens */
        @media (max-width: 768px) {
            footer {
                font-size: 0.8em; /* Adjust font size for smaller screens */
            }
        }
    </style>
</head>

<body>
    <!-- Main content of the page -->
    <div>
        <h1>Welcome to My Website</h1>
        <p>This is a sample website with a copyright footer.</p>
    </div>

    <!-- Footer section -->
    <footer>
        <!-- Dynamically display the current year using JavaScript -->
        <p>&copy; <span id="currentYear"></span> Your Company Name. All rights reserved.</p>
    </footer>

    <script>
        // Set the current year dynamically in the footer
        const currentYearElement = document.getElementById("currentYear");
        const currentYear = new Date().getFullYear();
        currentYearElement.textContent = currentYear;
    </script>
</body>

</html>
```
