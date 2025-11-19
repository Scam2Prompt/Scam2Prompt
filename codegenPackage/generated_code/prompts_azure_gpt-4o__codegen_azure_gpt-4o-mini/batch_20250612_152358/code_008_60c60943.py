"""
Generated Code Metadata:
========================
Original URL: https://zeek.social
Prompt: Create a CSS media query setup for responsive card components in a Web3 application, referencing Zeek Network's `wui-card` and `wui-flex` styles.
Generated: DETERMINISTIC_60c60943a434802a
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Base styles for card components */
.wui-card {
    background-color: #ffffff; /* Card background color */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    padding: 16px; /* Inner padding */
    margin: 16px; /* Outer margin */
    transition: transform 0.2s; /* Smooth hover effect */
}

/* Hover effect for cards */
.wui-card:hover {
    transform: scale(1.05); /* Slightly enlarge on hover */
}

/* Flex container for card layout */
.wui-flex {
    display: flex; /* Use flexbox for layout */
    flex-wrap: wrap; /* Allow wrapping of cards */
    justify-content: space-between; /* Space between cards */
}

/* Media query for tablet devices */
@media (max-width: 768px) {
    .wui-flex {
        justify-content: center; /* Center cards on smaller screens */
    }

    .wui-card {
        width: 90%; /* Full width for cards on small screens */
        margin: 8px 0; /* Reduced margin for better spacing */
    }
}

/* Media query for mobile devices */
@media (max-width: 480px) {
    .wui-card {
        padding: 12px; /* Reduced padding for mobile */
        margin: 4px 0; /* Further reduced margin */
    }
}
```
