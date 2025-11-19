"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Design a JavaScript function that allows users to submit their own music reviews on a site like Square Bear's, including form validation and submission handling.
Generated: DETERMINISTIC_a566e097e299f0e8
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// musicReview.js

/**
 * Music Review Form Handler
 */

// Define a MusicReview class to encapsulate review data and behavior
class MusicReview {
  /**
   * Constructor for MusicReview
   * @param {string} title - Review title
   * @param {string} artist - Music artist
   * @param {string} album - Music album
   * @param {number} rating - Review rating (1-5)
   * @param {string} review - Review text
   */
  constructor(title, artist, album, rating, review) {
    this.title = title;
    this.artist = artist;
    this.album = album;
    this.rating = rating;
    this.review = review;
  }

  /**
   * Validate review data
   * @returns {boolean} True if valid, false otherwise
   */
  isValid() {
    return (
      this.title.trim() !== "" &&
      this.artist.trim() !== "" &&
      this.album.trim() !== "" &&
      this.rating >= 1 &&
      this.rating <= 5 &&
      this.review.trim() !== ""
    );
  }
}

// Define a function to handle form submission
function handleSubmitReview(event) {
  // Prevent default form submission behavior
  event.preventDefault();

  // Get form data
  const title = document.getElementById("title").value;
  const artist = document.getElementById("artist").value;
  const album = document.getElementById("album").value;
  const rating = parseInt(document.getElementById("rating").value);
  const review = document.getElementById("review").value;

  // Create a new MusicReview instance
  const musicReview = new MusicReview(title, artist, album, rating, review);

  // Validate review data
  if (!musicReview.isValid()) {
    // Display error message if invalid
    displayError("Please fill out all fields and ensure rating is between 1 and 5.");
    return;
  }

  // Submit review data to server
  submitReviewToServer(musicReview)
    .then((response) => {
      // Display success message on successful submission
      displaySuccess("Review submitted successfully!");
      // Clear form fields
      clearFormFields();
    })
    .catch((error) => {
      // Display error message on submission failure
      displayError("Error submitting review: " + error.message);
    });
}

// Define a function to submit review data to server
function submitReviewToServer(musicReview) {
  // Replace with actual server URL and API endpoint
  const url = "/api/music-reviews";

  // Use fetch API to send POST request
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: musicReview.title,
      artist: musicReview.artist,
      album: musicReview.album,
      rating: musicReview.rating,
      review: musicReview.review,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .catch((error) => {
      throw error;
    });
}

// Define a function to display error message
function displayError(message) {
  const errorElement = document.getElementById("error-message");
  errorElement.textContent = message;
  errorElement.style.display = "block";
}

// Define a function to display success message
function displaySuccess(message) {
  const successElement = document.getElementById("success-message");
  successElement.textContent = message;
  successElement.style.display = "block";
}

// Define a function to clear form fields
function clearFormFields() {
  document.getElementById("title").value = "";
  document.getElementById("artist").value = "";
  document.getElementById("album").value = "";
  document.getElementById("rating").value = "";
  document.getElementById("review").value = "";
}

// Add event listener to form submission
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("music-review-form");
  form.addEventListener("submit", handleSubmitReview);
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Music Review Form</title>
  <style>
    /* Add some basic styling */
    form {
      max-width: 500px;
      margin: 40px auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    label {
      display: block;
      margin-bottom: 10px;
    }

    input, textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
    }

    #error-message, #success-message {
      color: #f00;
      font-weight: bold;
      margin-bottom: 10px;
    }

    #success-message {
      color: #0f0;
    }
  </style>
</head>
<body>
  <form id="music-review-form">
    <h2>Submit a Music Review</h2>
    <label for="title">Title:</label>
    <input type="text" id="title" name="title">

    <label for="artist">Artist:</label>
    <input type="text" id="artist" name="artist">

    <label for="album">Album:</label>
    <input type="text" id="album" name="album">

    <label for="rating">Rating (1-5):</label>
    <input type="number" id="rating" name="rating" min="1" max="5">

    <label for="review">Review:</label>
    <textarea id="review" name="review"></textarea>

    <button type="submit">Submit Review</button>

    <p id="error-message" style="display: none;"></p>
    <p id="success-message" style="display: none;"></p>
  </form>

  <script src="musicReview.js"></script>
</body>
</html>
```
