"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightningzaim.online
Prompt: Generate CSS code to style the MFO offer cards with the colors specified in the "theme" section of lightningzaim.online, including `cardBg`, `cardText`, and `cardBorder`.
Generated: DETERMINISTIC_65e924eefde4ad1b
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* MFO Offer Card Styles */

/* Base styles for the MFO offer card */
.mfo-offer-card {
  background-color: var(--cardBg); /* Background color from the theme */
  color: var(--cardText); /* Text color from the theme */
  border: 1px solid var(--cardBorder); /* Border color from the theme */
  border-radius: 8px; /* Rounded corners for a modern look */
  padding: 20px; /* Add padding inside the card */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth hover effects */
}

/* Hover effect for the card */
.mfo-offer-card:hover {
  transform: translateY(-5px); /* Slight lift on hover */
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15); /* Enhance shadow on hover */
}

/* Title inside the card */
.mfo-offer-card .card-title {
  font-size: 1.5rem; /* Large and prominent title */
  font-weight: bold; /* Bold for emphasis */
  margin-bottom: 10px; /* Spacing below the title */
  color: inherit; /* Use the inherited text color */
}

/* Description text in the card */
.mfo-offer-card .card-description {
  font-size: 1rem; /* Standard text size for the description */
  line-height: 1.5; /* Improve readability */
  margin-bottom: 15px; /* Add spacing below the description */
  color: inherit; /* Use the inherited text color */
}

/* Button inside the card */
.mfo-offer-card .card-button {
  display: inline-block; /* Button-like appearance */
  padding: 10px 20px; /* Padding for clickable area */
  background-color: var(--cardBorder); /* Use the border color for the button background */
  color: var(--cardBg); /* Contrast text color for the button */
  font-size: 1rem; /* Standard button text size */
  font-weight: bold; /* Bold text for emphasis */
  text-align: center; /* Center the text */
  text-decoration: none; /* Remove underline */
  border-radius: 5px; /* Rounded corners for the button */
  transition: background-color 0.3s ease, color 0.3s ease; /* Smooth hover transitions */
}

/* Hover effect for the button */
.mfo-offer-card .card-button:hover {
  background-color: var(--cardText); /* Change background color on hover */
  color: var(--cardBg); /* Flip the text color for contrast */
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .mfo-offer-card {
    padding: 15px; /* Reduce padding for smaller screens */
  }

  .mfo-offer-card .card-title {
    font-size: 1.25rem; /* Slightly smaller title font size */
  }

  .mfo-offer-card .card-description {
    font-size: 0.9rem; /* Adjust description font size */
  }
}
```
