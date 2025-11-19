"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-96qjy03xf-reown-com.vercel.app
Prompt: Generate a sample code snippet for sign-in with Ethereum using wagmi in AppKit.
Generated: DETERMINISTIC_121a8aee3cd67a7d
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary libraries and hooks from wagmi
import { useAccount, useConnect, useDisconnect, useSignMessage } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { useState } from 'react';

// Sample Ethereum Sign-In Component
const EthereumSignIn = () => {
  const { connect } = useConnect({
    connector: new InjectedConnector(), // Use InjectedConnector for wallet connection (e.g., MetaMask)
  });
  const { disconnect } = useDisconnect(); // Hook to disconnect wallet
  const { isConnected, address } = useAccount(); // Account details
  const { signMessage } = useSignMessage(); // Hook for signing messages

  // State variable to store the signed message
  const [signedMessage, setSignedMessage] = useState<string | null>(null);

  // State variable to store errors
  const [error, setError] = useState<string | null>(null);

  // Function: Connect Wallet
  const handleConnect = async () => {
    try {
      setError(null); // Clear previous errors
      await connect(); // Attempt to connect wallet
    } catch (err: any) {
      setError(err.message); // Capture and store error message
    }
  };

  // Function: Disconnect Wallet
  const handleDisconnect = async () => {
    disconnect(); // Disconnect wallet
    setSignedMessage(null); // Reset signed message state
  };

  // Function: Sign-In via Ethereum (Sign Message)
  const handleSignIn = async () => {
    try {
      setError(null); // Clear previous errors
      const message = `Sign this message to authenticate: ${new Date().toISOString()}`; // Custom message
      const signature = await signMessage({ message }); // Sign the message
      setSignedMessage(signature); // Store signed message
    } catch (err: any) {
      setError(err.message); // Capture and store error message
    }
  };

  return (
    <div>
      {/* Display wallet connection status */}
      <div>
        <strong>Status:</strong> {isConnected ? 'Connected' : 'Disconnected'}
      </div>
      {/* Display wallet address if connected */}
      {isConnected && <div><strong>Wallet Address:</strong> {address}</div>}
      {/* Display signed message if available */}
      {signedMessage && (
        <div>
          <strong>Signed Message:</strong> {signedMessage}
        </div>
      )}
      {/* Display error messages */}
      {error && (
        <div style={{ color: 'red' }}>
          <strong>Error:</strong> {error}
        </div>
      )}
      <div>
        {/* Connect Wallet Button */}
        {!isConnected && (
          <button onClick={handleConnect}>Connect Wallet</button>
        )}
        {/* Disconnect Wallet Button */}
        {isConnected && (
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        )}
        {/* Sign-In Button */}
        {isConnected && !signedMessage && (
          <button onClick={handleSignIn}>Sign-In with Ethereum</button>
        )}
      </div>
    </div>
  );
};

export default EthereumSignIn;
```
