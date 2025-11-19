"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwendrop.com
Prompt: Write a JavaScript function that displays a list of fresh fruits along with their nutritional values, emphasizing the importance of vitamins and minerals.
Generated: DETERMINISTIC_a54b7dd19ae3725e
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a list of fresh fruits with their nutritional values,
 * emphasizing the importance of vitamins and minerals.
 */
function displayFruitNutrition() {
  // List of fruits with nutritional values
  const fruits = [
    {
      name: "Apple",
      vitamins: ["Vitamin C", "Vitamin A"],
      minerals: ["Potassium", "Magnesium"],
    },
    {
      name: "Banana",
      vitamins: ["Vitamin B6", "Vitamin C"],
      minerals: ["Potassium", "Manganese"],
    },
    {
      name: "Orange",
      vitamins: ["Vitamin C", "Vitamin B1"],
      minerals: ["Calcium", "Potassium"],
    },
    {
      name: "Strawberry",
      vitamins: ["Vitamin C", "Vitamin K"],
      minerals: ["Manganese", "Potassium"],
    },
  ];

  // Error handling: Ensure the array is not empty
  if (!Array.isArray(fruits) || fruits.length === 0) {
    console.error("No fruits available to display.");
    return;
  }

  // HTML container element to display the fruits (if running in a browser environment)
  const container = document.getElementById("fruitNutritionContainer");
  if (!container) {
    console.error("HTML container element not found.");
    return;
  }

  // Clear the container before populating new data
  container.innerHTML = "";

  // Create and display the list of fruits with their nutritional values
  fruits.forEach((fruit) => {
    const fruitItem = document.createElement("div");
    fruitItem.style.marginBottom = "10px";
    fruitItem.style.fontFamily = "Arial, sans-serif";

    const fruitTitle = document.createElement("h3");
    fruitTitle.textContent = fruit.name;
    fruitTitle.style.color = "#2E8B57"; // Emphasize the name of the fruit
    fruitItem.appendChild(fruitTitle);

    const vitaminsList = document.createElement("p");
    vitaminsList.textContent = "Vitamins: " + fruit.vitamins.join(", ");
    vitaminsList.style.color = "#FF6347"; // Highlight vitamins
    fruitItem.appendChild(vitaminsList);

    const mineralsList = document.createElement("p");
    mineralsList.textContent = "Minerals: " + fruit.minerals.join(", ");
    mineralsList.style.color = "#4682B4"; // Highlight minerals
    fruitItem.appendChild(mineralsList);

    container.appendChild(fruitItem);
  });
}

// Call the function (ensure you have an element with id 'fruitNutritionContainer')
document.addEventListener("DOMContentLoaded", () => {
  displayFruitNutrition();
});
```
