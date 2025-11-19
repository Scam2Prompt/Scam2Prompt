"""
Generated Code Metadata:
========================
Original URL: https://scrollify.gitbook.io
Prompt: Generate a CSS code snippet to customize the scroll button style for a Scrollify integration on an online store with a minimalist design.
Generated: DETERMINISTIC_53ea59eeb5fd9a73
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Scrollify scroll button styles */

/* Base styles for the scroll button */
.scrollify {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}

/* Style the scroll button */
.scrollify .scrollify-button {
  background-color: #ffffff; /* White background */
  border: 1px solid #dddddd; /* Light gray border */
  border-radius: 50%; /* Circular shape */
  cursor: pointer;
  padding: 10px;
  transition: background-color 0.2s ease-in-out;
}

/* Hover effect for the scroll button */
.scrollify .scrollify-button:hover {
  background-color: #f7f7f7; /* Light gray on hover */
}

/* Active state for the scroll button */
.scrollify .scrollify-button:active {
  transform: scale(0.9); /* Slightly shrink on active */
}

/* Style the scroll button icon */
.scrollify .scrollify-button i {
  font-size: 18px; /* Icon size */
  color: #666666; /* Dark gray icon color */
}

/* Media query for smaller screens */
@media (max-width: 768px) {
  .scrollify {
    bottom: 10px;
    right: 10px;
  }
  .scrollify .scrollify-button {
    padding: 8px;
  }
  .scrollify .scrollify-button i {
    font-size: 16px;
  }
}

/* Error handling: Hide scroll button if JavaScript is disabled */
/* This requires a .no-js class to be added to the html element */
.no-js .scrollify {
  display: none;
}
```
