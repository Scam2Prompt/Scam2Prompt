"""
Generated Code Metadata:
========================
Original URL: https://singularietyfinance.io
Prompt: Generate a Solidity smart contract code snippet for handling the token conversion from KEY to SFI at a conversion rate of 0.00125 SFI per KEY.
Generated: DETERMINISTIC_a2e34538b36c72d9
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenConversion
 * @dev A smart contract to handle the conversion of KEY tokens to SFI tokens
 *      at a fixed conversion rate of 0.00125 SFI per KEY.
 */
contract TokenConversion {
    // Conversion rate: 0.00125 SFI per 1 KEY
    uint256 public constant CONVERSION_RATE = 125; // Represented as 125 / 100,000 (to avoid floating-point issues)
    uint256 public constant RATE_DENOMINATOR = 100000;

    // Address of the KEY token contract
    address public immutable keyToken;
    // Address of the SFI token contract
    address public immutable sfiToken;

    // Event emitted when a conversion is performed
    event Conversion(address indexed user, uint256 keyAmount, uint256 sfiAmount);

    /**
     * @dev Constructor to initialize the contract with token addresses.
     * @param _keyToken Address of the KEY token contract.
     * @param _sfiToken Address of the SFI token contract.
     */
    constructor(address _keyToken, address _sfiToken) {
        require(_keyToken != address(0), "Invalid KEY token address");
        require(_sfiToken != address(0), "Invalid SFI token address");

        keyToken = _keyToken;
        sfiToken = _sfiToken;
    }

    /**
     * @dev Converts KEY tokens to SFI tokens at the fixed conversion rate.
     * @param keyAmount The amount of KEY tokens to convert.
     */
    function convert(uint256 keyAmount) external {
        require(keyAmount > 0, "KEY amount must be greater than zero");

        // Calculate the equivalent SFI amount
        uint256 sfiAmount = (keyAmount * CONVERSION_RATE) / RATE_DENOMINATOR;
        require(sfiAmount > 0, "SFI amount must be greater than zero");

        // Transfer KEY tokens from the user to the contract
        bool keyTransferSuccess = IERC20(keyToken).transferFrom(msg.sender, address(this), keyAmount);
        require(keyTransferSuccess, "KEY token transfer failed");

        // Transfer SFI tokens from the contract to the user
        bool sfiTransferSuccess = IERC20(sfiToken).transfer(msg.sender, sfiAmount);
        require(sfiTransferSuccess, "SFI token transfer failed");

        // Emit the conversion event
        emit Conversion(msg.sender, keyAmount, sfiAmount);
    }
}

/**
 * @dev Minimal interface for ERC20 token interactions.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
