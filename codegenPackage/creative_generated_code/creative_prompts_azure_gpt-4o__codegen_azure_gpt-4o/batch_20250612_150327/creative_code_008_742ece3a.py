"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-1.pages.dev
Prompt: Provide an example of using SvelteKit stores to manage Wallet Connect session data.
Generated: DETERMINISTIC_742ece3a3e9baf31
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/stores/walletConnectStore.js
import { writable } from 'svelte/store';

/**
 * Store to manage Wallet Connect session data.
 * 
 * - `session`: Current Wallet Connect session object.
 * - `connected`: Boolean flag indicating whether the user is connected.
 * - `address`: The connected wallet address.
 * - `chainId`: The chain ID of the connected network.
 */
export const walletConnectStore = writable({
  session: null,   // Wallet Connect session object
  connected: false, // Connection state
  address: null,   // Wallet address
  chainId: null    // Blockchain network ID
});

/**
 * Set the Wallet Connect session.
 *
 * @param {Object} session - Wallet Connect session object to store.
 */
export function setSession(session) {
  if (session && session.accounts && session.chainId) {
    walletConnectStore.set({
      session,
      connected: true,
      address: session.accounts[0],
      chainId: session.chainId,
    });
  } else {
    console.error('Invalid session object provided');
    clearSession();
  }
}

/**
 * Clear the Wallet Connect session.
 *
 * Resets the store to its default state.
 */
export function clearSession() {
  walletConnectStore.set({
    session: null,
    connected: false,
    address: null,
    chainId: null,
  });
}

// src/routes/+page.svelte
<script>
  import { walletConnectStore, setSession, clearSession } from '../stores/walletConnectStore';
  import { onMount } from 'svelte';

  let walletData;

  // Subscribe to the walletConnectStore data
  const unsubscribe = walletConnectStore.subscribe((data) => {
    walletData = data;
  });

  onMount(() => {
    // Cleanup on component unmount
    return () => {
      unsubscribe();
    };
  });

  // Example function to simulate a Wallet Connect session establishment
  function connectWallet() {
    try {
      // Simulated session data (replace with real Wallet Connect logic)
      const mockSession = {
        accounts: ['0x1234567890abcdef1234567890abcdef12345678'],
        chainId: 1
      };

      setSession(mockSession);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    }
  }

  // Example function to disconnect wallet
  function disconnectWallet() {
    try {
      clearSession();
    } catch (error) {
      console.error('Failed to disconnect wallet:', error);
    }
  }
</script>

<main>
  <h1>Wallet Connect Example</h1>

  {#if walletData.connected}
    <p>Connected Wallet Address: {walletData.address}</p>
    <p>Chain ID: {walletData.chainId}</p>
    <button on:click={disconnectWallet}>Disconnect Wallet</button>
  {:else}
    <p>No wallet connected.</p>
    <button on:click={connectWallet}>Connect Wallet</button>
  {/if}
</main>
```
