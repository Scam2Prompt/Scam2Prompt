"""
Generated Code Metadata:
========================
Original URL: https://puffer.pages.dev
Prompt: Generate an example of a smart contract that utilizes Puffer's liquid staking features for efficient capital management.
Generated: DETERMINISTIC_48aec2c039f18068
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PufferLiquidStaking
 * @dev A smart contract for liquid staking with Puffer's efficient capital management features
 * @notice Allows users to stake ETH and receive liquid staking tokens (pufETH) in return
 */
contract PufferLiquidStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Interface for the staked ETH token (pufETH)
    IERC20 public pufETH;

    // Total amount of ETH staked
    uint256 public totalStaked;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedBalances;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 totalRewards);

    /**
     * @dev Constructor initializes the pufETH token contract
     * @param _pufETHAddress Address of the pufETH token contract
     */
    constructor(address _pufETHAddress) {
        require(_pufETHAddress != address(0), "Invalid token address");
        pufETH = IERC20(_pufETHAddress);
    }

    /**
     * @dev Stake ETH and receive pufETH tokens
     * @notice Users can stake ETH and receive liquid staking tokens in return
     */
    function stake() external payable nonReentrant {
        require(msg.value > 0, "Cannot stake 0 ETH");

        // Update user balance and total staked
        stakedBalances[msg.sender] += msg.value;
        totalStaked += msg.value;

        // Mint pufETH tokens 1:1 with staked ETH
        pufETH.safeTransfer(msg.sender, msg.value);

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Unstake pufETH tokens and receive ETH
     * @param amount Amount of pufETH to unstake
     * @notice Users can unstake their pufETH tokens to receive ETH back
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Burn pufETH tokens
        pufETH.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer ETH back to user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute staking rewards to all stakers
     * @notice Only owner can call this to distribute rewards
     */
    function distributeRewards() external payable onlyOwner {
        require(msg.value > 0, "No rewards to distribute");

        uint256 totalRewards = msg.value;
        if (totalStaked == 0) {
            // If no one is staking, return the rewards
            (bool success, ) = owner().call{value: totalRewards}("");
            require(success, "Reward return failed");
            return;
        }

        // Calculate reward per staked ETH
        uint256 rewardPerToken = totalRewards / totalStaked;

        // Mint additional pufETH as rewards
        pufETH.safeTransfer(address(this), totalRewards);

        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Get the current staking balance for a user
     * @param user Address of the user to query
     * @return The staked balance of the user
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the total amount of ETH staked in the contract
     * @return The total staked ETH amount
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
