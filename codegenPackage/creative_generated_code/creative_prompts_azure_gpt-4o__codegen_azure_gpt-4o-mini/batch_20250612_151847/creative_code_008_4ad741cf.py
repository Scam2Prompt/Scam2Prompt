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

```javascript
// TestimonialCarousel.js
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './TestimonialCarousel.css'; // Importing the CSS for styling

/**
 * TestimonialCarousel component displays a carousel of testimonials.
 * It cycles through the testimonials every few seconds.
 * 
 * @param {Array} testimonials - An array of testimonial objects containing name, year, and message.
 */
const TestimonialCarousel = ({ testimonials }) => {
    const [currentIndex, setCurrentIndex] = useState(0);
    const [isPaused, setIsPaused] = useState(false);

    // Change testimonial every 5 seconds unless paused
    useEffect(() => {
        const interval = setInterval(() => {
            if (!isPaused) {
                setCurrentIndex((prevIndex) => 
                    (prevIndex + 1) % testimonials.length
                );
            }
        }, 5000);

        return () => clearInterval(interval); // Cleanup on unmount
    }, [isPaused, testimonials.length]);

    // Handle clicking the next button
    const handleNext = () => {
        setCurrentIndex((prevIndex) => 
            (prevIndex + 1) % testimonials.length
        );
    };

    // Handle clicking the previous button
    const handlePrev = () => {
        setCurrentIndex((prevIndex) => 
            (prevIndex - 1 + testimonials.length) % testimonials.length
        );
    };

    // Toggle pause state on mouse enter/leave
    const togglePause = () => {
        setIsPaused((prev) => !prev);
    };

    return (
        <div className="testimonial-carousel" onMouseEnter={togglePause} onMouseLeave={togglePause}>
            <div className="testimonial-item">
                <h3>{testimonials[currentIndex].name}</h3>
                <p className="year">{`(Angkatan SQI ${testimonials[currentIndex].year})`}</p>
                <p className="message">{testimonials[currentIndex].message}</p>
            </div>
            <button className="prev" onClick={handlePrev}>❮</button>
            <button className="next" onClick={handleNext}>❯</button>
        </div>
    );
};

// PropTypes for type-checking
TestimonialCarousel.propTypes = {
    testimonials: PropTypes.arrayOf(
        PropTypes.shape({
            name: PropTypes.string.isRequired,
            year: PropTypes.number.isRequired,
            message: PropTypes.string.isRequired
        })
    ).isRequired
};

export default TestimonialCarousel;
```

```css
/* TestimonialCarousel.css */
.testimonial-carousel {
    position: relative;
    width: 80%;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    text-align: center;
    background-color: #f9f9f9;
}

.testimonial-item {
    margin-bottom: 20px;
}

.prev, .next {
    cursor: pointer;
    padding: 10px;
    margin: 5px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.prev:hover, .next:hover {
    background-color: #0056b3;
}
```

```javascript
// App.js
import React from 'react';
import TestimonialCarousel from './TestimonialCarousel';

// Sample testimonials
const testimonials = [
    {
        name: "Fulan",
        year: 2018,
        message: "Sekolah Quran Indonesia changed my life! The teachings are profound."
    },
    {
        name: "Fulanah",
        year: 2022,
        message: "I gained so much knowledge and my love for the Quran has grown immensely!"
    }
];

const App = () => {
    return (
        <div className="App">
            <h1>Testimonials</h1>
            <TestimonialCarousel testimonials={testimonials} />
        </div>
    );
};

export default App;
``` 

This code provides a complete implementation of a testimonial carousel in React, along with necessary styling and type-checking.
