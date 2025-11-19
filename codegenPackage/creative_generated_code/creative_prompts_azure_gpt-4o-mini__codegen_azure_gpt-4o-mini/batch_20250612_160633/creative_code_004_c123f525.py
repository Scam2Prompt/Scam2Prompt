"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Design a user interface component that showcases seasonal products like enfeites de árvore de Natal, as featured on the Camicado website, with options to filter by price and color.
Generated: DETERMINISTIC_c123f52577c373b2
Batch ID: 20250612_160633
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
import './SeasonalProducts.css'; // Assuming you have a CSS file for styles

// Component to display seasonal products with filtering options
const SeasonalProducts = ({ products }) => {
  // State to hold the filtered products
  const [filteredProducts, setFilteredProducts] = useState(products);
  
  // State to hold selected filters
  const [selectedColor, setSelectedColor] = useState('');
  const [priceRange, setPriceRange] = useState([0, 100]); // Example price range

  useEffect(() => {
    // Filter products whenever filters are updated
    const applyFilters = () => {
      let updatedProducts = products;
      
      // Filter by color
      if (selectedColor) {
        updatedProducts = updatedProducts.filter(product => product.color === selectedColor);
      }

      // Filter by price
      updatedProducts = updatedProducts.filter(product => 
        product.price >= priceRange[0] && product.price <= priceRange[1]
      );

      setFilteredProducts(updatedProducts);
    };

    applyFilters();
  }, [selectedColor, priceRange, products]);

  // Handler for color filter change
  const handleColorChange = (event) => {
    setSelectedColor(event.target.value);
  };

  // Handler for price range change
  const handlePriceChange = (event) => {
    const value = event.target.value.split(',');
    setPriceRange([Number(value[0]), Number(value[1])]);
  };

  return (
    <div className="seasonal-products">
      <h2>Seasonal Products</h2>

      {/* Filter Options */}
      <div className="filters">
        <label>
          Color:
          <select onChange={handleColorChange}>
            <option value="">All</option>
            <option value="red">Red</option>
            <option value="green">Green</option>
            <option value="gold">Gold</option>
            {/* Add more colors as needed */}
          </select>
        </label>

        <label>
          Price Range:
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={priceRange[0]} 
            onChange={handlePriceChange}
          />
          to
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={priceRange[1]} 
            onChange={handlePriceChange}
          />
        </label>
      </div>

      {/* Products List */}
      <div className="products-list">
        {filteredProducts.length > 0 ? (
          filteredProducts.map(product => (
            <div key={product.id} className="product-item">
              <h3>{product.name}</h3>
              <p>Price: ${product.price}</p>
              <p>Color: {product.color}</p>
              {/* Assume product.image is available */}
              <img src={product.image} alt={product.name} />
            </div>
          ))
        ) : (
          <p>No products found matching your filters.</p>
        )}
      </div>
    </div>
  );
};

// PropTypes for type checking
SeasonalProducts.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      color: PropTypes.string.isRequired,
      image: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default SeasonalProducts;
```

```css
/* SeasonalProducts.css */
.seasonal-products {
  padding: 20px;
}

.filters {
  margin-bottom: 20px;
}

.products-list {
  display: flex;
  flex-wrap: wrap;
}

.product-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  margin: 10px;
  width: calc(33.333% - 40px); /* Three items per row with margin */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

.product-item img {
  max-width: 100%;
  height: auto;
}
```
