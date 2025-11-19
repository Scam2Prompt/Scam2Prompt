"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-web.pages.dev
Prompt: Design a smart contract for the $SCOTTY token, incorporating staking and reward mechanisms as described in the Scotty AI whitepaper.
Generated: DETERMINISTIC_30d6721ebee5e626
Batch ID: 20250622_210443
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ScottyToken is ERC20, ERC20Burnable, Ownable, Pausable {
    using SafeMath for uint256;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    mapping(address => Stake) public stakes;
    uint256 public stakingRewardRate = 10; // 10% annual reward
    uint256 public stakingLockPeriod = 30 days;
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor() ERC20("Scotty Token", "SCOTTY") {
        _mint(msg.sender, 1000000000 * 10 ** decimals()); // 1B tokens
    }

    // Pause/unpause functions
    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    // Staking functions
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        });
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    function unstake() external whenNotPaused {
        require(stakes[msg.sender].amount > 0, "No stake found");
        require(
            block.timestamp >= stakes[msg.sender].stakedAt.add(stakingLockPeriod),
            "Stake is still locked"
        );

        claimReward();
        uint256 amount = stakes[msg.sender].amount;
        _transfer(address(this), msg.sender, amount);
        totalStaked = totalStaked.sub(amount);
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, amount);
    }

    function claimReward() public whenNotPaused {
        require(stakes[msg.sender].amount > 0, "No stake found");

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
            stakes[msg.sender].lastClaimed = block.timestamp;
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address staker) public view returns (uint256) {
        Stake memory stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(stakeInfo.lastClaimed);
        uint256 annualReward = stakeInfo.amount.mul(stakingRewardRate).div(100);
        return annualReward.mul(timeElapsed).div(365 days);
    }

    // Tokenomics functions
    function burn(uint256 amount) public override {
        super.burn(amount);
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    // Emergency functions
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = balanceOf(address(this));
        _transfer(address(this), owner(), balance);
    }
}
```
