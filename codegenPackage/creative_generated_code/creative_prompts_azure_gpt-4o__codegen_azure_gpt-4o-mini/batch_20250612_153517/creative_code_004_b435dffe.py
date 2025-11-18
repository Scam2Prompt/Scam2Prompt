"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: How do I customize the "Connect Wallet" button in RainbowKit to match the design shown in the RainbowKit example demo?
Generated: DETERMINISTIC_b435dffe6c7afdef
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React from 'react';
import { RainbowKitProvider, ConnectButton } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';

const customStyles = {
  button: {
    background: '#4B5563', // Button background color
    color: '#FFFFFF',       // Button text color
    borderRadius: '8px',    // Rounded corners
    border: 'none',         // No border
    padding: '10px 20px',   // Padding
    fontSize: '16px',       // Font size
    cursor: 'pointer',      // Cursor style
    transition: 'background 0.3s ease', // Transition effect
  },
  buttonHover: {
    background: '#3B4252', // Button background color on hover
  },
};

const CustomConnectButton = () => {
  // Handle button hover state
  const [isHovered, setIsHovered] = React.useState(false);

  return (
    <button
      style={{
        ...customStyles.button,
        ...(isHovered ? customStyles.buttonHover : {}),
      }}
      onMouseEnter={() => setIsHovered(true)} // Change style on hover
      onMouseLeave={() => setIsHovered(false)} // Revert style when not hovered
      onClick={() => {
        // Handle button click with error handling
        try {
          // Call the connect wallet function from RainbowKit
          console.log("Connect Wallet clicked");
          // Add any additional logic needed for connecting the wallet here
        } catch (error) {
          console.error("Failed to connect wallet", error); // Log any errors
        }
      }}
    >
      Connect Wallet
    </button>
  );
};

const App = () => {
  return (
    <RainbowKitProvider>
      <div style={{ padding: '20px', textAlign: 'center' }}>
        {/* Render the custom connect button */}
        <CustomConnectButton />
      </div>
    </RainbowKitProvider>
  );
};

export default App;
```
