"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: Create a JavaScript function that dynamically populates a webpage with testimonials and portfolio items from a paving block manufacturer, inspired by the content on Komando Block Cirebon.
Generated: DETERMINISTIC_cf2ed844a4823959
Batch ID: 20250612_161700
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/project1-image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/project1-image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/project2-image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/jane-doe.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/john-doe.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/project2-image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// testimonials.js

/**
 * Testimonial data model
 * @typedef {Object} Testimonial
 * @property {string} id - Unique identifier
 * @property {string} name - Customer name
 * @property {string} review - Testimonial review
 * @property {string} image - Customer image URL
 */

/**
 * Portfolio item data model
 * @typedef {Object} PortfolioItem
 * @property {string} id - Unique identifier
 * @property {string} title - Portfolio item title
 * @property {string} description - Portfolio item description
 * @property {string[]} images - Portfolio item image URLs
 */

/**
 * Dynamically populates a webpage with testimonials and portfolio items.
 * @param {Object} data - Data object containing testimonials and portfolio items
 * @param {Testimonial[]} data.testimonials - Array of testimonials
 * @param {PortfolioItem[]} data.portfolioItems - Array of portfolio items
 */
function populateWebpage(data) {
    try {
        // Check if data object is valid
        if (!data || !data.testimonials || !data.portfolioItems) {
            throw new Error('Invalid data object');
        }

        // Select HTML elements to populate
        const testimonialsContainer = document.getElementById('testimonials');
        const portfolioContainer = document.getElementById('portfolio');

        // Populate testimonials
        data.testimonials.forEach((testimonial) => {
            const testimonialHTML = `
                <div class="testimonial">
                    <img src="${testimonial.image}" alt="${testimonial.name}">
                    <p>${testimonial.review}</p>
                    <p>— ${testimonial.name}</p>
                </div>
            `;
            testimonialsContainer.insertAdjacentHTML('beforeend', testimonialHTML);
        });

        // Populate portfolio items
        data.portfolioItems.forEach((portfolioItem) => {
            const portfolioItemHTML = `
                <div class="portfolio-item">
                    <h2>${portfolioItem.title}</h2>
                    <p>${portfolioItem.description}</p>
                    <div class="portfolio-item-images">
                        ${portfolioItem.images.map((image) => `<img src="${image}">`).join('')}
                    </div>
                </div>
            `;
            portfolioContainer.insertAdjacentHTML('beforeend', portfolioItemHTML);
        });
    } catch (error) {
        console.error('Error populating webpage:', error);
    }
}

// Example usage:
const data = {
    testimonials: [
        {
            id: '1',
            name: 'John Doe',
            review: 'Komando Block Cirebon is the best!',
            image: 'https://example.com/john-doe.jpg',
        },
        {
            id: '2',
            name: 'Jane Doe',
            review: 'Their paving blocks are top-notch!',
            image: 'https://example.com/jane-doe.jpg',
        },
    ],
    portfolioItems: [
        {
            id: '1',
            title: 'Paving Block Project 1',
            description: 'This is a sample project',
            images: ['https://example.com/project1-image1.jpg', 'https://example.com/project1-image2.jpg'],
        },
        {
            id: '2',
            title: 'Paving Block Project 2',
            description: 'This is another sample project',
            images: ['https://example.com/project2-image1.jpg', 'https://example.com/project2-image2.jpg'],
        },
    ],
};

// Call the function when the DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    populateWebpage(data);
});
```
