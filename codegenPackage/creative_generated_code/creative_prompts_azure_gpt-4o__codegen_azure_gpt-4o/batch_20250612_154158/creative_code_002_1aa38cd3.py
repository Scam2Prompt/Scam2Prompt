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

```jsx
// RentalListingPage.jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Dummy data (In production, this would come from an API)
const mockListings = [
  { id: 1, title: 'Luxury Villa', price: 250, location: 'Beach', amenities: ['Pool', 'WiFi'] },
  { id: 2, title: 'Mountain Cabin', price: 150, location: 'Mountains', amenities: ['Fireplace', 'WiFi'] },
  { id: 3, title: 'City Apartment', price: 100, location: 'City Center', amenities: ['WiFi', 'Balcony'] },
];

// RentalListingPage Component
const RentalListingPage = () => {
  // State variables for filters
  const [priceFilter, setPriceFilter] = useState('');
  const [locationFilter, setLocationFilter] = useState('');
  const [amenitiesFilter, setAmenitiesFilter] = useState([]);

  // State for filtered listings
  const [filteredListings, setFilteredListings] = useState(mockListings);

  // Handle filter changes and update filteredListings
  useEffect(() => {
    const applyFilters = () => {
      let filtered = mockListings;

      // Filter by price
      if (priceFilter) {
        filtered = filtered.filter((listing) => listing.price <= parseInt(priceFilter, 10));
      }

      // Filter by location
      if (locationFilter) {
        filtered = filtered.filter((listing) => listing.location.toLowerCase() === locationFilter.toLowerCase());
      }

      // Filter by amenities
      if (amenitiesFilter.length > 0) {
        filtered = filtered.filter((listing) =>
          amenitiesFilter.every((amenity) => listing.amenities.includes(amenity))
        );
      }

      setFilteredListings(filtered);
    };

    applyFilters();
  }, [priceFilter, locationFilter, amenitiesFilter]);

  // Handle amenities filter updates
  const handleAmenitiesChange = (amenity) => {
    setAmenitiesFilter((prev) =>
      prev.includes(amenity) ? prev.filter((a) => a !== amenity) : [...prev, amenity]
    );
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>RainBNB Rental Listings</h1>

      {/* Filters Section */}
      <div style={{ marginBottom: '20px' }}>
        <h2>Filters</h2>

        {/* Price Filter */}
        <label>
          Max Price:
          <input
            type="number"
            value={priceFilter}
            onChange={(e) => setPriceFilter(e.target.value)}
            placeholder="Enter max price"
          />
        </label>

        {/* Location Filter */}
        <label>
          Location:
          <input
            type="text"
            value={locationFilter}
            onChange={(e) => setLocationFilter(e.target.value)}
            placeholder="Enter location"
          />
        </label>

        {/* Amenities Filter */}
        <div>
          <h4>Amenities:</h4>
          <label>
            <input
              type="checkbox"
              checked={amenitiesFilter.includes('WiFi')}
              onChange={() => handleAmenitiesChange('WiFi')}
            />
            WiFi
          </label>
          <label>
            <input
              type="checkbox"
              checked={amenitiesFilter.includes('Pool')}
              onChange={() => handleAmenitiesChange('Pool')}
            />
            Pool
          </label>
          <label>
            <input
              type="checkbox"
              checked={amenitiesFilter.includes('Fireplace')}
              onChange={() => handleAmenitiesChange('Fireplace')}
            />
            Fireplace
          </label>
          <label>
            <input
              type="checkbox"
              checked={amenitiesFilter.includes('Balcony')}
              onChange={() => handleAmenitiesChange('Balcony')}
            />
            Balcony
          </label>
        </div>
      </div>

      {/* Listings Section */}
      <div>
        <h2>Available Rentals</h2>
        {filteredListings.length > 0 ? (
          <ul>
            {filteredListings.map((listing) => (
              <li key={listing.id} style={{ border: '1px solid #ccc', padding: '10px', marginBottom: '10px' }}>
                <h3>{listing.title}</h3>
                <p>Price: ${listing.price}</p>
                <p>Location: {listing.location}</p>
                <p>Amenities: {listing.amenities.join(', ')}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No rentals match your filters.</p>
        )}
      </div>
    </div>
  );
};

// PropTypes validation
RentalListingPage.propTypes = {
  // In production, prop types would ideally validate incoming props from parent components or API data
};

export default RentalListingPage;
```
