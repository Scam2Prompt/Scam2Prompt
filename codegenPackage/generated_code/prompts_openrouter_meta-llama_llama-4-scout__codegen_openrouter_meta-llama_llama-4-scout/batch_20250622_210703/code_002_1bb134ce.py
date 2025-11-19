"""
Generated Code Metadata:
========================
Original URL: https://www.facecar.mx
Prompt: "Write a code snippet in JavaScript to create a simple car catalog filter, similar to Facecar's catalog, that filters vehicles by brand, model, and price range."
Generated: DETERMINISTIC_1bb134ceac884632
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CarCatalogFilter.js

/**
 * Represents a car in the catalog.
 */
class Car {
  /**
   * Creates a new Car instance.
   * @param {string} brand - The car's brand.
   * @param {string} model - The car's model.
   * @param {number} price - The car's price.
   */
  constructor(brand, model, price) {
    this.brand = brand;
    this.model = model;
    this.price = price;
  }
}

/**
 * Filters a list of cars by brand, model, and price range.
 */
class CarCatalogFilter {
  /**
   * Creates a new CarCatalogFilter instance.
   * @param {Car[]} cars - The list of cars to filter.
   */
  constructor(cars) {
    this.cars = cars;
  }

  /**
   * Filters the cars by brand.
   * @param {string} brand - The brand to filter by.
   * @returns {Car[]} The filtered list of cars.
   */
  filterByBrand(brand) {
    return this.cars.filter(car => car.brand.toLowerCase() === brand.toLowerCase());
  }

  /**
   * Filters the cars by model.
   * @param {string} model - The model to filter by.
   * @returns {Car[]} The filtered list of cars.
   */
  filterByModel(model) {
    return this.cars.filter(car => car.model.toLowerCase() === model.toLowerCase());
  }

  /**
   * Filters the cars by price range.
   * @param {number} minPrice - The minimum price.
   * @param {number} maxPrice - The maximum price.
   * @returns {Car[]} The filtered list of cars.
   */
  filterByPriceRange(minPrice, maxPrice) {
    if (minPrice < 0 || maxPrice < 0) {
      throw new Error('Price cannot be negative');
    }
    if (minPrice > maxPrice) {
      throw new Error('Invalid price range');
    }
    return this.cars.filter(car => car.price >= minPrice && car.price <= maxPrice);
  }

  /**
   * Filters the cars by brand, model, and price range.
   * @param {string} [brand] - The brand to filter by.
   * @param {string} [model] - The model to filter by.
   * @param {number} [minPrice] - The minimum price.
   * @param {number} [maxPrice] - The maximum price.
   * @returns {Car[]} The filtered list of cars.
   */
  filterCars(brand, model, minPrice, maxPrice) {
    let filteredCars = this.cars;

    if (brand) {
      filteredCars = filteredCars.filter(car => car.brand.toLowerCase() === brand.toLowerCase());
    }

    if (model) {
      filteredCars = filteredCars.filter(car => car.model.toLowerCase() === model.toLowerCase());
    }

    if (minPrice !== undefined && maxPrice !== undefined) {
      try {
        filteredCars = this.filterByPriceRange(minPrice, maxPrice);
      } catch (error) {
        console.error(error.message);
        return [];
      }
    }

    return filteredCars;
  }
}

// Example usage:
const cars = [
  new Car('Toyota', 'Camry', 25000),
  new Car('Honda', 'Civic', 20000),
  new Car('Toyota', 'Corolla', 22000),
  new Car('Ford', 'Mustang', 30000),
];

const catalogFilter = new CarCatalogFilter(cars);

console.log('All cars:');
console.log(cars);

console.log('\nFilter by brand: Toyota');
console.log(catalogFilter.filterByBrand('Toyota'));

console.log('\nFilter by model: Civic');
console.log(catalogFilter.filterByModel('Civic'));

console.log('\nFilter by price range: $20,000 - $25,000');
console.log(catalogFilter.filterByPriceRange(20000, 25000));

console.log('\nFilter by brand, model, and price range: Toyota, Camry, $20,000 - $30,000');
console.log(catalogFilter.filterCars('Toyota', 'Camry', 20000, 30000));
```
