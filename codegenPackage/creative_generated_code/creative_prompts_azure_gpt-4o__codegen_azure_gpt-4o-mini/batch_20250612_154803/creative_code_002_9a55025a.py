"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multisig-astronize-hotwallet.bitkubblockchain.net
Prompt: Generate a script to connect to the Multi Sig Wallet Tool on Bitkub blockchain and verify wallet signatures using Metamask.
Generated: DETERMINISTIC_9a55025ae4b0d490
Batch ID: 20250612_154803
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Constants
const MULTI_SIG_WALLET_ADDRESS = 'YOUR_MULTISIG_WALLET_ADDRESS'; // Replace with your Multi-Sig Wallet address
const METAMASK_PROVIDER = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura Project ID

// Initialize Web3 with Metamask provider
const web3 = new Web3(window.ethereum);

// Enable Ethereum provider
async function enableEthereum() {
    if (window.ethereum) {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Ethereum accounts connected.');
        } catch (error) {
            console.error('User denied account access:', error);
        }
    } else {
        console.error('Metamask is not installed. Please install it.');
        alert('Metamask is not installed. Please install it.');
    }
}

// Verify signatures against the Multi-Sig Wallet
async function verifySignature(message, signature) {
    try {
        // Recover the address from the signature
        const signerAddress = ethers.utils.verifyMessage(message, signature);
        
        // Get the list of owners from the Multi-Sig Wallet Contract
        const multiSigWalletContract = new web3.eth.Contract(MULTI_SIG_WALLET_ABI, MULTI_SIG_WALLET_ADDRESS);
        
        // Fetch owners
        const owners = await multiSigWalletContract.methods.getOwners().call();

        // Check if the recovered address is one of the owners
        if (owners.includes(signerAddress)) {
            console.log('Signature verified: ', signerAddress);
            return true;
        } else {
            console.error('Signature verification failed: Address not an owner');
            return false;
        }
    } catch (error) {
        console.error('Error verifying signature:', error);
        return false;
    }
}

// Execute the connection and verification process
async function main() {
    await enableEthereum();

    const message = 'Your message to verify'; // Replace with the message you want to verify
    const signature = 'SIGNATURE_FROM_THE_USER'; // Replace with the signature provided by the user

    const isVerified = await verifySignature(message, signature);
    if (isVerified) {
        console.log('The signature is valid.');
    } else {
        console.log('The signature is invalid or not from an authorized owner.');
    }
}

// Run the main function
main();
```

**Note**: Make sure to replace `YOUR_MULTISIG_WALLET_ADDRESS` and `YOUR_INFURA_PROJECT_ID` with the actual Multi-Sig Wallet address and your Infura Project ID. Also ensure that `MULTI_SIG_WALLET_ABI` is defined elsewhere in your code with the correct ABI for the Multi-Sig Wallet contract.
