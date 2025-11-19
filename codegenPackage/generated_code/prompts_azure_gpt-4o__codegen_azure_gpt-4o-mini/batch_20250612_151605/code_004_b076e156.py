"""
Generated Code Metadata:
========================
Original URL: https://runetech0.github.io
Prompt: Provide a step-by-step guide to integrate a "new content available" notification feature in a Jekyll blog, inspired by Rune Tech's implementation.
Generated: DETERMINISTIC_b076e15615c7d3e6
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- _includes/notification.html -->
<div id="notification" style="display: none; position: fixed; bottom: 20px; right: 20px; background-color: #4CAF50; color: white; padding: 15px; border-radius: 5px; z-index: 1000;">
    New content is available! <a href="#" id="notification-link" style="color: white; text-decoration: underline;">Check it out!</a>
</div>

<script>
    // Function to show the notification
    function showNotification() {
        const notification = document.getElementById('notification');
        notification.style.display = 'block';

        // Automatically hide the notification after 5 seconds
        setTimeout(() => {
            notification.style.display = 'none';
        }, 5000);
    }

    // Function to check for new content
    async function checkForNewContent() {
        try {
            // Fetch the latest posts from the Jekyll API or a JSON file
            const response = await fetch('/path/to/latest-posts.json');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const latestPosts = await response.json();

            // Logic to determine if new content is available
            const currentPosts = [...document.querySelectorAll('.post')].map(post => post.dataset.postId);
            const newPosts = latestPosts.filter(post => !currentPosts.includes(post.id));

            // If new posts are found, show the notification
            if (newPosts.length > 0) {
                showNotification();
            }
        } catch (error) {
            console.error('Error checking for new content:', error);
        }
    }

    // Check for new content on page load
    document.addEventListener('DOMContentLoaded', () => {
        checkForNewContent();
    });
</script>
```

```yaml
# _config.yml
# Add a new configuration for the latest posts JSON file
latest_posts_json: "/path/to/latest-posts.json"
```

```html
<!-- In your layout file (e.g., default.html) -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }}</title>
    <link rel="stylesheet" href="/path/to/styles.css">
</head>
<body>
    {% include notification.html %}
    <main>
        {{ content }}
    </main>
</body>
</html>
```

```json
// latest-posts.json (example structure)
[
    { "id": "post-1", "title": "First Post", "url": "/first-post/" },
    { "id": "post-2", "title": "Second Post", "url": "/second-post/" }
]
```

```html
<!-- In your post files, ensure to add a data attribute for the post ID -->
<article class="post" data-post-id="post-1">
    <h2><a href="/first-post/">First Post</a></h2>
    <p>Content of the first post...</p>
</article>
<article class="post" data-post-id="post-2">
    <h2><a href="/second-post/">Second Post</a></h2>
    <p>Content of the second post...</p>
</article>
```

This code provides a complete implementation of a "new content available" notification feature for a Jekyll blog, following best practices and including error handling.
