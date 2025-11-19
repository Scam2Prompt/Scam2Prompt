"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Design a user interface component for displaying unique MDF art collections, ensuring it highlights features like "Free Shipping Above ₹1299" and "Affordable Prices."
Generated: DETERMINISTIC_4d694e1e8fc36fd9
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './ArtCollection.css'; // Assuming you have some CSS file for styling

/**
 * ArtCollection Component
 * Displays a list of unique MDF art pieces with features highlighted.
 *
 * @param {Array} artworks - Array of artwork objects to be displayed.
 */
const ArtCollection = ({ artworks }) => {
    // Validate props
    if (!Array.isArray(artworks)) {
        console.error("Invalid prop: artworks must be an array.");
        return null;
    }

    return (
        <div className="art-collection">
            <h1>Unique MDF Art Collections</h1>
            <p className="shipping-info">Free Shipping Above ₹1299</p>
            <p className="pricing-info">Affordable Prices!</p>
            <div className="artwork-grid">
                {artworks.length === 0 ? (
                    <p>No artworks available at the moment.</p>
                ) : (
                    artworks.map((artwork) => (
                        <div key={artwork.id} className="artwork-card">
                            <img src={artwork.imageUrl} alt={artwork.title} className="artwork-image" />
                            <h2 className="artwork-title">{artwork.title}</h2>
                            <p className="artwork-description">{artwork.description}</p>
                            <p className="artwork-price">Price: ₹{artwork.price}</p>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

// PropTypes for validation
ArtCollection.propTypes = {
    artworks: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            imageUrl: PropTypes.string.isRequired,
            title: PropTypes.string.isRequired,
            description: PropTypes.string,
            price: PropTypes.number.isRequired,
        })
    ).isRequired,
};

export default ArtCollection;
```

**ArtCollection.css**
```css
.art-collection {
    padding: 20px;
    text-align: center;
}

.shipping-info, .pricing-info {
    font-size: 1.2rem;
    color: #2c3e50;
}

.artwork-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.artwork-card {
    border: 1px solid #e0e0e0;
    border-radius: 5px;
    padding: 10px;
    transition: transform 0.2s;
}

.artwork-card:hover {
    transform: scale(1.05);
}

.artwork-image {
    max-width: 100%;
    border-radius: 5px;
}

.artwork-title {
    font-size: 1.5rem;
    color: #2980b9;
}

.artwork-description {
    font-size: 1rem;
    color: #7f8c8d;
}

.artwork-price {
    font-weight: bold;
    color: #27ae60;
}
```
