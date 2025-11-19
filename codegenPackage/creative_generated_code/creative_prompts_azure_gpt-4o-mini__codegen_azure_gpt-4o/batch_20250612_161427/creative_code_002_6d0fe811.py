"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Explain how to implement a smart contract for managing staking tiers and rewards for the AITECH token.
Generated: DETERMINISTIC_6d0fe811362759ca
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Staking Contract for AITECH Token
 * @dev This contract manages staking tiers and rewards for AITECH token holders.
 */
contract AITECHStaking {
    // Struct to represent a staking tier
    struct Tier {
        uint256 minStake; // Minimum amount required to qualify for this tier
        uint256 rewardRate; // Reward rate (percentage) for this tier
    }

    // Struct to represent a staker's details
    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 tier; // Current tier of the staker
        uint256 lastClaimed; // Timestamp of the last reward claim
    }

    // Mapping of staker addresses to their stakes
    mapping(address => Stake) private stakes;

    // Array of staking tiers
    Tier[] public tiers;

    // AITECH token interface
    IERC20 public aitechToken;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event RewardsClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier isStaker(address _staker) {
        require(stakes[_staker].amount > 0, "No stake found for this address");
        _;
    }

    /**
     * @dev Constructor to initialize contract
     * @param _aitechToken Address of the AITECH token contract
     * @param _tiers Array of staking tiers (minStake, rewardRate)
     */
    constructor(address _aitechToken, Tier[] memory _tiers) {
        require(_aitechToken != address(0), "Invalid token address");
        require(_tiers.length > 0, "At least one tier is required");
        owner = msg.sender;
        aitechToken = IERC20(_aitechToken);

        // Initialize tiers
        for (uint256 i = 0; i < _tiers.length; i++) {
            tiers.push(Tier(_tiers[i].minStake, _tiers[i].rewardRate));
        }
    }

    /**
     * @dev Stake AITECH tokens to qualify for rewards
     * @param _amount Amount of AITECH tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer AITECH tokens to the contract
        require(
            aitechToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Determine appropriate tier based on amount staked
        uint256 stakerTier = 0;
        for (uint256 i = 0; i < tiers.length; i++) {
            if (_amount >= tiers[i].minStake) {
                stakerTier = i;
            }
        }

        // Update stake details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].tier = stakerTier;
        stakes[msg.sender].lastClaimed = block.timestamp;

        emit Staked(msg.sender, _amount, stakerTier);
    }

    /**
     * @dev Claim rewards based on the staking tier
     */
    function claimRewards() external isStaker(msg.sender) {
        Stake storage stakeDetails = stakes[msg.sender];
        Tier memory stakerTier = tiers[stakeDetails.tier];

        // Calculate rewards based on reward rate and staking duration
        uint256 timeElapsed = block.timestamp - stakeDetails.lastClaimed;
        uint256 reward = (stakeDetails.amount * stakerTier.rewardRate * timeElapsed) / (365 days * 100);

        // Ensure contract has enough tokens to pay rewards
        require(
            aitechToken.balanceOf(address(this)) >= reward,
            "Insufficient contract balance to pay rewards"
        );

        // Update last claimed timestamp
        stakeDetails.lastClaimed = block.timestamp;

        // Transfer rewards to user
        require(aitechToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens and stop receiving rewards
     */
    function unstake() external isStaker(msg.sender) {
        Stake storage stakeDetails = stakes[msg.sender];
        uint256 amount = stakeDetails.amount;

        // Reset staker's details
        stakeDetails.amount = 0;
        stakeDetails.tier = 0;
        stakeDetails.lastClaimed = 0;

        // Transfer staked tokens back to user
        require(aitechToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Add a new staking tier
     * @param _minStake Minimum stake amount for the tier
     * @param _rewardRate Reward rate for the tier
     */
    function addTier(uint256 _minStake, uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        tiers.push(Tier(_minStake, _rewardRate));
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    fallback() external payable {
        revert("This contract does not accept Ether");
    }

    receive() external payable {
        revert("This contract does not accept Ether");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
