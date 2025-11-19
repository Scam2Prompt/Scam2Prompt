"""
Generated Code Metadata:
========================
Original URL: https://maskextension.teachable.com
Prompt: "Create a CSS snippet to style a 'Main menu' section for a Teachable site, ensuring it matches the aesthetic of the Maskextension site."
Generated: DETERMINISTIC_f084d77eae65d60b
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Main Menu Styling for Teachable Site */
/* This CSS snippet is designed to match the aesthetic of the Maskextension site */

/* General container for the main menu */
.main-menu {
  display: flex; /* Align menu items horizontally */
  justify-content: center; /* Center menu items */
  align-items: center; /* Vertically align items */
  background-color: #1a1a1a; /* Dark background for a sleek look */
  padding: 20px; /* Add spacing around the menu */
  border-bottom: 2px solid #444; /* Subtle border for separation */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
}

/* Individual menu items */
.main-menu a {
  text-decoration: none; /* Remove underline from links */
  color: #f5f5f5; /* Light text color for contrast */
  font-size: 16px; /* Readable font size */
  font-weight: 500; /* Slightly bold for emphasis */
  margin: 0 15px; /* Spacing between menu items */
  transition: color 0.3s ease, transform 0.3s ease; /* Smooth hover effects */
}

/* Hover effect for menu items */
.main-menu a:hover {
  color: #00bcd4; /* Highlight color on hover */
  transform: scale(1.1); /* Slight zoom effect */
}

/* Active menu item styling */
.main-menu a.active {
  color: #00bcd4; /* Highlight active menu item */
  font-weight: 600; /* Make active item slightly bolder */
  border-bottom: 2px solid #00bcd4; /* Underline active item */
}

/* Responsive design for smaller screens */
@media (max-width: 768px) {
  .main-menu {
    flex-direction: column; /* Stack menu items vertically */
    padding: 15px; /* Adjust padding for smaller screens */
  }

  .main-menu a {
    margin: 10px 0; /* Adjust spacing for vertical layout */
    font-size: 14px; /* Slightly smaller font size */
  }
}
```
