"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Develop a front-end component using React that displays testimonials from clients who sold their houses quickly, similar to the testimonials section on Metis Assets' webpage.
Generated: DETERMINISTIC_8796a5a571467ceb
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// TestimonialsComponent.jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './TestimonialsComponent.css'; // Importing styles for the component

/**
 * TestimonialsComponent
 * A React component to display client testimonials.
 * 
 * Props:
 * - testimonials: Array of testimonial objects with the following structure:
 *   {
 *     id: number,
 *     name: string,
 *     message: string,
 *     image: string (URL to the client's image)
 *   }
 */
const TestimonialsComponent = ({ testimonials }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  // Function to handle navigation to the next testimonial
  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % testimonials.length);
  };

  // Function to handle navigation to the previous testimonial
  const handlePrev = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? testimonials.length - 1 : prevIndex - 1
    );
  };

  // Render the component
  return (
    <div className="testimonials-container">
      <h2 className="testimonials-title">What Our Clients Say</h2>
      {testimonials.length > 0 ? (
        <div className="testimonial">
          <img
            src={testimonials[currentIndex].image}
            alt={`${testimonials[currentIndex].name}'s testimonial`}
            className="testimonial-image"
          />
          <p className="testimonial-message">"{testimonials[currentIndex].message}"</p>
          <p className="testimonial-name">- {testimonials[currentIndex].name}</p>
          <div className="testimonial-navigation">
            <button onClick={handlePrev} className="nav-button">
              Previous
            </button>
            <button onClick={handleNext} className="nav-button">
              Next
            </button>
          </div>
        </div>
      ) : (
        <p className="no-testimonials">No testimonials available.</p>
      )}
    </div>
  );
};

// PropTypes for type checking
TestimonialsComponent.propTypes = {
  testimonials: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      message: PropTypes.string.isRequired,
      image: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default TestimonialsComponent;

/* TestimonialsComponent.css */
/* Basic styles for the TestimonialsComponent */
.testimonials-container {
  text-align: center;
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}

.testimonials-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.testimonial {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background-color: #f9f9f9;
}

.testimonial-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.testimonial-message {
  font-style: italic;
  margin-bottom: 10px;
}

.testimonial-name {
  font-weight: bold;
  margin-bottom: 20px;
}

.testimonial-navigation {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.nav-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.nav-button:hover {
  background-color: #0056b3;
}

.no-testimonials {
  font-size: 18px;
  color: #888;
}
```
