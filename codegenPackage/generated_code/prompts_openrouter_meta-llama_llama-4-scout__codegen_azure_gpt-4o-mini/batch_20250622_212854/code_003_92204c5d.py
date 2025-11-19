"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Develop a JavaScript function to display a list of Jaguar Land Rover models, including their prices and promo information, similar to the product list on jaguarlandroverjakarta.com.
Generated: DETERMINISTIC_92204c5d983634a6
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to display a list of Jaguar Land Rover models with their prices and promo information.
 * This function fetches data from a predefined source and renders it in a specified HTML element.
 * 
 * @param {string} containerId - The ID of the HTML element where the models will be displayed.
 */
async function displayJLRModels(containerId) {
    // Sample data representing Jaguar Land Rover models
    const models = [
        {
            name: "Jaguar F-PACE",
            price: "$50,000",
            promo: "Get 0% financing for 60 months"
        },
        {
            name: "Land Rover Discovery",
            price: "$55,000",
            promo: "Lease for $499/month for 36 months"
        },
        {
            name: "Jaguar XE",
            price: "$40,000",
            promo: "Special offer: $5,000 off MSRP"
        },
        {
            name: "Range Rover Velar",
            price: "$60,000",
            promo: "Receive a complimentary service package"
        }
    ];

    // Get the container element by ID
    const container = document.getElementById(containerId);
    
    // Check if the container exists
    if (!container) {
        console.error(`Container with ID "${containerId}" not found.`);
        return;
    }

    // Clear any existing content in the container
    container.innerHTML = '';

    // Create a list to display the models
    const modelList = document.createElement('ul');

    // Iterate over the models and create list items
    models.forEach(model => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <strong>${model.name}</strong><br>
            Price: ${model.price}<br>
            Promo: ${model.promo}
        `;
        modelList.appendChild(listItem);
    });

    // Append the model list to the container
    container.appendChild(modelList);
}

// Example usage: Call the function to display models in a container with ID 'jlr-models'
displayJLRModels('jlr-models');
```

Make sure to have an HTML element with the ID `jlr-models` in your HTML file for the function to work correctly:

```html
<div id="jlr-models"></div>
```
