"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Develop a web3 integration script that connects a MetaMask wallet to the Pepe Unchained presale platform for purchasing and staking $PEPU tokens.
Generated: DETERMINISTIC_9d7fd99a80f5be9f
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // Web3 library for Ethereum interaction
import { ethers } from 'ethers'; // Ethers.js for wallet interaction
import { useEffect, useState } from 'react'; // React hooks for state management
import { ToastContainer, toast } from 'react-toastify'; // For notifications

// Define the contract address and ABI (Application Binary Interface)
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress'; // Replace with the actual token contract address
const TOKEN_ABI = [ /* ... ABI Array ... */ ]; // Replace with the actual ABI

// Main functional component for the integration
const PepeUnchainedPresale = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);

    // Connect to MetaMask wallet on component mount
    useEffect(() => {
        const initializeWeb3 = async () => {
            // Check if MetaMask is installed
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
                
                try {
                    // Request account access
                    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    setAccount(accounts[0]);
                    // Initialize contract
                    const tokenContract = new web3Instance.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
                    setContract(tokenContract);
                } catch (error) {
                    // Handle errors during account access
                    toast.error('Error accessing your MetaMask account. Please check your wallet.');
                    console.error('Error connecting to MetaMask', error);
                }
            } else {
                // Handle the case where MetaMask is not installed
                toast.error('MetaMask is not installed. Please install it to use this feature.');
            }
        };
        
        initializeWeb3();
    }, []);

    // Function to handle token purchase
    const purchaseTokens = async (amount) => {
        if (!contract || !account) {
            toast.error('You must connect to your MetaMask wallet first.');
            return;
        }

        try {
            const value = web3.utils.toWei(amount.toString(), 'ether'); // Convert to wei
            await contract.methods.buyTokens().send({ from: account, value });
            toast.success('Tokens purchased successfully!');
        } catch (error) {
            // Handle errors during the transaction
            toast.error('Error purchasing tokens. Please try again.');
            console.error('Purchase error', error);
        }
    };

    // Function to stake tokens
    const stakeTokens = async (amount) => {
        if (!contract || !account) {
            toast.error('You must connect to your MetaMask wallet first.');
            return;
        }

        try {
            await contract.methods.stakeTokens(amount).send({ from: account });
            toast.success('Tokens staked successfully!');
        } catch (error) {
            // Handle errors during the staking process
            toast.error('Error staking tokens. Please try again.');
            console.error('Staking error', error);
        }
    };

    // Render the component
    return (
        <div>
            <h1>Pepe Unchained Presale</h1>
            <p>Connected account: {account ? account : 'Not connected'}</p>
            <button onClick={() => purchaseTokens(0.1)}>Purchase 0.1 $PEPU</button>
            <button onClick={() => stakeTokens(10)}>Stake 10 $PEPU</button>
            <ToastContainer />
        </div>
    );
};

export default PepeUnchainedPresale;
```

### Notes:
- Make sure to replace `TOKEN_CONTRACT_ADDRESS` and `TOKEN_ABI` with the actual contract address and ABI for the Pepe Unchained token.
- The function `buyTokens()` and `stakeTokens(amount)` assumes you have those methods defined in your smart contract.
- Error handling is implemented for connecting to the wallet, purchasing tokens, and staking tokens.
- A notification system (using `react-toastify`) is included for user feedback.
