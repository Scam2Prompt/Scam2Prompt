"""
Generated Code Metadata:
========================
Original URL: https://ion2.pages.dev
Prompt: Create a function in JavaScript to validate wallet addresses for Ethereum, Cosmos, BSC, or EVM and display eligibility results for an $ION giveaway.
Generated: DETERMINISTIC_a909efcd59b64cab
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates a wallet address for Ethereum, Cosmos, BSC, or EVM and checks eligibility for the $ION giveaway.
 */

// Import required libraries
const { ethers } = require('ethers');
const { Bech32 } = require('bech32');

/**
 * Validates a wallet address for the given blockchain.
 * @param {string} address - The wallet address to validate.
 * @param {string} blockchain - The blockchain to validate for (Ethereum, Cosmos, BSC, or EVM).
 * @returns {boolean} True if the address is valid, false otherwise.
 */
function validateAddress(address, blockchain) {
    try {
        switch (blockchain.toLowerCase()) {
            case 'ethereum':
            case 'evm':
                // Validate Ethereum/EVM address
                return ethers.utils.isAddress(address);
            case 'cosmos':
                // Validate Cosmos address
                try {
                    const decoded = Bech32.decode(address);
                    return decoded.prefix === 'cosmos' && decoded.bech32 === address;
                } catch (error) {
                    return false;
                }
            case 'bsc':
                // Validate BSC address (same as Ethereum)
                return ethers.utils.isAddress(address);
            default:
                throw new Error(`Unsupported blockchain: ${blockchain}`);
        }
    } catch (error) {
        console.error(`Error validating address: ${error.message}`);
        return false;
    }
}

/**
 * Checks eligibility for the $ION giveaway.
 * @param {string} address - The wallet address to check.
 * @param {string} blockchain - The blockchain to check for.
 * @returns {object} An object containing the eligibility result and a message.
 */
function checkEligibility(address, blockchain) {
    const isValid = validateAddress(address, blockchain);
    if (!isValid) {
        return { eligible: false, message: 'Invalid wallet address' };
    }

    // TO DO: implement actual eligibility logic here (e.g., check balance, previous participation, etc.)
    // For demonstration purposes, assume all valid addresses are eligible
    return { eligible: true, message: 'Congratulations, you are eligible for the $ION giveaway!' };
}

// Example usage
function main() {
    const addresses = [
        { address: '0x1234567890123456789012345678901234567890', blockchain: 'Ethereum' },
        { address: 'cosmos1q2w3e4r5t6z7y8u9i0o', blockchain: 'Cosmos' },
        { address: '0x9876543210987654321098765432109876543210', blockchain: 'BSC' },
        { address: 'invalid-address', blockchain: 'Ethereum' },
    ];

    addresses.forEach(({ address, blockchain }) => {
        const result = checkEligibility(address, blockchain);
        console.log(`Address: ${address} (${blockchain}) - Eligible: ${result.eligible}, Message: ${result.message}`);
    });
}

main();
```
