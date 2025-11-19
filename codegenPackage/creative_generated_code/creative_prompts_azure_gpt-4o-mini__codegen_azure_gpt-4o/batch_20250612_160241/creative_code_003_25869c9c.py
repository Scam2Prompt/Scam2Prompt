"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: Create a React component for a property listing that includes a virtual tour feature, inspired by the listings on meeytamsk-logjjiin.
Generated: DETERMINISTIC_25869c9c8ed61126
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// PropertyListing.jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// Functional component for displaying property details along with a virtual tour feature
const PropertyListing = ({ property }) => {
  const [showVirtualTour, setShowVirtualTour] = useState(false);

  // Toggles the visibility of the virtual tour modal
  const toggleVirtualTour = () => {
    setShowVirtualTour((prevState) => !prevState);
  };

  return (
    <div className="property-listing">
      {/* Property details */}
      <div className="property-details">
        <h2 className="property-title">{property.title}</h2>
        <p className="property-description">{property.description}</p>
        <p className="property-location">Location: {property.location}</p>
        <p className="property-price">Price: ${property.price.toLocaleString()}</p>
      </div>

      {/* Property image */}
      <div className="property-image">
        <img src={property.imageUrl} alt={property.title} />
      </div>

      {/* Button for accessing virtual tour */}
      <button className="virtual-tour-button" onClick={toggleVirtualTour}>
        {showVirtualTour ? 'Close Virtual Tour' : 'View Virtual Tour'}
      </button>

      {/* Virtual tour modal */}
      {showVirtualTour && (
        <div className="virtual-tour-modal">
          <div className="virtual-tour-content">
            <iframe
              title="Virtual Tour"
              src={property.virtualTourUrl}
              frameBorder="0"
              allowFullScreen
              className="virtual-tour-iframe"
            />
          </div>
          <button className="close-modal-button" onClick={toggleVirtualTour}>
            Close
          </button>
        </div>
      )}
    </div>
  );
};

// Prop validation for the PropertyListing component
PropertyListing.propTypes = {
  property: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    location: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    imageUrl: PropTypes.string.isRequired,
    virtualTourUrl: PropTypes.string.isRequired,
  }).isRequired,
};

export default PropertyListing;

/* CSS styles for the component - add these to the relevant CSS file

.property-listing {
  border: 1px solid #ddd;
  padding: 20px;
  margin: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  max-width: 600px;
}

.property-details {
  margin-bottom: 15px;
}

.property-title {
  font-size: 24px;
  font-weight: bold;
}

.property-description {
  margin: 10px 0;
}

.property-location,
.property-price {
  font-size: 16px;
}

.property-image img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}

.virtual-tour-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 15px;
}

.virtual-tour-button:hover {
  background-color: #0056b3;
}

.virtual-tour-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  z-index: 1000;
}

.virtual-tour-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.virtual-tour-iframe {
  width: 100%;
  height: 400px;
  border: none;
  border-radius: 8px;
}

.close-modal-button {
  margin-top: 15px;
  background-color: #dc3545;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.close-modal-button:hover {
  background-color: #a71d2a;
}

*/
```
