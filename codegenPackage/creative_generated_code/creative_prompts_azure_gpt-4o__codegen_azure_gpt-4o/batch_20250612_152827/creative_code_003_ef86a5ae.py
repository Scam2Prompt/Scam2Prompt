"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airpot-02.vercel.app
Prompt: Provide an example of integrating Phantom wallet authentication into a Terms of Service acceptance flow, inspired by the HONEY CUBE website.
Generated: DETERMINISTIC_ef86a5ae0e95a942
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
import { useState } from "react";

// Phantom wallet integration function
const connectPhantomWallet = async () => {
  try {
    // Check if Phantom wallet is available
    const isPhantomAvailable = window.solana && window.solana.isPhantom;
    if (!isPhantomAvailable) {
      throw new Error("Phantom wallet not detected. Please install Phantom.");
    }

    // Request connection to Phantom wallet
    const walletResponse = await window.solana.connect();
    return walletResponse.publicKey.toString(); // Return the connected wallet's public key
  } catch (error) {
    console.error("Error connecting to Phantom wallet:", error);
    throw error;
  }
};

// Terms of Service acceptance flow
const TermsOfServiceFlow = () => {
  const [publicKey, setPublicKey] = useState(null);
  const [isTermsAccepted, setIsTermsAccepted] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const handleConnectWallet = async () => {
    try {
      // Attempt to connect to Phantom wallet
      const connectedPublicKey = await connectPhantomWallet();
      setPublicKey(connectedPublicKey);
    } catch (error) {
      setErrorMessage(error.message);
    }
  };

  const handleAcceptTerms = () => {
    if (!publicKey) {
      setErrorMessage("Please connect your Phantom wallet before accepting the Terms of Service.");
      return;
    }

    setIsTermsAccepted(true);
    alert("Terms of Service accepted successfully!");
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Terms of Service</h1>
      <p>
        By accepting the Terms of Service, you agree to abide by all rules and policies outlined
        herein. Please connect your Phantom wallet to proceed.
      </p>

      {/* Show connected wallet public key */}
      {publicKey && <p><strong>Connected Wallet:</strong> {publicKey}</p>}

      {/* Wallet connection button */}
      <button onClick={handleConnectWallet} style={{ margin: "10px 0" }}>
        Connect Phantom Wallet
      </button>

      {/* Terms acceptance button */}
      <button onClick={handleAcceptTerms} style={{ margin: "10px 0" }}>
        Accept Terms of Service
      </button>

      {/* Error message display */}
      {errorMessage && (
        <p style={{ color: "red", marginTop: "10px" }}>{errorMessage}</p>
      )}

      {/* Success message */}
      {isTermsAccepted && (
        <p style={{ color: "green", marginTop: "10px" }}>
          Thank you for accepting the Terms of Service!
        </p>
      )}
    </div>
  );
};

export default TermsOfServiceFlow;
```
