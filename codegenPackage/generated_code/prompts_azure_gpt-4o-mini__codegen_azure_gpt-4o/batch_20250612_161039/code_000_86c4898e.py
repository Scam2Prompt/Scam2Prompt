"""
Generated Code Metadata:
========================
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Generate code to implement a Sign-In with Ethereum feature using the wagmi library as described in the Web3Modal documentation.
Generated: DETERMINISTIC_86c4898ef819e722
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and hooks
import React, { useState } from 'react';
import { useAccount, useConnect, useSignMessage, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

// Sign-In with Ethereum Component
const SignInWithEthereum = () => {
  // State to manage the signed message and error
  const [signedMessage, setSignedMessage] = useState(null);
  const [error, setError] = useState(null);

  // Wagmi hooks for account, connection, signing, and disconnecting
  const { connect } = useConnect({
    connector: new InjectedConnector(),
  });
  const { disconnect } = useDisconnect();
  const { address, isConnected } = useAccount();
  const { signMessageAsync } = useSignMessage();

  // Function to handle signing in
  const handleSignIn = async () => {
    try {
      setError(null); // Clear previous errors

      // Generate a message for the user to sign
      const message = `Sign-In with Ethereum\n\nAddress: ${address}\n\nNonce: ${Math.floor(Math.random() * 1000000)}`;

      // Sign the message
      const signature = await signMessageAsync({ message });

      // Save the signed message
      setSignedMessage(signature);

      // Log the signed message (replace with actual backend verification logic)
      console.log('Signed Message:', signature);
    } catch (err) {
      // Handle errors gracefully
      setError(err.message || 'An error occurred while signing the message.');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      {/* Display connection status */}
      <h2>Sign-In with Ethereum</h2>
      {isConnected ? (
        <div>
          <p>Connected Address: {address}</p>
          <button onClick={handleSignIn} style={{ marginRight: '10px' }}>
            Sign Message
          </button>
          <button onClick={disconnect}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connect}>Connect Wallet</button>
      )}

      {/* Display signed message */}
      {signedMessage && (
        <div style={{ marginTop: '20px' }}>
          <h3>Signed Message:</h3>
          <p>{signedMessage}</p>
        </div>
      )}

      {/* Display error message */}
      {error && (
        <div style={{ marginTop: '20px', color: 'red' }}>
          <h3>Error:</h3>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default SignInWithEthereum;
```
