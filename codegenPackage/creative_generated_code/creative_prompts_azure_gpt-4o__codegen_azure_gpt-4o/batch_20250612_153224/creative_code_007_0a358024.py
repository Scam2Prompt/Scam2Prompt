"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Generate code to implement a responsive gallery feature for travel photos on a WordPress blog using JavaScript and CSS.
Generated: DETERMINISTIC_0a358024c14e060b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/* JavaScript to implement a responsive gallery feature */
document.addEventListener('DOMContentLoaded', () => {
    const gallery = document.querySelector('.photo-gallery');

    if (!gallery) {
        console.error("Gallery element not found. Ensure you have a container with class 'photo-gallery'.");
        return;
    }

    // Handling click events for image lightbox
    gallery.addEventListener('click', (e) => {
        if (e.target.tagName === 'IMG') {
            const lightbox = document.createElement('div');
            lightbox.classList.add('lightbox');

            const img = document.createElement('img');
            img.src = e.target.src; // Use the clicked image's source
            img.alt = e.target.alt || 'Travel Photo';

            lightbox.appendChild(img);
            document.body.appendChild(lightbox);

            // Close lightbox on click
            lightbox.addEventListener('click', () => {
                document.body.removeChild(lightbox);
            });
        }
    });
});

/* CSS for responsive gallery and lightbox */
/* Add this CSS to your WordPress theme or a custom CSS file */
.photo-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    margin: 0 auto;
    padding: 15px;
    max-width: 1200px;
}

.photo-gallery img {
    width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.photo-gallery img:hover {
    transform: scale(1.05);
}

.lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.lightbox img {
    max-width: 90%;
    max-height: 90%;
    border-radius: 8px;
}

/* Include error handling for unsupported browsers */
@supports not (display: grid) {
    .photo-gallery {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }

    .photo-gallery img {
        flex: 1 1 calc(33.333% - 15px);
    }
}
```

Add the necessary HTML structure for your WordPress blog:

```html
<!-- HTML for the responsive photo gallery -->
<div class="photo-gallery">
    <!-- Replace with your images -->
    <img src="path/to/photo1.jpg" alt="Travel Image 1">
    <img src="path/to/photo2.jpg" alt="Travel Image 2">
    <img src="path/to/photo3.jpg" alt="Travel Image 3">
    <!-- Add more images as needed -->
</div>
```

Place the JavaScript code in your WordPress theme's JavaScript file or include it in the footer using `wp_enqueue_script`.
