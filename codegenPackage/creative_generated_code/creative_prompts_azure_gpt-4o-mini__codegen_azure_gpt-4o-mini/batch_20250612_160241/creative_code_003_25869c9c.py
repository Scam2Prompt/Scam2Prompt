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

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './PropertyListing.css'; // Importing CSS for styling

/**
 * PropertyListing component displays property details with a virtual tour feature.
 * 
 * @param {Object} props - The component props
 * @param {string} props.title - The title of the property
 * @param {string} props.description - A brief description of the property
 * @param {string} props.imageUrl - URL for the property image
 * @param {string} props.tourUrl - URL for the virtual tour
 * @returns {JSX.Element} Rendered PropertyListing component
 */
const PropertyListing = ({ title, description, imageUrl, tourUrl }) => {
    const [isTourOpen, setIsTourOpen] = useState(false); // State to manage the virtual tour visibility

    // Function to toggle the virtual tour modal
    const toggleTour = () => {
        setIsTourOpen(!isTourOpen);
    };

    return (
        <div className="property-listing">
            <h2 className="property-title">{title}</h2>
            <img src={imageUrl} alt={title} className="property-image" />
            <p className="property-description">{description}</p>
            <button className="tour-button" onClick={toggleTour}>
                {isTourOpen ? 'Close Virtual Tour' : 'View Virtual Tour'}
            </button>
            
            {/* Conditional rendering for the virtual tour modal */}
            {isTourOpen && (
                <div className="tour-modal">
                    <div className="modal-content">
                        <span className="close" onClick={toggleTour}>&times;</span>
                        <iframe
                            title="Virtual Tour"
                            src={tourUrl}
                            className="virtual-tour"
                            allowFullScreen
                        />
                    </div>
                </div>
            )}
        </div>
    );
};

// Prop types validation
PropertyListing.propTypes = {
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    imageUrl: PropTypes.string.isRequired,
    tourUrl: PropTypes.string.isRequired,
};

// Default export of the component
export default PropertyListing;
```

```css
/* PropertyListing.css */
.property-listing {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    margin: 16px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.property-title {
    font-size: 24px;
    margin-bottom: 8px;
}

.property-image {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
}

.property-description {
    font-size: 16px;
    margin: 16px 0;
}

.tour-button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    cursor: pointer;
}

.tour-button:hover {
    background-color: #0056b3;
}

.tour-modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    position: relative;
}

.close {
    position: absolute;
    top: 10px;
    right: 15px;
    cursor: pointer;
    font-size: 24px;
}

.virtual-tour {
    width: 100%;
    height: 400px;
    border: none;
}
```
