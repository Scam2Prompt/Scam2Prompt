"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a Web3 React hook to manage wallet connections and display account details, based on the Dapp Starter template.
Generated: DETERMINISTIC_a575d2cfc914bba4
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { useCallback, useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3Provider } from '@ethersproject/providers';

// Supported chain IDs
const supportedChainIds = [1, 3, 4, 5, 42, 137, 80001];

// Initialize the injected connector
export const injectedConnector = new InjectedConnector({
  supportedChainIds,
});

/**
 * Hook for managing wallet connections and account details
 */
export function useWallet() {
  const { activate, deactivate, account, active, library, chainId } = useWeb3React<Web3Provider>();
  const [error, setError] = useState<Error | null>(null);
  const [isConnecting, setIsConnecting] = useState(false);

  /**
   * Connect to the wallet
   */
  const connect = useCallback(async () => {
    setIsConnecting(true);
    setError(null);
    try {
      await activate(injectedConnector, (error) => {
        if (error.name === 'UnsupportedChainIdError') {
          error.message = 'Unsupported network. Please switch to a supported network.';
        }
        setError(error);
      });
    } catch (err) {
      setError(err as Error);
    } finally {
      setIsConnecting(false);
    }
  }, [activate]);

  /**
   * Disconnect from the wallet
   */
  const disconnect = useCallback(() => {
    setError(null);
    deactivate();
  }, [deactivate]);

  /**
   * Auto-connect wallet if previously connected
   */
  useEffect(() => {
    const tryConnect = async () => {
      const isAuthorized = await injectedConnector.isAuthorized();
      if (isAuthorized && !active) {
        await connect();
      }
    };

    tryConnect();
  }, [active, connect]);

  /**
   * Get the ENS name if available
   */
  const [ensName, setEnsName] = useState<string | null>(null);
  useEffect(() => {
    if (!account || !library || !active) return;

    let mounted = true;

    const resolveEnsName = async () => {
      try {
        const name = await library.lookupAddress(account);
        if (mounted) setEnsName(name);
      } catch (err) {
        console.error('Error resolving ENS name:', err);
        if (mounted) setEnsName(null);
      }
    };

    resolveEnsName();

    return () => {
      mounted = false;
    };
  }, [account, library, active]);

  return {
    account,
    ensName,
    chainId,
    isActive: active,
    isConnecting,
    error,
    connect,
    disconnect,
    provider: library,
  };
}
```
