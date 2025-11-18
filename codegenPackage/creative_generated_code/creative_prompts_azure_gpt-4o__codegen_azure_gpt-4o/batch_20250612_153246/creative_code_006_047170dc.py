"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Develop a JavaScript function to display a notification banner about Nzotho FET College's holiday closure dates (December 13th, 2024 to January 5th, 2025) on the homepage.
Generated: DETERMINISTIC_047170dcc103dcef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a notification banner about Nzotho FET College's holiday closure dates.
 * The banner will appear on the homepage and notify users about the closure period.
 */
function displayHolidayClosureBanner() {
  try {
    // Banner message
    const message = "Nzotho FET College will be closed for the holidays from December 13th, 2024 to January 5th, 2025.";

    // Check if a banner already exists to prevent duplicate banners
    if (document.getElementById("holiday-banner")) {
      console.warn("Holiday banner already exists.");
      return;
    }

    // Create a div element for the banner
    const banner = document.createElement("div");
    banner.id = "holiday-banner"; // Unique ID for the banner
    banner.style.position = "fixed";
    banner.style.top = "0";
    banner.style.left = "0";
    banner.style.width = "100%";
    banner.style.backgroundColor = "#ffcc00";
    banner.style.color = "#000";
    banner.style.textAlign = "center";
    banner.style.padding = "10px";
    banner.style.zIndex = "1000";
    banner.style.fontSize = "16px";
    banner.style.boxShadow = "0 2px 5px rgba(0, 0, 0, 0.2)";

    // Add message text to the banner
    banner.textContent = message;

    // Create a close button for the banner
    const closeButton = document.createElement("button");
    closeButton.textContent = "×";
    closeButton.style.marginLeft = "10px";
    closeButton.style.border = "none";
    closeButton.style.backgroundColor = "transparent";
    closeButton.style.cursor = "pointer";
    closeButton.style.fontSize = "18px";
    closeButton.style.color = "#000";
    closeButton.onclick = function () {
      // Remove the banner from the DOM when the close button is clicked
      document.body.removeChild(banner);
    };

    // Append the close button to the banner
    banner.appendChild(closeButton);

    // Append the banner to the body of the document
    document.body.appendChild(banner);
  } catch (error) {
    // Log any errors during banner creation
    console.error("Error displaying holiday closure banner:", error);
  }
}

// Call the function to display the banner on page load
window.onload = displayHolidayClosureBanner;
```
