"""
Generated Code Metadata:
========================
Original URL: https://immediatebyte.org
Prompt: Generate code to create a clickable image with a beautiful hover effect and an active title link for a blog post item, as seen in the PRESTIGE-DATTES template.
Generated: DETERMINISTIC_904dab7ab4a30c7d
Batch ID: 20250622_211310
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image.jpg": {
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
<!-- 
  Blog Post Item Component
  =========================
  A clickable image with a beautiful hover effect and an active title link.
-->

<div class="blog-post-item">
  <a href="#" class="image-link">
    <img 
      src="https://example.com/image.jpg" 
      alt="Blog Post Image" 
      class="image"
    />
    <div class="hover-overlay">
      <div class="hover-content">
        <i class="fas fa-plus"></i>
      </div>
    </div>
  </a>
  <a href="#" class="title-link">
    <h2 class="title">Blog Post Title</h2>
  </a>
</div>
```

```css
/* 
  Blog Post Item Styles
  =====================
*/

.blog-post-item {
  position: relative;
  margin-bottom: 20px;
}

.image-link {
  position: relative;
  display: block;
}

.image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  transition: transform 0.2s ease-in-out;
}

.hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
  border-radius: 10px;
}

.hover-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #fff;
  font-size: 24px;
}

.image-link:hover .image {
  transform: scale(1.05);
}

.image-link:hover .hover-overlay {
  opacity: 1;
}

.title-link {
  display: block;
  margin-top: 10px;
  text-decoration: none;
  color: #333;
}

.title-link:hover {
  color: #666;
}

.title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}
```

```javascript
// No JavaScript required for this component
```
