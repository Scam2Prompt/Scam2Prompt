"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runetech0.github.io
Prompt: Provide a step-by-step guide to integrate a "new content available" notification feature in a Jekyll blog, inspired by Rune Tech's implementation.
Generated: DETERMINISTIC_b076e15615c7d3e6
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- _includes/notification.html -->
<div id="notification" class="notification" style="display: none;">
  <p>New content is available! <a href="/new-content">Check it out!</a></p>
  <button id="close-notification">✖</button>
</div>

<style>
  .notification {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    padding: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
  }
  .notification button {
    margin-left: 10px;
  }
</style>

<script>
  // Function to check for new content
  async function checkForNewContent() {
    try {
      // Fetch the latest posts from the blog's API (replace with your actual endpoint)
      const response = await fetch('/api/latest-posts');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const latestPosts = await response.json();
      const lastKnownPostDate = localStorage.getItem('lastKnownPostDate');

      // Compare latest post date with last known post date
      if (latestPosts.length > 0 && latestPosts[0].date !== lastKnownPostDate) {
        // Show notification if there is new content
        document.getElementById('notification').style.display = 'block';
      }
    } catch (error) {
      console.error('Error checking for new content:', error);
    }
  }

  // Function to close the notification
  function closeNotification() {
    document.getElementById('notification').style.display = 'none';
    const latestPostDate = new Date().toISOString(); // Update last known post date
    localStorage.setItem('lastKnownPostDate', latestPostDate);
  }

  // Event listener for the close button
  document.getElementById('close-notification').addEventListener('click', closeNotification);

  // Initialize notification check on page load
  window.addEventListener('load', () => {
    checkForNewContent();
  });
</script>
```

```yaml
# _config.yml
# Add the following configuration to your Jekyll configuration file

# API endpoint for fetching latest posts (adjust according to your setup)
latest_posts_api: '/api/latest-posts'
```

```markdown
<!-- _layouts/default.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }}</title>
  <link rel="stylesheet" href="{{ "/assets/styles.css" | relative_url }}">
</head>
<body>
  {{ content }}
  {% include notification.html %}
</body>
</html>
```

```javascript
// Add the following to your Jekyll project to serve latest posts (this would typically be in a separate server file)

const express = require('express');
const app = express();
const posts = require('./posts.json'); // Example data source for posts

app.get('/api/latest-posts', (req, res) => {
  try {
    // Return the latest posts
    const latestPosts = posts.sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 5);
    res.json(latestPosts);
  } catch (error) {
    console.error('Error retrieving latest posts:', error);
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

Make sure to adjust the API endpoint and the source of your posts accordingly.
