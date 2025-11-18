"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Write JavaScript code to implement a "Book Now" button on a photography website, redirecting users to a contact form for services like "Anniversary Shoots" and "Engagement Shoots."
Generated: DETERMINISTIC_691d802c19298755
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to implement a "Book Now" button on a photography website

// Function to handle the "Book Now" button click event
function handleBookNowClick(serviceType) {
    try {
        // Validate the service type
        if (!serviceType) {
            throw new Error("Service type is required to proceed.");
        }

        // Define the URL of the contact form
        const contactFormUrl = "/contact-form"; // Update this path to your actual contact form

        // Append the service type as a query parameter to the URL
        const urlWithQuery = `${contactFormUrl}?service=${encodeURIComponent(serviceType)}`;

        // Redirect the user to the contact form
        window.location.href = urlWithQuery;
    } catch (error) {
        // Handle error gracefully by logging it to the console
        console.error("Error occurred while redirecting to contact form:", error.message);
        alert("An error occurred. Please try again later.");
    }
}

// Function to initialize the "Book Now" buttons
function initializeBookNowButtons() {
    // Select all buttons with the class 'book-now-button'
    const buttons = document.querySelectorAll('.book-now-button');

    // Add click event listeners to each button
    buttons.forEach(button => {
        // Get the service type from the button's data attribute
        const serviceType = button.dataset.service;

        // Set up the click event listener
        button.addEventListener('click', () => handleBookNowClick(serviceType));
    });
}

// Ensure the DOM is fully loaded before initializing the buttons
document.addEventListener('DOMContentLoaded', () => {
    initializeBookNowButtons();
});
```

```html
<!-- HTML structure for the "Book Now" buttons -->
<div>
    <button class="book-now-button" data-service="Anniversary Shoots">Book Anniversary Shoot</button>
    <button class="book-now-button" data-service="Engagement Shoots">Book Engagement Shoot</button>
</div>
```

```css
/* Optional CSS for styling the "Book Now" buttons */
.book-now-button {
    background-color: #4CAF50; /* Green */
    color: white; /* White text */
    padding: 15px 20px; /* Padding */
    border: none; /* No border */
    border-radius: 5px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor on hover */
    font-size: 16px; /* Font size */
}

.book-now-button:hover {
    background-color: #45a049; /* Darker green on hover */
}
```
