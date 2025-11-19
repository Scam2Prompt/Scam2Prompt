"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-eng.pages.dev
Prompt: Design a simple smart contract in Solidity for a meme coin ecosystem like Pepe Unchained, incorporating features such as token staking and rewards distribution.
Generated: DETERMINISTIC_67b810aed46ff3ac
Batch ID: 20250622_204621
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MemeCoin is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant REWARD_RATE = 10; // 10 tokens per staked token per year
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public constant MIN_STAKE_AMOUNT = 1000 * 10**18; // Minimum 1000 tokens to stake

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor() ERC20("Pepe Unchained", "PEPU") {
        _mint(msg.sender, 1000000000 * 10**18); // 1 billion tokens
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            _claimRewards(msg.sender);
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        });
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        _claimRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    function _claimRewards(address user) internal {
        uint256 reward = calculateRewards(user);
        if (reward > 0) {
            stakes[user].lastClaimed = block.timestamp;
            _mint(user, reward);
            emit RewardClaimed(user, reward);
        }
    }

    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeInfo = stakes[user];
        if (stakeInfo.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - stakeInfo.lastClaimed;
        return (stakeInfo.amount * REWARD_RATE * timeElapsed) / (REWARD_INTERVAL * 100);
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```
