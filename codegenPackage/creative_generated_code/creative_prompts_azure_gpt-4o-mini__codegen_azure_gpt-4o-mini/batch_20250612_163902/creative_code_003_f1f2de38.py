"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-io.web.app
Prompt: Explain how to create a user-friendly interface for the Crudo Protocol that allows users to connect their wallets and participate in the presale.
Generated: DETERMINISTIC_f1f2de3848de6203
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { Button, Modal, Input, Alert } from 'antd';

// Initialize web3
const web3 = new Web3(window.ethereum);

// Define the main component
const CrudoPresale = () => {
    // State variables for wallet connection and presale participation
    const [account, setAccount] = useState('');
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [inputValue, setInputValue] = useState('');
    const [error, setError] = useState('');

    // Function to connect wallet
    const connectWallet = async () => {
        try {
            const accounts = await web3.eth.requestAccounts();
            setAccount(accounts[0]);
            setError('');
        } catch (err) {
            console.error('Failed to connect wallet:', err);
            setError('Failed to connect wallet. Please try again.');
        }
    };

    // Function to handle presale participation
    const participateInPresale = async () => {
        setError(''); // Clear previous errors
        try {
            // Assume `presaleContract` is a previously initialized contract instance
            const amount = web3.utils.toWei(inputValue, 'ether');
            await presaleContract.methods.participate().send({ from: account, value: amount });
            alert('Successfully participated in presale!');
        } catch (err) {
            console.error('Participation failed:', err);
            setError('Failed to participate in presale. Please check your input and try again.');
        }
    };

    // Effect to enable wallet connection on component mount
    useEffect(() => {
        if (window.ethereum) {
            window.ethereum.on('accountsChanged', (accounts) => {
                setAccount(accounts[0]);
            });
        }
    }, []);

    return (
        <div>
            <h1>Crudo Protocol Presale</h1>
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <Button type="primary" onClick={() => setIsModalVisible(true)}>
                        Participate in Presale
                    </Button>
                </div>
            ) : (
                <Button type="primary" onClick={connectWallet}>
                    Connect Wallet
                </Button>
            )}

            {/* Modal for participation */}
            <Modal
                title="Participate in Presale"
                visible={isModalVisible}
                onOk={participateInPresale}
                onCancel={() => setIsModalVisible(false)}
            >
                <Input
                    placeholder="Amount in ETH"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    type="number"
                    min="0"
                />
                {error && <Alert message={error} type="error" showIcon />}
            </Modal>
        </div>
    );
};

// Export the component for use in the application
export default CrudoPresale;
```
