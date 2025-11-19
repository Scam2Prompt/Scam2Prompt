"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: How do I set the initial supply and maximum sell per person for a token on TicketChain?
Generated: DETERMINISTIC_b53e0e890f1b11ff
Batch ID: 20250612_162346
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
 * @title TicketChainToken
 * @dev A contract for managing token supply and maximum sell per person.
 * This contract follows ERC20 standards for creating and managing a token on the blockchain.
 */
contract TicketChainToken {
    // State variables
    uint256 public initialSupply;       // The total supply of tokens at contract creation
    uint256 public maxSellPerPerson;    // The maximum number of tokens one person can sell

    address public owner;               // The address of the contract owner

    event InitialSupplySet(uint256 supply);          // Emitted when the initial supply is set
    event MaxSellPerPersonSet(uint256 maxSell);      // Emitted when the max sell per person is set

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the contract owner and initializes default values.
     */
    constructor() {
        owner = msg.sender; // Set contract owner to the deployer
    }

    /**
     * @dev Function to set the initial supply of the token.
     * @param _supply The initial supply value to be set.
     * Requirements:
     * - Only the owner can call this function.
     * - The initial supply must be greater than zero.
     */
    function setInitialSupply(uint256 _supply) external onlyOwner {
        require(_supply > 0, "Initial supply must be greater than zero");
        initialSupply = _supply;

        // Emit an event for tracking supply updates
        emit InitialSupplySet(_supply);
    }

    /**
     * @dev Function to set the maximum sell limit per person.
     * @param _maxSell The maximum number of tokens one person can sell.
     * Requirements:
     * - Only the owner can call this function.
     * - The max sell limit must be greater than zero.
     */
    function setMaxSellPerPerson(uint256 _maxSell) external onlyOwner {
        require(_maxSell > 0, "Max sell per person must be greater than zero");
        maxSellPerPerson = _maxSell;

        // Emit an event for tracking limit updates
        emit MaxSellPerPersonSet(_maxSell);
    }
}
```
