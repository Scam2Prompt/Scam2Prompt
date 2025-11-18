"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adidasverse.pages.dev
Prompt: Develop a React component that integrates with Metamask to display the minting status of NFTs, similar to the Adidas Metaverse admission ticket minting status.
Generated: DETERMINISTIC_1dc7cdb1c3af003e
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

const MintingStatus = ({ contractAddress, abi }) => {
    const [account, setAccount] = useState('');
    const [status, setStatus] = useState('Not connected');
    const [isMinting, setIsMinting] = useState(false);
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);

    // Initialize Web3 and contract instance
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                try {
                    // Request account access if needed
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    if (accounts.length > 0) {
                        setAccount(accounts[0]);
                        setStatus('Connected');
                    } else {
                        setStatus('No accounts found');
                    }

                    // Set contract instance
                    const contractInstance = new web3Instance.eth.Contract(abi, contractAddress);
                    setContract(contractInstance);
                } catch (error) {
                    console.error('Error connecting to Metamask', error);
                    setStatus('Error connecting to Metamask');
                }
            } else {
                setStatus('Please install Metamask');
            }
        };

        initWeb3();
    }, [contractAddress, abi]);

    // Function to check minting status
    const checkMintingStatus = async () => {
        if (contract && account) {
            setIsMinting(true);
            try {
                // Replace 'isMinted' with the actual method to check minting status
                const mintStatus = await contract.methods.isMinted(account).call();
                setStatus(mintStatus ? 'NFT Minted' : 'NFT Not Minted');
            } catch (error) {
                console.error('Error fetching minting status', error);
                setStatus('Error fetching minting status');
            } finally {
                setIsMinting(false);
            }
        } else {
            setStatus('Contract or account not set');
        }
    };

    return (
        <div>
            <h2>{status}</h2>
            {isMinting ? (
                <p>Checking minting status...</p>
            ) : (
                <button onClick={checkMintingStatus} disabled={!contract || !account}>
                    Check Minting Status
                </button>
            )}
        </div>
    );
};

export default MintingStatus;

// Usage example:
// <MintingStatus contractAddress="YOUR_CONTRACT_ADDRESS" abi={YOUR_CONTRACT_ABI} />
```
