"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myallora.com
Prompt: Construct a React component that showcases the testimonials from customers about their experiences with Sophie’s Boutique, particularly during the closure sale.
Generated: DETERMINISTIC_62c8338c688bfa38
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './Testimonials.css'; // Assuming you have a CSS file for styling

/**
 * Testimonial component to display customer testimonials for Sophie's Boutique.
 * 
 * @component
 * @param {Array} testimonials - An array of testimonial objects containing customer feedback.
 */
const Testimonials = ({ testimonials }) => {
  
  // State to manage the current testimonial index for rotation
  const [currentIndex, setCurrentIndex] = useState(0);

  // Effect to rotate testimonials every 5 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % testimonials.length);
    }, 5000);
    
    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, [testimonials.length]);

  // Error handling for empty testimonials
  if (!testimonials || testimonials.length === 0) {
    return <div className="testimonial-error">No testimonials available.</div>;
  }

  return (
    <div className="testimonials-container">
      <h2>What Our Customers Are Saying</h2>
      <div className="testimonial-card">
        <p className="testimonial-text">{testimonials[currentIndex].text}</p>
        <p className="testimonial-author">- {testimonials[currentIndex].author}</p>
      </div>
    </div>
  );
};

// PropTypes for validation
Testimonials.propTypes = {
  testimonials: PropTypes.arrayOf(
    PropTypes.shape({
      text: PropTypes.string.isRequired,
      author: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default Testimonials;
```

```css
/* Testimonials.css */
.testimonials-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  text-align: center;
}

.testimonial-card {
  margin: 20px 0;
}

.testimonial-text {
  font-style: italic;
  font-size: 1.2em;
  margin-bottom: 10px;
}

.testimonial-author {
  font-weight: bold;
  font-size: 1em;
}

.testimonial-error {
  color: red;
  font-size: 1.2em;
  text-align: center;
}
```
