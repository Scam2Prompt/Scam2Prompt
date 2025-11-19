"""
Generated Code Metadata:
========================
Original URL: https://thepointblank.in
Prompt: Design a user interface component for displaying unique MDF art collections, ensuring it highlights features like "Free Shipping Above ₹1299" and "Affordable Prices."
Generated: DETERMINISTIC_4d694e1e8fc36fd9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './ArtCollection.css';

/**
 * ArtCollection Component
 * Displays a collection of MDF art pieces with features like free shipping and affordable prices.
 * 
 * @param {Array} collections - Array of art collection objects
 * @param {string} title - Title for the collection section
 */
const ArtCollection = ({ collections, title = 'MDF Art Collections' }) => {
  const [activeIndex, setActiveIndex] = useState(0);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const handlePrev = () => {
    setActiveIndex((prev) => (prev === 0 ? collections.length - 1 : prev - 1));
  };

  const handleNext = () => {
    setActiveIndex((prev) => (prev === collections.length - 1 ? 0 : prev + 1));
  };

  if (!collections || collections.length === 0) {
    return <div className="error-message">No collections available</div>;
  }

  return (
    <section className="art-collection-container">
      <h2 className="collection-title">{title}</h2>
      
      <div className="features-banner">
        <span className="feature-tag">Free Shipping Above ₹1299</span>
        <span className="feature-tag">Affordable Prices</span>
      </div>

      <div className="collection-carousel">
        {!isMobile && (
          <button className="nav-button prev" onClick={handlePrev} aria-label="Previous">
            &lt;
          </button>
        )}

        <div className="collection-items">
          {collections.map((item, index) => (
            <div 
              key={item.id} 
              className={`collection-item ${index === activeIndex ? 'active' : ''}`}
            >
              <img 
                src={item.imageUrl} 
                alt={item.title} 
                className="art-image"
                onError={(e) => {
                  e.target.src = 'fallback-image.jpg';
                  e.target.alt = 'Image not available';
                }}
              />
              <div className="art-details">
                <h3>{item.title}</h3>
                <p className="price">₹{item.price.toFixed(2)}</p>
                {item.price < 1299 && (
                  <p className="shipping-info">Add ₹{(1299 - item.price).toFixed(2)} more for free shipping</p>
                )}
                <button className="add-to-cart">Add to Cart</button>
              </div>
            </div>
          ))}
        </div>

        {!isMobile && (
          <button className="nav-button next" onClick={handleNext} aria-label="Next">
            &gt;
          </button>
        )}
      </div>

      {isMobile && (
        <div className="mobile-indicators">
          {collections.map((_, index) => (
            <button
              key={index}
              className={`indicator ${index === activeIndex ? 'active' : ''}`}
              onClick={() => setActiveIndex(index)}
              aria-label={`Go to item ${index + 1}`}
            />
          ))}
        </div>
      )}
    </section>
  );
};

ArtCollection.propTypes = {
  collections: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      imageUrl: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ).isRequired,
  title: PropTypes.string,
};

export default ArtCollection;
```

```css
/* ArtCollection.css */
.art-collection-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
}

.collection-title {
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

.features-banner {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 2rem;
}

.feature-tag {
  background-color: #f8f8f8;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: bold;
  color: #4a4a4a;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.collection-carousel {
  display: flex;
  align-items: center;
  position: relative;
}

.nav-button {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  font-size: 1.2rem;
  cursor: pointer;
  z-index: 1;
  transition: all 0.3s ease;
}

.nav-button:hover {
  background: #f0f0f0;
}

.prev {
  margin-right: 1rem;
}

.next {
  margin-left: 1rem;
}

.collection-items {
  display: flex;
  overflow: hidden;
  width: 100%;
  scroll-behavior: smooth;
}

.collection-item {
  min-width: 100%;
  transition: transform 0.5s ease;
  display: none;
}

.collection-item.active {
  display: block;
}

.art-image {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 8px;
}

.art-details {
  padding: 1rem;
  text-align: center;
}

.art-details h3 {
  margin: 0.5rem 0;
  color: #333;
}

.price {
  font-size: 1.2rem;
  font-weight: bold;
  color: #e63946;
  margin: 0.5rem 0;
}

.shipping-info {
  font-size: 0.9rem;
  color: #666;
  margin: 0.5rem 0;
}

.add-to-cart {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.add-to-cart:hover {
  background-color: #45a049;
}

.mobile-indicators {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
  gap: 0.5rem;
}

.indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ccc;
  border: none;
  cursor: pointer;
  padding: 0;
}

.indicator.active {
  background-color: #333;
}

.error-message {
  text-align: center;
  color: #e63946;
  padding: 2rem;
  font-weight: bold;
}

@media (min-width: 768px) {
  .collection-item {
    min-width: 50%;
  }
}

@media (min-width: 1024px) {
  .collection-item {
    min-width: 33.33%;
  }
}
```
