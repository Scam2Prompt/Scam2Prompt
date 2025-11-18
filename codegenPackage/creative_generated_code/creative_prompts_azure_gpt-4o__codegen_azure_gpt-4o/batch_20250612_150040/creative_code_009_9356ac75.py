"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Create a React component that accepts a USDT wallet address as input and generates a QR code image for blockchain formats like ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
Generated: DETERMINISTIC_9356ac75e756720d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React, { useState } from "react";
import QRCode from "qrcode.react"; // Library for generating QR codes
import PropTypes from "prop-types";

// QRCodeGenerator Component
const QRCodeGenerator = ({ address }) => {
  // State to store the selected blockchain format
  const [blockchainFormat, setBlockchainFormat] = useState("ERC-20");

  // Available blockchain formats
  const blockchainFormats = ["ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"];

  // Generate data string for the QR code based on blockchain format
  const generateDataString = () => {
    if (!address) {
      return ""; // Handle empty wallet address gracefully
    }
    return `${blockchainFormat}:${address}`;
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      {/* Wallet address input display */}
      <div style={{ marginBottom: "10px" }}>
        <strong>Wallet Address:</strong> {address || "No address provided"}
      </div>

      {/* Dropdown menu for selecting blockchain format */}
      <div style={{ marginBottom: "20px" }}>
        <label htmlFor="blockchainFormat">Select Blockchain Format: </label>
        <select
          id="blockchainFormat"
          value={blockchainFormat}
          onChange={(e) => setBlockchainFormat(e.target.value)}
        >
          {blockchainFormats.map((format) => (
            <option key={format} value={format}>
              {format}
            </option>
          ))}
        </select>
      </div>

      {/* Render the QR code */}
      <div>
        {address ? (
          <QRCode
            value={generateDataString()}
            size={200} // Size of the QR code
            level="Q" // Error correction level
            includeMargin={true} // Add margin around QR code
          />
        ) : (
          <p>Please provide a valid wallet address.</p>
        )}
      </div>
    </div>
  );
};

// PropTypes for type checking
QRCodeGenerator.propTypes = {
  address: PropTypes.string.isRequired, // Wallet address is required
};

export default QRCodeGenerator;
```

This React component accepts a USDT wallet address as a prop (`address`) and generates a QR code based on the selected blockchain format. It includes dropdown functionality for selecting between blockchain formats like ERC-20, TRC-20, BEP-20, Omni, and BEP-2. Proper error handling ensures that a QR code is only generated if a valid wallet address is provided.
