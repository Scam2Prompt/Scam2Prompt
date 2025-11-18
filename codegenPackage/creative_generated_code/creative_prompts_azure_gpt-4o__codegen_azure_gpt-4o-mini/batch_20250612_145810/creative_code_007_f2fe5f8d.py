"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-secret.vercel.app
Prompt: Write a React component that uses MetaMask to sign a message and verify the signature on the blockchain.
Generated: DETERMINISTIC_f2fe5f8dc25b9eea
Batch ID: 20250612_145810
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

/**
 * MetaMaskSigner component allows users to sign a message using MetaMask
 * and verify the signature on the blockchain.
 */
const MetaMaskSigner = () => {
    const [account, setAccount] = useState(null);
    const [message, setMessage] = useState('');
    const [signature, setSignature] = useState('');
    const [isVerified, setIsVerified] = useState(null);
    const web3 = new Web3(window.ethereum);

    // Request user accounts on component mount
    useEffect(() => {
        const fetchAccounts = async () => {
            if (window.ethereum) {
                try {
                    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    setAccount(accounts[0]);
                } catch (error) {
                    console.error("Error fetching accounts: ", error);
                }
            } else {
                console.error("Please install MetaMask!");
            }
        };
        fetchAccounts();
    }, []);

    /**
     * Sign the message using MetaMask
     */
    const signMessage = async () => {
        if (!account) {
            console.error("Account not connected");
            return;
        }
        try {
            const signedMessage = await web3.eth.personal.sign(message, account);
            setSignature(signedMessage);
        } catch (error) {
            console.error("Error signing message: ", error);
        }
    };

    /**
     * Verify the signature on the blockchain
     */
    const verifySignature = async () => {
        if (!signature || !account) {
            console.error("Signature or account is missing");
            return;
        }
        try {
            const signer = await web3.eth.personal.ecRecover(message, signature);
            setIsVerified(signer.toLowerCase() === account.toLowerCase());
        } catch (error) {
            console.error("Error verifying signature: ", error);
        }
    };

    return (
        <div>
            <h2>MetaMask Message Signer</h2>
            <div>
                <label>Message:</label>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Enter message to sign"
                />
            </div>
            <button onClick={signMessage}>Sign Message</button>
            {signature && (
                <div>
                    <h3>Signature:</h3>
                    <p>{signature}</p>
                    <button onClick={verifySignature}>Verify Signature</button>
                </div>
            )}
            {isVerified !== null && (
                <div>
                    <h3>Verification Result:</h3>
                    <p>{isVerified ? "Signature is valid!" : "Signature is invalid."}</p>
                </div>
            )}
        </div>
    );
};

export default MetaMaskSigner;
```
