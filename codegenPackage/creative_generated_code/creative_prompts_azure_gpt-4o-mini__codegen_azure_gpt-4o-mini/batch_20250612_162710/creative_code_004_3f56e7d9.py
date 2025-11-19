"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Construct a React component that shows a product gallery for the "Conjunto Infantil Meia Malha/Moletinho Urban" from "Somos Corujas."
Generated: DETERMINISTIC_3f56e7d9bb9771cd
Batch ID: 20250612_162710
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './ProductGallery.css'; // Import CSS for styling

const ProductGallery = ({ product }) => {
    const [selectedImage, setSelectedImage] = useState(product.images[0]);

    // Handle image click to select the clicked image
    const handleImageClick = (image) => {
        setSelectedImage(image);
    };

    return (
        <div className="product-gallery">
            <div className="gallery-main-image">
                <img src={selectedImage} alt={product.name} />
            </div>
            <div className="gallery-thumbnails">
                {product.images.map((image, index) => (
                    <img
                        key={index}
                        src={image}
                        alt={`${product.name} thumbnail ${index + 1}`}
                        onClick={() => handleImageClick(image)}
                        className={`thumbnail ${image === selectedImage ? 'selected' : ''}`}
                    />
                ))}
            </div>
            <div className="product-info">
                <h2>{product.name}</h2>
                <p>{product.description}</p>
                <span className="product-price">{`R$ ${product.price}`}</span>
            </div>
        </div>
    );
};

// Prop types validation
ProductGallery.propTypes = {
    product: PropTypes.shape({
        name: PropTypes.string.isRequired,
        description: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
        images: PropTypes.arrayOf(PropTypes.string).isRequired,
    }).isRequired,
};

// Sample product data for testing
const sampleProduct = {
    name: "Conjunto Infantil Meia Malha/Moletinho Urban",
    description: "Comfortable and stylish outfit for kids.",
    price: 149.90,
    images: [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
    ],
};

// Render the ProductGallery component with sample data
const App = () => (
    <div className="app">
        <ProductGallery product={sampleProduct} />
    </div>
);

export default App;
```

```css
/* ProductGallery.css */

.product-gallery {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.gallery-main-image img {
    width: 300px;
    height: auto;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.gallery-thumbnails {
    display: flex;
    justify-content: center;
}

.thumbnail {
    width: 60px;
    height: 60px;
    margin: 0 5px;
    cursor: pointer;
    opacity: 0.6;
    transition: opacity 0.3s;
}

.thumbnail.selected {
    border: 2px solid #007BFF;
    opacity: 1;
}

.product-info {
    text-align: center;
    margin-top: 10px;
}

.product-price {
    font-size: 1.5em;
    color: #333;
}
```
