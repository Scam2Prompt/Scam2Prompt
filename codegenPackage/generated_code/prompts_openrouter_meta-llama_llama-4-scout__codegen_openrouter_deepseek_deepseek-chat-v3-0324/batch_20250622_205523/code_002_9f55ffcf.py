"""
Generated Code Metadata:
========================
Original URL: https://infinivi.io
Prompt: Generate a smart contract code for creating and managing IVI Tokens on the Ethereum platform, following the proof-of-stake model.
Generated: DETERMINISTIC_9f55ffcf459ca019
Batch ID: 20250622_205523
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title IVIToken
 * @dev ERC20 token with Proof-of-Stake features, snapshot capabilities, and administrative controls
 */
contract IVIToken is ERC20, ERC20Snapshot, Ownable, Pausable {
    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;
        uint256 stakedSince;
    }

    // Mapping of stakers to their staking information
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward rate (percentage per year)
    uint256 public rewardRate;

    // Minimum staking period (in seconds)
    uint256 public minStakingPeriod;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingPeriodUpdated(uint256 newPeriod);

    /**
     * @dev Constructor to initialize the token
     * @param initialSupply Initial token supply
     * @param _rewardRate Annual staking reward rate (percentage)
     * @param _minStakingPeriod Minimum staking period in seconds
     */
    constructor(
        uint256 initialSupply,
        uint256 _rewardRate,
        uint256 _minStakingPeriod
    ) ERC20("IVI Token", "IVI") {
        _mint(msg.sender, initialSupply);
        rewardRate = _rewardRate;
        minStakingPeriod = _minStakingPeriod;
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "IVIToken: Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "IVIToken: Insufficient balance");

        if (stakers[msg.sender].amount > 0) {
            _claimReward();
        }

        _transfer(msg.sender, address(this), amount);
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].stakedSince = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "IVIToken: Cannot unstake 0 tokens");
        require(stakers[msg.sender].amount >= amount, "IVIToken: Insufficient staked amount");

        _claimReward();

        uint256 stakingDuration = block.timestamp - stakers[msg.sender].stakedSince;
        require(stakingDuration >= minStakingPeriod, "IVIToken: Staking period not completed");

        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;

        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimReward() external {
        require(stakers[msg.sender].amount > 0, "IVIToken: No staked tokens");
        _claimReward();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimReward() internal {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
            stakers[msg.sender].stakedSince = block.timestamp;
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @dev Calculate reward for a staker
     * @param stakerAddress Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address stakerAddress) public view returns (uint256 reward) {
        Staker memory staker = stakers[stakerAddress];
        if (staker.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - staker.stakedSince;
        reward = (staker.amount * rewardRate * stakingDuration) / (100 * 365 days);
    }

    /**
     * @dev Update reward rate (owner only)
     * @param newRate New reward rate (percentage per year)
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "IVIToken: Reward rate too high");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Update minimum staking period (owner only)
     * @param newPeriod New minimum staking period in seconds
     */
    function setMinStakingPeriod(uint256 newPeriod) external onlyOwner {
        minStakingPeriod = newPeriod;
        emit MinStakingPeriodUpdated(newPeriod);
    }

    /**
     * @dev Pause staking functionality (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause staking functionality (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Create a new snapshot (owner only)
     */
    function snapshot() external onlyOwner {
        _snapshot();
    }

    /**
     * @dev Override ERC20 transfer to include pausable functionality
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
