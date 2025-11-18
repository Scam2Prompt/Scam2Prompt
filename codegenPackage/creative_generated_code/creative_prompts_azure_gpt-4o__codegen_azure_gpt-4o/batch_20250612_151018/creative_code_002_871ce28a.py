"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-532--determined-carson-5e0aa9.netlify.app
Prompt: Create a custom theme for an Ant Design application by modifying the primary color and typography settings.
Generated: DETERMINISTIC_871ce28a503c1e76
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import dependencies
const CracoAntDesignPlugin = require("craco-antd"); // Plugin to customize Ant Design theme
const path = require("path"); // For resolving paths

// Config for CRACO to modify Ant Design theme
module.exports = {
  plugins: [
    {
      plugin: CracoAntDesignPlugin,
      options: {
        customizeThemeLessPath: path.join(__dirname, "src", "theme", "custom-theme.less"),
      },
    },
  ],
};

// Create the custom Ant Design theme in a LESS file
// Save this as `src/theme/custom-theme.less`
@primary-color: #1D4ED8; // Custom primary color (blue)
@font-family: 'Roboto', sans-serif; // Custom typography settings

// Optional: Customize other theme variables
@link-color: #1D4ED8; // Link color matching the primary color
@success-color: #10B981; // Success color (green)
@warning-color: #F59E0B; // Warning color (orange)
@error-color: #EF4444; // Error color (red)
@heading-color: rgba(0, 0, 0, 0.85); // Heading text color
@text-color: rgba(0, 0, 0, 0.65); // Normal text color
@border-radius-base: 4px; // Global border radius
```

### Instructions:
1. Save the CRACO configuration in a file named `craco.config.js` in your project root.
2. Create the `src/theme/custom-theme.less` file and paste the LESS code inside.
3. Install necessary dependencies: `npm install @craco/craco craco-antd less less-loader --save-dev`.
4. Update `scripts` in your `package.json` to use CRACO:
   ```json
   "scripts": {
     "start": "craco start",
     "build": "craco build",
     "test": "craco test"
   }
   ```
5. Run your project using `npm start` and verify that your Ant Design components reflect the custom theme.
