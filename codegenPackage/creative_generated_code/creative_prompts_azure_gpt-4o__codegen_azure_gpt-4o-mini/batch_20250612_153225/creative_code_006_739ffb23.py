"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Build a React component that displays a gallery of furniture products, such as "kệ rượu quầy bar hiện đại" (modern bar wine racks), with filters for material type and price.
Generated: DETERMINISTIC_739ffb23ef6fecc9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Sample furniture data
const initialProducts = [
  { id: 1, name: 'Kệ Rượu Gỗ Sồi', material: 'Wood', price: 300, imageUrl: 'url-to-image-1' },
  { id: 2, name: 'Kệ Rượu Kim Loại', material: 'Metal', price: 450, imageUrl: 'url-to-image-2' },
  { id: 3, name: 'Kệ Rượu Thủy Tinh', material: 'Glass', price: 600, imageUrl: 'url-to-image-3' },
  // Add more products as needed
];

const FurnitureGallery = () => {
  // State to hold products and filters
  const [products, setProducts] = useState(initialProducts);
  const [filteredProducts, setFilteredProducts] = useState(initialProducts);
  const [selectedMaterial, setSelectedMaterial] = useState('');
  const [maxPrice, setMaxPrice] = useState(1000);

  // Effect to filter products based on selected filters
  useEffect(() => {
    const applyFilters = () => {
      let filtered = products;
      
      if (selectedMaterial) {
        filtered = filtered.filter(product => product.material === selectedMaterial);
      }

      if (maxPrice) {
        filtered = filtered.filter(product => product.price <= maxPrice);
      }

      setFilteredProducts(filtered);
    };

    applyFilters();
  }, [selectedMaterial, maxPrice, products]);

  // Handler for material filter change
  const handleMaterialChange = (event) => {
    setSelectedMaterial(event.target.value);
  };

  // Handler for max price filter change
  const handlePriceChange = (event) => {
    setMaxPrice(Number(event.target.value));
  };

  return (
    <div className="furniture-gallery">
      <h1>Furniture Gallery</h1>
      
      {/* Filters Section */}
      <div className="filters">
        <select onChange={handleMaterialChange} value={selectedMaterial}>
          <option value="">All Materials</option>
          <option value="Wood">Wood</option>
          <option value="Metal">Metal</option>
          <option value="Glass">Glass</option>
        </select>

        <input
          type="number"
          placeholder="Max Price"
          value={maxPrice}
          onChange={handlePriceChange}
        />
      </div>

      {/* Products Display Section */}
      <div className="products">
        {filteredProducts.length > 0 ? (
          filteredProducts.map(product => (
            <div key={product.id} className="product">
              <img src={product.imageUrl} alt={product.name} />
              <h2>{product.name}</h2>
              <p>Material: {product.material}</p>
              <p>Price: ${product.price}</p>
            </div>
          ))
        ) : (
          <p>No products found matching the selected filters.</p>
        )}
      </div>
    </div>
  );
};

// PropTypes for type checking
FurnitureGallery.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      material: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      imageUrl: PropTypes.string.isRequired,
    })
  ),
};

// Export the component
export default FurnitureGallery;
```
