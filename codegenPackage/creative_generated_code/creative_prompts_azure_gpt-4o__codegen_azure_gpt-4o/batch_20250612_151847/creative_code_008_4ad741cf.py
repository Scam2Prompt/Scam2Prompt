"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Generate code using React to create a testimonial carousel for Sekolah Quran Indonesia's website, dynamically displaying testimonials from alumni such as Fulan (Angkatan SQI 2018) and Fulanah (Angkatan SQI 2022).
Generated: DETERMINISTIC_4ad741cff774b001
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules
import React, { useState } from 'react';

// Carousel Component
const TestimonialCarousel = () => {
  // Array to store testimonials
  const testimonials = [
    { name: 'Fulan', graduationYear: 'Angkatan SQI 2018', message: 'Sekolah Quran Indonesia has truly changed my life for the better.' },
    { name: 'Fulanah', graduationYear: 'Angkatan SQI 2022', message: 'An amazing experience that helped me grow spiritually and academically.' },
    // Add more testimonials as needed
  ];

  // State to track the currently active testimonial
  const [currentIndex, setCurrentIndex] = useState(0);

  // Function to go to the next testimonial
  const nextTestimonial = () => {
    if (currentIndex < testimonials.length - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setCurrentIndex(0); // Loop back to the first testimonial
    }
  };

  // Function to go to the previous testimonial
  const prevTestimonial = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    } else {
      setCurrentIndex(testimonials.length - 1); // Loop back to the last testimonial
    }
  };

  return (
    <div className="testimonial-carousel" style={styles.carouselContainer}>
      {/* Display testimonial content */}
      <div style={styles.testimonialContent}>
        <p style={styles.message}>"{testimonials[currentIndex].message}"</p>
        <p style={styles.author}>
          - {testimonials[currentIndex].name} ({testimonials[currentIndex].graduationYear})
        </p>
      </div>
      
      {/* Navigation buttons */}
      <div style={styles.navButtons}>
        <button onClick={prevTestimonial} style={styles.button}>
          &lt; Previous
        </button>
        <button onClick={nextTestimonial} style={styles.button}>
          Next &gt;
        </button>
      </div>
    </div>
  );
};

// Inline styles for simplicity (use CSS or a styling library in production)
const styles = {
  carouselContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    maxWidth: '600px',
    margin: '0 auto',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '10px',
    backgroundColor: '#f9f9f9',
  },
  testimonialContent: {
    textAlign: 'center',
    marginBottom: '20px',
  },
  message: {
    fontSize: '1.2em',
    fontStyle: 'italic',
    marginBottom: '10px',
  },
  author: {
    fontSize: '1em',
    fontWeight: 'bold',
  },
  navButtons: {
    display: 'flex',
    justifyContent: 'space-between',
    width: '100%',
  },
  button: {
    padding: '10px 20px',
    fontSize: '1em',
    cursor: 'pointer',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    transition: 'background-color 0.3s',
  },
};

// Export the component
export default TestimonialCarousel;
```
