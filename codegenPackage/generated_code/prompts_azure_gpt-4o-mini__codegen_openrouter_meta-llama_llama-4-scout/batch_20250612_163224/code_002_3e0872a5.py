"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Create a JavaScript code example for a web application that displays coffee specials, referencing the unique features of 8 Coffee's menu.
Generated: DETERMINISTIC_3e0872a5a29ff613
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CoffeeSpecials.js

/**
 * Represents a coffee special with its name, description, and price.
 */
class CoffeeSpecial {
  /**
   * Creates a new CoffeeSpecial instance.
   * @param {string} name - The name of the coffee special.
   * @param {string} description - A brief description of the coffee special.
   * @param {number} price - The price of the coffee special.
   */
  constructor(name, description, price) {
    this.name = name;
    this.description = description;
    this.price = price;
  }
}

/**
 * Represents the 8 Coffee menu.
 */
class CoffeeMenu {
  /**
   * Creates a new CoffeeMenu instance.
   */
  constructor() {
    this.specials = [];
  }

  /**
   * Adds a coffee special to the menu.
   * @param {CoffeeSpecial} special - The coffee special to add.
   */
  addSpecial(special) {
    this.specials.push(special);
  }

  /**
   * Retrieves all coffee specials from the menu.
   * @returns {CoffeeSpecial[]} An array of coffee specials.
   */
  getSpecials() {
    return this.specials;
  }
}

// Create the 8 Coffee menu
const eightCoffeeMenu = new CoffeeMenu();

// Add coffee specials to the menu
eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Creamy Caramel Delight",
  "Espresso, vanilla syrup, and steamed milk topped with caramel sauce and whipped cream.",
  4.50
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Mocha Madness",
  "Rich espresso, chocolate syrup, and steamed milk topped with whipped cream and chocolate shavings.",
  4.75
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Cinnamon Sugar Rush",
  "Sweet and spicy espresso, steamed milk, and a sprinkle of cinnamon sugar.",
  4.25
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Pumpkin Spice Latte",
  "Fall favorite espresso, pumpkin puree, and steamed milk topped with whipped cream and pumpkin pie spice.",
  4.95
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Iced Coffee with Flavor Shots",
  "Cold brew coffee with a choice of flavor shots: vanilla, hazelnut, or caramel.",
  3.50
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Cappuccino",
  "Strong espresso, steamed milk, and a layer of foam.",
  4.00
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Latte",
  "Espresso and steamed milk with a thin layer of foam.",
  3.75
));

eightCoffeeMenu.addSpecial(new CoffeeSpecial(
  "Americano",
  "Espresso diluted with hot water, served with a twist of lemon.",
  3.25
));

// Display coffee specials
try {
  const specials = eightCoffeeMenu.getSpecials();

  if (specials.length === 0) {
    console.log("No coffee specials available.");
  } else {
    console.log("8 Coffee Specials:");
    specials.forEach((special, index) => {
      console.log(` ${index + 1}. ${special.name} - $${special.price.toFixed(2)}`);
      console.log(`   ${special.description}`);
    });
  }
} catch (error) {
  console.error("Error displaying coffee specials:", error.message);
}
```
