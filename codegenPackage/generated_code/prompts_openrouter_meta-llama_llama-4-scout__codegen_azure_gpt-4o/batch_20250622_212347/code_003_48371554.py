"""
Generated Code Metadata:
========================
Original URL: https://prominsac.com
Prompt: Design a simple CSS style for a navigation item that includes an icon and title, inspired by the layout seen on Prominsac's webpage.
Generated: DETERMINISTIC_48371554f16c4f3d
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Navigation Item Style */
/* This CSS defines a clean and responsive style for a navigation item with an icon and title */

/* Container for the navigation item */
.nav-item {
  display: flex; /* Align icon and title horizontally */
  align-items: center; /* Center items vertically */
  padding: 10px 15px; /* Add spacing around the item */
  background-color: #f8f9fa; /* Light background color */
  border-radius: 5px; /* Rounded corners for a modern look */
  transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effect */
  text-decoration: none; /* Remove underline for links */
  color: #333; /* Default text color */
}

/* Icon style */
.nav-item .icon {
  font-size: 20px; /* Adjust icon size */
  margin-right: 10px; /* Add spacing between icon and title */
  color: #007bff; /* Icon color */
}

/* Title style */
.nav-item .title {
  font-size: 16px; /* Adjust font size for the title */
  font-weight: 500; /* Slightly bold text for emphasis */
}

/* Hover effect */
.nav-item:hover {
  background-color: #e2e6ea; /* Slightly darker background on hover */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add subtle shadow on hover */
  color: #0056b3; /* Change text color on hover */
}

/* Active state */
.nav-item.active {
  background-color: #007bff; /* Highlight active item */
  color: #fff; /* White text for active item */
}

```
