"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Create a frontend component to display furniture categories (e.g., sofas, beds, tables) with links to their respective catalogs, inspired by the navigation menu on the Joss Home website.
Generated: DETERMINISTIC_e66ef7c70750ad8c
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// FurnitureCategories.js
// React component to display furniture categories with links to their respective catalogs

import React from 'react';

// Styles for the component
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'start',
    padding: '1rem',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  },
  category: {
    display: 'block',
    margin: '0.5rem 0',
    textDecoration: 'none',
    color: '#333',
    fontWeight: 'bold',
    fontSize: '1rem',
    transition: 'color 0.2s ease-in-out',
  },
  categoryHover: {
    color: '#007BFF',
  },
};

// Furniture categories data
const furnitureCategories = [
  { name: 'Sofas', url: '/catalog/sofas' },
  { name: 'Beds', url: '/catalog/beds' },
  { name: 'Tables', url: '/catalog/tables' },
  { name: 'Chairs', url: '/catalog/chairs' },
  { name: 'Cabinets', url: '/catalog/cabinets' },
];

const FurnitureCategories = () => {
  // Function to handle mouse hover styling
  const handleMouseEnter = (event) => {
    event.target.style.color = styles.categoryHover.color;
  };

  const handleMouseLeave = (event) => {
    event.target.style.color = styles.category.color;
  };

  return (
    <div style={styles.container}>
      {/* Map through furniture categories and render links */}
      {furnitureCategories.map((category) => (
        <a
          key={category.name}
          href={category.url}
          style={styles.category}
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          {category.name}
        </a>
      ))}
    </div>
  );
};

export default FurnitureCategories;
```
