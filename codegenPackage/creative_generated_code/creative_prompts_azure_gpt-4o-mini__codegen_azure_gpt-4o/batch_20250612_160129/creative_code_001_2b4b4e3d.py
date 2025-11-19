"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: What JavaScript code can I use to enhance the Uniswap interface with a smooth scroll-to-top functionality?
Generated: DETERMINISTIC_2b4b4e3dcc9bdf17
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Smooth Scroll-to-Top Functionality for Uniswap Interface

// Ensure the DOM is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', () => {
    // Create a "Scroll to Top" button element
    const scrollToTopButton = document.createElement('button');
    
    // Apply styles to the button for visibility and positioning
    scrollToTopButton.innerText = '↑'; // Unicode arrow pointing up
    scrollToTopButton.style.position = 'fixed';
    scrollToTopButton.style.bottom = '20px';
    scrollToTopButton.style.right = '20px';
    scrollToTopButton.style.padding = '10px 15px';
    scrollToTopButton.style.backgroundColor = '#5c67f2'; // Matches Uniswap branding
    scrollToTopButton.style.color = '#fff';
    scrollToTopButton.style.border = 'none';
    scrollToTopButton.style.borderRadius = '50%';
    scrollToTopButton.style.cursor = 'pointer';
    scrollToTopButton.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    scrollToTopButton.style.display = 'none'; // Initially hidden
    
    // Add the button to the body
    document.body.appendChild(scrollToTopButton);

    // Scroll event listener to toggle button visibility
    window.addEventListener('scroll', () => {
        // Show the button only if the user scrolls down more than 300px
        if (window.scrollY > 300) {
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    // Click event listener for smooth scrolling
    scrollToTopButton.addEventListener('click', () => {
        // Smoothly scroll back to the top of the page
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Error handling: Ensure smooth scrolling is supported
    if (!('scrollBehavior' in document.documentElement.style)) {
        console.warn('Smooth scroll behavior is not supported by this browser.');
        // Fallback: Implement instant scrolling
        scrollToTopButton.addEventListener('click', () => {
            window.scrollTo(0, 0);
        });
    }
});
```
