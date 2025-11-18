"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Write JavaScript code to implement a dynamic pricing calculator for services, including optional add-ons like 24-hour delivery, as offered on YourPalmReading.com.
Generated: DETERMINISTIC_2c5f21a2bd0f8f06
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamic Pricing Calculator for services on YourPalmReading.com
 * This script calculates the total price for selected services and optional add-ons.
 * Author: Professional Developer
 */

// Pricing constants for base services and optional add-ons
const PRICING = {
  // Base services
  basicPalmReading: 50,
  detailedPalmReading: 100,
  tarotCardReading: 75,
  
  // Add-ons
  twentyFourHourDelivery: 20,
  personalizedReport: 15,
  followUpSession: 30
};

/**
 * Calculate total price based on selected services and add-ons
 *
 * @param {Array<string>} selectedServices - List of selected service keys from PRICING
 * @param {Array<string>} selectedAddOns - List of selected add-on keys from PRICING
 * @returns {number} - Total price for the user's selections
 */
function calculateTotalPrice(selectedServices, selectedAddOns) {
  try {
    // Validate inputs - ensure arrays are provided
    if (!Array.isArray(selectedServices) || !Array.isArray(selectedAddOns)) {
      throw new Error("Invalid input: selectedServices and selectedAddOns must be arrays.");
    }

    // Calculate service cost
    const serviceCost = selectedServices.reduce((total, service) => {
      if (!PRICING[service]) {
        throw new Error(`Invalid service selection: ${service}`);
      }
      return total + PRICING[service];
    }, 0);

    // Calculate add-on cost
    const addOnCost = selectedAddOns.reduce((total, addOn) => {
      if (!PRICING[addOn]) {
        throw new Error(`Invalid add-on selection: ${addOn}`);
      }
      return total + PRICING[addOn];
    }, 0);

    // Compute total cost
    return serviceCost + addOnCost;

  } catch (error) {
    console.error("Error calculating total price:", error.message);
    return 0; // Return 0 as a fallback
  }
}

/**
 * Example usage - Uncomment to test
 */
// Define user selections
const selectedServices = ["basicPalmReading", "tarotCardReading"];
const selectedAddOns = ["twentyFourHourDelivery", "personalizedReport"];

// Calculate total price based on user selections
const totalPrice = calculateTotalPrice(selectedServices, selectedAddOns);

// Display total price to the user
console.log("Total Price:", `$${totalPrice}`);
```
