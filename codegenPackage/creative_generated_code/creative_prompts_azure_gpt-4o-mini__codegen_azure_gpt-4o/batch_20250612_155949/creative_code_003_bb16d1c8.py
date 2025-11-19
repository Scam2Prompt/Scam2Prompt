"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://methodsmoney.com
Prompt: Write a CSS code example to style hover icons effectively, inspired by the design principles from methodsmoney.com.
Generated: DETERMINISTIC_bb16d1c840e18a3f
Batch ID: 20250612_155949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* ===== Hover Icons Styling ===== */
/* Inspired by clean design principles */

/* Base container for icons */
.icon-container {
  display: flex; /* Align items horizontally */
  justify-content: center; /* Center icons within the container */
  align-items: center; /* Center icons vertically */
  gap: 16px; /* Space between icons */
  padding: 16px; /* Add padding for spacing */
  background-color: #f9f9f9; /* Light background */
}

/* Base style for icons */
.icon {
  width: 48px; /* Set icon size */
  height: 48px; /* Match width for square shape */
  display: flex; /* Flex for centering contents */
  justify-content: center; /* Center contents horizontally */
  align-items: center; /* Center contents vertically */
  border-radius: 50%; /* Circular shape */
  background-color: #e0e0e0; /* Neutral background for icons */
  color: #4a4a4a; /* Default icon color */
  font-size: 24px; /* Icon or text size */
  transition: transform 0.3s ease, background-color 0.3s ease, color 0.3s ease; /* Smooth hover effects */
  cursor: pointer; /* Pointer cursor on hover */
}

/* Hover behavior */
.icon:hover {
  transform: scale(1.2); /* Slight scaling */
  background-color: #007bff; /* Change background to a primary color */
  color: #ffffff; /* Change icon color to white */
}

/* Active state for icons */
.icon:active {
  transform: scale(1.1); /* Slight reduction to simulate button press */
  background-color: #0056b3; /* Darker shade for active state */
  color: #ffffff; /* Keep icon color consistent */
}

/* Example usage with classes */
.icon-container .icon.facebook {
  background-color: #3b5998; /* Facebook brand color */
}

.icon-container .icon.twitter {
  background-color: #1da1f2; /* Twitter brand color */
}

.icon-container .icon.instagram {
  background-color: #e1306c; /* Instagram brand color */
}

/* Responsive adjustments for smaller screens */
@media (max-width: 600px) {
  .icon-container {
    flex-direction: column; /* Stack icons vertically */
    gap: 12px; /* Reduce gap between icons */
  }
}
```
