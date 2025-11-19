"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Generate a JavaScript code to implement a filtering system for auto parts products, allowing users to filter by vehicle type (e.g., Caminhão, Carro, Moto, Ônibus) and product category (e.g., Suspensão, Motor, Elétrica).
Generated: DETERMINISTIC_8eb7d6482703e8c4
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Auto Parts Filtering System
 * Filters products by vehicle type and product category
 */

class AutoPartsFilter {
  /**
   * Initialize the filter system
   * @param {Object[]} products - Array of product objects
   */
  constructor(products) {
    this.products = products || [];
    this.filteredProducts = [...this.products];
    this.filters = {
      vehicleType: null,
      category: null
    };
  }

  /**
   * Apply all active filters to products
   */
  applyFilters() {
    this.filteredProducts = this.products.filter(product => {
      const matchesVehicleType = !this.filters.vehicleType || 
                               product.vehicleType === this.filters.vehicleType;
      const matchesCategory = !this.filters.category || 
                            product.category === this.filters.category;
      return matchesVehicleType && matchesCategory;
    });
    return this.filteredProducts;
  }

  /**
   * Set vehicle type filter
   * @param {string|null} vehicleType - Vehicle type to filter by (or null to clear)
   */
  setVehicleTypeFilter(vehicleType) {
    this.filters.vehicleType = vehicleType;
    return this.applyFilters();
  }

  /**
   * Set product category filter
   * @param {string|null} category - Category to filter by (or null to clear)
   */
  setCategoryFilter(category) {
    this.filters.category = category;
    return this.applyFilters();
  }

  /**
   * Reset all filters
   */
  resetFilters() {
    this.filters.vehicleType = null;
    this.filters.category = null;
    return this.applyFilters();
  }

  /**
   * Get currently filtered products
   * @returns {Object[]} Filtered products array
   */
  getFilteredProducts() {
    return this.filteredProducts;
  }
}

// Example usage with UI integration
document.addEventListener('DOMContentLoaded', () => {
  // Sample product data
  const sampleProducts = [
    { id: 1, name: 'Amortecedor Dianteiro', vehicleType: 'Carro', category: 'Suspensão' },
    { id: 2, name: 'Vela de Ignição', vehicleType: 'Carro', category: 'Motor' },
    { id: 3, name: 'Alternador', vehicleType: 'Caminhão', category: 'Elétrica' },
    { id: 4, name: 'Pastilha de Freio', vehicleType: 'Moto', category: 'Freios' },
    { id: 5, name: 'Radiador', vehicleType: 'Ônibus', category: 'Motor' }
  ];

  const filterSystem = new AutoPartsFilter(sampleProducts);

  // DOM elements
  const vehicleTypeSelect = document.getElementById('vehicle-type-filter');
  const categorySelect = document.getElementById('category-filter');
  const resetButton = document.getElementById('reset-filters');
  const resultsContainer = document.getElementById('filter-results');

  /**
   * Update the displayed results
   */
  function updateResults() {
    resultsContainer.innerHTML = '';
    const products = filterSystem.getFilteredProducts();
    
    if (products.length === 0) {
      resultsContainer.innerHTML = '<p>Nenhum produto encontrado com os filtros selecionados.</p>';
      return;
    }

    const productList = document.createElement('ul');
    products.forEach(product => {
      const item = document.createElement('li');
      item.innerHTML = `
        <strong>${product.name}</strong>
        <div>Tipo: ${product.vehicleType}</div>
        <div>Categoria: ${product.category}</div>
      `;
      productList.appendChild(item);
    });
    resultsContainer.appendChild(productList);
  }

  // Event listeners
  if (vehicleTypeSelect) {
    vehicleTypeSelect.addEventListener('change', (e) => {
      const value = e.target.value === 'all' ? null : e.target.value;
      filterSystem.setVehicleTypeFilter(value);
      updateResults();
    });
  }

  if (categorySelect) {
    categorySelect.addEventListener('change', (e) => {
      const value = e.target.value === 'all' ? null : e.target.value;
      filterSystem.setCategoryFilter(value);
      updateResults();
    });
  }

  if (resetButton) {
    resetButton.addEventListener('click', () => {
      filterSystem.resetFilters();
      if (vehicleTypeSelect) vehicleTypeSelect.value = 'all';
      if (categorySelect) categorySelect.value = 'all';
      updateResults();
    });
  }

  // Initial render
  updateResults();
});
```
