"""
Generated Code Metadata:
========================
Original URL: https://www.rainbnb.live
Prompt: Provide an example of a React.js component that could be used to build a feature for a web app like RainBNB.
Generated: DETERMINISTIC_fcd08832da022b77
Batch ID: 20250612_150246
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
import axios from 'axios';

/**
 * PropertyListing Component - Displays a property listing card with details
 * @param {Object} props - Component props
 * @param {Object} props.property - Property details object
 * @param {function} props.onFavoriteToggle - Callback for favorite toggle
 * @param {boolean} props.isFavorite - Indicates if property is favorited
 */
const PropertyListing = ({ property, onFavoriteToggle, isFavorite }) => {
  const [imageLoaded, setImageLoaded] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleImageLoad = () => {
    setImageLoaded(true);
  };

  const handleFavoriteClick = async () => {
    try {
      setLoading(true);
      await onFavoriteToggle(property.id);
    } catch (err) {
      setError('Failed to update favorite status');
      console.error('Favorite toggle error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="property-card" data-testid="property-card">
      {error && <div className="error-message">{error}</div>}
      
      <div className="property-image-container">
        {!imageLoaded && <div className="image-placeholder">Loading image...</div>}
        <img
          src={property.imageUrl}
          alt={property.title}
          onLoad={handleImageLoad}
          style={{ display: imageLoaded ? 'block' : 'none' }}
          className="property-image"
        />
      </div>

      <div className="property-details">
        <div className="property-header">
          <h3 className="property-title">{property.title}</h3>
          <button
            onClick={handleFavoriteClick}
            disabled={loading}
            className={`favorite-button ${isFavorite ? 'favorited' : ''}`}
            aria-label={isFavorite ? 'Remove from favorites' : 'Add to favorites'}
          >
            {loading ? '...' : '♥'}
          </button>
        </div>

        <div className="property-location">
          <span className="location-icon">📍</span>
          <span>{property.location}</span>
        </div>

        <div className="property-price">
          <span className="price-amount">${property.price}</span>
          <span className="price-period"> / night</span>
        </div>

        <div className="property-rating">
          <span className="rating-stars">{'★'.repeat(property.rating)}</span>
          <span className="rating-count">({property.reviewCount})</span>
        </div>

        <div className="property-amenities">
          {property.amenities.slice(0, 3).map((amenity, index) => (
            <span key={index} className="amenity-tag">
              {amenity}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};

PropertyListing.propTypes = {
  property: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    imageUrl: PropTypes.string.isRequired,
    location: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    rating: PropTypes.number.isRequired,
    reviewCount: PropTypes.number.isRequired,
    amenities: PropTypes.arrayOf(PropTypes.string).isRequired,
  }).isRequired,
  onFavoriteToggle: PropTypes.func.isRequired,
  isFavorite: PropTypes.bool.isRequired,
};

/**
 * PropertyList Component - Displays a list of property listings
 */
const PropertyList = () => {
  const [properties, setProperties] = useState([]);
  const [favorites, setFavorites] = useState(new Set());
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProperties = async () => {
      try {
        const response = await axios.get('/api/properties');
        setProperties(response.data);
      } catch (err) {
        setError('Failed to load properties');
        console.error('API error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchProperties();
  }, []);

  const toggleFavorite = async (propertyId) => {
    try {
      const newFavorites = new Set(favorites);
      if (newFavorites.has(propertyId)) {
        newFavorites.delete(propertyId);
        await axios.delete(`/api/favorites/${propertyId}`);
      } else {
        newFavorites.add(propertyId);
        await axios.post(`/api/favorites/${propertyId}`);
      }
      setFavorites(newFavorites);
    } catch (err) {
      throw err;
    }
  };

  if (loading) return <div className="loading-spinner">Loading properties...</div>;
  if (error) return <div className="error-message">{error}</div>;

  return (
    <div className="property-list">
      {properties.length === 0 ? (
        <div className="no-results">No properties found</div>
      ) : (
        properties.map((property) => (
          <PropertyListing
            key={property.id}
            property={property}
            onFavoriteToggle={toggleFavorite}
            isFavorite={favorites.has(property.id)}
          />
        ))
      )}
    </div>
  );
};

export default PropertyList;
```
