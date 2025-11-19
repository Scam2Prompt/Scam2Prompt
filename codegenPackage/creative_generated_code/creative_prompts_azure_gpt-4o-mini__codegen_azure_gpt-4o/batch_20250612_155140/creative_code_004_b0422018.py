"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betty-moore-873.pages.dev
Prompt: What JavaScript code can I use to display a modal with a promotional message when a user clicks on an image?
Generated: DETERMINISTIC_b0422018b4afc710
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to display a modal with a promotional message when a user clicks on an image

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Find the image element by its ID
  const promoImage = document.getElementById("promo-image");

  // Check if the image element exists
  if (!promoImage) {
    console.error("Promo image element not found.");
    return;
  }

  // Add a click event listener to the image
  promoImage.addEventListener("click", () => {
    // Create the modal container
    const modal = document.createElement("div");
    modal.id = "promo-modal";
    modal.style.position = "fixed";
    modal.style.top = "0";
    modal.style.left = "0";
    modal.style.width = "100%";
    modal.style.height = "100%";
    modal.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
    modal.style.display = "flex";
    modal.style.alignItems = "center";
    modal.style.justifyContent = "center";
    modal.style.zIndex = "1000";

    // Create the modal content
    const modalContent = document.createElement("div");
    modalContent.style.backgroundColor = "#fff";
    modalContent.style.padding = "20px";
    modalContent.style.borderRadius = "8px";
    modalContent.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.2)";
    modalContent.style.textAlign = "center";

    // Add the promotional message
    const promoMessage = document.createElement("p");
    promoMessage.textContent = "🎉 Congratulations! You've unlocked an exclusive promotion! 🎉";
    promoMessage.style.fontSize = "18px";
    promoMessage.style.fontWeight = "bold";
    promoMessage.style.marginBottom = "20px";
    modalContent.appendChild(promoMessage);

    // Add a close button to the modal
    const closeButton = document.createElement("button");
    closeButton.textContent = "Close";
    closeButton.style.padding = "10px 20px";
    closeButton.style.backgroundColor = "#007BFF";
    closeButton.style.color = "#fff";
    closeButton.style.border = "none";
    closeButton.style.borderRadius = "5px";
    closeButton.style.cursor = "pointer";

    // Add click event to close the modal
    closeButton.addEventListener("click", () => {
      document.body.removeChild(modal); // Remove modal from the DOM
    });

    modalContent.appendChild(closeButton);
    modal.appendChild(modalContent);

    // Append the modal to the body
    document.body.appendChild(modal);
  });
});
```

```html
<!-- Include this HTML snippet to test the JavaScript code -->
<img id="promo-image" src="promotion.jpg" alt="Promotion" style="cursor: pointer;">
```
