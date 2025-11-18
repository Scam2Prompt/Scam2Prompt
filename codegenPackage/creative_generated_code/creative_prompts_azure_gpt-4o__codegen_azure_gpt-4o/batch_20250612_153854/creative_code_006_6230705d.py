"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Create a function in Solidity that handles airdrops for the MegaRabbit NFT collection, ensuring these count toward the total supply limit.
Generated: DETERMINISTIC_6230705d7f1fdd66
Batch ID: 20250612_153854
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
 * @title MegaRabbitAirdrop
 * @dev Handles airdrops for the MegaRabbit NFT collection while enforcing the total supply limit.
 */
contract MegaRabbitAirdrop {
    // State variables
    uint256 public totalSupply;
    uint256 public maxSupply;
    address public owner;
    mapping(address => uint256) public airdropped; // Keeps track of addresses that have received airdrops

    // Events
    event Airdrop(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner!");
        _;
    }

    modifier withinSupplyLimit(uint256 _amount) {
        require(totalSupply + _amount <= maxSupply, "Exceeds max supply!");
        _;
    }

    // Constructor
    constructor(uint256 _maxSupply) {
        owner = msg.sender;
        maxSupply = _maxSupply;
        totalSupply = 0; // Initialize the total supply to 0
    }

    /**
     * @dev Airdrops NFTs to recipients while ensuring the total supply does not exceed the limit.
     * @param recipients Array of recipient addresses.
     * @param amount Number of NFTs to airdrop to each recipient.
     */
    function airdrop(address[] memory recipients, uint256 amount)
        external
        onlyOwner
        withinSupplyLimit(recipients.length * amount)
    {
        require(amount > 0, "Airdrop amount must be greater than 0!");
        require(recipients.length > 0, "Recipients list cannot be empty!");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address!");

            airdropped[recipients[i]] += amount; // Update airdrop mapping
            emit Airdrop(recipients[i], amount); // Emit the airdrop event
        }

        totalSupply += recipients.length * amount; // Update the total supply
    }

    /**
     * @dev Updates the max supply limit.
     * @param newMaxSupply New max supply value.
     */
    function updateMaxSupply(uint256 newMaxSupply) external onlyOwner {
        require(newMaxSupply >= totalSupply, "New max supply cannot be less than the current total supply!");
        maxSupply = newMaxSupply;
    }
}
```
