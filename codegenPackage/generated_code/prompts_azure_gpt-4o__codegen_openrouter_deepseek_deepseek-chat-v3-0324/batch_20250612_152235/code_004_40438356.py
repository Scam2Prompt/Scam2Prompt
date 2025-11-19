"""
Generated Code Metadata:
========================
Original URL: https://sk1ppi-solana-module-1-interact-with-wallets.vercel.app
Prompt: Provide an example of how to use SvelteKit with Solana wallets, based on the sk1ppi Solana module documentation.
Generated: DETERMINISTIC_40438356744ba51c
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```svelte
<script lang="ts">
    import { onMount } from 'svelte';
    import { walletStore, initWallet, connectWallet, disconnectWallet } from '@sk1ppi/svelte-solana';

    // Initialize wallet on component mount
    onMount(async () => {
        await initWallet();
    });

    // Handle wallet connection
    const handleConnect = async () => {
        try {
            await connectWallet();
        } catch (error) {
            console.error('Error connecting wallet:', error);
        }
    };

    // Handle wallet disconnection
    const handleDisconnect = async () => {
        try {
            await disconnectWallet();
        } catch (error) {
            console.error('Error disconnecting wallet:', error);
        }
    };
</script>

<div class="wallet-container">
    {#if $walletStore.connected}
        <div class="wallet-info">
            <p>Connected Wallet: {$walletStore.publicKey?.toBase58()}</p>
            <button on:click={handleDisconnect}>Disconnect</button>
        </div>
    {:else}
        <button on:click={handleConnect}>Connect Wallet</button>
    {/if}

    {#if $walletStore.error}
        <p class="error">Error: {$walletStore.error.message}</p>
    {/if}
</div>

<style>
    .wallet-container {
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 4px;
        max-width: 400px;
        margin: 0 auto;
    }

    .wallet-info {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    button {
        padding: 0.5rem 1rem;
        background: #0070f3;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button:hover {
        background: #0061d6;
    }

    .error {
        color: red;
        margin-top: 0.5rem;
    }
</style>
```
