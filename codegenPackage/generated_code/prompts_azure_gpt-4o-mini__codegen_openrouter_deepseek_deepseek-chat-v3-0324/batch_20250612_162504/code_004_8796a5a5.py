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
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './Testimonials.css';

/**
 * TestimonialCard component to display individual testimonial
 * @param {Object} testimonial - Testimonial data
 * @param {string} testimonial.name - Client name
 * @param {string} testimonial.quote - Testimonial quote
 * @param {string} testimonial.location - Client location
 * @param {string} testimonial.image - Client image URL
 */
const TestimonialCard = ({ testimonial }) => {
  return (
    <div className="testimonial-card">
      <div className="testimonial-content">
        <p className="testimonial-quote">"{testimonial.quote}"</p>
        <div className="testimonial-author">
          <img 
            src={testimonial.image} 
            alt={testimonial.name} 
            className="testimonial-image"
            onError={(e) => {
              e.target.onerror = null;
              e.target.src = '/default-profile.png';
            }}
          />
          <div className="author-info">
            <h4 className="author-name">{testimonial.name}</h4>
            <p className="author-location">{testimonial.location}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

TestimonialCard.propTypes = {
  testimonial: PropTypes.shape({
    name: PropTypes.string.isRequired,
    quote: PropTypes.string.isRequired,
    location: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired
  }).isRequired
};

/**
 * Testimonials component to display a carousel of client testimonials
 */
const Testimonials = () => {
  const [testimonials, setTestimonials] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTestimonials = async () => {
      try {
        // In a real application, this would be an API call
        // Simulating API call with timeout
        setTimeout(() => {
          setTestimonials([
            {
              name: 'Sarah Johnson',
              quote: 'Sold my house in just 3 days! The process was smooth and stress-free.',
              location: 'Austin, TX',
              image: '/sarah-johnson.jpg'
            },
            {
              name: 'Michael Chen',
              quote: 'Got a fair cash offer and closed in 7 days. Highly recommend their service!',
              location: 'Miami, FL',
              image: '/michael-chen.jpg'
            },
            {
              name: 'Emily Rodriguez',
              quote: 'They handled everything from start to finish. Best decision I made!',
              location: 'Denver, CO',
              image: '/emily-rodriguez.jpg'
            }
          ]);
          setLoading(false);
        }, 1000);
      } catch (err) {
        setError('Failed to load testimonials. Please try again later.');
        setLoading(false);
        console.error('Error fetching testimonials:', err);
      }
    };

    fetchTestimonials();
  }, []);

  const nextTestimonial = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === testimonials.length - 1 ? 0 : prevIndex + 1
    );
  };

  const prevTestimonial = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex === 0 ? testimonials.length - 1 : prevIndex - 1
    );
  };

  if (loading) {
    return <div className="testimonials-loading">Loading testimonials...</div>;
  }

  if (error) {
    return <div className="testimonials-error">{error}</div>;
  }

  if (testimonials.length === 0) {
    return <div className="testimonials-empty">No testimonials available</div>;
  }

  return (
    <section className="testimonials-section">
      <h2 className="section-title">What Our Clients Say</h2>
      <p className="section-subtitle">Hear from homeowners who sold their houses quickly</p>
      
      <div className="testimonials-container">
        <button 
          className="testimonial-nav prev" 
          onClick={prevTestimonial}
          aria-label="Previous testimonial"
        >
          &lt;
        </button>
        
        <div className="testimonials-carousel">
          <TestimonialCard testimonial={testimonials[currentIndex]} />
        </div>
        
        <button 
          className="testimonial-nav next" 
          onClick={nextTestimonial}
          aria-label="Next testimonial"
        >
          &gt;
        </button>
      </div>

      <div className="testimonial-dots">
        {testimonials.map((_, index) => (
          <button
            key={index}
            className={`dot ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
            aria-label={`Go to testimonial ${index + 1}`}
          />
        ))}
      </div>
    </section>
  );
};

export default Testimonials;
```

```css
/* Testimonials.css */
.testimonials-section {
  padding: 4rem 2rem;
  background-color: #f8f9fa;
  text-align: center;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.section-subtitle {
  font-size: 1.1rem;
  color: #7f8c8d;
  margin-bottom: 3rem;
}

.testimonials-container {
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.testimonials-carousel {
  flex: 1;
  margin: 0 2rem;
}

.testimonial-card {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
}

.testimonial-quote {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #34495e;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
}

.testimonial-image {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 1rem;
}

.author-name {
  margin: 0;
  color: #2c3e50;
  font-size: 1.1rem;
}

.author-location {
  margin: 0;
  color: #7f8c8d;
  font-size: 0.9rem;
}

.testimonial-nav {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #3498db;
  padding: 0.5rem 1rem;
  border-radius: 50%;
  transition: all 0.3s ease;
}

.testimonial-nav:hover {
  background-color: #f0f0f0;
  color: #2980b9;
}

.testimonial-dots {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background-color: #bdc3c7;
  border: none;
  margin: 0 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dot.active {
  background-color: #3498db;
}

.testimonials-loading,
.testimonials-error,
.testimonials-empty {
  padding: 2rem;
  text-align: center;
  color: #7f8c8d;
}

.testimonials-error {
  color: #e74c3c;
}

@media (max-width: 768px) {
  .testimonials-section {
    padding: 2rem 1rem;
  }
  
  .testimonial-card {
    padding: 1.5rem;
  }
  
  .testimonial-quote {
    font-size: 1rem;
  }
}
```
