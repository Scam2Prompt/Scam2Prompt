"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealtokens.pages.dev
Prompt: Write code to integrate a wallet connection widget for purchasing $SEAL tokens using ETH, SOL, USDT, and USDC, as described on the Sealana Presale page.
Generated: DETERMINISTIC_43e74669936b1a5f
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import dependencies
import React, { useState, useEffect } from "react";
import Web3 from "web3"; // For Ethereum and ERC-20 tokens
import { WalletAdapterNetwork } from "@solana/wallet-adapter-base";
import { Connection, clusterApiUrl, PublicKey, Transaction } from "@solana/web3.js";
import { USDC_MINT_ADDRESS, USDT_MINT_ADDRESS } from "./constants"; // Assume constants file defines SOL stablecoin mints
import { WalletModalProvider, WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import { useConnection, useWallet } from "@solana/wallet-adapter-react";
import "./styles.css"; // Assume CSS for styling

// Main Wallet Connection Widget component
const WalletConnectionWidget = () => {
    const [web3, setWeb3] = useState(null); // For Ethereum-based tokens
    const [ethAccount, setEthAccount] = useState(null); // Ethereum wallet address
    const { connection } = useConnection(); // Solana connection
    const { publicKey, sendTransaction } = useWallet(); // Solana wallet
    const [selectedCurrency, setSelectedCurrency] = useState("ETH"); // Default currency
    const [amount, setAmount] = useState(""); // Token purchase amount
    const [loading, setLoading] = useState(false); // Loading state
    const [error, setError] = useState(null); // Error state

    // Initialize Web3 for Ethereum wallets
    useEffect(() => {
        if (window.ethereum) {
            setWeb3(new Web3(window.ethereum));
        } else {
            setError("Ethereum wallet not detected. Please install MetaMask.");
        }
    }, []);

    // Connect Ethereum wallet
    const connectEthereumWallet = async () => {
        try {
            if (!web3) throw new Error("Web3 not initialized.");
            const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
            setEthAccount(accounts[0]);
        } catch (err) {
            setError(err.message);
        }
    };

    // Handle token purchase
    const handlePurchase = async () => {
        if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
            setError("Invalid amount. Please enter a valid number.");
            return;
        }
        setLoading(true);
        setError(null);

        try {
            switch (selectedCurrency) {
                case "ETH":
                    await purchaseWithETH();
                    break;
                case "SOL":
                    await purchaseWithSOL();
                    break;
                case "USDT":
                    await purchaseWithStablecoin(USDT_MINT_ADDRESS);
                    break;
                case "USDC":
                    await purchaseWithStablecoin(USDC_MINT_ADDRESS);
                    break;
                default:
                    setError("Unsupported currency selected.");
            }
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    // Purchase using ETH
    const purchaseWithETH = async () => {
        if (!ethAccount) throw new Error("Ethereum wallet not connected.");
        const sealanaContractAddress = "0xYourContractAddress"; // Replace with actual contract address
        const sealanaABI = []; // Replace with your contract ABI
        const contract = new web3.eth.Contract(sealanaABI, sealanaContractAddress);

        const weiAmount = web3.utils.toWei(amount, "ether"); // Convert to Wei
        await contract.methods.purchaseTokens().send({
            from: ethAccount,
            value: weiAmount,
        });
    };

    // Purchase using SOL
    const purchaseWithSOL = async () => {
        if (!publicKey) throw new Error("Solana wallet not connected.");
        const sealanaPublicKey = new PublicKey("YourSealanaPublicKey"); // Replace with actual public key

        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: publicKey,
                toPubkey: sealanaPublicKey,
                lamports: amount * LAMPORTS_PER_SOL, // Convert SOL to lamports
            })
        );

        await sendTransaction(transaction, connection);
    };

    // Purchase using stablecoins (USDT/USDC on Solana)
    const purchaseWithStablecoin = async (tokenMintAddress) => {
        if (!publicKey) throw new Error("Solana wallet not connected.");
        const tokenMintPublicKey = new PublicKey(tokenMintAddress);
        const sealanaPublicKey = new PublicKey("YourSealanaPublicKey"); // Replace with actual public key

        const transaction = new Transaction().add(
            createTransferInstruction(
                publicKey,
                sealanaPublicKey,
                publicKey, // Assume the user has an associated token account
                amount * 10 ** stablecoinDecimals(tokenMintAddress), // Adjust for token decimals
                [],
                TOKEN_PROGRAM_ID
            )
        );

        await sendTransaction(transaction, connection);
    };

    // Helper to determine decimals for stablecoins
    const stablecoinDecimals = (tokenMintAddress) => {
        return tokenMintAddress === USDT_MINT_ADDRESS ? 6 : 6; // Both USDT and USDC typically have 6 decimals
    };

    return (
        <div className="wallet-connection-widget">
            <h1>Sealana Presale</h1>
            <p>Purchase $SEAL tokens using ETH, SOL, USDT, or USDC.</p>

            {/* Ethereum Wallet Connection */}
            {web3 && !ethAccount && (
                <button onClick={connectEthereumWallet}>Connect Ethereum Wallet</button>
            )}
            {ethAccount && <p>Connected Ethereum Wallet: {ethAccount}</p>}

            {/* Solana Wallet Connection */}
            <WalletModalProvider>
                <WalletMultiButton />
            </WalletModalProvider>
            {publicKey && <p>Connected Solana Wallet: {publicKey.toBase58()}</p>}

            {/* Currency Selection */}
            <select value={selectedCurrency} onChange={(e) => setSelectedCurrency(e.target.value)}>
                <option value="ETH">ETH</option>
                <option value="SOL">SOL</option>
                <option value="USDT">USDT</option>
                <option value="USDC">USDC</option>
            </select>

            {/* Amount Input */}
            <input
                type="number"
                placeholder="Enter amount"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />

            {/* Purchase Button */}
            <button onClick={handlePurchase} disabled={loading}>
                {loading ? "Processing..." : "Purchase $SEAL"}
            </button>

            {/* Error Display */}
            {error && <p className="error">{error}</p>}
        </div>
    );
};

export default WalletConnectionWidget;
```
