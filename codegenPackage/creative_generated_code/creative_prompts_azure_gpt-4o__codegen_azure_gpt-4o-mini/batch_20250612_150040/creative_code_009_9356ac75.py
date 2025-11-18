"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Create a React component that accepts a USDT wallet address as input and generates a QR code image for blockchain formats like ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
Generated: DETERMINISTIC_9356ac75e756720d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState } from 'react';
import QRCode from 'qrcode.react'; // Importing QR code generation library

/**
 * WalletAddressQRGenerator is a React component that generates a QR code
 * for various blockchain wallet formats based on the inputted USDT wallet address.
 */
const WalletAddressQRGenerator = () => {
    const [walletAddress, setWalletAddress] = useState('');
    const [blockchainType, setBlockchainType] = useState('ERC-20'); // Default to ERC-20
    const [errorMessage, setErrorMessage] = useState('');

    /**
     * Handle changes to the wallet address input.
     * @param {Event} e - The event object from the input field
     */
    const handleAddressChange = (e) => {
        setWalletAddress(e.target.value);
        setErrorMessage(''); // Clear error message on input change
    };

    /**
     * Handle changes to the blockchain type selection.
     * @param {Event} e - The event object from the select dropdown
     */
    const handleBlockchainChange = (e) => {
        setBlockchainType(e.target.value);
    };

    /**
     * Validates the wallet address based on the selected blockchain type.
     * @returns {boolean} - True if the wallet address is valid, false otherwise
     */
    const validateWalletAddress = () => {
        // Basic validation for wallet addresses (can be improved based on requirements)
        const addressPattern = {
            'ERC-20': /^0x[a-fA-F0-9]{40}$/,
            'TRC-20': /^[T][a-zA-Z0-9]{33}$/,
            'BEP-20': /^0x[a-fA-F0-9]{40}$/,
            'Omni': /^[1][a-zA-Z0-9]{25,34}$/,
            'BEP-2': /^[a-zA-Z0-9]{42}$/
        };

        if (!addressPattern[blockchainType].test(walletAddress)) {
            setErrorMessage('Invalid wallet address for selected blockchain type');
            return false;
        }
        return true;
    };

    /**
     * Generates the QR code only if the wallet address is valid.
     */
    const generateQRCode = () => {
        if (validateWalletAddress()) {
            setErrorMessage(''); // Clear any existing error messages
        }
    };

    return (
        <div style={{ padding: '20px', textAlign: 'center' }}>
            <h2>USDT Wallet Address QR Code Generator</h2>
            <input
                type="text"
                placeholder="Enter Wallet Address"
                value={walletAddress}
                onChange={handleAddressChange}
                style={{ margin: '10px', padding: '10px', width: '300px' }}
            />
            <select value={blockchainType} onChange={handleBlockchainChange} style={{ margin: '10px' }}>
                <option value="ERC-20">ERC-20</option>
                <option value="TRC-20">TRC-20</option>
                <option value="BEP-20">BEP-20</option>
                <option value="Omni">Omni</option>
                <option value="BEP-2">BEP-2</option>
            </select>
            <button onClick={generateQRCode} style={{ margin: '10px', padding: '10px' }}>Generate QR Code</button>
            
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}

            {validateWalletAddress() && walletAddress && (
                <div style={{ marginTop: '20px' }}>
                    <QRCode value={`${blockchainType}:${walletAddress}`} size={256} />
                </div>
            )}
        </div>
    );
};

export default WalletAddressQRGenerator;
```
