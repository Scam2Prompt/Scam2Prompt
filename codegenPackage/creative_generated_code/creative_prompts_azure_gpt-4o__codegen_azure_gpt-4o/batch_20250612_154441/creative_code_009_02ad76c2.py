"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Develop a React component to display a carousel of "Trending Belts" with clickable images and links to product pages, as featured on Belts Mania.
Generated: DETERMINISTIC_02ad76c2439c95f6
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// TrendingBeltsCarousel.jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './TrendingBeltsCarousel.css';

/**
 * TrendingBeltsCarousel Component
 * Displays a carousel of trending belts with clickable images and links.
 *
 * Props:
 * - belts: Array of belt objects with the following structure:
 *   { id: string, name: string, imageUrl: string, productUrl: string }
 */
const TrendingBeltsCarousel = ({ belts }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  // Handles moving to the next slide
  const goToNextSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % belts.length);
  };

  // Handles moving to the previous slide
  const goToPrevSlide = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? belts.length - 1 : prevIndex - 1
    );
  };

  return (
    <div className="carousel-container">
      {/* Carousel Controls */}
      <button
        className="carousel-control prev"
        onClick={goToPrevSlide}
        aria-label="Previous Slide"
      >
        &#9664;
      </button>

      <button
        className="carousel-control next"
        onClick={goToNextSlide}
        aria-label="Next Slide"
      >
        &#9654;
      </button>

      {/* Carousel Slide */}
      {belts.length > 0 && (
        <div className="carousel-slide">
          <a
            href={belts[currentIndex].productUrl}
            target="_blank"
            rel="noopener noreferrer"
          >
            <img
              src={belts[currentIndex].imageUrl}
              alt={belts[currentIndex].name}
              className="carousel-image"
            />
          </a>
          <p className="carousel-caption">{belts[currentIndex].name}</p>
        </div>
      )}

      {/* Error Handling: No belts available */}
      {belts.length === 0 && <p className="carousel-error">No belts available.</p>}
    </div>
  );
};

// Define PropTypes for component props validation
TrendingBeltsCarousel.propTypes = {
  belts: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      imageUrl: PropTypes.string.isRequired,
      productUrl: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default TrendingBeltsCarousel;

/* TrendingBeltsCarousel.css */
/* Basic styles for the carousel */
.carousel-container {
  position: relative;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  overflow: hidden;
}

.carousel-control {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: none;
  color: white;
  font-size: 20px;
  padding: 10px;
  cursor: pointer;
  z-index: 10;
}

.carousel-control.prev {
  left: 10px;
}

.carousel-control.next {
  right: 10px;
}

.carousel-slide {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.carousel-image {
  width: 100%;
  max-width: 500px;
  border-radius: 10px;
  cursor: pointer;
}

.carousel-caption {
  margin-top: 10px;
  font-size: 16px;
  font-weight: bold;
}

.carousel-error {
  color: red;
  font-size: 18px;
  font-weight: bold;
}
```
