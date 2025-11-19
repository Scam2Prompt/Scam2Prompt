"""
Generated Code Metadata:
========================
Original URL: https://dcqex.com
Prompt: How do I implement JavaScript error handling for a DeFi application that relies on user interaction?
Generated: DETERMINISTIC_a56c5b426142ca1d
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Error handling utilities for DeFi applications
 */

// Error types specific to DeFi operations
class DeFiError extends Error {
  constructor(message) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}

class InsufficientBalanceError extends DeFiError {
  constructor(token, balance, required) {
    super(`Insufficient ${token} balance. You have ${balance}, but need ${required}`);
    this.token = token;
    this.balance = balance;
    this.required = required;
  }
}

class TransactionRevertedError extends DeFiError {
  constructor(reason) {
    super(`Transaction reverted: ${reason}`);
    this.reason = reason;
  }
}

class NetworkError extends DeFiError {
  constructor(network, details) {
    super(`Network error on ${network}: ${details}`);
    this.network = network;
    this.details = details;
  }
}

/**
 * Wraps a contract interaction with proper error handling
 * @param {Function} contractCall - The contract function to call
 * @param {Object} params - Parameters for the contract call
 * @returns {Promise} - Resolves with transaction result or rejects with formatted error
 */
async function handleContractInteraction(contractCall, params = {}) {
  try {
    const tx = await contractCall(params);
    const receipt = await tx.wait();
    return receipt;
  } catch (error) {
    if (error.code === 'INSUFFICIENT_FUNDS') {
      throw new InsufficientBalanceError(
        params.token || 'ETH',
        params.balance || 'unknown',
        params.required || 'unknown'
      );
    } else if (error.data?.message?.includes('reverted')) {
      const reason = error.data.message.match(/reverted with reason string '(.*?)'/)?.[1] || 'unknown';
      throw new TransactionRevertedError(reason);
    } else if (error.code === 'NETWORK_ERROR') {
      throw new NetworkError(params.network || 'unknown', error.message);
    } else {
      throw new DeFiError(`Contract interaction failed: ${error.message}`);
    }
  }
}

/**
 * Error boundary component for React-based DeFi apps
 */
function DeFiErrorBoundary({ children }) {
  const [error, setError] = useState(null);

  const resetError = () => {
    setError(null);
  };

  if (error) {
    return (
      <div className="error-boundary">
        <h2>Something went wrong</h2>
        <p>{error.message}</p>
        {error instanceof InsufficientBalanceError && (
          <button onClick={() => window.location.href = '/deposit'}>
            Deposit Funds
          </button>
        )}
        <button onClick={resetError}>Try Again</button>
      </div>
    );
  }

  return children;
}

/**
 * Global error handler for uncaught exceptions
 */
function setupGlobalErrorHandling() {
  window.onerror = (message, source, lineno, colno, error) => {
    console.error('Global error:', { message, source, lineno, colno, error });
    // Send to error tracking service
    if (window.trackError) {
      window.trackError(error);
    }
    return true; // Prevent default error handling
  };

  window.onunhandledrejection = (event) => {
    console.error('Unhandled rejection:', event.reason);
    // Send to error tracking service
    if (window.trackError) {
      window.trackError(event.reason);
    }
    event.preventDefault(); // Prevent default error handling
  };
}

/**
 * Utility to display user-friendly error messages
 * @param {Error} error - The error to display
 * @param {HTMLElement} element - The element to display the error in
 */
function displayUserFriendlyError(error, element) {
  let message = 'An unexpected error occurred';
  
  if (error instanceof InsufficientBalanceError) {
    message = `You don't have enough ${error.token} to complete this transaction.`;
  } else if (error instanceof TransactionRevertedError) {
    message = `Transaction failed: ${error.reason}`;
  } else if (error instanceof NetworkError) {
    message = `Network issues detected. Please check your connection.`;
  } else if (error.message) {
    message = error.message;
  }

  element.textContent = message;
  element.classList.add('error-message');
}

// Example usage:
/*
try {
  const receipt = await handleContractInteraction(
    contract.deposit,
    { token: 'ETH', balance: '1.0', required: '2.0' }
  );
  console.log('Transaction successful:', receipt);
} catch (error) {
  displayUserFriendlyError(error, document.getElementById('error-display'));
}
*/
```
