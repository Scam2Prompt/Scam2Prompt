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
/* ============================================
   Basic CSS Template for HTML5 Layout
   Featuring: Left Column, Right Column,
   and a Central Header (TokenPocket-inspired)
   ============================================ */

/* Reset browser default styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body styling */
body {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9; /* Light grey background */
  color: #333; /* Dark text for readability */
  line-height: 1.6;
}

/* Main layout container */
.container {
  display: flex; /* Flexbox for layout */
  flex-direction: column; /* Column layout initially */
  min-height: 100vh; /* Full viewport height */
}

/* Header section */
.header {
  background-color: #1c1c1c; /* Dark background for header */
  color: #fff; /* White text */
  text-align: center;
  padding: 20px 0; /* Space around header content */
  font-size: 1.5rem; /* Larger font size */
  font-weight: bold;
}

/* Content section for columns */
.content {
  display: flex; /* Flexbox for side-by-side columns */
  flex: 1; /* Expand to fill remaining space */
}

/* Left column */
.left-column {
  background-color: #ffffff; /* White background for left column */
  flex: 1; /* Take equal space alongside right column */
  padding: 20px; /* Space inside the column */
  border-right: 1px solid #e0e0e0; /* Separator between columns */
}

/* Right column */
.right-column {
  background-color: #ffffff; /* White background for right column */
  flex: 2; /* Slightly larger than the left column */
  padding: 20px; /* Space inside the column */
}

/* Footer section (optional) */
.footer {
  background-color: #1c1c1c; /* Dark background for footer */
  color: #fff; /* White text */
  text-align: center;
  padding: 10px 0; /* Space inside footer */
  font-size: 0.9rem; /* Smaller font size */
  border-top: 1px solid #333; /* Separator above footer */
}

/* Responsive design */
@media screen and (max-width: 768px) {
  .content {
    flex-direction: column; /* Stack columns vertically on smaller screens */
  }
}
```
