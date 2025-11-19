"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betty-moore-873.pages.dev
Prompt: Provide an example of using HTML and CSS to create an eye-catching call-to-action button for a special offer.
Generated: DETERMINISTIC_0718527be70a6141
Batch ID: 20250612_155140
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
    <title>Call to Action Button Example</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Resetting margin and padding for a more consistent look across browsers */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Body styles */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f9f9f9;
        }

        /* Container for the button */
        .cta-container {
            text-align: center;
        }

        /* Call-to-action button styles */
        .cta-button {
            background-color: #ff5722; /* Bright orange for visibility */
            color: #ffffff; /* White text for contrast */
            padding: 15px 30px; /* Adequate padding for a comfortable click area */
            font-size: 18px; /* Larger font size for emphasis */
            border: none; /* Remove default border */
            border-radius: 5px; /* Rounded corners */
            cursor: pointer; /* Change cursor to pointer on hover */
            transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth transition effects */
            text-decoration: none; /* Remove underline for links */
        }

        /* Button hover and active states */
        .cta-button:hover {
            background-color: #e64a19; /* Darker shade on hover */
            transform: scale(1.05); /* Slightly increase the size on hover */
        }

        .cta-button:active {
            transform: scale(0.95); /* Scale down on click */
        }
    </style>
</head>
<body>
    <div class="cta-container">
        <h1>Special Offer Just for You!</h1>
        <p>Get 50% off your first purchase. Limited time only!</p>
        <a href="#" class="cta-button">Claim Your Offer</a>
    </div>
    
    <script>
        // Optional: Add click event listener to the button
        document.querySelector('.cta-button').addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default anchor behavior
            alert('Offer Claimed!'); // Notify the user (replace with actual logic)
        });
    </script>
</body>
</html>
```
