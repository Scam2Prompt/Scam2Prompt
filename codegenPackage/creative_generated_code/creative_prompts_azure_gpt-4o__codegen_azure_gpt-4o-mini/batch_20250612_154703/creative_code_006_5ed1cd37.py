"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarterm.org
Prompt: Generate code to implement a StellarTerm-like modal for swapping assets (e.g., XLM to USDC) on the Stellar Decentralized Exchange, ensuring it adheres to the open-source principles of StellarTerm.
Generated: DETERMINISTIC_5ed1cd37bafcd7f5
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import StellarSdk from 'stellar-sdk';
import { Button, Modal, Input, Select, notification } from 'antd';

const { Option } = Select;

// Function to fetch the available asset pairs for swapping
const fetchAssetPairs = async () => {
    // Fetch the asset pairs from Stellar DEX or any reliable API
    // This is a placeholder; replace with actual API call
    return [
        { base: 'XLM', counter: 'USDC' },
        { base: 'USDC', counter: 'XLM' },
        // Add more pairs as needed
    ];
};

// Main component for the asset swap modal
const SwapModal = ({ visible, onClose }) => {
    const [assetPairs, setAssetPairs] = useState([]);
    const [baseAsset, setBaseAsset] = useState('XLM');
    const [counterAsset, setCounterAsset] = useState('USDC');
    const [amount, setAmount] = useState('');
    const [exchangeRate, setExchangeRate] = useState(0);

    // Fetch asset pairs when the component mounts
    useEffect(() => {
        const getAssetPairs = async () => {
            try {
                const pairs = await fetchAssetPairs();
                setAssetPairs(pairs);
            } catch (error) {
                notification.error({
                    message: 'Error fetching asset pairs',
                    description: error.message,
                });
            }
        };

        getAssetPairs();
    }, []);

    // Function to handle the swap
    const handleSwap = async () => {
        try {
            // Validate input
            if (!amount || isNaN(amount) || amount <= 0) {
                throw new Error('Please enter a valid amount.');
            }

            // Implement actual swap logic using Stellar SDK or your backend API
            // Placeholder for the swapping logic
            console.log(`Swapping ${amount} ${baseAsset} to ${counterAsset}...`);

            // Display success notification
            notification.success({
                message: 'Swap Successful',
                description: `Successfully swapped ${amount} ${baseAsset} to ${counterAsset}.`,
            });

            // Reset fields after successful swap
            setAmount('');
        } catch (error) {
            notification.error({
                message: 'Swap Failed',
                description: error.message,
            });
        }
    };

    // Handle changes in the base and counter assets
    const handleBaseAssetChange = (value) => {
        setBaseAsset(value);
        setCounterAsset(value === 'XLM' ? 'USDC' : 'XLM'); // Swap counter asset based on base asset
    };

    // Render the modal component
    return (
        <Modal
            title="Swap Assets"
            visible={visible}
            onCancel={onClose}
            footer={[
                <Button key="swap" type="primary" onClick={handleSwap}>
                    Swap
                </Button>,
                <Button key="cancel" onClick={onClose}>
                    Cancel
                </Button>,
            ]}
        >
            <Select value={baseAsset} onChange={handleBaseAssetChange} style={{ width: '100%', marginBottom: '16px' }}>
                {assetPairs.map((pair, index) => (
                    <Option key={index} value={pair.base}>{pair.base}</Option>
                ))}
            </Select>
            <Input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder={`Amount in ${baseAsset}`}
                style={{ marginBottom: '16px' }}
            />
            <p>
                Exchange Rate: {exchangeRate} {counterAsset} per {baseAsset}
            </p>
        </Modal>
    );
};

// PropTypes validation for the SwapModal component
SwapModal.propTypes = {
    visible: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
};

export default SwapModal;
```
