"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-nft-dapp-frontend.vercel.app
Prompt: How do I implement wallet connection functionality in a Sui NFT Dapp?
Generated: DETERMINISTIC_738e37c747d354db
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { useEffect, useState } from 'react';
import { SuiClient, WalletProvider, useWallet } from '@mysten/sui'; // Example Sui SDK

// Define the WalletConnect component
const WalletConnect = () => {
    // State to manage wallet connection status and address
    const [isConnected, setIsConnected] = useState(false);
    const [walletAddress, setWalletAddress] = useState(null);
    
    // Get wallet connection methods from the useWallet hook
    const wallet = useWallet();

    // Effect to handle wallet connection status changes
    useEffect(() => {
        const handleConnection = async () => {
            try {
                // Check if the wallet is connected
                if (wallet.connected) {
                    setIsConnected(true);
                    setWalletAddress(wallet.address);
                } else {
                    setIsConnected(false);
                    setWalletAddress(null);
                }
            } catch (error) {
                console.error('Error checking wallet connection:', error);
                // Handle error (e.g., show notification to the user)
            }
        };

        handleConnection();
    }, [wallet.connected, wallet.address]);

    // Function to connect the wallet
    const connectWallet = async () => {
        try {
            await wallet.connect(); // Connecting to the wallet
            setIsConnected(true);
            setWalletAddress(wallet.address);
        } catch (error) {
            console.error('Error connecting to wallet:', error);
            // Notify the user about the connection issue
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        wallet.disconnect(); // Disconnecting from the wallet
        setIsConnected(false);
        setWalletAddress(null);
    };

    return (
        <div>
            <h1>Sui NFT DApp Wallet Connection</h1>
            {isConnected ? (
                <div>
                    <p>Connected Wallet: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the WalletConnect component
export default WalletConnect;

// Usage example (in App.js or a similar file)
// import WalletConnect from './WalletConnect';
// function App() {
//     return (
//         <WalletProvider>
//             <WalletConnect />
//         </WalletProvider>
//     );
// }

```
