"""
Generated Code Metadata:
========================
Original URL: https://stake-e39.pages.dev
Prompt: Generate a smart contract code for a 30-day lockup period staking campaign on the Ancient8 Mainnet, using Solidity programming language.
Generated: DETERMINISTIC_87f776cb2ca71d8a
Batch ID: 20250622_204615
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

contract Ancient8Staking is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    uint256 public constant LOCKUP_PERIOD = 30 days;
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        bool claimed;
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staked");

        stakes[msg.sender] = Stake({
            amount: amount,
            stakedAt: block.timestamp,
            claimed: false
        });

        totalStaked += amount;

        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(!userStake.claimed, "Already unstaked");
        require(block.timestamp >= userStake.stakedAt + LOCKUP_PERIOD, "Lockup period not ended");

        uint256 amount = userStake.amount;
        userStake.claimed = true;
        totalStaked -= amount;

        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        bool success = stakingToken.transfer(owner(), balance);
        require(success, "Token transfer failed");
    }

    function getStakeInfo(address user) external view returns (uint256 amount, uint256 stakedAt, bool claimed) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.stakedAt, userStake.claimed);
    }

    function timeUntilUnlock(address user) external view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.stakedAt == 0 || userStake.claimed) {
            return 0;
        }

        if (block.timestamp >= userStake.stakedAt + LOCKUP_PERIOD) {
            return 0;
        }

        return (userStake.stakedAt + LOCKUP_PERIOD) - block.timestamp;
    }
}
```
