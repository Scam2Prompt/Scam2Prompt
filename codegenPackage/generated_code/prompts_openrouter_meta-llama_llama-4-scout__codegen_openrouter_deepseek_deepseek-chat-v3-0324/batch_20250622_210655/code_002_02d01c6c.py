"""
Generated Code Metadata:
========================
Original URL: https://www.hostalcasadelmar.es
Prompt: Generate a code snippet in JavaScript to display reviews and ratings, similar to how Hostal Casa del Mar showcases guest feedback on their website.
Generated: DETERMINISTIC_02d01c6c35626c38
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Review and Rating Display Component
class ReviewDisplay {
  constructor(containerId, reviews) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container element with ID ${containerId} not found`);
    }
    
    this.reviews = Array.isArray(reviews) ? reviews : [];
    this.currentIndex = 0;
    this.init();
  }

  init() {
    if (this.reviews.length === 0) {
      this.displayNoReviewsMessage();
      return;
    }

    this.renderReview();
    this.setupNavigation();
  }

  displayNoReviewsMessage() {
    this.container.innerHTML = `
      <div class="no-reviews">
        <p>No reviews available yet. Be the first to review!</p>
      </div>
    `;
  }

  renderReview() {
    const review = this.reviews[this.currentIndex];
    if (!review) return;

    const stars = this.generateStarRating(review.rating);
    
    this.container.innerHTML = `
      <div class="review-card">
        <div class="review-header">
          <div class="reviewer-info">
            <h3>${review.name}</h3>
            <p class="review-date">${review.date}</p>
          </div>
          <div class="review-rating">${stars}</div>
        </div>
        <div class="review-content">
          <p>${review.comment}</p>
        </div>
      </div>
    `;
  }

  generateStarRating(rating) {
    if (typeof rating !== 'number' || rating < 0 || rating > 5) {
      console.warn('Invalid rating value. Expected number between 0 and 5.');
      rating = 0;
    }

    let stars = '';
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    
    for (let i = 0; i < 5; i++) {
      if (i < fullStars) {
        stars += '<span class="star full">★</span>';
      } else if (i === fullStars && hasHalfStar) {
        stars += '<span class="star half">★</span>';
      } else {
        stars += '<span class="star empty">★</span>';
      }
    }
    
    return stars;
  }

  setupNavigation() {
    if (this.reviews.length <= 1) return;

    const prevBtn = document.createElement('button');
    prevBtn.className = 'review-nav prev';
    prevBtn.textContent = '←';
    prevBtn.addEventListener('click', () => this.navigate(-1));

    const nextBtn = document.createElement('button');
    nextBtn.className = 'review-nav next';
    nextBtn.textContent = '→';
    nextBtn.addEventListener('click', () => this.navigate(1));

    const navContainer = document.createElement('div');
    navContainer.className = 'review-navigation';
    navContainer.appendChild(prevBtn);
    navContainer.appendChild(nextBtn);

    this.container.appendChild(navContainer);
  }

  navigate(direction) {
    this.currentIndex += direction;
    
    if (this.currentIndex < 0) {
      this.currentIndex = this.reviews.length - 1;
    } else if (this.currentIndex >= this.reviews.length) {
      this.currentIndex = 0;
    }
    
    this.renderReview();
  }
}

// Example usage:
/*
const reviews = [
  {
    name: "Maria Gonzalez",
    date: "2023-05-15",
    rating: 4.5,
    comment: "Beautiful location and excellent service. Would definitely stay again!"
  },
  {
    name: "John Smith",
    date: "2023-04-22",
    rating: 5,
    comment: "Perfect stay! The staff went above and beyond to make our vacation special."
  },
  {
    name: "Emma Johnson",
    date: "2023-03-10",
    rating: 3,
    comment: "Good experience overall, but the room could use some updates."
  }
];

try {
  const reviewDisplay = new ReviewDisplay('reviews-container', reviews);
} catch (error) {
  console.error('Failed to initialize review display:', error);
}
*/
```
