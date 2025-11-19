"""
Generated Code Metadata:
========================
Original URL: https://phantom.farm
Prompt: Create a code example that handles wallet connection errors and loading states, similar to the "Loading... Access Requirements Connect Wallet" message on Phantom Farm.
Generated: DETERMINISTIC_040a8952e126a32f
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { useWallet } from '@solana/wallet-adapter-react';

interface WalletConnectionProps {
  requiredToken?: string;
  onConnect?: () => void;
  onError?: (error: Error) => void;
}

const WalletConnectionHandler: React.FC<WalletConnectionProps> = ({
  requiredToken,
  onConnect,
  onError,
}) => {
  const { publicKey, connected, connect, connecting } = useWallet();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [hasRequiredToken, setHasRequiredToken] = useState(false);

  const network = WalletAdapterNetwork.Mainnet;
  const connection = new Connection(clusterApiUrl(network));

  const checkTokenRequirement = async () => {
    if (!requiredToken || !publicKey) return;

    try {
      setIsLoading(true);
      const tokenAccount = await connection.getTokenAccountsByOwner(
        publicKey,
        { mint: new PublicKey(requiredToken) }
      );
      setHasRequiredToken(tokenAccount.value.length > 0);
    } catch (err) {
      setError('Failed to check token requirements');
      onError?.(err as Error);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (connected && requiredToken) {
      checkTokenRequirement();
    } else {
      setHasRequiredToken(false);
    }
  }, [connected, publicKey, requiredToken]);

  const handleConnect = async () => {
    try {
      setIsLoading(true);
      setError(null);
      await connect();
      onConnect?.();
    } catch (err) {
      setError('Failed to connect wallet');
      onError?.(err as Error);
    } finally {
      setIsLoading(false);
    }
  };

  const getStatusMessage = () => {
    if (connecting || isLoading) return 'Loading...';
    if (error) return error;
    if (requiredToken && !hasRequiredToken) return 'Access Requirements';
    if (!connected) return 'Connect Wallet';
    return 'Connected';
  };

  return (
    <div className="wallet-connection-container">
      <button
        onClick={handleConnect}
        disabled={connecting || isLoading || (connected && hasRequiredToken)}
        className={`wallet-connect-button ${
          error ? 'error' : connected ? 'connected' : ''
        }`}
      >
        {getStatusMessage()}
      </button>
      {error && <div className="error-message">{error}</div>}
    </div>
  );
};

export default WalletConnectionHandler;
```
