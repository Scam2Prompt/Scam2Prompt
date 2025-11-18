"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightningzaim.online
Prompt: Develop a JavaScript function to append URL parameters (`aff_sub3`, `sys_sub1`, `sys_sub5`) to outbound links for tracking purposes, as outlined in the constant URL parameters settings on lightningzaim.online.
Generated: DETERMINISTIC_c772fc5ac05b5586
Batch ID: 20250612_145615
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to append URL parameters to outbound links for tracking purposes.
 * This script assumes the constant URL parameter values are defined globally or can be updated as needed.
 */

// Constants for URL parameters
const TRACKING_PARAMETERS = {
  aff_sub3: "value1", // Replace with actual value
  sys_sub1: "value2", // Replace with actual value
  sys_sub5: "value3", // Replace with actual value
};

/**
 * Appends tracking parameters to outbound links.
 */
function appendTrackingParameters() {
  try {
    // Get all anchor tags on the page
    const links = document.querySelectorAll('a[href^="http://"], a[href^="https://"]');

    links.forEach((link) => {
      // Check if the link is outbound (not pointing to the current domain)
      const currentDomain = window.location.hostname;
      const linkDomain = new URL(link.href).hostname;

      if (linkDomain !== currentDomain) {
        // Append tracking parameters
        const url = new URL(link.href);

        Object.keys(TRACKING_PARAMETERS).forEach((param) => {
          url.searchParams.set(param, TRACKING_PARAMETERS[param]);
        });

        // Update the link href with the new URL including parameters
        link.href = url.toString();
      }
    });
  } catch (error) {
    // Log any errors for debugging
    console.error("Error appending tracking parameters to outbound links:", error);
  }
}

// Run the function after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", appendTrackingParameters);
```
