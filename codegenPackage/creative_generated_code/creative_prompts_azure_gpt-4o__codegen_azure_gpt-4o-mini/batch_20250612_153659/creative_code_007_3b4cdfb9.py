"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetdash-staking.vercel.app
Prompt: Recommend best practices for implementing secure wallet connections in a Next.js app for staking cryptocurrency, referencing the AssetDash staking system.
Generated: DETERMINISTIC_3b4cdfb96e95ae6b
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/api/connectWallet.js

import { NextApiRequest, NextApiResponse } from 'next';
import { ethers } from 'ethers';

// Function to connect to the user's Ethereum wallet securely
export default async function handler(req = NextApiRequest, res = NextApiResponse) {
    try {
        // Check if the request method is POST
        if (req.method !== 'POST') {
            return res.status(405).json({ message: 'Method Not Allowed' });
        }

        // Validate the request body
        const { walletAddress } = req.body;
        if (!walletAddress || !ethers.utils.isAddress(walletAddress)) {
            return res.status(400).json({ message: 'Invalid wallet address' });
        }

        // Connect to the Ethereum network (Mainnet or specify your network)
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Request account access
        await provider.send('eth_requestAccounts', []);

        // Get the connected signer (user's wallet)
        const signer = provider.getSigner();
        
        // Log the connected wallet address
        const userAddress = await signer.getAddress();

        // Check if the connected wallet matches the provided address
        if (userAddress.toLowerCase() !== walletAddress.toLowerCase()) {
            return res.status(401).json({ message: 'Unauthorized: Wallet address does not match' });
        }

        // Successful connection response
        return res.status(200).json({ message: 'Wallet connected successfully', address: userAddress });
    } catch (error) {
        console.error('Error connecting wallet:', error);
        return res.status(500).json({ message: 'Internal Server Error' });
    }
}

// Utility function to initialize the wallet connection
export const connectWallet = async () => {
    if (typeof window !== 'undefined' && window.ethereum) {
        try {
            const response = await fetch('/api/connectWallet', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ walletAddress: window.ethereum.selectedAddress }),
            });

            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.message || 'Failed to connect wallet');
            }
            return data;
        } catch (error) {
            console.error('Wallet connection error:', error);
            throw error; // Propagate error to the caller
        }
    } else {
        throw new Error('Ethereum provider not found. Please install MetaMask or similar wallet.');
    }
};

// Sample usage in a React component
// import { connectWallet } from '../api/connectWallet';

// const YourComponent = () => {
//     const handleConnect = async () => {
//         try {
//             const result = await connectWallet();
//             console.log(result.message); // Successfully connected
//         } catch (error) {
//             alert(error.message); // Handle error gracefully
//         }
//     };

//     return (
//         <button onClick={handleConnect}>Connect Wallet</button>
//     );
// };
```
