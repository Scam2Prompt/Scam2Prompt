"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Develop a smart contract in Solidity for a crypto casino token with a staking rewards system, similar to $TGC, including functions for token staking, reward distribution, and airdrop management.
Generated: DETERMINISTIC_98d1f865caaec905
Batch ID: 20250622_205230
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CasinoToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    uint256 public constant REWARD_RATE = 10; // 10% annual reward
    uint256 public constant REWARD_INTERVAL = 1 days;
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public totalStaked;
    
    mapping(address => Stake) public stakes;
    mapping(address => bool) public airdropRecipients;
    uint256 public airdropAmount;
    uint256 public airdropEndTime;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event Airdrop(address indexed recipient, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _airdropAmount,
        uint256 _airdropDuration
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        airdropAmount = _airdropAmount;
        airdropEndTime = block.timestamp.add(_airdropDuration);
    }

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

    function unstake() external {
        require(stakes[msg.sender].amount > 0, "No stake found");
        require(
            block.timestamp >= stakes[msg.sender].stakedAt.add(MIN_STAKE_DURATION),
            "Minimum stake duration not reached"
        );

        claimReward();
        uint256 amount = stakes[msg.sender].amount;
        totalStaked = totalStaked.sub(amount);
        _transfer(address(this), msg.sender, amount);
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, amount);
    }

    function claimReward() public {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
            stakes[msg.sender].lastClaimed = block.timestamp;
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        if (stakes[user].amount == 0) return 0;

        uint256 stakedTime = block.timestamp.sub(stakes[user].lastClaimed);
        uint256 reward = stakes[user].amount
            .mul(REWARD_RATE)
            .mul(stakedTime)
            .div(100)
            .div(365 days);
            
        return reward;
    }

    function claimAirdrop() external {
        require(block.timestamp <= airdropEndTime, "Airdrop period ended");
        require(!airdropRecipients[msg.sender], "Already claimed airdrop");
        require(balanceOf(msg.sender) > 0, "Must hold tokens to claim airdrop");

        airdropRecipients[msg.sender] = true;
        _mint(msg.sender, airdropAmount);
        emit Airdrop(msg.sender, airdropAmount);
    }

    function updateAirdrop(uint256 newAmount, uint256 newDuration) external onlyOwner {
        airdropAmount = newAmount;
        airdropEndTime = block.timestamp.add(newDuration);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function withdrawStuckTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
