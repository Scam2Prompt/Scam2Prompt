"""
Generated Code Metadata:
========================
Original URL: https://check.wenser.e2p.xyz
Prompt: "Generate JavaScript code for a simple domain details checker that displays information when JavaScript is enabled."
Generated: DETERMINISTIC_ab8c719cf7c0687c
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Domain Details Checker
// This script checks if JavaScript is enabled and displays domain details on the webpage.

document.addEventListener("DOMContentLoaded", () => {
  try {
    // Get the domain details
    const domainDetails = {
      hostname: window.location.hostname, // The domain name of the current page
      protocol: window.location.protocol, // The protocol used (http or https)
      port: window.location.port || "default", // The port number (or 'default' if not specified)
      pathname: window.location.pathname, // The path of the current page
    };

    // Create a container to display the domain details
    const container = document.createElement("div");
    container.style.border = "1px solid #ccc";
    container.style.padding = "10px";
    container.style.margin = "10px";
    container.style.backgroundColor = "#f9f9f9";
    container.style.fontFamily = "Arial, sans-serif";

    // Add a heading
    const heading = document.createElement("h2");
    heading.textContent = "Domain Details";
    heading.style.color = "#333";
    container.appendChild(heading);

    // Add the domain details to the container
    for (const [key, value] of Object.entries(domainDetails)) {
      const detail = document.createElement("p");
      detail.textContent = `${key.charAt(0).toUpperCase() + key.slice(1)}: ${value}`;
      detail.style.margin = "5px 0";
      container.appendChild(detail);
    }

    // Append the container to the body
    document.body.appendChild(container);
  } catch (error) {
    // Handle any errors gracefully
    console.error("An error occurred while fetching domain details:", error);

    // Display an error message to the user
    const errorMessage = document.createElement("p");
    errorMessage.textContent = "An error occurred while fetching domain details. Please check the console for more information.";
    errorMessage.style.color = "red";
    errorMessage.style.fontWeight = "bold";
    document.body.appendChild(errorMessage);
  }
});
```
