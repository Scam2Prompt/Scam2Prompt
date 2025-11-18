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

```jsx
// FurnitureCategories.js
import React from 'react';
import PropTypes from 'prop-types';
import './FurnitureCategories.css';

/**
 * FurnitureCategories component displays the categories of furniture
 * as a navigation menu with links to their respective catalogs.
 *
 * @param {Array} categories - An array of furniture category objects.
 * Each category object should have a 'name' and 'link' property.
 */
const FurnitureCategories = ({ categories }) => {
  if (!Array.isArray(categories) || categories.length === 0) {
    console.error('Invalid categories prop: Expected a non-empty array.');
    return <div>No categories available</div>;
  }

  return (
    <nav className="furniture-categories">
      <h2>Furniture Categories</h2>
      <ul>
        {categories.map((category, index) => (
          <li key={index}>
            <a href={category.link} className="category-link">
              {category.name}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
};

// PropTypes validation for the categories prop
FurnitureCategories.propTypes = {
  categories: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      link: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default FurnitureCategories;
```

```css
/* FurnitureCategories.css */
.furniture-categories {
  background-color: #f8f8f8;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.furniture-categories h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.furniture-categories ul {
  list-style-type: none;
  padding: 0;
}

.furniture-categories li {
  margin: 5px 0;
}

.category-link {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.category-link:hover {
  color: #007BFF;
}
```

### Usage Example
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import FurnitureCategories from './FurnitureCategories';

const categories = [
  { name: 'Sofas', link: '/catalog/sofas' },
  { name: 'Beds', link: '/catalog/beds' },
  { name: 'Tables', link: '/catalog/tables' },
];

ReactDOM.render(
  <FurnitureCategories categories={categories} />,
  document.getElementById('root')
);
```
