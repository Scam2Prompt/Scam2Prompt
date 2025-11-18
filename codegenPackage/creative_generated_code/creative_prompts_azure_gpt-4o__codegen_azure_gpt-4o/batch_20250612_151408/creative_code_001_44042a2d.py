"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Create a function in JavaScript that dynamically displays car listings with details like model, year, mileage, and price, similar to the format used on the Helfen Motors website.
Generated: DETERMINISTIC_44042a2d6256d631
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display car listings on a webpage.
 * @param {Array} carListings - Array of car objects containing details like model, year, mileage, and price.
 */
function displayCarListings(carListings) {
  // Validate input
  if (!Array.isArray(carListings)) {
    console.error("Invalid input: carListings must be an array.");
    return;
  }

  // Get the container where the car listings will be displayed
  const container = document.getElementById("car-listings-container");
  if (!container) {
    console.error("Container element with id 'car-listings-container' not found.");
    return;
  }

  // Clear the container before appending new listings
  container.innerHTML = "";

  // Loop through each car object and create its HTML representation
  carListings.forEach((car) => {
    // Validate car object structure
    if (
      !car.model ||
      !car.year ||
      !car.mileage ||
      !car.price ||
      typeof car.model !== "string" ||
      typeof car.year !== "number" ||
      typeof car.mileage !== "number" ||
      typeof car.price !== "number"
    ) {
      console.error("Invalid car object:", car);
      return;
    }

    // Create a container for each car listing
    const carCard = document.createElement("div");
    carCard.className = "car-card";

    // Add car model
    const model = document.createElement("h2");
    model.textContent = `Model: ${car.model}`;
    carCard.appendChild(model);

    // Add car year
    const year = document.createElement("p");
    year.textContent = `Year: ${car.year}`;
    carCard.appendChild(year);

    // Add car mileage
    const mileage = document.createElement("p");
    mileage.textContent = `Mileage: ${car.mileage} km`;
    carCard.appendChild(mileage);

    // Add car price
    const price = document.createElement("p");
    price.textContent = `Price: $${car.price}`;
    carCard.appendChild(price);

    // Append the car card to the container
    container.appendChild(carCard);
  });
}

// Example usage:
const sampleCarListings = [
  { model: "Toyota Corolla", year: 2020, mileage: 15000, price: 20000 },
  { model: "Ford Mustang", year: 2018, mileage: 30000, price: 25000 },
  { model: "Honda Civic", year: 2021, mileage: 10000, price: 22000 },
];

// Assuming there is a container in the HTML with id "car-listings-container"
document.addEventListener("DOMContentLoaded", () => {
  displayCarListings(sampleCarListings);
});
```

```html
<!-- Example HTML structure -->
<div id="car-listings-container"></div>

<!-- Include the JavaScript code above as part of a <script> tag or external file -->
```
