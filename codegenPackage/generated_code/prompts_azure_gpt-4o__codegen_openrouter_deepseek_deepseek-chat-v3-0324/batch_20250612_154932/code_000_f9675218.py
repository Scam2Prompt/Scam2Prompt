"""
Generated Code Metadata:
========================
Original URL: https://aria.fyi
Prompt: Write a smart contract in Solidity to interact with the ARIA20 token on Ethereum, including functions for staking and transferring tokens as described in the Arianee Protocol documentation.
Generated: DETERMINISTIC_f96752186bfc4788
Batch ID: 20250612_154932
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ARIA20 Staking Contract
 * @dev Implements staking and transfer functions for ARIA20 tokens
 */
contract ARIA20Staking is Ownable, ReentrancyGuard {
    IERC20 public aria20Token;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardRate;
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Events
    event TokensStaked(address indexed user, uint256 amount, uint256 rewardRate);
    event TokensUnstaked(address indexed user, uint256 amount, uint256 reward);
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Constructor function
     * @param _aria20TokenAddress The address of the ARIA20 token contract
     */
    constructor(address _aria20TokenAddress) {
        require(_aria20TokenAddress != address(0), "Invalid token address");
        aria20Token = IERC20(_aria20TokenAddress);
    }

    /**
     * @dev Stake ARIA20 tokens
     * @param amount The amount of tokens to stake
     * @param rewardRate The reward rate for staking (percentage per period)
     */
    function stakeTokens(uint256 amount, uint256 rewardRate) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staked");

        // Transfer tokens from user to this contract
        bool success = aria20Token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            rewardRate: rewardRate
        });

        emit TokensStaked(msg.sender, amount, rewardRate);
    }

    /**
     * @dev Unstake ARIA20 tokens and claim rewards
     */
    function unstakeTokens() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender);

        // Delete the stake
        delete stakes[msg.sender];

        // Transfer staked amount + reward back to user
        bool success = aria20Token.transfer(msg.sender, stakedAmount + reward);
        require(success, "Token transfer failed");

        emit TokensUnstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculate reward for a staker
     * @param staker The address of the staker
     * @return The calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * userStake.rewardRate * stakingDuration) / (100 * 365 days);
    }

    /**
     * @dev Transfer ARIA20 tokens
     * @param to The recipient address
     * @param amount The amount to transfer
     */
    function transferTokens(address to, uint256 amount) external nonReentrant {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than 0");

        bool success = aria20Token.transferFrom(msg.sender, to, amount);
        require(success, "Token transfer failed");

        emit TokensTransferred(msg.sender, to, amount);
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param tokenAddress The token contract address
     * @param amount The amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20 token = IERC20(tokenAddress);
        bool success = token.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }
}
```
