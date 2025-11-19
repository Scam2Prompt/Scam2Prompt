"""
Generated Code Metadata:
========================
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Design a webpage section that showcases a big sale or on-site event, including details about the event and a call-to-action.
Generated: DETERMINISTIC_0c9db8d2366c1868
Batch ID: 20250622_212444
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
    <title>Big Sale Event</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section id="big-sale" class="event-section">
        <div class="container">
            <h1 class="event-title">Huge Summer Sale!</h1>
            <p class="event-date">July 1 - July 15, 2023</p>
            <p class="event-description">
                Join us for our biggest sale of the year! Enjoy discounts up to 50% on selected items.
                Don't miss out on exclusive deals and offers available only during this event.
            </p>
            <a href="#shop-now" class="cta-button">Shop Now</a>
        </div>
    </section>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Styling for the event section */
.event-section {
    background-color: #ffcc00; /* Bright background for visibility */
    color: #333; /* Dark text for contrast */
    padding: 20px;
    text-align: center;
}

.container {
    max-width: 800px;
    margin: 0 auto; /* Center the container */
}

.event-title {
    font-size: 2.5em; /* Large title */
    margin-bottom: 10px;
}

.event-date {
    font-size: 1.2em; /* Slightly smaller date */
    margin-bottom: 15px;
}

.event-description {
    font-size: 1em; /* Standard description size */
    margin-bottom: 20px;
}

.cta-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007bff; /* Button color */
    color: white; /* Button text color */
    text-decoration: none; /* Remove underline */
    border-radius: 5px; /* Rounded corners */
    transition: background-color 0.3s; /* Smooth transition */
}

.cta-button:hover {
    background-color: #0056b3; /* Darker shade on hover */
}
```

```javascript
// script.js

// Function to handle the call-to-action button click
document.addEventListener('DOMContentLoaded', () => {
    const ctaButton = document.querySelector('.cta-button');

    // Check if the button exists before adding an event listener
    if (ctaButton) {
        ctaButton.addEventListener('click', (event) => {
            event.preventDefault(); // Prevent default anchor behavior
            // Redirect to the shopping section or page
            window.location.href = '#shop-now'; // Change this to the actual shop URL
        });
    } else {
        console.error('CTA button not found'); // Log error if button is missing
    }
});
```
