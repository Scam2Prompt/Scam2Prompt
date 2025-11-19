"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hgdsjhgdjhsgff.pages.dev
Prompt: Provide an example of a JavaScript function that prompts users to enable cookies.
Generated: DETERMINISTIC_996c6f62bf4bdb79
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to prompt users to enable cookies if they are disabled.
 * This function checks if cookies are enabled in the browser and
 * displays a message prompting the user to enable them if necessary.
 */
function promptEnableCookies() {
  try {
    // Check if cookies are enabled by attempting to set and retrieve a test cookie
    document.cookie = "test_cookie=enabled; path=/";
    const cookiesEnabled = document.cookie.indexOf("test_cookie=enabled") !== -1;

    // If cookies are disabled, display a prompt message to the user
    if (!cookiesEnabled) {
      // Create a modal div element
      const modal = document.createElement("div");
      
      // Style the modal for visibility
      modal.style.position = "fixed";
      modal.style.top = "50%";
      modal.style.left = "50%";
      modal.style.transform = "translate(-50%, -50%)";
      modal.style.backgroundColor = "#ffffff";
      modal.style.padding = "20px";
      modal.style.border = "1px solid #ccc";
      modal.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
      modal.style.zIndex = "1000";

      // Add text to the modal
      modal.textContent = "Cookies are disabled in your browser. Please enable cookies to continue.";

      // Append modal to the body
      document.body.appendChild(modal);

      // Optionally add a button to close the modal
      const closeButton = document.createElement("button");
      closeButton.textContent = "Close";
      closeButton.style.marginTop = "10px";
      closeButton.style.padding = "5px 10px";
      closeButton.style.cursor = "pointer";

      // Add an event listener to remove the modal when the button is clicked
      closeButton.addEventListener("click", () => {
        document.body.removeChild(modal);
      });

      // Append the button to the modal
      modal.appendChild(closeButton);
    } else {
      console.log("Cookies are enabled.");
    }

    // Clean up the test cookie
    document.cookie = "test_cookie=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC";
  } catch (error) {
    console.error("An error occurred while checking cookies:", error);
  }
}

// Call the function on page load
window.onload = promptEnableCookies;
```
