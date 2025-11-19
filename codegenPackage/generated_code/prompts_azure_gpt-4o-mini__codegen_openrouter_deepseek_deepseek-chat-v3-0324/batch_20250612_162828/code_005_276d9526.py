"""
Generated Code Metadata:
========================
Original URL: https://nft-gnosis.net
Prompt: Provide an example of how to use MetaMask Snaps to extend wallet functionalities in a decentralized application.
Generated: DETERMINISTIC_276d9526c5d0c96e
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready example of using MetaMask Snaps to extend wallet functionalities in a decentralized application:

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// Configuration constants
const SNAP_ID = 'npm:@metamask/example-snap';
const SNAP_VERSION = '^1.0.0';

/**
 * Checks if the Snap is installed
 * @param {ethers.providers.Web3Provider} provider - Web3 provider
 * @returns {Promise<boolean>} - Whether the Snap is installed
 */
async function isSnapInstalled(provider) {
  try {
    const result = await provider.send('wallet_getSnaps', {});
    return result[SNAP_ID]?.version !== undefined;
  } catch (error) {
    console.error('Failed to check installed snaps:', error);
    return false;
  }
}

/**
 * Installs the Snap if not already installed
 * @param {ethers.providers.Web3Provider} provider - Web3 provider
 * @returns {Promise<void>}
 */
async function installSnap(provider) {
  try {
    await provider.send('wallet_requestSnaps', {
      [SNAP_ID]: { version: SNAP_VERSION },
    });
    console.log('Snap installed successfully');
  } catch (error) {
    console.error('Failed to install snap:', error);
    throw new Error(`Snap installation failed: ${error.message}`);
  }
}

/**
 * Invokes a custom RPC method exposed by the Snap
 * @param {ethers.providers.Web3Provider} provider - Web3 provider
 * @param {string} method - Method name to call
 * @param {any[]} params - Parameters to pass
 * @returns {Promise<any>} - Result from the Snap
 */
async function invokeSnapMethod(provider, method, params = []) {
  try {
    const result = await provider.send('wallet_invokeSnap', {
      snapId: SNAP_ID,
      request: { method, params },
    });
    return result;
  } catch (error) {
    console.error(`Failed to invoke snap method ${method}:`, error);
    throw new Error(`Snap method invocation failed: ${error.message}`);
  }
}

/**
 * Component demonstrating MetaMask Snap integration
 */
function MetaMaskSnapIntegration() {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState('');
  const [snapInstalled, setSnapInstalled] = useState(false);
  const [customResult, setCustomResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Initialize provider and check Snap status
  useEffect(() => {
    async function init() {
      if (window.ethereum) {
        try {
          const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(web3Provider);
          
          const accounts = await web3Provider.listAccounts();
          if (accounts.length > 0) {
            setAccount(accounts[0]);
          }
          
          const installed = await isSnapInstalled(web3Provider);
          setSnapInstalled(installed);
        } catch (err) {
          console.error('Initialization error:', err);
          setError('Failed to initialize provider');
        }
      }
    }

    init();

    // Handle account changes
    if (window.ethereum) {
      window.ethereum.on('accountsChanged', (accounts) => {
        setAccount(accounts[0] || '');
      });
    }

    return () => {
      if (window.ethereum) {
        window.ethereum.removeListener('accountsChanged');
      }
    };
  }, []);

  /**
   * Handles connecting to MetaMask
   */
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error('MetaMask not detected');
      }

      setLoading(true);
      const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts',
      });
      setAccount(accounts[0]);
      setLoading(false);
    } catch (err) {
      console.error('Failed to connect:', err);
      setError(err.message);
      setLoading(false);
    }
  };

  /**
   * Handles installing the Snap
   */
  const handleInstallSnap = async () => {
    if (!provider) return;

    try {
      setLoading(true);
      await installSnap(provider);
      setSnapInstalled(true);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  /**
   * Calls a custom method from the Snap
   */
  const callCustomMethod = async () => {
    if (!provider) return;

    try {
      setLoading(true);
      // Example: Call a custom method with some parameters
      const result = await invokeSnapMethod(
        provider,
        'custom_method',
        ['param1', 'param2']
      );
      setCustomResult(result);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>MetaMask Snap Integration</h1>
      
      {!account ? (
        <button onClick={connectWallet} disabled={loading}>
          {loading ? 'Connecting...' : 'Connect Wallet'}
        </button>
      ) : (
        <p>Connected account: {account}</p>
      )}

      {provider && !snapInstalled && (
        <div>
          <button onClick={handleInstallSnap} disabled={loading}>
            {loading ? 'Installing...' : 'Install Snap'}
          </button>
        </div>
      )}

      {provider && snapInstalled && (
        <div>
          <p>Snap is installed!</p>
          <button onClick={callCustomMethod} disabled={loading}>
            {loading ? 'Calling...' : 'Call Custom Method'}
          </button>
          {customResult && (
            <div>
              <p>Method result:</p>
              <pre>{JSON.stringify(customResult, null, 2)}</pre>
            </div>
          )}
        </div>
      )}

      {error && (
        <div style={{ color: 'red' }}>
          <p>Error:</p>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default MetaMaskSnapIntegration;
```

This code assumes you have the following dependencies in your project:
```json
{
  "dependencies": {
    "ethers": "^5.7.2",
    "react": "^18.2.0"
  }
}
```
