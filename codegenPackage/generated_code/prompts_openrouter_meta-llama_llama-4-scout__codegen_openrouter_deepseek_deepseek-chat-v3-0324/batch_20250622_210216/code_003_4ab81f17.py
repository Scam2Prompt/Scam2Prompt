"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Develop a basic smart contract in Solidity for the Green Bitcoin ($GBTC) token, implementing the gamified green staking mechanism and reward distribution.
Generated: DETERMINISTIC_4ab81f175386494a
Batch ID: 20250622_210216
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract GreenBitcoin is ERC20, ERC20Burnable, Ownable, Pausable {
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
        uint256 stakingDuration;
    }

    uint256 public constant REWARD_RATE = 10; // 10% annual reward
    uint256 public constant MIN_STAKE_DURATION = 30 days;
    uint256 public constant MAX_STAKE_DURATION = 365 days;
    uint256 public constant MIN_STAKE_AMOUNT = 100 * 10**18; // 100 GBTC

    mapping(address => Stake[]) public stakes;
    mapping(address => uint256) public totalStaked;

    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor() ERC20("Green Bitcoin", "GBTC") {
        _mint(msg.sender, 21000000 * 10**18); // 21 million GBTC
    }

    function stake(uint256 amount, uint256 duration) external whenNotPaused {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(duration >= MIN_STAKE_DURATION, "Duration too short");
        require(duration <= MAX_STAKE_DURATION, "Duration too long");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _transfer(msg.sender, address(this), amount);

        stakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            lastClaimTime: block.timestamp,
            stakingDuration: duration
        }));

        totalStaked[msg.sender] += amount;

        emit Staked(msg.sender, amount, duration);
    }

    function unstake(uint256 stakeIndex) external {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = stakes[msg.sender][stakeIndex];
        require(block.timestamp >= userStake.startTime + userStake.stakingDuration, "Staking period not ended");

        uint256 reward = calculateReward(msg.sender, stakeIndex);
        uint256 totalAmount = userStake.amount + reward;

        _mint(msg.sender, reward);
        _transfer(address(this), msg.sender, userStake.amount);

        // Remove the stake
        stakes[msg.sender][stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        totalStaked[msg.sender] -= userStake.amount;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    function claimReward(uint256 stakeIndex) external {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = stakes[msg.sender][stakeIndex];

        uint256 reward = calculateReward(msg.sender, stakeIndex);
        require(reward > 0, "No rewards available");

        userStake.lastClaimTime = block.timestamp;
        _mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(address user, uint256 stakeIndex) public view returns (uint256) {
        require(stakeIndex < stakes[user].length, "Invalid stake index");
        Stake storage userStake = stakes[user][stakeIndex];

        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        uint256 annualReward = (userStake.amount * REWARD_RATE) / 100;
        uint256 reward = (annualReward * timeElapsed) / 365 days;

        return reward;
    }

    function getStakesCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }

    function getStakeInfo(address user, uint256 stakeIndex) external view returns (Stake memory) {
        require(stakeIndex < stakes[user].length, "Invalid stake index");
        return stakes[user][stakeIndex];
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```
