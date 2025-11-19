"""
Generated Code Metadata:
========================
Original URL: https://anamalika.com
Prompt: Create a JavaScript function that filters makeup products by skin type and provides detailed information about كريمات الأساس available on the site.
Generated: DETERMINISTIC_85c060584370e9a8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a makeup product.
 */
class MakeupProduct {
  /**
   * Creates a new MakeupProduct instance.
   * @param {string} name - The name of the product.
   * @param {string} skinType - The skin type the product is suitable for.
   * @param {string} description - A detailed description of the product.
   */
  constructor(name, skinType, description) {
    this.name = name;
    this.skinType = skinType;
    this.description = description;
  }
}

/**
 * Represents a foundation cream product.
 */
class FoundationCream extends MakeupProduct {
  /**
   * Creates a new FoundationCream instance.
   * @param {string} name - The name of the product.
   * @param {string} skinType - The skin type the product is suitable for.
   * @param {string} description - A detailed description of the product.
   * @param {string} shade - The shade of the foundation cream.
   * @param {string} finish - The finish of the foundation cream (e.g. matte, satin).
   */
  constructor(name, skinType, description, shade, finish) {
    super(name, skinType, description);
    this.shade = shade;
    this.finish = finish;
  }
}

/**
 * Filters makeup products by skin type and provides detailed information about foundation creams.
 */
class MakeupProductFilter {
  /**
   * Creates a new MakeupProductFilter instance.
   * @param {MakeupProduct[]} products - An array of makeup products.
   */
  constructor(products) {
    this.products = products;
  }

  /**
   * Filters products by skin type.
   * @param {string} skinType - The skin type to filter by.
   * @returns {MakeupProduct[]} An array of products suitable for the given skin type.
   */
  filterBySkinType(skinType) {
    return this.products.filter(product => product.skinType === skinType);
  }

  /**
   * Gets detailed information about foundation creams available on the site.
   * @param {string} skinType - The skin type to filter by.
   * @returns {FoundationCream[]} An array of foundation cream products suitable for the given skin type.
   */
  getFoundationCreams(skinType) {
    try {
      const filteredProducts = this.filterBySkinType(skinType);
      return filteredProducts.filter(product => product instanceof FoundationCream);
    } catch (error) {
      console.error('Error getting foundation creams:', error);
      return [];
    }
  }
}

// Example usage:
const products = [
  new FoundationCream('Foundation Cream 1', 'normal', 'A liquid foundation cream with a matte finish.', 'shade1', 'matte'),
  new FoundationCream('Foundation Cream 2', 'dry', 'A liquid foundation cream with a satin finish.', 'shade2', 'satin'),
  new MakeupProduct('Powder 1', 'normal', 'A translucent powder for setting makeup.'),
  new FoundationCream('Foundation Cream 3', 'normal', 'A liquid foundation cream with a natural finish.', 'shade3', 'natural'),
];

const filter = new MakeupProductFilter(products);
const foundationCreamsForNormalSkin = filter.getFoundationCreams('normal');

console.log('Foundation Creams for Normal Skin:');
foundationCreamsForNormalSkin.forEach(cream => {
  console.log(`Name: ${cream.name}`);
  console.log(`Shade: ${cream.shade}`);
  console.log(`Finish: ${cream.finish}`);
  console.log(`Description: ${cream.description}`);
  console.log('------------------------');
});
```
