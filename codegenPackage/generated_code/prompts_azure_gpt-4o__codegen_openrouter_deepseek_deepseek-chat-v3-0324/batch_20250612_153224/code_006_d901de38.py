"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Develop a React component to display property details dynamically, including images, price, and specifications, referencing the "Propiedad destacada" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_d901de385d69d0e1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * PropertyDetails Component
 * Displays detailed information about a property including images, price, and specifications.
 * 
 * @param {Object} props - Component props
 * @param {Object} props.property - Property data object
 * @param {boolean} props.isFeatured - Whether the property is featured
 */
const PropertyDetails = ({ property, isFeatured = false }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Simulate loading data
    const timer = setTimeout(() => {
      if (!property) {
        setError('No property data available');
      } else {
        setError(null);
      }
      setLoading(false);
    }, 500);

    return () => clearTimeout(timer);
  }, [property]);

  const handleNextImage = () => {
    setCurrentImageIndex((prevIndex) => 
      (prevIndex + 1) % property.images.length
    );
  };

  const handlePrevImage = () => {
    setCurrentImageIndex((prevIndex) => 
      (prevIndex - 1 + property.images.length) % property.images.length
    );
  };

  if (loading) {
    return <div className="property-loading">Loading property details...</div>;
  }

  if (error) {
    return <div className="property-error">Error: {error}</div>;
  }

  return (
    <div className={`property-details ${isFeatured ? 'featured' : ''}`}>
      {isFeatured && (
        <div className="featured-badge">Propiedad destacada</div>
      )}
      
      <div className="property-images">
        {property.images.length > 1 && (
          <>
            <button 
              className="image-nav prev" 
              onClick={handlePrevImage}
              aria-label="Previous image"
            >
              &lt;
            </button>
            <button 
              className="image-nav next" 
              onClick={handleNextImage}
              aria-label="Next image"
            >
              &gt;
            </button>
          </>
        )}
        <img 
          src={property.images[currentImageIndex]} 
          alt={`Property ${currentImageIndex + 1}`} 
          className="property-main-image"
        />
        <div className="image-indicator">
          {currentImageIndex + 1} / {property.images.length}
        </div>
      </div>

      <div className="property-info">
        <h2 className="property-title">{property.title}</h2>
        <p className="property-location">{property.location}</p>
        
        <div className="property-price">
          <span className="price">{property.price}</span>
          {property.originalPrice && (
            <span className="original-price">{property.originalPrice}</span>
          )}
        </div>

        <div className="property-specs">
          <div className="spec-item">
            <span className="spec-icon">🛏️</span>
            <span>{property.bedrooms} Habitaciones</span>
          </div>
          <div className="spec-item">
            <span className="spec-icon">🛁</span>
            <span>{property.bathrooms} Baños</span>
          </div>
          <div className="spec-item">
            <span className="spec-icon">📏</span>
            <span>{property.area} m²</span>
          </div>
        </div>

        <div className="property-description">
          <h3>Descripción</h3>
          <p>{property.description}</p>
        </div>

        <button className="contact-button">Contactar</button>
      </div>
    </div>
  );
};

PropertyDetails.propTypes = {
  property: PropTypes.shape({
    title: PropTypes.string.isRequired,
    location: PropTypes.string.isRequired,
    price: PropTypes.string.isRequired,
    originalPrice: PropTypes.string,
    images: PropTypes.arrayOf(PropTypes.string).isRequired,
    bedrooms: PropTypes.number.isRequired,
    bathrooms: PropTypes.number.isRequired,
    area: PropTypes.number.isRequired,
    description: PropTypes.string.isRequired,
  }).isRequired,
  isFeatured: PropTypes.bool,
};

export default PropertyDetails;
```

```css
/* PropertyDetails.css */
.property-details {
  display: flex;
  flex-direction: column;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background: white;
  position: relative;
}

.property-details.featured {
  border: 2px solid #ff6b6b;
}

.featured-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  background: #ff6b6b;
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  font-weight: bold;
  z-index: 1;
}

.property-images {
  position: relative;
  height: 300px;
  overflow: hidden;
}

.property-main-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.3s;
}

.image-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 18px;
  cursor: pointer;
  z-index: 2;
}

.image-nav.prev {
  left: 10px;
}

.image-nav.next {
  right: 10px;
}

.image-indicator {
  position: absolute;
  bottom: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 14px;
}

.property-info {
  padding: 20px;
}

.property-title {
  margin: 0 0 5px 0;
  font-size: 22px;
  color: #333;
}

.property-location {
  margin: 0 0 15px 0;
  color: #666;
  font-size: 16px;
}

.property-price {
  margin: 15px 0;
  font-size: 24px;
  font-weight: bold;
  color: #2c3e50;
}

.original-price {
  text-decoration: line-through;
  color: #999;
  font-size: 18px;
  margin-left: 10px;
}

.property-specs {
  display: flex;
  gap: 20px;
  margin: 15px 0;
  flex-wrap: wrap;
}

.spec-item {
  display: flex;
  align-items: center;
  gap: 5px;
  color: #555;
}

.spec-icon {
  font-size: 18px;
}

.property-description {
  margin: 20px 0;
}

.property-description h3 {
  margin: 0 0 10px 0;
  font-size: 18px;
  color: #333;
}

.property-description p {
  margin: 0;
  color: #555;
  line-height: 1.5;
}

.contact-button {
  background: #3498db;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  width: 100%;
  transition: background 0.3s;
}

.contact-button:hover {
  background: #2980b9;
}

.property-loading,
.property-error {
  padding: 20px;
  text-align: center;
  color: #666;
}

.property-error {
  color: #e74c3c;
}

@media (min-width: 768px) {
  .property-details {
    flex-direction: row;
  }

  .property-images {
    width: 50%;
    height: auto;
  }

  .property-info {
    width: 50%;
  }
}
```
