"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Write a JavaScript function for optimizing website performance, inspired by the programming tips shared on https://a2ip.ru.
Generated: DETERMINISTIC_8e205b6542892d51
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Optimizes website performance by performing several tasks:
 * 1. Minifies CSS and JS files.
 * 2. Compresses images.
 * 3. Implements lazy loading for images.
 * 4. Caches resources for better loading speed.
 */
class PerformanceOptimizer {
    constructor() {
        this.imageSelector = 'img.lazyload'; // Selector for images to lazy load
    }

    /**
     * Minifies a given string of JavaScript code.
     * @param {string} jsCode - The JavaScript code to minify.
     * @returns {string} - Minified JavaScript code.
     */
    minifyJS(jsCode) {
        try {
            return jsCode.replace(/\s+/g, ' ').trim(); // Simple minification
        } catch (error) {
            console.error('Error minifying JS:', error);
            return jsCode; // Return original on error
        }
    }

    /**
     * Minifies a given string of CSS code.
     * @param {string} cssCode - The CSS code to minify.
     * @returns {string} - Minified CSS code.
     */
    minifyCSS(cssCode) {
        try {
            return cssCode.replace(/\s+/g, ' ').trim(); // Simple minification
        } catch (error) {
            console.error('Error minifying CSS:', error);
            return cssCode; // Return original on error
        }
    }

    /**
     * Compresses images on the page using the specified selector.
     * @param {string} selector - The selector for images to compress.
     */
    compressImages(selector) {
        const images = document.querySelectorAll(selector);
        images.forEach((img) => {
            // Dummy compression simulation (actual implementation would require a library)
            img.src = img.src.replace(/(.*)\.(jpg|jpeg|png|gif)/, '$1-compressed.$2');
        });
    }

    /**
     * Implements lazy loading for images.
     */
    lazyLoadImages() {
        const images = document.querySelectorAll(this.imageSelector);
        const options = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1,
        };

        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src; // Set the real image source
                    img.classList.remove('lazyload');
                    observer.unobserve(img);
                }
            });
        }, options);

        images.forEach((img) => {
            imageObserver.observe(img);
        });
    }

    /**
     * Caches resources for better loading speed.
     * This is a basic implementation that utilizes the Cache API.
     */
    cacheResources() {
        if ('caches' in window) {
            caches.open('site-cache-v1').then((cache) => {
                cache.addAll([
                    '/', // Cache root
                    '/styles.css', // Cache CSS files
                    '/script.js', // Cache JS files
                    // Add additional resources as needed
                ]).catch((error) => {
                    console.error('Error caching resources:', error);
                });
            });
        }
    }

    /**
     * Main function to execute all performance optimization tasks.
     */
    optimize() {
        this.lazyLoadImages();
        this.cacheResources();
        // Provide the minified versions of your CSS and JS files
        // Example usage:
        const minifiedJS = this.minifyJS('function test() { console.log("test"); }');
        const minifiedCSS = this.minifyCSS('body { margin: 0; }');
        console.log('Minified JS:', minifiedJS);
        console.log('Minified CSS:', minifiedCSS);
    }
}

// Usage
const optimizer = new PerformanceOptimizer();
optimizer.optimize();
```
