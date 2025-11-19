"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Generate a smart contract in Solidity to manage the $ROOST token rewards distribution for the top contributors in a cryptocurrency presale.
Generated: DETERMINISTIC_ab158385509041a2
Batch ID: 20250612_163443
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionalities and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $ROOST token rewards distribution
contract RoostToken is ERC20, Ownable {
    // Mapping to track rewards for each contributor
    mapping(address => uint256) public rewards;

    // Event to log reward distribution
    event RewardsDistributed(address indexed contributor, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Roost Token", "$ROOST") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1,000,000 ROOST tokens
    }

    // Function to distribute rewards to top contributors
    // Only callable by the contract owner
    function distributeRewards(address[] calldata contributors, uint256[] calldata amounts) external onlyOwner {
        require(contributors.length == amounts.length, "Contributors and amounts must match");

        for (uint256 i = 0; i < contributors.length; i++) {
            // Check if the contributor's address is valid
            require(contributors[i] != address(0), "Invalid contributor address");

            // Update the rewards for the contributor
            rewards[contributors[i]] += amounts[i];

            // Emit event for the distributed rewards
            emit RewardsDistributed(contributors[i], amounts[i]);
        }
    }

    // Function to claim rewards by the contributor
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset the contributor's rewards
        rewards[msg.sender] = 0;

        // Transfer the rewards from the contract to the contributor
        _transfer(address(this), msg.sender, rewardAmount);
    }

    // Allow the owner to withdraw excess tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        // Transfer specified amount to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
