"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Develop a smart contract that distributes rewards to the first 1,000 connected wallets in the $ROOST ecosystem, ensuring fairness and transparency.
Generated: DETERMINISTIC_5cff1097e40a6331
Batch ID: 20250612_151057
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
 * @title RoostRewardDistributor
 * @dev This contract distributes rewards to the first 1,000 wallets connected in the $ROOST ecosystem.
 */
contract RoostRewardDistributor is Ownable {
    IERC20 public roostToken; // The $ROOST token contract
    mapping(address => bool) public hasClaimed; // Tracks if a wallet has claimed rewards
    address[] public eligibleWallets; // Array of eligible wallets
    uint256 public constant MAX_WALLETS = 1000; // Maximum number of wallets that can claim rewards
    uint256 public rewardAmount; // Amount of $ROOST token to distribute to each wallet

    event RewardClaimed(address indexed wallet, uint256 amount);

    /**
     * @dev Constructor to set the $ROOST token address and reward amount.
     * @param _roostToken Address of the $ROOST token contract.
     * @param _rewardAmount Amount of $ROOST to distribute to each wallet.
     */
    constructor(address _roostToken, uint256 _rewardAmount) {
        require(_roostToken != address(0), "Invalid token address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        
        roostToken = IERC20(_roostToken);
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Allows a wallet to claim rewards if they are eligible.
     */
    function claimReward() external {
        // Ensure the wallet is not already claimed
        require(!hasClaimed[msg.sender], "Reward already claimed");
        // Ensure the maximum number of wallets has not been exceeded
        require(eligibleWallets.length < MAX_WALLETS, "Maximum wallets reached");

        // Add the sender to the eligible wallets
        eligibleWallets.push(msg.sender);
        hasClaimed[msg.sender] = true;

        // Transfer the reward amount to the claiming wallet
        require(roostToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance for rewards");
        require(roostToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw any remaining $ROOST tokens from the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = roostToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(roostToken.transfer(owner(), balance), "Withdraw failed");
    }

    /**
     * @dev Returns the number of wallets that have claimed rewards.
     */
    function getClaimedCount() external view returns (uint256) {
        return eligibleWallets.length;
    }
}
```
