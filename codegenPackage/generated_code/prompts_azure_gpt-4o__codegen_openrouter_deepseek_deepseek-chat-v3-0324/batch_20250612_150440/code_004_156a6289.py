"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-ey3dlgbqo-offchain-labs.vercel.app
Prompt: Write a function to handle token bridging errors when using WalletConnect with the Arbitrum Token Bridge.
Generated: DETERMINISTIC_156a6289bc3c490c
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { WalletConnectConnector } from '@web3-react/walletconnect-connector';
import { BridgeError, BridgeErrorCode } from './types';

/**
 * Handles token bridging errors when using WalletConnect with Arbitrum Token Bridge.
 * @param {Error} error - The error object thrown during bridging.
 * @param {WalletConnectConnector} connector - The WalletConnect connector instance.
 * @returns {BridgeError} - Standardized bridge error object.
 */
export function handleTokenBridgeError(
  error: Error,
  connector: WalletConnectConnector
): BridgeError {
  // Standard error codes for known bridge issues
  const errorMapping: Record<string, BridgeErrorCode> = {
    'user rejected transaction': BridgeErrorCode.USER_REJECTED,
    'insufficient funds': BridgeErrorCode.INSUFFICIENT_FUNDS,
    'network mismatch': BridgeErrorCode.NETWORK_MISMATCH,
    'transaction failed': BridgeErrorCode.TRANSACTION_FAILED,
    'gas estimation failed': BridgeErrorCode.GAS_ESTIMATION_FAILED,
    'token not supported': BridgeErrorCode.TOKEN_NOT_SUPPORTED,
  };

  // Check if error is from user closing WalletConnect modal
  if (error.message.includes('User closed modal')) {
    return {
      code: BridgeErrorCode.USER_CLOSED_MODAL,
      message: 'User closed WalletConnect modal',
      originalError: error,
    };
  }

  // Check if error is from session disconnect
  if (error.message.includes('Session disconnected')) {
    void connector.close(); // Clean up connection
    return {
      code: BridgeErrorCode.SESSION_DISCONNECTED,
      message: 'WalletConnect session disconnected',
      originalError: error,
    };
  }

  // Check for known bridge errors
  const lowerCaseMessage = error.message.toLowerCase();
  for (const [key, code] of Object.entries(errorMapping)) {
    if (lowerCaseMessage.includes(key)) {
      return {
        code,
        message: error.message,
        originalError: error,
      };
    }
  }

  // Default case for unhandled errors
  return {
    code: BridgeErrorCode.UNKNOWN_ERROR,
    message: 'Unknown bridging error occurred',
    originalError: error,
  };
}

// types.ts
export enum BridgeErrorCode {
  USER_REJECTED = 'USER_REJECTED',
  INSUFFICIENT_FUNDS = 'INSUFFICIENT_FUNDS',
  NETWORK_MISMATCH = 'NETWORK_MISMATCH',
  TRANSACTION_FAILED = 'TRANSACTION_FAILED',
  GAS_ESTIMATION_FAILED = 'GAS_ESTIMATION_FAILED',
  TOKEN_NOT_SUPPORTED = 'TOKEN_NOT_SUPPORTED',
  USER_CLOSED_MODAL = 'USER_CLOSED_MODAL',
  SESSION_DISCONNECTED = 'SESSION_DISCONNECTED',
  UNKNOWN_ERROR = 'UNKNOWN_ERROR',
}

export interface BridgeError {
  code: BridgeErrorCode;
  message: string;
  originalError: Error;
}
```
