"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Develop a CSS style for a fullscreen slider that aligns with the design aesthetics of the IMST Telehealth homepage, focusing on visual clarity and simplicity.
Generated: DETERMINISTIC_52a32f29279dcc3f
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Fullscreen Slider CSS for IMST Telehealth Homepage */
/* This stylesheet is designed to ensure clarity, simplicity, and alignment with professional design aesthetics */

/* Base styling for the slider container */
.slider-container {
    position: relative; /* Allows positioning of child elements */
    width: 100vw; /* Full viewport width */
    height: 100vh; /* Full viewport height */
    overflow: hidden; /* Prevents content spill outside the container */
    background-color: #f5f5f5; /* Neutral background for clarity */
    display: flex; /* Flexbox for alignment */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
}

/* Individual slide styles */
.slide {
    position: absolute; /* Overlay positioning */
    width: 100%; /* Full width of the slider */
    height: 100%; /* Full height of the slider */
    background-size: cover; /* Covers the entire slide area */
    background-position: center; /* Centers the background image */
    opacity: 0; /* Start hidden */
    transition: opacity 0.5s ease-in-out; /* Smooth fade effect */
}

/* Active slide */
.slide.active {
    opacity: 1; /* Fully visible */
}

/* Navigation buttons styling */
.nav-button {
    position: absolute; /* Positioned within the slider container */
    top: 50%; /* Center vertically */
    transform: translateY(-50%); /* Adjust for perfect centering */
    background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
    color: #ffffff; /* White text color for contrast */
    border: none; /* No border for a clean look */
    padding: 10px 20px; /* Button padding */
    cursor: pointer; /* Pointer cursor on hover */
    font-size: 18px; /* Readable font size */
    z-index: 10; /* Ensures buttons are above slides */
    transition: background-color 0.3s ease; /* Smooth hover effect */
}

/* Left navigation button */
.nav-button.left {
    left: 15px; /* Positioned near the left edge */
}

/* Right navigation button */
.nav-button.right {
    right: 15px; /* Positioned near the right edge */
}

/* Navigation button hover effect */
.nav-button:hover {
    background-color: rgba(0, 0, 0, 0.7); /* Darker background on hover */
}

/* Dot navigation styling */
.nav-dots {
    position: absolute; /* Positioned within the slider container */
    bottom: 20px; /* Positioned near the bottom */
    width: 100%; /* Full width for centering dots */
    display: flex; /* Flexbox for alignment */
    justify-content: center; /* Center dots horizontally */
    gap: 10px; /* Spacing between dots */
    z-index: 10; /* Above slides */
}

.nav-dot {
    width: 12px; /* Dot width */
    height: 12px; /* Dot height */
    border-radius: 50%; /* Circular dots */
    background-color: rgba(0, 0, 0, 0.5); /* Neutral semi-transparent color */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background-color 0.3s ease; /* Smooth hover effect */
}

/* Active navigation dot */
.nav-dot.active {
    background-color: #007bff; /* Highlight color (e.g., blue accent) */
}

/* Hover effect for navigation dots */
.nav-dot:hover {
    background-color: rgba(0, 0, 0, 0.7); /* Darker on hover */
}

/* Responsive adjustments for small screens */
@media (max-width: 768px) {
    .nav-button {
        font-size: 16px; /* Adjust font size for smaller screens */
        padding: 8px 16px; /* Adjust padding for smaller screens */
    }
    .nav-dot {
        width: 10px; /* Adjust dot size */
        height: 10px; /* Adjust dot size */
    }
}
```
