"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Generate code for adding coupon functionality to an e-commerce store using Strikingly's platform.
Generated: DETERMINISTIC_9834d9415ff5b2ea
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Strikingly Custom Code: Add Coupon Functionality to E-Commerce Store

// Ensure this script is embedded in the Strikingly website via the "Custom Code" feature.
// This script assumes the use of Strikingly’s e-commerce feature with a custom checkout experience.

// Coupon Feature Configuration
const couponConfig = {
  coupons: {
    "DISCOUNT10": 0.10, // Coupon code "DISCOUNT10" gives a 10% discount
    "SAVE20": 0.20,     // Coupon code "SAVE20" gives a 20% discount
    "FREESHIP": "FREE_SHIPPING" // Coupon code "FREESHIP" gives free shipping
  },
  shippingCost: 10.00, // Default shipping cost
  currency: "USD"      // Currency for the store
};

document.addEventListener("DOMContentLoaded", () => {
  // Ensure the coupon input and apply button exist
  const couponInput = document.getElementById("coupon-code");
  const applyButton = document.getElementById("apply-coupon");
  const totalElement = document.getElementById("total-price");
  const shippingElement = document.getElementById("shipping-cost");
  const errorMessageElement = document.getElementById("coupon-error");

  if (!couponInput || !applyButton || !totalElement || !shippingElement || !errorMessageElement) {
    console.error("Missing required DOM elements for coupon functionality.");
    return;
  }

  // Event listener for applying the coupon
  applyButton.addEventListener("click", () => {
    const couponCode = couponInput.value.trim().toUpperCase(); // Normalize input
    const originalTotal = parseFloat(totalElement.dataset.originalPrice); // Original total price stored in a data attribute

    if (!couponConfig.coupons[couponCode]) {
      // Show error message if coupon is invalid
      errorMessageElement.textContent = "Invalid coupon code. Please try again.";
      errorMessageElement.style.display = "block";
      return;
    }

    // Hide previous error message
    errorMessageElement.style.display = "none";

    let discountedPrice = originalTotal;
    let shippingCost = couponConfig.shippingCost;

    // Apply the coupon discount
    const discount = couponConfig.coupons[couponCode];
    if (typeof discount === "number") {
      discountedPrice = originalTotal - originalTotal * discount;
    } else if (discount === "FREE_SHIPPING") {
      shippingCost = 0.00;
    }

    // Update the displayed total price and shipping cost
    totalElement.textContent = `${couponConfig.currency} ${discountedPrice.toFixed(2)}`;
    shippingElement.textContent = `${couponConfig.currency} ${shippingCost.toFixed(2)}`;
  });
});
```

### HTML Structure Example (required for the script to work):
```html
<!-- Coupon Input Section -->
<div>
  <label for="coupon-code">Coupon Code:</label>
  <input type="text" id="coupon-code" placeholder="Enter coupon code">
  <button id="apply-coupon">Apply Coupon</button>
  <p id="coupon-error" style="color: red; display: none;"></p>
</div>

<!-- Display Prices -->
<div>
  <p>Shipping Cost: <span id="shipping-cost">USD 10.00</span></p>
  <p>Total: <span id="total-price" data-original-price="100.00">USD 100.00</span></p>
</div>
```
