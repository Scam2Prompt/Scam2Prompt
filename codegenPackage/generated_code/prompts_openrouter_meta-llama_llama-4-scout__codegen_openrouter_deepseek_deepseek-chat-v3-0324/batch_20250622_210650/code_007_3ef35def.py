"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Develop a ReactJS component to display product and service offerings similar to RanchiOffline, which categorizes products and services under different sections.
Generated: DETERMINISTIC_3ef35def94bffac2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * ProductServiceCard component to display individual product/service details
 * @param {Object} props - Component props
 * @param {string} props.title - Title of the product/service
 * @param {string} props.description - Description of the product/service
 * @param {string} props.imageUrl - URL of the product/service image
 * @param {string} props.price - Price of the product/service
 */
const ProductServiceCard = ({ title, description, imageUrl, price }) => {
  return (
    <div className="product-service-card">
      <div className="card-image">
        <img src={imageUrl} alt={title} />
      </div>
      <div className="card-content">
        <h3>{title}</h3>
        <p>{description}</p>
        <div className="price">{price}</div>
      </div>
    </div>
  );
};

ProductServiceCard.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  imageUrl: PropTypes.string.isRequired,
  price: PropTypes.string.isRequired,
};

/**
 * CategorySection component to display a category with its products/services
 * @param {Object} props - Component props
 * @param {string} props.categoryName - Name of the category
 * @param {Array} props.items - Array of products/services in the category
 */
const CategorySection = ({ categoryName, items }) => {
  return (
    <div className="category-section">
      <h2>{categoryName}</h2>
      <div className="items-container">
        {items.map((item, index) => (
          <ProductServiceCard
            key={index}
            title={item.title}
            description={item.description}
            imageUrl={item.imageUrl}
            price={item.price}
          />
        ))}
      </div>
    </div>
  );
};

CategorySection.propTypes = {
  categoryName: PropTypes.string.isRequired,
  items: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      imageUrl: PropTypes.string.isRequired,
      price: PropTypes.string.isRequired,
    })
  ).isRequired,
};

/**
 * Main ProductServiceDisplay component
 * @param {Object} props - Component props
 * @param {Array} props.categories - Array of categories with their products/services
 */
const ProductServiceDisplay = ({ categories }) => {
  const [activeCategory, setActiveCategory] = useState(null);

  const handleCategoryClick = (categoryName) => {
    setActiveCategory(categoryName === activeCategory ? null : categoryName);
  };

  return (
    <div className="product-service-display">
      <div className="category-tabs">
        {categories.map((category, index) => (
          <button
            key={index}
            className={`tab ${activeCategory === category.name ? 'active' : ''}`}
            onClick={() => handleCategoryClick(category.name)}
          >
            {category.name}
          </button>
        ))}
      </div>

      <div className="category-content">
        {activeCategory
          ? categories
              .filter((category) => category.name === activeCategory)
              .map((category, index) => (
                <CategorySection
                  key={index}
                  categoryName={category.name}
                  items={category.items}
                />
              ))
          : categories.map((category, index) => (
              <CategorySection
                key={index}
                categoryName={category.name}
                items={category.items}
              />
            ))}
      </div>
    </div>
  );
};

ProductServiceDisplay.propTypes = {
  categories: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      items: PropTypes.arrayOf(
        PropTypes.shape({
          title: PropTypes.string.isRequired,
          description: PropTypes.string.isRequired,
          imageUrl: PropTypes.string.isRequired,
          price: PropTypes.string.isRequired,
        })
      ).isRequired,
    })
  ).isRequired,
};

export default ProductServiceDisplay;
```
