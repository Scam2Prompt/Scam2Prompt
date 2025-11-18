"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenp0cket.net
Prompt: Create a CSS stylesheet for an HTML5 template with a layout featuring a left column, right column, and a central header, inspired by the TokenPocket design.
Generated: DETERMINISTIC_279e78eacefe743b
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Global Styles */
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4; /* Light background for better readability */
}

/* Container for the main layout */
.container {
    display: flex; /* Utilizing flexbox for layout */
    flex-direction: column; /* Stacking columns vertically */
    height: 100vh; /* Full viewport height */
}

/* Header Styles */
.header {
    background-color: #3a3a3a; /* Dark header background */
    color: #ffffff; /* White text for contrast */
    text-align: center; /* Centering header text */
    padding: 20px; /* Padding for spacing */
    font-size: 24px; /* Font size for header */
}

/* Main content area */
.main {
    display: flex; /* Flexbox for side-by-side layout */
    flex: 1; /* Take remaining space */
}

/* Left Column Styles */
.left-column {
    background-color: #ffffff; /* White background for left column */
    width: 250px; /* Fixed width for left column */
    padding: 15px; /* Padding for content spacing */
    border-right: 1px solid #dddddd; /* Light border for separation */
}

/* Right Column Styles */
.right-column {
    background-color: #ffffff; /* White background for right column */
    width: 250px; /* Fixed width for right column */
    padding: 15px; /* Padding for content spacing */
    border-left: 1px solid #dddddd; /* Light border for separation */
}

/* Central Content Styles */
.center-content {
    flex: 1; /* Take remaining space between columns */
    padding: 15px; /* Padding for spacing */
    background-color: #e9e9e9; /* Light grey for central content */
}

/* Responsive Design */
@media (max-width: 768px) {
    .main {
        flex-direction: column; /* Stack columns vertically on small screens */
    }

    .left-column,
    .right-column {
        width: 100%; /* Full width for columns in small screens */
        border: none; /* Remove borders for better mobile view */
    }
}
```
