"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Create a Webflow-compatible scroll progress indicator that uses SVG and includes a "Back to Top" button, as detailed on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_44581a85514e841d
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Scroll Progress Indicator with Back to Top Button**
=====================================================

### HTML
```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scroll Progress Indicator</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="progress-container">
        <svg class="progress-svg" viewBox="0 0 100 10">
            <rect class="progress-bar" x="0" y="0" width="0" height="10" fill="#333" />
        </svg>
    </div>
    <button class="back-to-top" aria-label="Back to top">
        <svg viewBox="0 0 20 20">
            <path d="M10 18l-6-6 6-6 1.41 1.41L9.83 10h6.34l-4.58 4.59L10 18z" fill="#333" />
        </svg>
    </button>

    <script src="script.js"></script>
</body>
</html>
```

### CSS (in styles.css file)
```css
/* styles.css */

.progress-container {
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

.progress-bar {
    transition: width 0.2s ease-in-out;
}

.back-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #fff;
    border: none;
    padding: 10px;
    cursor: pointer;
    z-index: 1000;
}

.back-to-top svg {
    width: 20px;
    height: 20px;
}
```

### JavaScript (in script.js file)
```javascript
// script.js

class ScrollProgressIndicator {
    constructor() {
        this.progressBar = document.querySelector('.progress-bar');
        this.backToTopButton = document.querySelector('.back-to-top');
        this.progressContainer = document.querySelector('.progress-container');

        this.handleScroll = this.handleScroll.bind(this);
        this.handleBackToTopClick = this.handleBackToTopClick.bind(this);

        window.addEventListener('scroll', this.handleScroll);
        this.backToTopButton.addEventListener('click', this.handleBackToTopClick);
    }

    handleScroll() {
        const scrollPosition = window.scrollY;
        const documentHeight = document.body.offsetHeight;
        const windowHeight = window.innerHeight;
        const progress = (scrollPosition / (documentHeight - windowHeight)) * 100;

        this.progressBar.setAttribute('width', `${progress}%`);

        if (progress > 50) {
            this.backToTopButton.classList.add('visible');
        } else {
            this.backToTopButton.classList.remove('visible');
        }
    }

    handleBackToTopClick() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    destroy() {
        window.removeEventListener('scroll', this.handleScroll);
        this.backToTopButton.removeEventListener('click', this.handleBackToTopClick);
    }
}

const scrollProgressIndicator = new ScrollProgressIndicator();
```
