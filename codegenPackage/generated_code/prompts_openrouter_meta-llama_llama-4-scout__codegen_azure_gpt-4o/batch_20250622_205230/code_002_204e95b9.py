"""
Generated Code Metadata:
========================
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Generate a CSS code snippet to style a webpage with a sense of urgency, including a "Hurry up" message.
Generated: DETERMINISTIC_204e95b93df0b166
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* General styling for the webpage */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8d7da; /* Light red background to convey urgency */
  color: #721c24; /* Dark red text for emphasis */
}

/* Center the "Hurry up" message */
.hurry-up-message {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Full viewport height */
  text-align: center;
  font-size: 2rem; /* Large font size for visibility */
  font-weight: bold; /* Bold text for urgency */
  animation: pulse 1.5s infinite; /* Pulsing animation for urgency */
}

/* Button styling for call-to-action */
.urgent-button {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 1.2rem;
  font-weight: bold;
  color: #ffffff; /* White text for contrast */
  background-color: #dc3545; /* Bright red button for urgency */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-transform: uppercase; /* All caps for emphasis */
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

.urgent-button:hover {
  background-color: #b02a37; /* Darker red on hover */
}

/* Pulsing animation for the message */
@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.1); /* Slightly larger for emphasis */
    opacity: 0.8; /* Slight fade for effect */
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
```
