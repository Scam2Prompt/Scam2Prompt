"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a JavaScript function that displays the different consórcio plans (Mais Fácil, Normal, Premium) and their respective features as outlined on the Consórcio Chevrolet page.
Generated: DETERMINISTIC_da44f20d7a3dcd01
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Represents a Consórcio plan with its name and features.
 * @constructor
 * @param {string} name - The name of the consórcio plan.
 * @param {Array<string>} features - The features of the consórcio plan.
 */
function ConsorcioPlan(name, features) {
    this.name = name;
    this.features = features;
}

/**
 * Displays the available consórcio plans and their features in the console.
 * @function displayConsorcioPlans
 */
function displayConsorcioPlans() {
    // Define the different consórcio plans and their features
    const plans = [
        new ConsorcioPlan("Mais Fácil", [
            "Parcelas reduzidas",
            "Menor entrada",
            "Facilidade de aprovação"
        ]),
        new ConsorcioPlan("Normal", [
            "Parcelas padrão",
            "Entrada média",
            "Aprovação rápida"
        ]),
        new ConsorcioPlan("Premium", [
            "Parcelas exclusivas",
            "Maior flexibilidade de pagamento",
            "Aprovação prioritária"
        ])
    ];

    try {
        // Check if there are any plans to display
        if (!plans || plans.length === 0) {
            throw new Error("No consórcio plans to display.");
        }

        // Iterate over each plan and log its details
        plans.forEach(plan => {
            console.log(`Plan: ${plan.name}`);
            console.log("Features:");
            plan.features.forEach(feature => {
                console.log(`- ${feature}`);
            });
            console.log('-----------------------');
        });
    } catch (error) {
        // Handle and log any errors that occur during execution
        console.error("An error occurred while displaying consórcio plans:", error.message);
    }
}

// Call the function to display the consórcio plans
displayConsorcioPlans();
```
