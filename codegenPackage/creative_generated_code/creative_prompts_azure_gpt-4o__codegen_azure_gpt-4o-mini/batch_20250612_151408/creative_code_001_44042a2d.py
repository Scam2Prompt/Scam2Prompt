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
 * Car Listing Class to represent a car with its details.
 */
class Car {
    constructor(model, year, mileage, price) {
        this.model = model;
        this.year = year;
        this.mileage = mileage;
        this.price = price;
    }
}

/**
 * Function to create a car listing element and append it to the DOM.
 * @param {Car} car - The car object containing details to display.
 * @returns {HTMLElement} - The HTML element representing the car listing.
 */
function createCarListingElement(car) {
    const carElement = document.createElement('div');
    carElement.classList.add('car-listing');

    carElement.innerHTML = `
        <h2>${car.model}</h2>
        <p><strong>Year:</strong> ${car.year}</p>
        <p><strong>Mileage:</strong> ${car.mileage} miles</p>
        <p><strong>Price:</strong> $${car.price.toLocaleString()}</p>
    `;

    return carElement;
}

/**
 * Function to display a list of car listings on the webpage.
 * @param {Array<Car>} cars - An array of car objects to display.
 * @param {HTMLElement} container - The container element to append car listings to.
 */
function displayCarListings(cars, container) {
    // Clear the container before displaying new listings
    container.innerHTML = '';

    if (!Array.isArray(cars) || cars.length === 0) {
        const noResults = document.createElement('p');
        noResults.textContent = 'No cars available.';
        container.appendChild(noResults);
        return;
    }

    cars.forEach(car => {
        try {
            const carElement = createCarListingElement(car);
            container.appendChild(carElement);
        } catch (error) {
            console.error('Error displaying car listing:', error);
        }
    });
}

// Example usage
const carContainer = document.getElementById('car-container');
const carListings = [
    new Car('Toyota Camry', 2020, 15000, 24000),
    new Car('Honda Accord', 2019, 23000, 22000),
    new Car('Ford Mustang', 2021, 5000, 30000)
];

// Display the car listings on the page
displayCarListings(carListings, carContainer);
```

```html
<!-- HTML structure to use with the JavaScript code -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Listings</title>
    <style>
        .car-listing {
            border: 1px solid #ccc;
            padding: 16px;
            margin: 8px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div id="car-container"></div>
    <script src="path/to/your/script.js"></script>
</body>
</html>
```
