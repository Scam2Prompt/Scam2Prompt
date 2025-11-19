"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Develop a React component for displaying property listings with details like price, location, and features, similar to those showcased on Inmobiliaria Nueva Ciudad's website.
Generated: DETERMINISTIC_8fea36516732b7cd
Batch ID: 20250622_210655
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
import './PropertyListings.css';

/**
 * PropertyListingCard component displays individual property details
 * @param {Object} props - Component props
 * @param {Object} props.property - Property data object
 */
const PropertyListingCard = ({ property }) => {
  return (
    <div className="property-card">
      <div className="property-image-container">
        <img 
          src={property.imageUrl || '/default-property.jpg'} 
          alt={property.title} 
          className="property-image"
          onError={(e) => {
            e.target.src = '/default-property.jpg';
          }}
        />
        <div className="property-price">${property.price.toLocaleString()}</div>
      </div>
      
      <div className="property-details">
        <h3 className="property-title">{property.title}</h3>
        <p className="property-location">
          <i className="fas fa-map-marker-alt"></i> {property.location}
        </p>
        
        <div className="property-features">
          <div className="feature">
            <i className="fas fa-bed"></i> {property.bedrooms} beds
          </div>
          <div className="feature">
            <i className="fas fa-bath"></i> {property.bathrooms} baths
          </div>
          <div className="feature">
            <i className="fas fa-ruler-combined"></i> {property.area} sqft
          </div>
        </div>
        
        <button className="property-contact-btn">Contact Agent</button>
      </div>
    </div>
  );
};

PropertyListingCard.propTypes = {
  property: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    location: PropTypes.string.isRequired,
    bedrooms: PropTypes.number.isRequired,
    bathrooms: PropTypes.number.isRequired,
    area: PropTypes.number.isRequired,
    imageUrl: PropTypes.string,
  }).isRequired,
};

/**
 * PropertyListings component displays a grid of property listings
 * @param {Object} props - Component props
 * @param {Array} props.properties - Array of property objects
 * @param {boolean} props.loading - Loading state
 * @param {string} props.error - Error message
 */
const PropertyListings = ({ properties, loading, error }) => {
  const [filteredProperties, setFilteredProperties] = useState([]);
  const [filters, setFilters] = useState({
    minPrice: '',
    maxPrice: '',
    bedrooms: '',
    propertyType: '',
  });

  useEffect(() => {
    setFilteredProperties(properties);
  }, [properties]);

  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    setFilters(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const applyFilters = () => {
    let result = [...properties];
    
    if (filters.minPrice) {
      result = result.filter(p => p.price >= Number(filters.minPrice));
    }
    
    if (filters.maxPrice) {
      result = result.filter(p => p.price <= Number(filters.maxPrice));
    }
    
    if (filters.bedrooms) {
      result = result.filter(p => p.bedrooms >= Number(filters.bedrooms));
    }
    
    if (filters.propertyType) {
      result = result.filter(p => p.type === filters.propertyType);
    }
    
    setFilteredProperties(result);
  };

  const resetFilters = () => {
    setFilters({
      minPrice: '',
      maxPrice: '',
      bedrooms: '',
      propertyType: '',
    });
    setFilteredProperties(properties);
  };

  if (loading) {
    return <div className="loading-spinner">Loading properties...</div>;
  }

  if (error) {
    return <div className="error-message">Error: {error}</div>;
  }

  return (
    <div className="property-listings-container">
      <div className="filters-section">
        <h2>Filter Properties</h2>
        <div className="filter-controls">
          <div className="filter-group">
            <label>Min Price:</label>
            <input
              type="number"
              name="minPrice"
              value={filters.minPrice}
              onChange={handleFilterChange}
              placeholder="$"
            />
          </div>
          
          <div className="filter-group">
            <label>Max Price:</label>
            <input
              type="number"
              name="maxPrice"
              value={filters.maxPrice}
              onChange={handleFilterChange}
              placeholder="$"
            />
          </div>
          
          <div className="filter-group">
            <label>Bedrooms:</label>
            <select
              name="bedrooms"
              value={filters.bedrooms}
              onChange={handleFilterChange}
            >
              <option value="">Any</option>
              <option value="1">1+</option>
              <option value="2">2+</option>
              <option value="3">3+</option>
              <option value="4">4+</option>
            </select>
          </div>
          
          <div className="filter-group">
            <label>Property Type:</label>
            <select
              name="propertyType"
              value={filters.propertyType}
              onChange={handleFilterChange}
            >
              <option value="">Any</option>
              <option value="house">House</option>
              <option value="apartment">Apartment</option>
              <option value="condo">Condo</option>
              <option value="land">Land</option>
            </select>
          </div>
          
          <button onClick={applyFilters} className="apply-filters-btn">
            Apply Filters
          </button>
          
          <button onClick={resetFilters} className="reset-filters-btn">
            Reset
          </button>
        </div>
      </div>
      
      <div className="property-listings-grid">
        {filteredProperties.length > 0 ? (
          filteredProperties.map(property => (
            <PropertyListingCard key={property.id} property={property} />
          ))
        ) : (
          <div className="no-results">No properties match your filters.</div>
        )}
      </div>
    </div>
  );
};

PropertyListings.propTypes = {
  properties: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      location: PropTypes.string.isRequired,
      bedrooms: PropTypes.number.isRequired,
      bathrooms: PropTypes.number.isRequired,
      area: PropTypes.number.isRequired,
      imageUrl: PropTypes.string,
      type: PropTypes.string,
    })
  ).isRequired,
  loading: PropTypes.bool,
  error: PropTypes.string,
};

PropertyListings.defaultProps = {
  loading: false,
  error: null,
};

export default PropertyListings;
```
