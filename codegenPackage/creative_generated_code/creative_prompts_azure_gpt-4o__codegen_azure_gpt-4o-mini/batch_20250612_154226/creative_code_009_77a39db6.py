"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Create a CSS template for styling product quick-view modals similar to those on the "Wall Memes" website, ensuring responsiveness and user-friendly design.
Generated: DETERMINISTIC_77a39db64b1b57da
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* CSS Template for Styling Product Quick-View Modals */

/* Base styles for the modal overlay */
.modal-overlay {
    position: fixed; /* Fixed position for overlay */
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
    display: flex; /* Flexbox for centering */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    visibility: hidden; /* Hidden by default */
    opacity: 0; /* Invisible by default */
    transition: visibility 0s, opacity 0.3s ease; /* Transition for smooth appearance */
}

/* Modal style when it is active */
.modal-overlay.active {
    visibility: visible; /* Make visible */
    opacity: 1; /* Fully opaque */
}

/* Base styles for the modal */
.modal {
    background: white; /* White background for the modal */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    max-width: 90%; /* Max width of modal */
    width: 600px; /* Fixed width for larger screens */
    padding: 20px; /* Padding inside modal */
    position: relative; /* Position relative for absolute elements */
}

/* Close button styles */
.close-button {
    position: absolute; /* Absolute positioning */
    top: 10px; /* Space from the top */
    right: 10px; /* Space from the right */
    background: none; /* No background */
    border: none; /* No border */
    font-size: 18px; /* Font size */
    cursor: pointer; /* Pointer cursor */
}

/* Title styles */
.modal-title {
    font-size: 24px; /* Large font for title */
    margin: 0 0 10px; /* Margin below title */
}

/* Product image styles */
.product-image {
    max-width: 100%; /* Responsive image */
    height: auto; /* Maintain aspect ratio */
    border-radius: 8px; /* Rounded corners */
}

/* Product description styles */
.product-description {
    font-size: 16px; /* Font size for description */
    margin: 15px 0; /* Margin above and below */
}

/* Button styles */
.product-button {
    display: inline-block; /* Button as block element */
    background-color: #007bff; /* Bootstrap primary color */
    color: white; /* White text */
    padding: 10px 20px; /* Padding */
    border: none; /* No border */
    border-radius: 5px; /* Rounded corners */
    text-align: center; /* Center text */
    font-size: 16px; /* Font size */
    cursor: pointer; /* Pointer cursor */
    transition: background-color 0.3s; /* Transition for hover effect */
}

/* Button hover effect */
.product-button:hover {
    background-color: #0056b3; /* Darker shade on hover */
}

/* Responsive styles */
@media (max-width: 600px) {
    .modal {
        width: 90%; /* Full width on small screens */
    }

    .modal-title {
        font-size: 20px; /* Smaller title font */
    }

    .product-description {
        font-size: 14px; /* Smaller description font */
    }

    .product-button {
        font-size: 14px; /* Smaller button font */
    }
}
```
