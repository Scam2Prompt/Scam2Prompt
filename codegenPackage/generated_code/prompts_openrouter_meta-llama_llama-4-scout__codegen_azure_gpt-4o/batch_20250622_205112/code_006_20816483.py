"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Develop a React component for a webpage that showcases different types of eyewear, including men's and women's sunglasses and optical glasses, with filtering options by frame style and price range.
Generated: DETERMINISTIC_20816483d0a10320
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// EyewearShowcase.jsx
import React, { useState, useEffect } from 'react';

// Mock data for eyewear items
const eyewearData = [
  { id: 1, type: 'Sunglasses', gender: 'Men', frameStyle: 'Aviator', price: 120 },
  { id: 2, type: 'Sunglasses', gender: 'Women', frameStyle: 'Round', price: 150 },
  { id: 3, type: 'Optical Glasses', gender: 'Men', frameStyle: 'Rectangle', price: 80 },
  { id: 4, type: 'Optical Glasses', gender: 'Women', frameStyle: 'Cat Eye', price: 100 },
  { id: 5, type: 'Sunglasses', gender: 'Unisex', frameStyle: 'Wayfarer', price: 200 },
];

// EyewearShowcase Component
const EyewearShowcase = () => {
  const [eyewearItems, setEyewearItems] = useState(eyewearData); // State for eyewear items
  const [filters, setFilters] = useState({
    frameStyle: '',
    minPrice: '',
    maxPrice: '',
  }); // State for filters

  // Handle filter changes
  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters((prevFilters) => ({
      ...prevFilters,
      [name]: value,
    }));
  };

  // Filter eyewear items based on user input
  useEffect(() => {
    const filteredItems = eyewearData.filter((item) => {
      const matchesFrameStyle =
        filters.frameStyle === '' || item.frameStyle.toLowerCase().includes(filters.frameStyle.toLowerCase());
      const matchesMinPrice = filters.minPrice === '' || item.price >= parseFloat(filters.minPrice);
      const matchesMaxPrice = filters.maxPrice === '' || item.price <= parseFloat(filters.maxPrice);

      return matchesFrameStyle && matchesMinPrice && matchesMaxPrice;
    });

    setEyewearItems(filteredItems);
  }, [filters]);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Eyewear Showcase</h1>

      {/* Filter Section */}
      <div style={{ marginBottom: '20px' }}>
        <h2>Filters</h2>
        <div>
          <label>
            Frame Style:
            <input
              type="text"
              name="frameStyle"
              value={filters.frameStyle}
              onChange={handleFilterChange}
              placeholder="e.g., Aviator, Round"
            />
          </label>
        </div>
        <div>
          <label>
            Min Price:
            <input
              type="number"
              name="minPrice"
              value={filters.minPrice}
              onChange={handleFilterChange}
              placeholder="e.g., 50"
            />
          </label>
        </div>
        <div>
          <label>
            Max Price:
            <input
              type="number"
              name="maxPrice"
              value={filters.maxPrice}
              onChange={handleFilterChange}
              placeholder="e.g., 200"
            />
          </label>
        </div>
      </div>

      {/* Eyewear Items Section */}
      <div>
        <h2>Eyewear Items</h2>
        {eyewearItems.length > 0 ? (
          <ul>
            {eyewearItems.map((item) => (
              <li key={item.id}>
                <strong>{item.type}</strong> ({item.gender}) - {item.frameStyle} Frame - ${item.price}
              </li>
            ))}
          </ul>
        ) : (
          <p>No items match the selected filters.</p>
        )}
      </div>
    </div>
  );
};

export default EyewearShowcase;
```
