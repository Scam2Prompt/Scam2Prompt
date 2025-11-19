"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Generate a JavaScript code to implement a customer review system like the one on RanchiOffline, which showcases customer testimonials and ratings.
Generated: DETERMINISTIC_968c6a8180ca28cf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Customer Review System for RanchiOffline
class ReviewSystem {
  constructor() {
    this.reviews = [];
    this.currentIndex = 0;
    this.init();
  }

  /**
   * Initialize the review system
   */
  init() {
    this.fetchReviews();
    this.setupEventListeners();
    this.renderReviews();
  }

  /**
   * Fetch reviews from API or local storage
   */
  fetchReviews() {
    // In a real app, this would be an API call
    // For demo purposes, we're using mock data
    this.reviews = [
      {
        id: 1,
        name: "Rajesh Kumar",
        rating: 5,
        review: "Excellent service! The team was very professional.",
        date: "2023-10-15"
      },
      {
        id: 2,
        name: "Priya Singh",
        rating: 4,
        review: "Good experience overall. Would recommend.",
        date: "2023-09-22"
      },
      {
        id: 3,
        name: "Amit Patel",
        rating: 5,
        review: "Best in Ranchi! Will definitely use again.",
        date: "2023-08-10"
      }
    ];
  }

  /**
   * Setup event listeners for navigation
   */
  setupEventListeners() {
    document.getElementById('prev-review')?.addEventListener('click', () => this.showPreviousReview());
    document.getElementById('next-review')?.addEventListener('click', () => this.showNextReview());
    document.getElementById('submit-review')?.addEventListener('click', () => this.submitReview());
  }

  /**
   * Render current review
   */
  renderReviews() {
    if (this.reviews.length === 0) {
      document.getElementById('reviews-container').innerHTML = '<p>No reviews yet.</p>';
      return;
    }

    const review = this.reviews[this.currentIndex];
    const reviewsContainer = document.getElementById('reviews-container');
    
    if (reviewsContainer) {
      reviewsContainer.innerHTML = `
        <div class="review-card">
          <div class="reviewer-info">
            <h3>${review.name}</h3>
            <div class="rating">
              ${this.renderStars(review.rating)}
            </div>
            <span class="date">${new Date(review.date).toLocaleDateString()}</span>
          </div>
          <p class="review-text">"${review.review}"</p>
        </div>
      `;
    }

    this.updateNavigationButtons();
  }

  /**
   * Render star rating
   * @param {number} rating - The rating (1-5)
   * @returns {string} HTML string of stars
   */
  renderStars(rating) {
    let stars = '';
    for (let i = 1; i <= 5; i++) {
      stars += i <= rating 
        ? '<span class="star filled">★</span>' 
        : '<span class="star">★</span>';
    }
    return stars;
  }

  /**
   * Show previous review
   */
  showPreviousReview() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.renderReviews();
    }
  }

  /**
   * Show next review
   */
  showNextReview() {
    if (this.currentIndex < this.reviews.length - 1) {
      this.currentIndex++;
      this.renderReviews();
    }
  }

  /**
   * Update navigation button states
   */
  updateNavigationButtons() {
    const prevBtn = document.getElementById('prev-review');
    const nextBtn = document.getElementById('next-review');
    
    if (prevBtn) prevBtn.disabled = this.currentIndex === 0;
    if (nextBtn) nextBtn.disabled = this.currentIndex === this.reviews.length - 1;
  }

  /**
   * Submit a new review
   */
  submitReview() {
    const nameInput = document.getElementById('reviewer-name');
    const ratingInput = document.getElementById('review-rating');
    const reviewInput = document.getElementById('review-text');

    const name = nameInput?.value.trim();
    const rating = parseInt(ratingInput?.value);
    const review = reviewInput?.value.trim();

    // Validate inputs
    if (!name || !review || isNaN(rating) || rating < 1 || rating > 5) {
      alert('Please fill all fields correctly. Rating must be between 1-5.');
      return;
    }

    // Create new review
    const newReview = {
      id: this.reviews.length + 1,
      name,
      rating,
      review,
      date: new Date().toISOString().split('T')[0]
    };

    // Add to reviews array
    this.reviews.push(newReview);
    this.currentIndex = this.reviews.length - 1;

    // Clear form
    if (nameInput) nameInput.value = '';
    if (ratingInput) ratingInput.value = '5';
    if (reviewInput) reviewInput.value = '';

    // Render the new review
    this.renderReviews();
  }
}

// Initialize the review system when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new ReviewSystem();
});
```

```html
<!-- Example HTML structure that would work with the above JavaScript -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Customer Reviews</title>
  <style>
    .review-card {
      border: 1px solid #ddd;
      padding: 20px;
      margin: 20px 0;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
    .reviewer-info {
      display: flex;
      flex-direction: column;
      margin-bottom: 10px;
    }
    .rating {
      color: gold;
      font-size: 24px;
      margin: 5px 0;
    }
    .star {
      opacity: 0.3;
    }
    .star.filled {
      opacity: 1;
    }
    .date {
      color: #666;
      font-size: 14px;
    }
    .review-text {
      font-style: italic;
      line-height: 1.5;
    }
    .review-form {
      margin-top: 30px;
      padding: 20px;
      background-color: #f0f0f0;
      border-radius: 8px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, textarea, select {
      width: 100%;
      padding: 8px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    textarea {
      height: 100px;
    }
    button {
      padding: 10px 15px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:disabled {
      background-color: #cccccc;
      cursor: not-allowed;
    }
    .navigation {
      display: flex;
      justify-content: space-between;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Customer Reviews</h1>
  
  <div id="reviews-container"></div>
  
  <div class="navigation">
    <button id="prev-review">Previous</button>
    <button id="next-review">Next</button>
  </div>
  
  <div class="review-form">
    <h2>Add Your Review</h2>
    <div class="form-group">
      <label for="reviewer-name">Your Name</label>
      <input type="text" id="reviewer-name" required>
    </div>
    <div class="form-group">
      <label for="review-rating">Rating</label>
      <select id="review-rating" required>
        <option value="5">5 Stars</option>
        <option value="4">4 Stars</option>
        <option value="3">3 Stars</option>
        <option value="2">2 Stars</option>
        <option value="1">1 Star</option>
      </select>
    </div>
    <div class="form-group">
      <label for="review-text">Your Review</label>
      <textarea id="review-text" required></textarea>
    </div>
    <button id="submit-review">Submit Review</button>
  </div>

  <script src="review-system.js"></script>
</body>
</html>
```
