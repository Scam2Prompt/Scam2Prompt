"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Develop a Solidity smart contract for distributing rewards in a multichain Web3 gaming ecosystem, similar to Kewl's features mentioned on the GAINS Associates platform.
Generated: DETERMINISTIC_e382f432e3249370
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title RewardDistributor
 * @dev A smart contract to distribute rewards in a multichain Web3 gaming ecosystem.
 * The contract allows only the owner to set rewards and distribute them to players.
 */
contract RewardDistributor is Ownable, ReentrancyGuard {
    // Mapping to track player balances and rewards
    mapping(address => uint256) private playerBalances;
    mapping(address => uint256) private pendingRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed player, uint256 amount);
    event RewardClaimed(address indexed player, uint256 amount);

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    /**
     * @param _rewardToken Address of the ERC20 token contract used for rewards.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Distributes rewards to players.
     * @param players Array of player addresses to distribute rewards to.
     * @param amounts Array of reward amounts corresponding to each player.
     */
    function distributeRewards(address[] calldata players, uint256[] calldata amounts) external onlyOwner nonReentrant {
        require(players.length == amounts.length, "Mismatched array lengths");

        for (uint256 i = 0; i < players.length; i++) {
            require(players[i] != address(0), "Invalid player address");
            require(amounts[i] > 0, "Reward amount must be greater than zero");

            // Update the pending rewards for the player
            pendingRewards[players[i]] += amounts[i];

            // Emit event for tracking rewards
            emit RewardsDistributed(players[i], amounts[i]);
        }
    }

    /**
     * @dev Players can claim their rewards.
     */
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = pendingRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the pending rewards for the player
        pendingRewards[msg.sender] = 0;

        // Transfer rewards to the player
        bool success = rewardToken.transfer(msg.sender, rewardAmount);
        require(success, "Transfer failed");

        // Emit event for claimed rewards
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        // Transfer the specified amount to the owner
        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Withdraw transfer failed");
    }

    /**
     * @dev Returns the pending rewards of a specific player.
     * @param player Address of the player.
     * @return The amount of pending rewards for the player.
     */
    function getPendingRewards(address player) external view returns (uint256) {
        return pendingRewards[player];
    }
}
```
