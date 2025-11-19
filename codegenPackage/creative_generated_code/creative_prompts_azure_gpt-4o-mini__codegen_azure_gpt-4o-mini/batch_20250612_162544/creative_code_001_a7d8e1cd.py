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
 * Displays the pricing details for Playland Kenya's services.
 * This function retrieves and formats the pricing information
 * for the child package and individual activity costs.
 * 
 * @returns {void}
 */
function displayPricingDetails() {
    // Define pricing details
    const pricingDetails = {
        childPackage: {
            name: "Child Package",
            price: 1500, // Price in Kenyan Shillings
            description: "Includes access to all activities for children aged 3-12."
        },
        individualActivities: [
            {
                name: "Bouncy Castle",
                price: 300,
                description: "Fun and safe bouncing area."
            },
            {
                name: "Trampoline",
                price: 400,
                description: "Jumping fun for all ages."
            },
            {
                name: "Ball Pit",
                price: 250,
                description: "A colorful ball pit for children."
            }
        ]
    };

    // Function to format price as a string
    function formatPrice(price) {
        return `KSh ${price.toLocaleString()}`;
    }

    // Displaying the pricing details
    try {
        console.log("Pricing Details for Playland Kenya:");
        console.log(`\n${pricingDetails.childPackage.name}: ${formatPrice(pricingDetails.childPackage.price)}`);
        console.log(`${pricingDetails.childPackage.description}\n`);

        console.log("Individual Activities:");
        pricingDetails.individualActivities.forEach(activity => {
            console.log(`${activity.name}: ${formatPrice(activity.price)}`);
            console.log(`${activity.description}\n`);
        });
    } catch (error) {
        console.error("Error displaying pricing details:", error);
    }
}

// Call the function to display pricing details
displayPricingDetails();
```
