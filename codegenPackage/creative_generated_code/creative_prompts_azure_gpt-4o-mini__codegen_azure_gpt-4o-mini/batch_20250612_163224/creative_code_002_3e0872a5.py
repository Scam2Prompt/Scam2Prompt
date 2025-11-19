"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://putrastarboy.github.io
Prompt: Create a JavaScript code example for a web application that displays coffee specials, referencing the unique features of 8 Coffee's menu.
Generated: DETERMINISTIC_3e0872a5a29ff613
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Coffee Specials Display Application

// Coffee special data for 8 Coffee's menu
const coffeeSpecials = [
    {
        id: 1,
        name: "Caramel Macchiato",
        description: "Espresso layered with steamed milk and caramel syrup.",
        price: 4.50,
        features: ["Rich Caramel Flavor", "Espresso Base", "Velvety Milk"]
    },
    {
        id: 2,
        name: "Vanilla Latte",
        description: "Creamy latte with a hint of vanilla sweetness.",
        price: 4.00,
        features: ["Smooth Vanilla Essence", "Rich Creamy Texture", "Espresso Infusion"]
    },
    {
        id: 3,
        name: "Mocha Frappuccino",
        description: "Chilled coffee blended with chocolate and milk.",
        price: 5.00,
        features: ["Iced Coffee", "Chocolate Drizzle", "Whipped Cream Topping"]
    },
    {
        id: 4,
        name: "Cold Brew",
        description: "Slow-steeped cold coffee for a smooth flavor.",
        price: 3.50,
        features: ["Low Acidity", "Rich Flavor Profile", "Refreshing"]
    },
    {
        id: 5,
        name: "Hazelnut Cappuccino",
        description: "Classic cappuccino infused with hazelnut flavor.",
        price: 4.75,
        features: ["Nutty Aroma", "Foamy Milk", "Espresso"]
    },
    {
        id: 6,
        name: "Iced Caramel Coffee",
        description: "Iced coffee with caramel sauce and cream.",
        price: 4.25,
        features: ["Refreshing", "Sweet Caramel Notes", "Chilled"]
    },
    {
        id: 7,
        name: "Pumpkin Spice Latte",
        description: "Seasonal favorite with pumpkin and spices.",
        price: 4.75,
        features: ["Autumn Flavors", "Creamy Texture", "Spicy Aroma"]
    },
    {
        id: 8,
        name: "Matcha Green Tea Latte",
        description: "Smooth green tea latte with a hint of sweetness.",
        price: 5.50,
        features: ["Antioxidant Rich", "Creamy", "Unique Flavor"]
    }
];

// Function to display coffee specials in the HTML
function displayCoffeeSpecials() {
    const specialsContainer = document.getElementById('specials-container');
    
    // Check if the container exists
    if (!specialsContainer) {
        console.error("Specials container not found in the DOM.");
        return;
    }

    // Clear any existing specials
    specialsContainer.innerHTML = '';

    // Generate HTML for each coffee special
    coffeeSpecials.forEach(special => {
        const specialElement = document.createElement('div');
        specialElement.classList.add('coffee-special');

        specialElement.innerHTML = `
            <h2>${special.name} - $${special.price.toFixed(2)}</h2>
            <p>${special.description}</p>
            <ul>
                ${special.features.map(feature => `<li>${feature}</li>`).join('')}
            </ul>
        `;

        specialsContainer.appendChild(specialElement);
    });
}

// Initialize the application
function init() {
    displayCoffeeSpecials();
}

// Run the application on window load
window.onload = init;
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>8 Coffee Specials</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Today's Coffee Specials at 8 Coffee</h1>
    <div id="specials-container"></div>
    <script src="app.js"></script>
</body>
</html>
```

```css
/* CSS for styling coffee specials */
body {
    font-family: Arial, sans-serif;
}

h1 {
    text-align: center;
    color: #6f4e37; /* Coffee color */
}

.coffee-special {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
    background: #f9f9f9;
}

.coffee-special h2 {
    color: #6f4e37;
}

.coffee-special ul {
    list-style-type: none;
    padding: 0;
}

.coffee-special li {
    background: #f1f1f1;
    margin: 3px 0;
    padding: 5px;
    border-radius: 3px;
}
```
