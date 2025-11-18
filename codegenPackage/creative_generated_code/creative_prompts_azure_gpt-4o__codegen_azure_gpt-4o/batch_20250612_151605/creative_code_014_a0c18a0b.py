"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Create a JavaScript function to display promotional banners for "Poly-Market.hu" products, such as "Top termékek" or "Legújabb termékeink," based on user browsing history.
Generated: DETERMINISTIC_a0c18a0b1e54e3db
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to display promotional banners based on user browsing history

/**
 * Displays promotional banners for "Poly-Market.hu" products.
 * @param {Array<string>} browsingHistory - Array of product categories or user interests based on browsing history.
 * @returns {void}
 */
function displayPromotionalBanner(browsingHistory) {
  // Validate input
  if (!Array.isArray(browsingHistory)) {
    console.error("Invalid browsing history. Expected an array of product categories.");
    return;
  }

  // Define promotional banners
  const banners = {
    "Top termékek": "Nézd meg a legnépszerűbb termékeinket itt: Poly-Market.hu!",
    "Legújabb termékeink": "Fedezd fel legfrissebb termékeinket itt: Poly-Market.hu!",
    "Elektronika": "Elektronikai eszközök, amikre szükséged lehet - Poly-Market.hu!",
    "Sportfelszerelések": "Sportfelszerelések a legjobb áron - Poly-Market.hu!",
    "Divat": "Divat és kiegészítők, amiket imádni fogsz - Poly-Market.hu!"
  };

  // Determine the banner to display based on browsing history
  let selectedBanner = "Top termékek"; // Default banner
  for (const category of browsingHistory) {
    if (banners[category]) {
      selectedBanner = category;
      break;
    }
  }

  // Display the selected banner
  const bannerMessage = banners[selectedBanner];
  if (bannerMessage) {
    const bannerElement = document.createElement("div");
    bannerElement.className = "promotional-banner";
    bannerElement.textContent = bannerMessage;

    // Apply basic styles to the banner
    bannerElement.style.padding = "20px";
    bannerElement.style.backgroundColor = "#FFD700";
    bannerElement.style.color = "#000";
    bannerElement.style.fontSize = "18px";
    bannerElement.style.textAlign = "center";
    bannerElement.style.marginBottom = "10px";

    // Append the banner to the top of the webpage
    document.body.insertBefore(bannerElement, document.body.firstChild);
  } else {
    console.warn("No promotional banner available for the given browsing history.");
  }
}

// Example usage:
// Simulated browsing history of the user
const userBrowsingHistory = ["Elektronika", "Sportfelszerelések"];
displayPromotionalBanner(userBrowsingHistory);
```
