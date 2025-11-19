"""
Generated Code Metadata:
========================
Original URL: https://fuel-explorer.vercel.app
Prompt: Generate code to integrate a Fuel-compatible wallet into a decentralized application, ensuring users can connect their wallets and interact with the Fuel ecosystem.
Generated: DETERMINISTIC_cc44199ad916d73a
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary libraries and types
import { Wallet } from 'fuels';
import { Fuel } from '@fuel-wallet/sdk';
import { useEffect, useState } from 'react';

// Define types for wallet connection state
type WalletConnectionState = {
  wallet: Wallet | null;
  address: string | null;
  isConnected: boolean;
  error: string | null;
  isLoading: boolean;
};

// Initialize Fuel wallet SDK
const fuel = new Fuel();

// Custom hook for wallet connection
export function useFuelWallet() {
  const [state, setState] = useState<WalletConnectionState>({
    wallet: null,
    address: null,
    isConnected: false,
    error: null,
    isLoading: true,
  });

  // Check if Fuel wallet is available
  const checkFuelAvailability = async () => {
    try {
      const isAvailable = await fuel.isAvailable();
      if (!isAvailable) {
        throw new Error('Fuel wallet not detected');
      }
      return true;
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : 'Unknown error',
        isLoading: false,
      }));
      return false;
    }
  };

  // Connect to Fuel wallet
  const connectWallet = async () => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));
    try {
      const isAvailable = await checkFuelAvailability();
      if (!isAvailable) return;

      const accounts = await fuel.accounts();
      if (!accounts || accounts.length === 0) {
        throw new Error('No accounts found in Fuel wallet');
      }

      const wallet = await fuel.getWallet(accounts[0]);
      const address = wallet.address.toString();

      setState({
        wallet,
        address,
        isConnected: true,
        error: null,
        isLoading: false,
      });
    } catch (error) {
      setState((prev) => ({
        ...prev,
        error: error instanceof Error ? error.message : 'Failed to connect wallet',
        isLoading: false,
      }));
    }
  };

  // Disconnect wallet
  const disconnectWallet = () => {
    setState({
      wallet: null,
      address: null,
      isConnected: false,
      error: null,
      isLoading: false,
    });
  };

  // Check connection status on mount
  useEffect(() => {
    const checkConnection = async () => {
      const isAvailable = await checkFuelAvailability();
      if (!isAvailable) return;

      try {
        const accounts = await fuel.accounts();
        if (accounts && accounts.length > 0) {
          const wallet = await fuel.getWallet(accounts[0]);
          setState({
            wallet,
            address: wallet.address.toString(),
            isConnected: true,
            error: null,
            isLoading: false,
          });
        } else {
          setState((prev) => ({ ...prev, isLoading: false }));
        }
      } catch (error) {
        setState((prev) => ({
          ...prev,
          error: error instanceof Error ? error.message : 'Failed to check connection',
          isLoading: false,
        }));
      }
    };

    checkConnection();
  }, []);

  return {
    ...state,
    connectWallet,
    disconnectWallet,
  };
}

// Example component using the hook
export function WalletConnectButton() {
  const {
    address,
    isConnected,
    error,
    isLoading,
    connectWallet,
    disconnectWallet,
  } = useFuelWallet();

  const truncatedAddress = address
    ? `${address.substring(0, 6)}...${address.substring(address.length - 4)}`
    : null;

  return (
    <div>
      {error && <div className="error">{error}</div>}
      {isConnected ? (
        <div>
          <span>Connected: {truncatedAddress}</span>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet} disabled={isLoading}>
          {isLoading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      )}
    </div>
  );
}

// Utility function to send transaction
export async function sendTransaction(
  wallet: Wallet,
  toAddress: string,
  amount: number
) {
  if (!wallet) {
    throw new Error('Wallet not connected');
  }

  try {
    const tx = await wallet.transfer(toAddress, amount);
    const result = await tx.wait();
    return result;
  } catch (error) {
    throw new Error(
      error instanceof Error ? error.message : 'Transaction failed'
    );
  }
}
```
