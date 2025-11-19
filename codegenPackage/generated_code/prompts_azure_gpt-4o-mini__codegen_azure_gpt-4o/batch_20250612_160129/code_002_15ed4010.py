"""
Generated Code Metadata:
========================
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: Can you provide an example of using JavaScript to enable a scroll-to-top button in a decentralized exchange interface like Uniswap?
Generated: DETERMINISTIC_15ed4010211efe49
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Scroll-to-Top Button Implementation for a Decentralized Exchange Interface

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
  // Create the scroll-to-top button element
  const scrollToTopButton = document.createElement("button");
  scrollToTopButton.id = "scrollToTopButton";
  scrollToTopButton.textContent = "↑ Top";
  
  // Style the button (basic styling for demonstration purposes)
  scrollToTopButton.style.position = "fixed";
  scrollToTopButton.style.bottom = "20px";
  scrollToTopButton.style.right = "20px";
  scrollToTopButton.style.padding = "10px 15px";
  scrollToTopButton.style.fontSize = "16px";
  scrollToTopButton.style.backgroundColor = "#007bff";
  scrollToTopButton.style.color = "#fff";
  scrollToTopButton.style.border = "none";
  scrollToTopButton.style.borderRadius = "5px";
  scrollToTopButton.style.cursor = "pointer";
  scrollToTopButton.style.display = "none"; // Initially hidden
  scrollToTopButton.style.zIndex = "1000";

  // Append the button to the body
  document.body.appendChild(scrollToTopButton);

  // Function to handle scroll-to-top behavior
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth", // Smooth scrolling effect
    });
  };

  // Add click event listener to the button
  scrollToTopButton.addEventListener("click", scrollToTop);

  // Function to toggle button visibility based on scroll position
  const toggleButtonVisibility = () => {
    if (window.scrollY > 300) {
      // Show the button if scrolled down more than 300px
      scrollToTopButton.style.display = "block";
    } else {
      // Hide the button if scrolled up
      scrollToTopButton.style.display = "none";
    }
  };

  // Add scroll event listener to the window
  window.addEventListener("scroll", toggleButtonVisibility);

  // Error handling: Ensure the button is removed if the DOM is modified unexpectedly
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (!document.body.contains(scrollToTopButton)) {
        console.error("Scroll-to-top button was removed from the DOM unexpectedly.");
        observer.disconnect(); // Stop observing
      }
    });
  });

  // Start observing the DOM for changes
  observer.observe(document.body, { childList: true, subtree: true });
});
```
