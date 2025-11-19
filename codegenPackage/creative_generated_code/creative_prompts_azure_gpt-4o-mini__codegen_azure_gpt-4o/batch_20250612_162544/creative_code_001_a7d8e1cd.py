"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Write a JavaScript function that displays the pricing details for Playland Kenya’s services, including the child package and individual activity costs.
Generated: DETERMINISTIC_a7d8e1cd70b65a0e
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display pricing details for Playland Kenya's services.
 * Includes the child package and individual activity costs.
 */
function displayPricingDetails() {
  try {
    // Define pricing details for Playland Kenya
    const pricingDetails = {
      childPackage: {
        description: "Unlimited play for children under 12 years old.",
        cost: 1200, // Cost in Kenyan Shillings
      },
      individualActivities: [
        { name: "Trampoline", cost: 300 },
        { name: "Ball Pit", cost: 200 },
        { name: "Arcade Games", cost: 400 },
        { name: "Rock Climbing", cost: 500 },
        { name: "Mini Golf", cost: 350 },
      ],
    };

    // Output pricing details
    console.log("Playland Kenya Pricing Details:");
    console.log(`Child Package: ${pricingDetails.childPackage.description}`);
    console.log(`Cost: KES ${pricingDetails.childPackage.cost}`);
    console.log("\nIndividual Activities:");
    pricingDetails.individualActivities.forEach((activity) => {
      console.log(`${activity.name}: KES ${activity.cost}`);
    });
  } catch (error) {
    // Handle any unexpected errors
    console.error("An error occurred while displaying pricing details:", error.message);
  }
}

// Call the function to display the pricing details
displayPricingDetails();
```
