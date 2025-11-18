"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Write a smart contract function in Solidity that enables a wallet holding OUSD to opt-in for auto-compounding yield, as described in the Origin Dollar documentation.
Generated: DETERMINISTIC_6ce16cb7cc922c43
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title OUSD Auto-Compounding Opt-In Contract
 * @dev This contract allows OUSD holders to opt-in for auto-compounding yield.
 * @author Origin Protocol
 */

interface IOUSD {
    function balanceOf(address account) external view returns (uint256);
}

contract AutoCompoundingOptIn {
    // Mapping to track whether a wallet has opted in for auto-compounding
    mapping(address => bool) private _autoCompoundingEnabled;

    // Address of the OUSD token contract
    address private immutable _ousdToken;

    // Event emitted when a wallet opts in or out of auto-compounding
    event AutoCompoundingStatusUpdated(address indexed wallet, bool enabled);

    /**
     * @dev Constructor to set the OUSD token contract address.
     * @param ousdToken Address of the OUSD token contract
     */
    constructor(address ousdToken) {
        require(ousdToken != address(0), "Invalid OUSD token address");
        _ousdToken = ousdToken;
    }

    /**
     * @dev Function to opt-in or opt-out of auto-compounding yield.
     * @param enable Boolean indicating whether to enable or disable auto-compounding
     */
    function setAutoCompounding(bool enable) external {
        // Verify the caller holds OUSD
        IOUSD ousd = IOUSD(_ousdToken);
        uint256 balance = ousd.balanceOf(msg.sender);
        require(balance > 0, "Caller must hold OUSD to opt-in");

        // Update the auto-compounding status
        _autoCompoundingEnabled[msg.sender] = enable;

        // Emit event for tracking changes
        emit AutoCompoundingStatusUpdated(msg.sender, enable);
    }

    /**
     * @dev Function to check whether auto-compounding is enabled for a wallet.
     * @param wallet Address to check
     * @return Boolean indicating whether auto-compounding is enabled
     */
    function isAutoCompoundingEnabled(address wallet) external view returns (bool) {
        return _autoCompoundingEnabled[wallet];
    }
}
```
