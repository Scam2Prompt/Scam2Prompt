"""
Generated Code Metadata:
========================
Original URL: https://sk1ppi-solana-module-1-interact-with-wallets.vercel.app
Prompt: Generate SvelteKit code for a Solana wallet connection interface, incorporating details from the sk1ppi Solana module.
Generated: DETERMINISTIC_6881f8d03c1b6953
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
  // Import necessary modules from Svelte and sk1ppi
  import { onMount } from 'svelte';
  import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
  import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
  import { WalletProvider, ConnectionProvider, useWallet } from '@solana/wallet-adapter-react';
  import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
  import { ToastContainer, toast } from 'react-toastify';
  import 'react-toastify/dist/ReactToastify.css';

  // Define the network and connection
  const network = WalletAdapterNetwork.Devnet;
  const endpoint = clusterApiUrl(network);
  
  // Create a list of wallet adapters
  const wallets = [
    new PhantomWalletAdapter(),
  ];

  // Function to handle wallet connection
  const connectWallet = async () => {
    const { connected, publicKey } = useWallet();
    if (!connected) {
      try {
        await wallet.connect();
        toast.success('Wallet connected successfully!');
      } catch (error) {
        console.error('Connection error:', error);
        toast.error('Failed to connect wallet.');
      }
    } else {
      toast.info(`Wallet already connected: ${publicKey.toString()}`);
    }
  };

  // Function to handle wallet disconnection
  const disconnectWallet = async () => {
    const { connected } = useWallet();
    if (connected) {
      try {
        await wallet.disconnect();
        toast.success('Wallet disconnected successfully!');
      } catch (error) {
        console.error('Disconnection error:', error);
        toast.error('Failed to disconnect wallet.');
      }
    } else {
      toast.info('No wallet connected to disconnect.');
    }
  };

  // On component mount, check wallet connection status
  onMount(() => {
    const { connected } = useWallet();
    if (connected) {
      toast.info('Wallet is already connected.');
    }
  });
</script>

<template>
  <ConnectionProvider endpoint={endpoint}>
    <WalletProvider wallets={wallets} autoConnect>
      <div class="wallet-connection">
        <h1>Solana Wallet Connection</h1>
        <button on:click={connectWallet}>Connect Wallet</button>
        <button on:click={disconnectWallet}>Disconnect Wallet</button>
      </div>
      <ToastContainer />
    </WalletProvider>
  </ConnectionProvider>
</template>

<style>
  .wallet-connection {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }

  button {
    margin: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
</style>
```
