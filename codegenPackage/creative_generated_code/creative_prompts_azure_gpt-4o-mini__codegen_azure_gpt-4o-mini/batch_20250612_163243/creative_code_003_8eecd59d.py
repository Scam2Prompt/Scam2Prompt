"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api-cloudrectifier.pages.dev
Prompt: Provide an example of how to claim rewards using the Multichain protocol in a smart contract.
Generated: DETERMINISTIC_8eecd59dced9b974
Batch ID: 20250612_163243
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

// Importing the necessary interfaces for ERC20 and Multichain
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MultichainRewards is Ownable {
    // State variable to store the address of the rewards token
    IERC20 public rewardsToken;

    // Mapping to track whether an address has claimed rewards
    mapping(address => bool) public hasClaimed;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to initialize the rewards token address
     * @param _rewardsToken address of the ERC20 token contract for rewards
     */
    constructor(address _rewardsToken) {
        require(_rewardsToken != address(0), "Invalid token address");
        rewardsToken = IERC20(_rewardsToken);
    }

    /**
     * @dev Function to claim rewards
     * @param amount The amount of rewards to claim
     */
    function claimRewards(uint256 amount) external {
        // Check that the user has not already claimed rewards
        require(!hasClaimed[msg.sender], "Rewards already claimed");

        // Check that the contract has enough tokens to fulfill the claim
        require(rewardsToken.balanceOf(address(this)) >= amount, "Insufficient rewards in contract");

        // Update the claimed status for the user
        hasClaimed[msg.sender] = true;

        // Transfer the rewards to the claimant
        bool success = rewardsToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the rewards claimed event
        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw any leftover tokens
     * @param to The address to send the leftover rewards
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(rewardsToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the tokens to the specified address
        bool success = rewardsToken.transfer(to, amount);
        require(success, "Token withdrawal failed");
    }
}
```
