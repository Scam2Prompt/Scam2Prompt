"""
Generated Code Metadata:
========================
Original URL: https://1marbleclassic.com
Prompt: "Generate a customer testimonial collection system using a library like React or Angular, inspired by the testimonial section on 1Marble Classic's website."
Generated: DETERMINISTIC_c923d5fafd362747
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// TestimonialCollectionSystem.js - React Component for Testimonial Collection
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TestimonialCollectionSystem.css';

const TestimonialCollectionSystem = () => {
  const [testimonials, setTestimonials] = useState([]);
  const [newTestimonial, setNewTestimonial] = useState({
    name: '',
    role: '',
    company: '',
    content: '',
    rating: 5,
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch testimonials from API
  useEffect(() => {
    const fetchTestimonials = async () => {
      try {
        setIsLoading(true);
        const response = await axios.get('/api/testimonials');
        setTestimonials(response.data);
      } catch (err) {
        setError(err.message || 'Failed to fetch testimonials');
      } finally {
        setIsLoading(false);
      }
    };

    fetchTestimonials();
  }, []);

  // Handle form input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewTestimonial(prev => ({
      ...prev,
      [name]: value
    }));
  };

  // Handle rating change
  const handleRatingChange = (rating) => {
    setNewTestimonial(prev => ({
      ...prev,
      rating
    }));
  };

  // Submit new testimonial
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!newTestimonial.name || !newTestimonial.content) {
      setError('Name and testimonial content are required');
      return;
    }

    try {
      setIsLoading(true);
      const response = await axios.post('/api/testimonials', newTestimonial);
      setTestimonials([...testimonials, response.data]);
      setNewTestimonial({
        name: '',
        role: '',
        company: '',
        content: '',
        rating: 5,
      });
      setError(null);
    } catch (err) {
      setError(err.message || 'Failed to submit testimonial');
    } finally {
      setIsLoading(false);
    }
  };

  // Render star rating
  const renderStars = (rating) => {
    return [...Array(5)].map((_, i) => (
      <span 
        key={i} 
        className={`star ${i < rating ? 'filled' : ''}`}
        onClick={() => handleRatingChange(i + 1)}
      >
        ★
      </span>
    ));
  };

  return (
    <div className="testimonial-system">
      <h2>Customer Testimonials</h2>
      
      {error && <div className="error-message">{error}</div>}
      
      {/* Testimonial List */}
      <div className="testimonial-list">
        {isLoading ? (
          <div className="loading">Loading testimonials...</div>
        ) : testimonials.length > 0 ? (
          testimonials.map((testimonial) => (
            <div key={testimonial._id} className="testimonial-card">
              <div className="testimonial-header">
                <h3>{testimonial.name}</h3>
                <div className="testimonial-meta">
                  {testimonial.role && <span>{testimonial.role}</span>}
                  {testimonial.company && <span>, {testimonial.company}</span>}
                </div>
                <div className="testimonial-rating">
                  {renderStars(testimonial.rating)}
                </div>
              </div>
              <p className="testimonial-content">"{testimonial.content}"</p>
            </div>
          ))
        ) : (
          <div className="no-testimonials">No testimonials yet.</div>
        )}
      </div>

      {/* Add Testimonial Form */}
      <div className="add-testimonial">
        <h3>Share Your Experience</h3>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Name*</label>
            <input
              type="text"
              id="name"
              name="name"
              value={newTestimonial.name}
              onChange={handleInputChange}
              required
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="role">Role</label>
            <input
              type="text"
              id="role"
              name="role"
              value={newTestimonial.role}
              onChange={handleInputChange}
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="company">Company</label>
            <input
              type="text"
              id="company"
              name="company"
              value={newTestimonial.company}
              onChange={handleInputChange}
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="content">Testimonial*</label>
            <textarea
              id="content"
              name="content"
              value={newTestimonial.content}
              onChange={handleInputChange}
              required
            />
          </div>
          
          <div className="form-group">
            <label>Rating</label>
            <div className="rating-stars">
              {renderStars(newTestimonial.rating)}
            </div>
          </div>
          
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Submitting...' : 'Submit Testimonial'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default TestimonialCollectionSystem;
```

```css
/* TestimonialCollectionSystem.css */
.testimonial-system {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
}

.testimonial-system h2, .testimonial-system h3 {
  color: #333;
  margin-bottom: 1.5rem;
}

.error-message {
  color: #d32f2f;
  background-color: #fde7e7;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 4px;
}

.testimonial-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.testimonial-card {
  background: #fff;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.testimonial-header {
  margin-bottom: 1rem;
}

.testimonial-header h3 {
  margin: 0;
  color: #2c3e50;
}

.testimonial-meta {
  color: #7f8c8d;
  font-size: 0.9rem;
  margin: 0.5rem 0;
}

.testimonial-content {
  font-style: italic;
  color: #555;
  line-height: 1.6;
}

.testimonial-rating {
  margin: 0.5rem 0;
}

.star {
  color: #ccc;
  cursor: pointer;
  font-size: 1.2rem;
  margin-right: 0.2rem;
}

.star.filled {
  color: #f1c40f;
}

.add-testimonial {
  background: #f9f9f9;
  padding: 2rem;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #333;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group textarea {
  min-height: 120px;
  resize: vertical;
}

button {
  background: #3498db;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover {
  background: #2980b9;
}

button:disabled {
  background: #95a5a6;
  cursor: not-allowed;
}

.loading, .no-testimonials {
  text-align: center;
  padding: 2rem;
  color: #7f8c8d;
  grid-column: 1 / -1;
}

.rating-stars {
  display: flex;
  gap: 0.5rem;
}
```
