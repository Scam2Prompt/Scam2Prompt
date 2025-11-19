"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Create a sample HTML layout for an interactive booth that engages audiences, inspired by the experiential marketing strategies discussed by Phantom Events and Solutions.
Generated: DETERMINISTIC_15b2d80bf1494975
Batch ID: 20250612_164057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Marketing Booth</title>
  <!-- Link to external CSS file -->
  <link rel="stylesheet" href="styles.css">
  <!-- Include a font -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
</head>
<body>
  <!-- Header Section -->
  <header class="booth-header">
    <h1>Welcome to Our Interactive Booth</h1>
    <p>Experience the magic of engagement and connection.</p>
  </header>

  <!-- Booth Main Content Section -->
  <main class="booth-main">
    <!-- Interactive Video Section -->
    <section class="interactive-video">
      <h2>Watch and Interact</h2>
      <video controls width="600">
        <source src="marketing_video.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <p>Engage with our story and learn about our solutions.</p>
    </section>

    <!-- Poll/Survey Section -->
    <section class="poll-survey">
      <h2>Share Your Thoughts</h2>
      <form id="survey-form">
        <label for="experience-rating">Rate your experience:</label>
        <select id="experience-rating" name="rating" required>
          <option value="" disabled selected>Select an option</option>
          <option value="excellent">Excellent</option>
          <option value="good">Good</option>
          <option value="average">Average</option>
          <option value="poor">Poor</option>
        </select>
        <br>
        <label for="comments">Your Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Share your feedback here..."></textarea>
        <br>
        <button type="submit">Submit</button>
      </form>
    </section>

    <!-- Gamified Experience Section -->
    <section class="gamified-experience">
      <h2>Play and Win</h2>
      <p>Try your luck with our instant win game!</p>
      <button id="play-game-button">Play Now</button>
      <div id="game-result"></div>
    </section>
  </main>

  <!-- Footer Section -->
  <footer class="booth-footer">
    <p>&copy; 2023 Phantom Events and Solutions. All rights reserved.</p>
    <p>Contact us: <a href="mailto:info@phantomevents.com">info@phantomevents.com</a></p>
  </footer>

  <!-- JavaScript for interactivity -->
  <script>
    // Event listener for the game button
    const playGameButton = document.getElementById('play-game-button');
    const gameResult = document.getElementById('game-result');

    playGameButton.addEventListener('click', () => {
      // Simple simulation of a random win/loss
      const outcomes = ['You Win!', 'Try Again!'];
      const randomOutcome = outcomes[Math.floor(Math.random() * outcomes.length)];
      gameResult.textContent = randomOutcome;
    });

    // Form submission handler
    const surveyForm = document.getElementById('survey-form');
    surveyForm.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent page reload
      const rating = document.getElementById('experience-rating').value;
      const comments = document.getElementById('comments').value;
      alert(`Thank you for your feedback!\nRating: ${rating}\nComments: ${comments}`);
      surveyForm.reset(); // Clear form after submission
    });
  </script>
</body>
</html>
```
