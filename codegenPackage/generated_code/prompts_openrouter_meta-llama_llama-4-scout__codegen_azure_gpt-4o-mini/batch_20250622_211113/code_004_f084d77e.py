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
/* Main Menu Styles for Teachable Site */

/* Container for the main menu */
.main-menu {
    display: flex; /* Use flexbox for horizontal layout */
    justify-content: space-around; /* Space items evenly */
    align-items: center; /* Center items vertically */
    background-color: #ffffff; /* White background for the menu */
    padding: 20px; /* Padding around the menu */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

/* Individual menu items */
.main-menu a {
    text-decoration: none; /* Remove underline from links */
    color: #333333; /* Dark gray text color */
    font-size: 16px; /* Font size for menu items */
    padding: 10px 15px; /* Padding around each menu item */
    transition: color 0.3s ease; /* Smooth color transition on hover */
}

/* Hover effect for menu items */
.main-menu a:hover {
    color: #007bff; /* Change text color on hover */
}

/* Active menu item */
.main-menu a.active {
    font-weight: bold; /* Bold text for the active item */
    border-bottom: 2px solid #007bff; /* Underline for active item */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .main-menu {
        flex-direction: column; /* Stack items vertically on small screens */
        align-items: flex-start; /* Align items to the start */
    }

    .main-menu a {
        width: 100%; /* Full width for menu items */
        text-align: left; /* Align text to the left */
    }
}
```
