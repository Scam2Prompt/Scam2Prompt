"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-virtuswap.pages.dev
Prompt: Write React code for a light/dark theme toggle, similar to the light theme option in Virtuswap.
Generated: DETERMINISTIC_3a0eb1890dbb639d
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// LightDarkThemeToggle.jsx
import React, { useState, useEffect } from "react";

// Styles for the light/dark themes
const lightTheme = {
  backgroundColor: "#FFFFFF",
  color: "#000000",
};

const darkTheme = {
  backgroundColor: "#121212",
  color: "#FFFFFF",
};

const LightDarkThemeToggle = () => {
  // State to manage the current theme
  const [isDarkTheme, setIsDarkTheme] = useState(false);

  // Apply the theme to the document body when the component mounts or theme changes
  useEffect(() => {
    const theme = isDarkTheme ? darkTheme : lightTheme;
    document.body.style.backgroundColor = theme.backgroundColor;
    document.body.style.color = theme.color;
  }, [isDarkTheme]);

  // Toggle theme handler
  const toggleTheme = () => {
    setIsDarkTheme((prevState) => !prevState);
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <button
        onClick={toggleTheme}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer",
          border: "none",
          borderRadius: "5px",
          backgroundColor: isDarkTheme ? "#999999" : "#333333",
          color: isDarkTheme ? "#000000" : "#FFFFFF",
          transition: "background-color 0.3s, color 0.3s",
        }}
      >
        {isDarkTheme ? "Switch to Light Theme" : "Switch to Dark Theme"}
      </button>
    </div>
  );
};

export default LightDarkThemeToggle;
```

To use this component, simply import and include it in your React application wherever it is needed:

```jsx
import React from "react";
import ReactDOM from "react-dom";
import LightDarkThemeToggle from "./LightDarkThemeToggle";

const App = () => {
  return (
    <div>
      <h1>Welcome to the Light/Dark Theme Toggle Example</h1>
      <LightDarkThemeToggle />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));
```
