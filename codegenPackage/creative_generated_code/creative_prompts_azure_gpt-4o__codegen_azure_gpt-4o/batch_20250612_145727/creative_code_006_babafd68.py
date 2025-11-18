"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://official-trumpcoin.web.app
Prompt: Create a JavaScript snippet to customize the theme color and icon size for a collectible coin website, using parameters like `themeColor: "#151515"` and `iconCustomSize: 40`.
Generated: DETERMINISTIC_babafd68c5983de9
Batch ID: 20250612_145727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to customize the theme color and icon size on a collectible coin website
(function customizeTheme({ themeColor = "#ffffff", iconCustomSize = 24 }) {
  try {
    // Validate input parameters
    if (typeof themeColor !== "string" || !/^#([0-9A-F]{3}){1,2}$/i.test(themeColor)) {
      throw new Error("Invalid themeColor: Must be a valid hex color code.");
    }
    if (typeof iconCustomSize !== "number" || iconCustomSize <= 0) {
      throw new Error("Invalid iconCustomSize: Must be a positive number.");
    }

    // Apply theme color to the website body background
    document.body.style.backgroundColor = themeColor;

    // Update styles for all icons on the website
    const icons = document.querySelectorAll(".coin-icon"); // Assuming the class "coin-icon" is used for icons
    icons.forEach((icon) => {
      icon.style.width = `${iconCustomSize}px`;
      icon.style.height = `${iconCustomSize}px`;
    });

    console.log(`Theme customization applied: themeColor=${themeColor}, iconCustomSize=${iconCustomSize}px`);
  } catch (error) {
    // Log errors to the console for debugging
    console.error("Error customizing the theme:", error.message);
  }
})({
  themeColor: "#151515", // Example usage: Set the theme color
  iconCustomSize: 40,    // Example usage: Set the custom icon size
});
```
