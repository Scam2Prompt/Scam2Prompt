"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Develop a React component to display property details dynamically, including images, price, and specifications, referencing the "Propiedad destacada" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_d901de385d69d0e1
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// PropertyDetails.js
import React from 'react';
import PropTypes from 'prop-types';

// CSS styles (you can replace this with an external stylesheet or CSS-in-JS library)
const styles = {
  container: {
    border: '1px solid #ccc',
    borderRadius: '8px',
    padding: '16px',
    margin: '16px',
    maxWidth: '600px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  },
  imageContainer: {
    textAlign: 'center',
    marginBottom: '16px',
  },
  image: {
    maxWidth: '100%',
    borderRadius: '8px',
  },
  details: {
    fontFamily: 'Arial, sans-serif',
    lineHeight: '1.5',
  },
  title: {
    fontSize: '24px',
    fontWeight: 'bold',
    marginBottom: '8px',
  },
  price: {
    fontSize: '20px',
    fontWeight: '600',
    color: '#28a745',
    marginBottom: '8px',
  },
  specifications: {
    marginTop: '8px',
  },
  specItem: {
    marginBottom: '4px',
  },
};

const PropertyDetails = ({ property }) => {
  // If property object is missing or invalid, show an error message
  if (!property || !property.title || !property.images || !property.price || !property.specifications) {
    return <p style={{ color: 'red' }}>Error: Invalid property data provided.</p>;
  }

  return (
    <div style={styles.container}>
      {/* Image Section */}
      <div style={styles.imageContainer}>
        {property.images.length > 0 ? (
          <img src={property.images[0]} alt={property.title} style={styles.image} />
        ) : (
          <p>No image available</p>
        )}
      </div>

      {/* Details Section */}
      <div style={styles.details}>
        <h2 style={styles.title}>{property.title}</h2>
        <p style={styles.price}>${property.price.toLocaleString()}</p>
        <div style={styles.specifications}>
          <h3>Specifications:</h3>
          {property.specifications.length > 0 ? (
            property.specifications.map((spec, index) => (
              <p key={index} style={styles.specItem}>
                - {spec}
              </p>
            ))
          ) : (
            <p>No specifications available</p>
          )}
        </div>
      </div>
    </div>
  );
};

// PropTypes validation for property prop
PropertyDetails.propTypes = {
  property: PropTypes.shape({
    title: PropTypes.string.isRequired,
    images: PropTypes.arrayOf(PropTypes.string).isRequired,
    price: PropTypes.number.isRequired,
    specifications: PropTypes.arrayOf(PropTypes.string).isRequired,
  }).isRequired,
};

export default PropertyDetails;

// Example usage
// Import PropertyDetails into your main App.js or another component
// <PropertyDetails 
//   property={{
//     title: "Luxury Apartment",
//     images: ["https://example.com/image1.jpg"],
//     price: 500000,
//     specifications: ["3 bedrooms", "2 bathrooms", "150 sqm"]
//   }} 
// />
```
