"""
Generated Code Metadata:
========================
Original URL: https://methodsmoney.com
Prompt: Write a CSS code example to style hover icons effectively, inspired by the design principles from methodsmoney.com.
Generated: DETERMINISTIC_bb16d1c840e18a3f
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Base styles for the icon container */
.icon-container {
    display: inline-block; /* Allows for inline positioning */
    margin: 10px; /* Space around each icon */
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effects */
}

/* Base styles for the icons */
.icon {
    width: 50px; /* Set a fixed width for icons */
    height: 50px; /* Set a fixed height for icons */
    background-color: #f0f0f0; /* Light background color */
    border-radius: 10px; /* Rounded corners */
    display: flex; /* Flexbox for centering */
    align-items: center; /* Center vertically */
    justify-content: center; /* Center horizontally */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    cursor: pointer; /* Pointer cursor on hover */
}

/* Hover effect for icons */
.icon:hover {
    transform: scale(1.1); /* Slightly enlarge the icon */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Increase shadow on hover */
    background-color: #e0e0e0; /* Darker background on hover */
}

/* Optional: Active state for icons */
.icon:active {
    transform: scale(1.05); /* Slightly reduce size on click */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Reset shadow */
}

/* Responsive design for smaller screens */
@media (max-width: 600px) {
    .icon {
        width: 40px; /* Smaller icons on mobile */
        height: 40px; /* Smaller icons on mobile */
    }
}
```
