"""
Generated Code Metadata:
========================
Original URL: https://wahedabdelmajed.com
Prompt: "Design a simple CSS style for a 'Scroll to top' button that could be used on a blog with a similar layout to Dr. Wahed Abdelmajed's website."
Generated: DETERMINISTIC_423226fcb753f8e7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Scroll to Top Button Styles */

/* Container for the button */
.scroll-to-top {
  position: fixed; /* Keeps the button fixed on the screen */
  bottom: 20px; /* Distance from the bottom of the viewport */
  right: 20px; /* Distance from the right of the viewport */
  width: 50px; /* Width of the button */
  height: 50px; /* Height of the button */
  background-color: #007BFF; /* Button background color (blue) */
  color: #FFFFFF; /* Text/icon color (white) */
  border: none; /* Removes border */
  border-radius: 50%; /* Makes the button circular */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Adds a subtle shadow */
  cursor: pointer; /* Changes cursor to pointer on hover */
  display: flex; /* Enables flexbox for centering content */
  justify-content: center; /* Centers content horizontally */
  align-items: center; /* Centers content vertically */
  z-index: 1000; /* Ensures the button is above other elements */
  opacity: 0; /* Initially hidden */
  visibility: hidden; /* Prevents interaction when hidden */
  transition: opacity 0.3s ease, visibility 0.3s ease; /* Smooth transition for visibility */
}

/* Button becomes visible when scrolled down */
.scroll-to-top.show {
  opacity: 1; /* Makes the button visible */
  visibility: visible; /* Allows interaction */
}

/* Hover effect for the button */
.scroll-to-top:hover {
  background-color: #0056b3; /* Darker blue on hover */
}

/* Icon inside the button */
.scroll-to-top i {
  font-size: 24px; /* Icon size */
}

/* Example usage in HTML:
<button class="scroll-to-top" id="scrollToTopButton">
  <i class="fas fa-arrow-up"></i> <!-- Font Awesome icon -->
</button>
*/

/* JavaScript to toggle visibility based on scroll position:
document.addEventListener('scroll', () => {
  const scrollToTopButton = document.getElementById('scrollToTopButton');
  if (window.scrollY > 300) { // Show button after scrolling 300px
    scrollToTopButton.classList.add('show');
  } else {
    scrollToTopButton.classList.remove('show');
  }
});

scrollToTopButton.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' }); // Smooth scroll to top
});
*/
```
