"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksaacademy-classera.classera.com
Prompt: Create a CSS style for a loading animation that could be used on a webpage like the one at Classera's KSA Academy.
Generated: DETERMINISTIC_35616de0f8053f4e
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Loading animation style for a webpage */

/* Container for the loading animation */
.loader {
  position: relative; /* Ensures positioning is relative to the parent */
  width: 50px; /* Width of the loader */
  height: 50px; /* Height of the loader */
  margin: auto; /* Center the loader horizontally */
  border: 5px solid transparent; /* Transparent border for the spinning effect */
  border-top: 5px solid #3498db; /* Top border color for the spinning animation */
  border-radius: 50%; /* Makes the loader circular */
  animation: spin 1s linear infinite; /* Infinite spinning animation */
}

/* Keyframes for the spinning animation */
@keyframes spin {
  0% {
    transform: rotate(0deg); /* Start position */
  }
  100% {
    transform: rotate(360deg); /* End position (full rotation) */
  }
}

/* Optional: Full-screen loader wrapper for overlay effect */
.loader-overlay {
  position: fixed; /* Keeps the loader centered in the screen */
  top: 0;
  left: 0;
  width: 100%; /* Full-screen width */
  height: 100%; /* Full-screen height */
  background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
  display: flex; /* Allows centering of loader */
  justify-content: center; /* Centers horizontally */
  align-items: center; /* Centers vertically */
  z-index: 9999; /* Ensures the loader is above all other elements */
}
```
