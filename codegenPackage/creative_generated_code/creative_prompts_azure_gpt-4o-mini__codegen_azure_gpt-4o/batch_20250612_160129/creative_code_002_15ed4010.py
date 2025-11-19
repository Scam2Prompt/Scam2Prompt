"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-fork-chenxsan-bugfix-fix-scroll-top-uniswap.vercel.app
Prompt: Can you provide an example of using JavaScript to enable a scroll-to-top button in a decentralized exchange interface like Uniswap?
Generated: DETERMINISTIC_15ed4010211efe49
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Wait for the DOM to load before executing the script
document.addEventListener("DOMContentLoaded", () => {
  // Create a "Scroll to Top" button element
  const scrollToTopButton = document.createElement("button");
  scrollToTopButton.textContent = "↑ Top";
  scrollToTopButton.style.position = "fixed";
  scrollToTopButton.style.bottom = "20px";
  scrollToTopButton.style.right = "20px";
  scrollToTopButton.style.padding = "10px 15px";
  scrollToTopButton.style.fontSize = "16px";
  scrollToTopButton.style.backgroundColor = "#4CAF50"; // Match Uniswap's theme
  scrollToTopButton.style.color = "#FFF";
  scrollToTopButton.style.border = "none";
  scrollToTopButton.style.borderRadius = "5px";
  scrollToTopButton.style.cursor = "pointer";
  scrollToTopButton.style.display = "none"; // Hide initially
  scrollToTopButton.style.boxShadow = "0px 2px 5px rgba(0, 0, 0, 0.2)";
  scrollToTopButton.style.zIndex = "1000"; // Ensure it's above other content

  // Add the button to the body
  document.body.appendChild(scrollToTopButton);

  // Function to scroll to the top of the page
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth" // Smooth scrolling effect
    });
  };

  // Add a click event listener to the button
  scrollToTopButton.addEventListener("click", scrollToTop);

  // Show the button only when the user has scrolled down
  const handleScroll = () => {
    if (window.scrollY > 300) {
      // Show the button if the scroll position is greater than 300px
      scrollToTopButton.style.display = "block";
    } else {
      // Hide the button otherwise
      scrollToTopButton.style.display = "none";
    }
  };

  // Attach the scroll event listener to the window
  window.addEventListener("scroll", handleScroll);

  // Error handling in case of unexpected issues
  try {
    // Ensure the Uniswap interface integrates the button properly
    console.log("Scroll-to-top button initialized successfully.");
  } catch (error) {
    console.error("An error occurred while initializing the scroll-to-top button:", error);
  }
});
```
