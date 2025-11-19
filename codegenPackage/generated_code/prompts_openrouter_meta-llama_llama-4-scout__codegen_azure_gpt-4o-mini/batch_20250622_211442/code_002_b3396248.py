"""
Generated Code Metadata:
========================
Original URL: https://paal-stakings.pages.dev
Prompt: Generate a smart contract code in Solidity that allows users to stake their tokens and earn rewards in ETH, with different staking periods and APR rates, as described on the Paal AI Staking website.
Generated: DETERMINISTIC_b3396248ea2d24b8
Batch ID: 20250622_211442
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is ReentrancyGuard, Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake was created
        uint256 duration; // Duration of the stake in seconds
        uint256 apr; // Annual Percentage Rate
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake[]) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 duration, uint256 apr);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // The token being staked
    IERC20 public stakingToken;

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount, uint256 duration, uint256 apr) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(apr > 0, "APR must be greater than 0");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Create a new stake
        stakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: duration,
            apr: apr
        }));

        emit Staked(msg.sender, amount, duration, apr);
    }

    // Function to calculate rewards based on the stake
    function calculateReward(Stake memory stake) internal view returns (uint256) {
        uint256 timeStaked = block.timestamp - stake.startTime;
        if (timeStaked < stake.duration) {
            return 0; // No reward if the stake is not matured
        }
        uint256 reward = (stake.amount * stake.apr * timeStaked) / (365 days * 100);
        return reward;
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake memory userStake = stakes[msg.sender][stakeIndex];
        uint256 reward = calculateReward(userStake);

        // Remove the stake from the user's stakes
        stakes[msg.sender][stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        // Transfer staked tokens back to the user
        stakingToken.transfer(msg.sender, userStake.amount);

        // Transfer reward in ETH to the user
        payable(msg.sender).transfer(reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to withdraw contract's ETH balance (only owner)
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
