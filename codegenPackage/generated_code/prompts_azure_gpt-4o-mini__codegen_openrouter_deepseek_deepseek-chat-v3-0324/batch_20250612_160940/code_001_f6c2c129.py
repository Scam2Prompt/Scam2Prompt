"""
Generated Code Metadata:
========================
Original URL: https://sk1ppi-solana-module-1-interact-with-wallets.vercel.app
Prompt: What are the steps to interact with wallets in a SvelteKit application as mentioned on the sk1ppi Solana module site?
Generated: DETERMINISTIC_f6c2c1290acbf215
Batch ID: 20250612_160940
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
    import { walletStore, type WalletStore } from '@sk1ppi/solana-wallet-adapter-svelte';
    import { Connection, clusterApiUrl } from '@solana/web3.js';

    let wallet: WalletStore;
    let connection: Connection;
    let publicKey: string | null = null;
    let balance: number | null = null;
    let error: string | null = null;

    onMount(() => {
        // Initialize connection to Solana devnet
        connection = new Connection(clusterApiUrl('devnet'));

        // Subscribe to wallet store changes
        const unsubscribe = walletStore.subscribe((store) => {
            wallet = store;
            publicKey = wallet.publicKey?.toBase58() || null;
            
            if (wallet.connected && wallet.publicKey) {
                fetchBalance(wallet.publicKey).catch((err) => {
                    error = err.message;
                });
            } else {
                balance = null;
            }
        });

        return () => unsubscribe();
    });

    async function fetchBalance(publicKey: PublicKey) {
        try {
            const lamports = await connection.getBalance(publicKey);
            balance = lamports / 10 ** 9; // Convert lamports to SOL
            error = null;
        } catch (err) {
            error = 'Failed to fetch balance';
            throw err;
        }
    }

    async function connectWallet() {
        try {
            await wallet.connect();
            error = null;
        } catch (err) {
            error = 'Failed to connect wallet';
        }
    }

    async function disconnectWallet() {
        try {
            await wallet.disconnect();
            error = null;
        } catch (err) {
            error = 'Failed to disconnect wallet';
        }
    }
</script>

<div>
    {#if !wallet?.connected}
        <button on:click={connectWallet}>Connect Wallet</button>
    {:else}
        <div>
            <p>Connected: {publicKey}</p>
            {#if balance !== null}
                <p>Balance: {balance} SOL</p>
            {/if}
            <button on:click={disconnectWallet}>Disconnect</button>
        </div>
    {/if}

    {#if error}
        <p style="color: red;">Error: {error}</p>
    {/if}
</div>
```
