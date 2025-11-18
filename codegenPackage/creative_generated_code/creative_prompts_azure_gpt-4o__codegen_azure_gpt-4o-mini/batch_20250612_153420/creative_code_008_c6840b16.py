"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefcom.pages.dev
Prompt: Create a Solidity contract for distributing BEEF tokens in an airdrop, ensuring that 10% of the total supply is allocated for this purpose.
Generated: DETERMINISTIC_c6840b163ea091d7
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BEEFToken
 * @dev ERC20 Token with airdrop functionality
 */
contract BEEFToken is ERC20, Ownable {
    uint256 public constant AIRDROP_PERCENTAGE = 10; // Percentage of total supply for airdrop
    uint256 public airdropAmount; // Amount allocated for airdrop
    mapping(address => bool) public airdropClaimed; // Track addresses that have claimed their airdrop

    /**
     * @dev Constructor that mints totalSupply of tokens to the owner
     */
    constructor(uint256 totalSupply) ERC20("BEEF Token", "BEEF") {
        require(totalSupply > 0, "Total supply must be greater than zero");
        _mint(msg.sender, totalSupply);
        airdropAmount = (totalSupply * AIRDROP_PERCENTAGE) / 100; // Calculate airdrop amount
    }

    /**
     * @dev Function to airdrop tokens to a list of addresses
     * @param recipients List of addresses to receive airdrop
     */
    function airdropTokens(address[] calldata recipients) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(airdropAmount > 0, "No airdrop tokens available");

        uint256 totalAirdrop = recipients.length * (airdropAmount / totalSupply()); // Calculate total airdrop

        require(totalAirdrop <= airdropAmount, "Not enough tokens for airdrop");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(!airdropClaimed[recipient], "Airdrop already claimed by this address");
            require(recipient != address(0), "Invalid recipient address");

            // Transfer airdrop tokens to recipient
            _transfer(owner(), recipient, airdropAmount / recipients.length); 
            airdropClaimed[recipient] = true; // Mark as claimed
        }

        airdropAmount -= totalAirdrop; // Decrease airdrop amount after distribution
    }

    /**
     * @dev Function to check if an address has claimed their airdrop
     * @param account Address to check
     * @return bool indicating if the airdrop was claimed
     */
    function hasClaimedAirdrop(address account) external view returns (bool) {
        return airdropClaimed[account];
    }
}
```
