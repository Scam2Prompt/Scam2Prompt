"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Generate an example of a smart contract that utilizes low gas fees on the Metis Layer 2 network.
Generated: DETERMINISTIC_c183b4a5d6ae9bc9
Batch ID: 20250612_161301
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SimpleStorage
 * @dev A simple contract to store and retrieve a value, optimized for low gas usage on Metis Layer 2.
 */
contract SimpleStorage is Ownable {
    // Variable to store the value
    uint256 private storedValue;

    /**
     * @dev Event emitted when the stored value is updated.
     * @param oldValue The previous value before update.
     * @param newValue The new updated value.
     */
    event ValueUpdated(uint256 oldValue, uint256 newValue);

    /**
     * @dev Sets the initial value of storedValue.
     * @param initialValue The initial value to set.
     */
    constructor(uint256 initialValue) {
        require(initialValue > 0, "Initial value must be greater than 0");
        storedValue = initialValue;
    }

    /**
     * @dev Updates the stored value.
     * @param newValue The new value to store.
     */
    function updateValue(uint256 newValue) external onlyOwner {
        require(newValue != storedValue, "New value must be different");
        
        uint256 oldValue = storedValue;
        storedValue = newValue;
        
        emit ValueUpdated(oldValue, newValue);
    }

    /**
     * @dev Retrieves the current stored value.
     * @return The current stored value.
     */
    function getValue() external view returns (uint256) {
        return storedValue;
    }
}
```
