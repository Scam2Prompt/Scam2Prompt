"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Generate code using React to create a testimonial carousel for Sekolah Quran Indonesia's website, dynamically displaying testimonials from alumni such as Fulan (Angkatan SQI 2018) and Fulanah (Angkatan SQI 2022).
Generated: DETERMINISTIC_4ad741cff774b001
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './TestimonialCarousel.css';

/**
 * TestimonialCarousel component for displaying alumni testimonials in a rotating carousel.
 * @param {Object} props - Component props.
 * @param {Array} props.testimonials - Array of testimonial objects.
 * @param {number} [props.interval=5000] - Time between testimonial transitions in milliseconds.
 */
const TestimonialCarousel = ({ testimonials, interval = 5000 }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isPaused, setIsPaused] = useState(false);

  // Validate testimonials array
  if (!testimonials || !Array.isArray(testimonials) || testimonials.length === 0) {
    throw new Error('TestimonialCarousel requires a non-empty array of testimonials');
  }

  // Handle automatic carousel rotation
  useEffect(() => {
    if (isPaused) return;

    const timer = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % testimonials.length);
    }, interval);

    return () => clearInterval(timer);
  }, [currentIndex, interval, isPaused, testimonials.length]);

  // Handle manual navigation
  const goToIndex = (index) => {
    setCurrentIndex(index);
  };

  // Handle previous/next navigation
  const goToPrev = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === 0 ? testimonials.length - 1 : prevIndex - 1
    );
  };

  const goToNext = () => {
    setCurrentIndex((prevIndex) => 
      (prevIndex + 1) % testimonials.length
    );
  };

  return (
    <div 
      className="testimonial-carousel" 
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
    >
      <div className="testimonial-content">
        <button 
          className="carousel-button prev" 
          onClick={goToPrev}
          aria-label="Previous testimonial"
        >
          &lt;
        </button>

        <div className="testimonial-slide">
          <blockquote className="testimonial-quote">
            "{testimonials[currentIndex].quote}"
          </blockquote>
          <div className="testimonial-author">
            <strong>{testimonials[currentIndex].name}</strong>
            <span> (Angkatan SQI {testimonials[currentIndex].batch})</span>
          </div>
        </div>

        <button 
          className="carousel-button next" 
          onClick={goToNext}
          aria-label="Next testimonial"
        >
          &gt;
        </button>
      </div>

      <div className="carousel-indicators">
        {testimonials.map((_, index) => (
          <button
            key={index}
            className={`indicator ${index === currentIndex ? 'active' : ''}`}
            onClick={() => goToIndex(index)}
            aria-label={`Go to testimonial ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
};

TestimonialCarousel.propTypes = {
  testimonials: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
      batch: PropTypes.string.isRequired,
      quote: PropTypes.string.isRequired,
    })
  ).isRequired,
  interval: PropTypes.number,
};

export default TestimonialCarousel;
```

```css
/* TestimonialCarousel.css */
.testimonial-carousel {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
  position: relative;
}

.testimonial-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.testimonial-slide {
  flex: 1;
  padding: 0 2rem;
}

.testimonial-quote {
  font-size: 1.2rem;
  font-style: italic;
  margin-bottom: 1rem;
  color: #333;
}

.testimonial-author {
  font-size: 1rem;
  color: #555;
}

.carousel-button {
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #2c3e50;
  padding: 0.5rem;
  transition: color 0.3s;
}

.carousel-button:hover {
  color: #3498db;
}

.carousel-indicators {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
}

.indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #bdc3c7;
  border: none;
  cursor: pointer;
  padding: 0;
  transition: background-color 0.3s;
}

.indicator.active {
  background-color: #3498db;
}

.indicator:hover:not(.active) {
  background-color: #7f8c8d;
}
```

```jsx
// Example usage in App.js
import React from 'react';
import TestimonialCarousel from './TestimonialCarousel';

const App = () => {
  const testimonials = [
    {
      name: "Fulan",
      batch: "2018",
      quote: "SQI memberikan pemahaman yang mendalam tentang Al-Quran. Pengajarannya sangat berkualitas dan menyentuh hati."
    },
    {
      name: "Fulanah",
      batch: "2022",
      quote: "Pengalaman belajar di SQI mengubah hidup saya. Saya sekarang bisa membaca Al-Quran dengan tartil dan memahami maknanya."
    },
    {
      name: "Ali",
      batch: "2020",
      quote: "Metode pembelajaran SQI sangat efektif. Dalam waktu singkat, saya bisa menghafal beberapa juz dengan mutqin."
    }
  ];

  return (
    <div className="App">
      <h1>Testimoni Alumni Sekolah Quran Indonesia</h1>
      <TestimonialCarousel testimonials={testimonials} interval={7000} />
    </div>
  );
};

export default App;
```
