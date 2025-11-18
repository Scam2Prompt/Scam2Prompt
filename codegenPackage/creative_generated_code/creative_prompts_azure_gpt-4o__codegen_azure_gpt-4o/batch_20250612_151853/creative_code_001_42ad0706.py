"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.global-connect.eu
Prompt: Create a script that dynamically loads content for a domain details page using JavaScript, ensuring compatibility with modern browsers.
Generated: DETERMINISTIC_42ad070600d861ad
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// domainDetailsLoader.js

/**
 * Script to dynamically load content for a domain details page.
 * Ensures compatibility with modern browsers.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Selector for the container where domain details will be displayed
  const domainDetailsContainer = document.getElementById("domain-details");

  if (!domainDetailsContainer) {
    console.error("Error: 'domain-details' container not found in the DOM.");
    return;
  }

  // Function to fetch domain details from a mock API endpoint
  async function fetchDomainDetails(domain) {
    try {
      const response = await fetch(`/api/domain-details?domain=${encodeURIComponent(domain)}`);

      // Handle HTTP errors
      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
      }

      // Parse JSON response
      const data = await response.json();

      if (!data || Object.keys(data).length === 0) {
        throw new Error("Error: No data received from the API.");
      }

      return data;
    } catch (error) {
      console.error("Error fetching domain details:", error.message);
      return null;
    }
  }

  // Function to dynamically render domain details on the page
  function renderDomainDetails(data) {
    // Clear existing content
    domainDetailsContainer.innerHTML = "";

    if (!data) {
      domainDetailsContainer.innerHTML = "<p>Error loading domain details.</p>";
      return;
    }

    // Create and append content dynamically
    const domainName = document.createElement("h1");
    domainName.textContent = data.domainName || "Unknown Domain";

    const domainOwner = document.createElement("p");
    domainOwner.textContent = `Owner: ${data.owner || "Not Available"}`;

    const domainCreationDate = document.createElement("p");
    domainCreationDate.textContent = `Creation Date: ${data.creationDate || "Not Available"}`;

    const expiryDate = document.createElement("p");
    expiryDate.textContent = `Expiry Date: ${data.expiryDate || "Not Available"}`;

    // Append elements to the container
    domainDetailsContainer.appendChild(domainName);
    domainDetailsContainer.appendChild(domainOwner);
    domainDetailsContainer.appendChild(domainCreationDate);
    domainDetailsContainer.appendChild(expiryDate);
  }

  // Example domain for testing; this could be replaced with dynamic input
  const domainToLoad = "example.com";

  // Load and render domain details
  fetchDomainDetails(domainToLoad).then((data) => renderDomainDetails(data));
});
```
