"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: Create a frontend component to display furniture categories (e.g., sofas, beds, tables) with links to their respective catalogs, inspired by the navigation menu on the Joss Home website.
Generated: DETERMINISTIC_e66ef7c70750ad8c
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './FurnitureCategories.css'; // Importing CSS for styling

/**
 * FurnitureCategories Component
 * Displays a list of furniture categories with links to their respective catalogs.
 * 
 * @param {Array} categories - An array of category objects containing name and link.
 */
const FurnitureCategories = ({ categories }) => {
    // Error handling for empty categories
    if (!Array.isArray(categories) || categories.length === 0) {
        return <div className="error-message">No categories available.</div>;
    }

    return (
        <nav className="furniture-categories">
            <h2>Furniture Categories</h2>
            <ul>
                {categories.map((category) => (
                    <li key={category.name}>
                        <a href={category.link} className="category-link">
                            {category.name}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

// PropTypes for type checking
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

/* Basic styling for the furniture categories navigation */
.furniture-categories {
    background-color: #f8f8f8;
    padding: 20px;
    border-radius: 5px;
}

.furniture-categories h2 {
    margin-bottom: 15px;
    font-size: 1.5em;
}

.furniture-categories ul {
    list-style-type: none;
    padding: 0;
}

.furniture-categories li {
    margin: 10px 0;
}

.category-link {
    text-decoration: none;
    color: #007bff;
    font-weight: bold;
}

.category-link:hover {
    text-decoration: underline;
}

.error-message {
    color: red;
    font-weight: bold;
}
```
