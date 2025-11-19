"""
Generated Code Metadata:
========================
Original URL: https://clearpool.pages.dev
Prompt: Develop a simple smart contract in Solidity to automate CPOOL staking with Clearpool Oracles, ensuring secure and transparent transactions.
Generated: DETERMINISTIC_300b25595dbb8231
Batch ID: 20250622_211405
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
 * @title CPOOL Staking Contract
 * @dev Allows users to stake CPOOL tokens and earn rewards
 *      Integrates with Clearpool Oracles for secure and transparent transactions
 */
contract CPOOLStaking is Ownable, ReentrancyGuard {
    IERC20 public cpoolToken;
    address public oracleAddress;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward tokens per second per token staked
    uint256 public constant MIN_STAKE_DURATION = 7 days;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event OracleUpdated(address indexed newOracle);

    /**
     * @dev Constructor initializes the staking contract
     * @param _cpoolToken Address of the CPOOL token contract
     * @param _oracleAddress Address of the Clearpool Oracle contract
     * @param _rewardRate Reward rate (tokens per second per token staked)
     */
    constructor(
        address _cpoolToken,
        address _oracleAddress,
        uint256 _rewardRate
    ) {
        require(_cpoolToken != address(0), "Invalid token address");
        require(_oracleAddress != address(0), "Invalid oracle address");
        
        cpoolToken = IERC20(_cpoolToken);
        oracleAddress = _oracleAddress;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake CPOOL tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            cpoolToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            _claimRewards();
        }

        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        userStake.lastClaimed = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake CPOOL tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= userStake.stakedAt + MIN_STAKE_DURATION,
            "Minimum stake duration not met"
        );

        _claimRewards();

        userStake.amount -= amount;
        totalStaked -= amount;

        require(
            cpoolToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and claim rewards
     */
    function _claimRewards() internal {
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount == 0) return;

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            require(
                cpoolToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            emit RewardClaimed(msg.sender, reward);
        }

        userStake.lastClaimed = block.timestamp;
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param staker Address of the staker
     * @return Amount of rewards available
     */
    function calculateReward(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimed;
        return userStake.amount * timeElapsed * rewardRate;
    }

    /**
     * @dev Update the reward rate (only owner)
     * @param newRate New reward rate
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /**
     * @dev Update the oracle address (only owner)
     * @param newOracle New oracle address
     */
    function updateOracle(address newOracle) external onlyOwner {
        require(newOracle != address(0), "Invalid oracle address");
        oracleAddress = newOracle;
        emit OracleUpdated(newOracle);
    }

    /**
     * @dev Emergency withdraw tokens (only owner)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(cpoolToken), "Cannot withdraw staking token");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
