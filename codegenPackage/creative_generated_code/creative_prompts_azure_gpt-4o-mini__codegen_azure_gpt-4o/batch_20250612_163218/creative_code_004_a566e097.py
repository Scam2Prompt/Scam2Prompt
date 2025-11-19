"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Design a JavaScript function that allows users to submit their own music reviews on a site like Square Bear's, including form validation and submission handling.
Generated: DETERMINISTIC_a566e097e299f0e8
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to handle music review submission
document.addEventListener('DOMContentLoaded', () => {
  // Reference to the form element
  const reviewForm = document.getElementById('reviewForm');

  // Attach the submit event listener
  reviewForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form from submitting traditionally

    // Get form data
    const name = document.getElementById('name').value.trim();
    const review = document.getElementById('review').value.trim();
    const rating = document.getElementById('rating').value;

    // Validate form fields
    if (!validateForm(name, review, rating)) {
      alert('Please fill out all fields correctly before submitting.');
      return;
    }

    // Create review object
    const reviewData = {
      name: name,
      review: review,
      rating: parseInt(rating),
      submittedAt: new Date().toISOString(),
    };

    // Simulate submission (replace this with actual server submission logic)
    submitReview(reviewData)
      .then(() => {
        alert('Thank you for your review!');
        reviewForm.reset(); // Reset the form after successful submission
      })
      .catch((error) => {
        console.error('Error submitting review:', error);
        alert('Something went wrong. Please try again later.');
      });
  });
});

/**
 * Validates the form inputs to ensure they meet criteria.
 * @param {string} name - The name entered by the user.
 * @param {string} review - The review text entered by the user.
 * @param {string} rating - The rating selected by the user.
 * @returns {boolean} True if all fields are valid, false otherwise.
 */
function validateForm(name, review, rating) {
  // Check name is not empty and has at least 2 characters
  if (name.length < 2) return false;

  // Check review is not empty and has at least 10 characters
  if (review.length < 10) return false;

  // Check rating is between 1 and 5
  const parsedRating = parseInt(rating);
  if (isNaN(parsedRating) || parsedRating < 1 || parsedRating > 5) return false;

  return true;
}

/**
 * Simulates review submission to a server.
 * Replace this function with actual API call logic when backend is ready.
 * @param {object} reviewData - The review object containing user input.
 * @returns {Promise} A promise simulating server response.
 */
function submitReview(reviewData) {
  return new Promise((resolve, reject) => {
    // Simulate a delay
    setTimeout(() => {
      // Simulate successful submission
      resolve();
    }, 1000);

    // Uncomment and modify below to simulate an error
    // reject(new Error('Simulated server error'));
  });
}
```

### HTML Structure (To integrate with the above code):

```html
<form id="reviewForm">
  <label for="name">Your Name:</label>
  <input type="text" id="name" name="name" required>
  
  <label for="review">Your Review:</label>
  <textarea id="review" name="review" rows="4" required></textarea>
  
  <label for="rating">Rating (1 to 5):</label>
  <select id="rating" name="rating" required>
    <option value="" disabled selected>Select Rating</option>
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
    <option value="5">5</option>
  </select>
  
  <button type="submit">Submit Review</button>
</form>
```

### Notes:
- Add the HTML structure to your webpage.
- The JavaScript code assumes the form fields have the IDs `name`, `review`, and `rating`.
