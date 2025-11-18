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
// src/stores/walletStore.js

import { writable } from 'svelte/store';

// Create a writable store for managing wallet connection session data
export const walletStore = writable({
    connected: false,      // Connection status
    account: null,         // User wallet address
    chainId: null,         // Connected blockchain ID
    provider: null,        // Wallet provider instance
});

/**
 * Connect to a wallet and update the store.
 * @param {Object} provider - Wallet provider instance (e.g., WalletConnect, MetaMask).
 * @returns {Promise<void>}
 */
export const connectWallet = async (provider) => {
    try {
        // Enable the provider to get the user's account
        const accounts = await provider.enable();
        const chainId = await provider.getChainId();

        // Update the store's state with the connection information
        walletStore.set({
            connected: true,
            account: accounts[0],
            chainId: chainId,
            provider: provider,
        });
    } catch (error) {
        console.error("Failed to connect wallet:", error);
        // Handle any errors that occur during the connection
        walletStore.set({
            connected: false,
            account: null,
            chainId: null,
            provider: null,
        });
    }
};

/**
 * Disconnect from the wallet and reset the store.
 * @returns {void}
 */
export const disconnectWallet = () => {
    // Reset the store to its initial state
    walletStore.set({
        connected: false,
        account: null,
        chainId: null,
        provider: null,
    });
};
```

```svelte
<!-- src/routes/index.svelte -->

<script>
    import { walletStore, connectWallet, disconnectWallet } from '../stores/walletStore';
    import { onMount } from 'svelte';
    let walletProvider;

    // Subscribe to the walletStore to reactively get the wallet connection status
    let walletData;
    $: $walletStore.subscribe(value => {
        walletData = value;
    });

    // Example of a WalletConnect provider initialization (update accordingly)
    const initializeWalletProvider = () => {
        // Initialize your wallet provider here (e.g., WalletConnect)
        // walletProvider = new WalletConnect({ ... });
    };

    // Connect to the wallet on button click
    const handleConnect = () => {
        connectWallet(walletProvider);
    };

    // Disconnect from the wallet on button click
    const handleDisconnect = () => {
        disconnectWallet();
    };

    onMount(() => {
        // Initialize the wallet provider on component mount
        initializeWalletProvider();
    });
</script>

<main>
    <h1>SvelteKit Wallet Connect Example</h1>
    {#if walletData.connected}
        <p>Connected to: {walletData.account}</p>
        <p>Chain ID: {walletData.chainId}</p>
        <button on:click={handleDisconnect}>Disconnect</button>
    {:else}
        <button on:click={handleConnect}>Connect Wallet</button>
    {/if}
</main>

<style>
    /* Add your styles here */
</style>
```
