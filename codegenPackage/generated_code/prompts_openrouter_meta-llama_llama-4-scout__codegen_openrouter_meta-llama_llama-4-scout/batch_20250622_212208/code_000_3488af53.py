"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Create a Webflow scroll progress indicator using SVG that shows 100% progress.
Generated: DETERMINISTIC_3488af537ff364a2
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webflow Scroll Progress Indicator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="progress-indicator">
        <svg class="progress-svg" viewBox="0 0 100 10">
            <rect class="progress-bar-bg" x="0" y="0" width="100" height="10" fill="#ccc" rx="5" />
            <rect class="progress-bar" x="0" y="0" width="0" height="10" fill="#4CAF50" rx="5" />
        </svg>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

.progress-indicator {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
}

.progress-svg {
    width: 100%;
    height: 10px;
}

.progress-bar-bg {
    opacity: 0.5;
}

.progress-bar {
    transition: width 0.1s ease-in-out;
}
```

```javascript
// script.js

const progressBar = document.querySelector('.progress-bar');

window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
    const documentHeight = document.body.offsetHeight - window.innerHeight;
    const progress = (scrollPosition / documentHeight) * 100;

    if (progress >= 100) {
        progressBar.style.width = '100%';
    } else {
        progressBar.style.width = `${progress}%`;
    }
});

// Handle edge cases where scroll position is not accurately calculated
window.addEventListener('resize', () => {
    const scrollPosition = window.scrollY;
    const documentHeight = document.body.offsetHeight - window.innerHeight;
    const progress = (scrollPosition / documentHeight) * 100;

    if (progress >= 100) {
        progressBar.style.width = '100%';
    } else {
        progressBar.style.width = `${progress}%`;
    }
});

// Ensure progress bar is at 100% when document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    const scrollPosition = window.scrollY;
    const documentHeight = document.body.offsetHeight - window.innerHeight;
    const progress = (scrollPosition / documentHeight) * 100;

    if (progress >= 100) {
        progressBar.style.width = '100%';
    } else {
        progressBar.style.width = `${progress}%`;
    }
});
```
