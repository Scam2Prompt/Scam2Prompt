"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cint.privacykeeper.cc
Prompt: Generate a code snippet for handling broken links in a web application using JavaScript.
Generated: DETERMINISTIC_a6a3cc0b35f89292
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script detects and handles broken links on a web application.
 * It checks every <a> tag on the page and verifies whether the link is reachable.
 * If a link is broken, it logs the issue and optionally applies a visual indicator to the link.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Function to check if a link is reachable
  const checkLink = async (url) => {
    try {
      const response = await fetch(url, { method: "HEAD" });
      // A broken link is identified if the status code is not in the 200 range
      return response.ok;
    } catch (error) {
      console.error(`Error checking link (${url}):`, error.message);
      return false; // Treat as broken if fetch fails
    }
  };

  // Function to handle broken links
  const handleBrokenLinks = async () => {
    const links = document.querySelectorAll("a"); // Get all anchor tags
    for (let link of links) {
      const href = link.getAttribute("href");
      // Skip links without href or links with JavaScript void
      if (!href || href.startsWith("javascript:void")) continue;

      const isReachable = await checkLink(href);
      if (!isReachable) {
        console.warn(`Broken link detected: ${href}`);
        // Optionally, apply a visual indicator to broken links
        link.style.color = "red";
        link.style.textDecoration = "line-through";
        link.setAttribute("title", "This link appears to be broken");
      }
    }
  };

  // Run the broken link handler
  handleBrokenLinks();
});
```
