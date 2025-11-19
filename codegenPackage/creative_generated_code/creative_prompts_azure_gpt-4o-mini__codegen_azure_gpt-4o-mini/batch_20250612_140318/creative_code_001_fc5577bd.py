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
import React, { useState } from 'react';
import { useAccount, useConnect, useDisconnect, useProvider } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

// SignInWithEthereum Component
const SignInWithEthereum = () => {
  const [{ data: accountData }, disconnect] = useAccount();
  const [{ data, error, loading }, connect] = useConnect();
  const provider = useProvider();
  const [errorMessage, setErrorMessage] = useState('');

  // Function to handle sign-in
  const handleSignIn = async () => {
    try {
      if (!accountData) {
        // Trigger the connection to the wallet
        await connect(new InjectedConnector());
      } else {
        setErrorMessage('You are already signed in.');
      }
    } catch (err) {
      setErrorMessage(`Error connecting: ${err.message}`);
    }
  };

  // Function to handle sign-out
  const handleSignOut = async () => {
    try {
      await disconnect();
      setErrorMessage('');
    } catch (err) {
      setErrorMessage(`Error disconnecting: ${err.message}`);
    }
  };

  return (
    <div>
      <h1>Sign In with Ethereum</h1>
      {accountData ? (
        <div>
          <p>Connected Account: {accountData.address}</p>
          <button onClick={handleSignOut}>Sign Out</button>
        </div>
      ) : (
        <button onClick={handleSignIn} disabled={loading}>
          {loading ? 'Connecting...' : 'Sign In with MetaMask'}
        </button>
      )}
      {error && <p style={{ color: 'red' }}>Connection error: {error.message}</p>}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
    </div>
  );
};

export default SignInWithEthereum;
```
