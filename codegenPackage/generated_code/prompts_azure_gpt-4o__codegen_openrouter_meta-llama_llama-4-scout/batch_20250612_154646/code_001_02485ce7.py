"""
Generated Code Metadata:
========================
Original URL: https://harmankardon.com.ph
Prompt: Generate a JavaScript function that displays a list of Harman Kardon headphones, including their types (over-ear, in-ear, true wireless) and prices, as described on the Harman Kardon Philippines website.
Generated: DETERMINISTIC_02485ce78344ee65
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a Harman Kardon headphone product.
 */
class HarmanKardonHeadphone {
  /**
   * Creates a new HarmanKardonHeadphone instance.
   * @param {string} name - The name of the headphone.
   * @param {string} type - The type of the headphone (over-ear, in-ear, true wireless).
   * @param {number} price - The price of the headphone.
   */
  constructor(name, type, price) {
    this.name = name;
    this.type = type;
    this.price = price;
  }
}

/**
 * Displays a list of Harman Kardon headphones.
 */
class HarmanKardonHeadphoneList {
  /**
   * Creates a new HarmanKardonHeadphoneList instance.
   */
  constructor() {
    this.headphones = [];
  }

  /**
   * Adds a Harman Kardon headphone to the list.
   * @param {HarmanKardonHeadphone} headphone - The headphone to add.
   */
  addHeadphone(headphone) {
    if (!(headphone instanceof HarmanKardonHeadphone)) {
      throw new Error('Invalid headphone object');
    }
    this.headphones.push(headphone);
  }

  /**
   * Displays the list of Harman Kardon headphones.
   */
  displayHeadphones() {
    if (this.headphones.length === 0) {
      console.log('No headphones available');
      return;
    }

    console.log('Harman Kardon Headphones:');
    console.log('------------------------');

    this.headphones.forEach((headphone, index) => {
      console.log(`#${index + 1}`);
      console.log(`Name: ${headphone.name}`);
      console.log(`Type: ${headphone.type}`);
      console.log(`Price: ₱${headphone.price.toLocaleString()}`);
      console.log('------------------------');
    });
  }
}

// Example usage:
function main() {
  try {
    const headphoneList = new HarmanKardonHeadphoneList();

    headphoneList.addHeadphone(new HarmanKardonHeadphone('Onyx Studio 7', 'over-ear', 14995));
    headphoneList.addHeadphone(new HarmanKardonHeadphone('FlyTWS', 'true wireless', 9995));
    headphoneList.addHeadphone(new HarmanKardonHeadphone('SE 755BT', 'in-ear', 4995));

    headphoneList.displayHeadphones();
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
