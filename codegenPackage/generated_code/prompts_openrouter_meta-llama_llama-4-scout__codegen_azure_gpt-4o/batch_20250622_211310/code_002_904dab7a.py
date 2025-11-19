"""
Generated Code Metadata:
========================
Original URL: https://immediatebyte.org
Prompt: Generate code to create a clickable image with a beautiful hover effect and an active title link for a blog post item, as seen in the PRESTIGE-DATTES template.
Generated: DETERMINISTIC_904dab7ab4a30c7d
Batch ID: 20250622_211310
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/blog-post": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog Post Item</title>
  <style>
    /* Container for the blog post item */
    .blog-post {
      position: relative;
      width: 300px;
      margin: 20px auto;
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    /* Hover effect for the container */
    .blog-post:hover {
      transform: translateY(-5px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }

    /* Image styling */
    .blog-post img {
      width: 100%;
      height: auto;
      display: block;
    }

    /* Title link styling */
    .blog-post-title {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(0, 0, 0, 0.7);
      color: #fff;
      font-size: 18px;
      font-weight: bold;
      text-align: center;
      padding: 10px;
      text-decoration: none;
      transition: background 0.3s ease, color 0.3s ease;
    }

    /* Hover effect for the title link */
    .blog-post-title:hover {
      background: rgba(255, 255, 255, 0.9);
      color: #333;
    }
  </style>
</head>
<body>
  <!-- Blog post item -->
  <div class="blog-post">
    <!-- Clickable image -->
    <a href="https://example.com/blog-post" target="_blank">
      <img src="https://via.placeholder.com/300x200" alt="Blog Post Image">
    </a>
    <!-- Active title link -->
    <a href="https://example.com/blog-post" target="_blank" class="blog-post-title">
      Blog Post Title
    </a>
  </div>
</body>
</html>
```
