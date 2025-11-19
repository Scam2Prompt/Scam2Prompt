"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-470wtro6y-reown-com.vercel.app
Prompt: Can you provide a code example for implementing sign in with Ethereum using wagmi in AppKit?
Generated: DETERMINISTIC_fc5577bd4324f187
Batch ID: 20250612_140318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Sign-In with Ethereum implementation using wagmi and AppKit

import { useEffect, useState } from 'react';
import { useAccount, useConnect, useDisconnect, useSignMessage } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

// Sign-In with Ethereum component
const SignInWithEthereum = () => {
  // Wagmi hooks for wallet connection and signing
  const { connect, connectors, isLoading: isConnecting } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();
  const { signMessageAsync } = useSignMessage();

  // Local state for managing signed message and error
  const [signedMessage, setSignedMessage] = useState(null);
  const [error, setError] = useState(null);

  // Handle wallet connection
  const handleConnect = async () => {
    try {
      // Connect using the first available connector
      await connect({ connector: connectors[0] });
    } catch (err) {
      // Handle connection errors
      setError(err.message || 'Failed to connect wallet');
    }
  };

  // Handle signing message
  const handleSignMessage = async () => {
    try {
      if (!isConnected) {
        setError('Please connect your wallet first.');
        return;
      }

      // Prompt user to sign a message
      const message = 'Sign in with Ethereum to verify your identity.';
      const signed = await signMessageAsync({ message });
      setSignedMessage(signed);
    } catch (err) {
      // Handle signing errors
      setError(err.message || 'Failed to sign message');
    }
  };

  // Disconnect wallet
  const handleDisconnect = () => {
    disconnect();
    setSignedMessage(null);
    setError(null);
  };

  useEffect(() => {
    // Clear error when user connects/disconnects
    if (isConnected) setError(null);
  }, [isConnected]);

  return (
    <div>
      <h1>Sign-In with Ethereum</h1>

      {/* Show wallet address if connected */}
      {isConnected ? (
        <div>
          <p>Connected Wallet: {address}</p>
          <button onClick={handleSignMessage} disabled={isConnecting}>
            Sign Message
          </button>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnect} disabled={isConnecting}>
          Connect Wallet
        </button>
      )}

      {/* Display signed message */}
      {signedMessage && (
        <div>
          <h3>Signed Message</h3>
          <p>{signedMessage}</p>
        </div>
      )}

      {/* Display error if any */}
      {error && (
        <div style={{ color: 'red' }}>
          <p>Error: {error}</p>
        </div>
      )}
    </div>
  );
};

export default SignInWithEthereum;
```
