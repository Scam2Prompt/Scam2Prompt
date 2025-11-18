"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiro.pages.dev
Prompt: Write a smart contract in Solidity for an Ethereum-based token similar to $neiro, including functionality for rewarding participants in the project.
Generated: DETERMINISTIC_c57811e2ea7d846a
Batch ID: 20250612_151811
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The NeiroToken contract inherits from the ERC20 and Ownable contracts
contract NeiroToken is ERC20, Ownable {
    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Event to signal when rewards are distributed
    event RewardsDistributed(address indexed beneficiary, uint256 amount);
    
    // Total supply of the token
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens, with 18 decimals

    // Constructor to initialize the token
    constructor() ERC20("Neiro Token", "NEIRO") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
    }

    // Function to distribute rewards to participants
    function distributeRewards(address[] calldata beneficiaries, uint256[] calldata amounts) external onlyOwner {
        require(beneficiaries.length == amounts.length, "Mismatched arrays");
        
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            require(beneficiaries[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Invalid reward amount");
            require(balanceOf(msg.sender) >= amounts[i], "Insufficient balance");

            // Transfer the reward to the beneficiary
            _transfer(msg.sender, beneficiaries[i], amounts[i]);
            // Update the rewards mapping
            rewards[beneficiaries[i]] += amounts[i];
            emit RewardsDistributed(beneficiaries[i], amounts[i]); // Emit event for tracking
        }
    }

    // Function to retrieve the total rewards for a given address
    function getRewards(address beneficiary) external view returns (uint256) {
        return rewards[beneficiary];
    }
    
    // Function to burn tokens (optional)
    function burn(uint256 amount) external {
        _burn(msg.sender, amount); // Allow users to burn their own tokens
    }
}
```
