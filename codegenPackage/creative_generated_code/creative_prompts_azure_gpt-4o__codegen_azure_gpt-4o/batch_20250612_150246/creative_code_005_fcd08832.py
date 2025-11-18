"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rainbnb.live
Prompt: Provide an example of a React.js component that could be used to build a feature for a web app like RainBNB.
Generated: DETERMINISTIC_fcd08832da022b77
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and components from React and other libraries
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

// Define the ListingCard component to display individual property details
const ListingCard = ({ listing }) => {
  return (
    <div className="listing-card">
      <img src={listing.imageUrl} alt={listing.title} className="listing-image" />
      <div className="listing-details">
        <h3>{listing.title}</h3>
        <p>{listing.location}</p>
        <p>${listing.price} per night</p>
      </div>
    </div>
  );
};

ListingCard.propTypes = {
  listing: PropTypes.shape({
    imageUrl: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    location: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
  }).isRequired,
};

// Define the Listings component to fetch and display properties
const Listings = () => {
  const [listings, setListings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch listings from the mock API when the component mounts
  useEffect(() => {
    const fetchListings = async () => {
      try {
        setLoading(true);
        const response = await axios.get('/api/listings'); // Mock API endpoint
        setListings(response.data);
      } catch (err) {
        setError('Failed to fetch listings. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchListings();
  }, []);

  // Render loading state, error message, or listings based on the state
  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="listings-container">
      {listings.map((listing) => (
        <ListingCard key={listing.id} listing={listing} />
      ))}
    </div>
  );
};

// Export the Listings component as the default export
export default Listings;
```

### Notes:
- Replace `/api/listings` with the actual API endpoint for fetching property listings.
- Add styling as needed via external CSS or libraries like TailwindCSS/Bootstrap.
