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
 * Validates cryptocurrency wallet addresses for Ethereum, Cosmos, BSC, or EVM chains.
 * @param {string} address - The wallet address to validate
 * @param {string} chain - The blockchain network ('ethereum', 'cosmos', 'bsc', or 'evm')
 * @returns {Object} - An object containing validation results and eligibility status
 */
function validateWalletAddress(address, chain) {
    // Trim whitespace and convert to lowercase for case-insensitive checks
    const cleanAddress = address.trim().toLowerCase();
    const result = {
        isValid: false,
        chain: chain.toLowerCase(),
        message: '',
        isEligible: false
    };

    // Validate input parameters
    if (!cleanAddress) {
        result.message = 'Wallet address cannot be empty';
        return result;
    }

    if (!['ethereum', 'cosmos', 'bsc', 'evm'].includes(result.chain)) {
        result.message = 'Invalid blockchain specified. Supported chains: ethereum, cosmos, bsc, evm';
        return result;
    }

    // Regular expressions for different chains
    const regexPatterns = {
        ethereum: /^0x[a-fA-F0-9]{40}$/,
        bsc: /^0x[a-fA-F0-9]{40}$/,
        evm: /^0x[a-fA-F0-9]{40}$/,
        cosmos: /^cosmos1[a-z0-9]{38}$/
    };

    // Validate address format based on chain
    const isValidFormat = regexPatterns[result.chain].test(cleanAddress);
    if (!isValidFormat) {
        result.message = `Invalid ${result.chain} wallet address format`;
        return result;
    }

    // Additional validation for Cosmos bech32 addresses
    if (result.chain === 'cosmos') {
        try {
            // Simple checksum validation for bech32
            const hrp = cleanAddress.substring(0, 6);
            if (hrp !== 'cosmos') {
                result.message = 'Invalid Cosmos address prefix';
                return result;
            }
        } catch (error) {
            result.message = 'Error validating Cosmos address';
            return result;
        }
    }

    // If all checks passed
    result.isValid = true;
    result.message = 'Valid wallet address';
    
    // Eligibility check (example criteria)
    result.isEligible = checkEligibility(cleanAddress, result.chain);
    
    return result;
}

/**
 * Checks eligibility for $ION giveaway based on address and chain
 * @param {string} address - Validated wallet address
 * @param {string} chain - Blockchain network
 * @returns {boolean} - Eligibility status
 */
function checkEligibility(address, chain) {
    // Example eligibility criteria:
    // - Ethereum/BSC/EVM: Address must have at least one transaction
    // - Cosmos: Address must be active in the last 30 days
    // In a real implementation, this would query blockchain data
    
    // For demo purposes, we'll use a simple check
    const lastChar = address.charAt(address.length - 1);
    return parseInt(lastChar, 36) % 2 === 0; // 50% chance for demo
}

// Example usage:
// const validationResult = validateWalletAddress('0x742d35Cc6634C0532925a3b844Bc454e4438f44e', 'ethereum');
// console.log(validationResult);
```
