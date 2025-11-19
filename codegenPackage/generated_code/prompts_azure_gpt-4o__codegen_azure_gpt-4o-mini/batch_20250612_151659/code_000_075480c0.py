"""
Generated Code Metadata:
========================
Original URL: https://nft-minting-app-main.pages.dev
Prompt: Write JavaScript code to create a simple NFT minting application similar to the functionality described on the ALPACADABRAZ NFT website. Ensure the app requires JavaScript to run properly.
Generated: DETERMINISTIC_075480c01535654a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { useState, useEffect } from 'react';

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Smart contract ABI and address (replace with actual values)
const contractABI = [ /* ABI goes here */ ];
const contractAddress = '0xYourContractAddressHere';

// Create a functional component for the NFT minting application
const MintNFT = () => {
    // State variables for managing user input and transaction status
    const [account, setAccount] = useState('');
    const [minting, setMinting] = useState(false);
    const [error, setError] = useState(null);
    const [tokenURI, setTokenURI] = useState('');

    // Function to connect to the user's wallet
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (err) {
            console.error('Error connecting to wallet:', err);
            setError('Failed to connect wallet. Please try again.');
        }
    };

    // Function to mint the NFT
    const mintNFT = async () => {
        if (!tokenURI) {
            setError('Token URI is required.');
            return;
        }

        setMinting(true);
        setError(null);

        try {
            const contract = new web3.eth.Contract(contractABI, contractAddress);
            const transaction = await contract.methods.mintNFT(account, tokenURI).send({ from: account });

            console.log('Transaction successful:', transaction);
            alert('NFT minted successfully!');
        } catch (err) {
            console.error('Error minting NFT:', err);
            setError('Failed to mint NFT. Please check the console for details.');
        } finally {
            setMinting(false);
        }
    };

    // Effect to check if the user is already connected
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                }
            }
        };
        checkWalletConnection();
    }, []);

    return (
        <div>
            <h1>Mint Your NFT</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <button onClick={connectWallet}>
                {account ? `Connected: ${account}` : 'Connect Wallet'}
            </button>
            <div>
                <input
                    type="text"
                    placeholder="Enter Token URI"
                    value={tokenURI}
                    onChange={(e) => setTokenURI(e.target.value)}
                />
                <button onClick={mintNFT} disabled={minting || !account}>
                    {minting ? 'Minting...' : 'Mint NFT'}
                </button>
            </div>
        </div>
    );
};

// Export the MintNFT component
export default MintNFT;
```

### Notes:
- Replace `/* ABI goes here */` with the actual ABI of your NFT smart contract.
- Replace `'0xYourContractAddressHere'` with the actual deployed contract address.
- Ensure that the application is running in an environment that supports React and has access to the Ethereum provider (like MetaMask).
