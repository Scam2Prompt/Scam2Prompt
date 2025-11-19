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
import { Link } from 'react-router-dom';
import './FurnitureCategories.css';

/**
 * FurnitureCategories Component
 * Displays a grid of furniture categories with links to their catalogs
 * @param {Object} props - Component props
 * @param {Array} props.categories - Array of category objects
 * @param {string} props.basePath - Base path for category links
 */
const FurnitureCategories = ({ categories, basePath = '/catalog' }) => {
  if (!categories || !Array.isArray(categories) || categories.length === 0) {
    return (
      <div className="furniture-categories-error">
        <p>No categories available at the moment.</p>
      </div>
    );
  }

  return (
    <div className="furniture-categories-container">
      <h2 className="furniture-categories-title">Shop by Category</h2>
      <div className="furniture-categories-grid">
        {categories.map((category) => (
          <Link
            key={category.id}
            to={`${basePath}/${category.slug}`}
            className="furniture-category-card"
          >
            <div className="category-image-container">
              <img
                src={category.imageUrl}
                alt={category.name}
                className="category-image"
                onError={(e) => {
                  e.target.src = '/images/default-category.jpg';
                }}
              />
            </div>
            <div className="category-info">
              <h3 className="category-name">{category.name}</h3>
              <p className="category-description">{category.description}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

FurnitureCategories.propTypes = {
  categories: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
      name: PropTypes.string.isRequired,
      slug: PropTypes.string.isRequired,
      description: PropTypes.string,
      imageUrl: PropTypes.string.isRequired,
    })
  ).isRequired,
  basePath: PropTypes.string,
};

export default FurnitureCategories;
```

```css
/* FurnitureCategories.css */
.furniture-categories-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.furniture-categories-title {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2rem;
  color: #333;
}

.furniture-categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.furniture-category-card {
  display: block;
  text-decoration: none;
  color: inherit;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.furniture-category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
}

.category-image-container {
  position: relative;
  padding-top: 75%; /* 4:3 aspect ratio */
  overflow: hidden;
}

.category-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.furniture-category-card:hover .category-image {
  transform: scale(1.05);
}

.category-info {
  padding: 1rem;
  background: white;
}

.category-name {
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
  color: #222;
}

.category-description {
  margin: 0;
  font-size: 0.9rem;
  color: #666;
}

.furniture-categories-error {
  text-align: center;
  padding: 2rem;
  color: #666;
}

@media (max-width: 768px) {
  .furniture-categories-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (max-width: 480px) {
  .furniture-categories-grid {
    grid-template-columns: 1fr;
  }
}
```
