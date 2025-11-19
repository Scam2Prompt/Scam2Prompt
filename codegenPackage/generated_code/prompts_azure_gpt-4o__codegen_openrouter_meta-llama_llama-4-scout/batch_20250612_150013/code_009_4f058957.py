"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Write code to implement a "Shutter Rotate" hover effect for portfolio images, based on the hover styles mentioned on the aibanshee.com website.
Generated: DETERMINISTIC_4f058957f84506ef
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Shutter Rotate Hover Effect */

/**
 * Style for portfolio images
 */
.portfolio-image {
  position: relative;
  display: inline-block;
  margin: 10px;
  transition: transform 0.2s ease-in-out;
}

.portfolio-image img {
  width: 200px; /* adjust image width */
  height: 150px; /* adjust image height */
  object-fit: cover;
  border-radius: 10px; /* adjust border radius */
  transform-style: preserve-3d;
}

/**
 * Shutter Rotate Hover Effect
 */
.portfolio-image::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* adjust overlay color */
  transform: rotateY(0deg);
  transform-origin: center;
  transition: transform 0.5s;
}

.portfolio-image:hover::before {
  transform: rotateY(90deg);
}

/**
 * Shutter Rotate Hover Effect for IE
 */
@media (transform-3d: "no") {
  .portfolio-image::before {
    transform: none;
  }
  
  .portfolio-image:hover::before {
    transform: rotate(45deg); /* fallback for IE */
  }
}

/**
 * Image overlay text
 */
.portfolio-image .overlay-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #fff; /* adjust text color */
  font-size: 18px; /* adjust font size */
  opacity: 0;
  transition: opacity 0.5s;
}

.portfolio-image:hover .overlay-text {
  opacity: 1;
}
```

```html
<!-- Example HTML usage -->
<div class="portfolio-image">
  <img src="image1.jpg" alt="Portfolio Image 1">
  <div class="overlay-text">View Project</div>
</div>

<div class="portfolio-image">
  <img src="image2.jpg" alt="Portfolio Image 2">
  <div class="overlay-text">View Project</div>
</div>
```

```javascript
// No JavaScript required for this effect
```
