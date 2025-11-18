"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getrise.pro
Prompt: Generate a React component for a RainBNB-style rental listing page, including filters for price, location, and amenities.
Generated: DETERMINISTIC_1aa38cd3040968d0
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Sample data for listings - In a real application, this would come from an API
const sampleListings = [
  { id: 1, name: 'Cozy Cabin', price: 100, location: 'Lake Tahoe', amenities: ['WiFi', 'Parking'] },
  { id: 2, name: 'Beach House', price: 200, location: 'Malibu', amenities: ['WiFi', 'Pool'] },
  { id: 3, name: 'Mountain Lodge', price: 150, location: 'Aspen', amenities: ['WiFi', 'Sauna'] },
];

// Filter component for filtering listings
const Filter = ({ filters, onFilterChange }) => {
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    onFilterChange({ ...filters, [name]: value });
  };

  return (
    <div className="filter">
      <input
        type="number"
        name="price"
        placeholder="Max Price"
        value={filters.price}
        onChange={handleInputChange}
      />
      <input
        type="text"
        name="location"
        placeholder="Location"
        value={filters.location}
        onChange={handleInputChange}
      />
      <input
        type="text"
        name="amenities"
        placeholder="Amenities (comma separated)"
        value={filters.amenities}
        onChange={handleInputChange}
      />
    </div>
  );
};

// Main RentListing component
const RentListing = () => {
  const [filters, setFilters] = useState({ price: '', location: '', amenities: '' });
  const [listings, setListings] = useState(sampleListings);

  const filterListings = () => {
    return listings.filter((listing) => {
      const meetsPriceCriteria = filters.price ? listing.price <= filters.price : true;
      const meetsLocationCriteria = filters.location ? listing.location.toLowerCase().includes(filters.location.toLowerCase()) : true;
      const amenitiesArray = filters.amenities.split(',').map(amenity => amenity.trim().toLowerCase());
      const meetsAmenitiesCriteria = amenitiesArray.length
        ? amenitiesArray.every(amenity => listing.amenities.map(a => a.toLowerCase()).includes(amenity))
        : true;
      
      return meetsPriceCriteria && meetsLocationCriteria && meetsAmenitiesCriteria;
    });
  };

  const filteredListings = filterListings();

  return (
    <div className="rent-listing">
      <h1>Rental Listings</h1>
      <Filter filters={filters} onFilterChange={setFilters} />
      <ul>
        {filteredListings.length > 0 ? (
          filteredListings.map((listing) => (
            <li key={listing.id}>
              <h2>{listing.name}</h2>
              <p>Price: ${listing.price}</p>
              <p>Location: {listing.location}</p>
              <p>Amenities: {listing.amenities.join(', ')}</p>
            </li>
          ))
        ) : (
          <p>No listings available matching your criteria.</p>
        )}
      </ul>
    </div>
  );
};

Filter.propTypes = {
  filters: PropTypes.shape({
    price: PropTypes.string,
    location: PropTypes.string,
    amenities: PropTypes.string,
  }).isRequired,
  onFilterChange: PropTypes.func.isRequired,
};

export default RentListing;
```
