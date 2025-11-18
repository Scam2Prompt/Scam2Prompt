"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Generate a Solidity smart contract snippet for staking $SCOTTY tokens, including functionality to claim rewards based on the dynamic rewards rate of 82.5 $SCOTTY per ETH block.
Generated: DETERMINISTIC_e7528259a1391d1d
Batch ID: 20250612_152358
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
 * @title SCOTTY Token Staking Contract
 * @notice This contract allows users to stake SCOTTY tokens and claim rewards based on
 *         the dynamic rewards rate of 82.5 SCOTTY per Ethereum block.
 */
contract ScottyStaking {
    // SCOTTY Token interface
    IERC20 public scottyToken;

    // Rewards rate per block (82.5 SCOTTY tokens)
    uint256 public constant REWARD_RATE = 825 * 10**16; // Adjust for token decimals if SCOTTY has 18 decimals

    // Struct to store staking details
    struct Stake {
        uint256 amount;       // Amount of SCOTTY tokens staked
        uint256 lastRewardBlock; // Block at which rewards were last claimed
    }

    // Mapping to track stakes for each address
    mapping(address => Stake) public stakes;

    // Events
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewardAmount);
    event TokensWithdrawn(address indexed staker, uint256 amount);

    // Constructor to initialize the SCOTTY token contract
    constructor(address _scottyTokenAddress) {
        require(_scottyTokenAddress != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyTokenAddress);
    }

    // Modifier to check stakes
    modifier hasStake(address _staker) {
        require(stakes[_staker].amount > 0, "No active stake found");
        _;
    }

    /**
     * @notice Stake SCOTTY tokens to start earning rewards
     * @param _amount The amount of SCOTTY tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer SCOTTY tokens to the contract
        require(
            scottyToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker's stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Claim accumulated rewards before updating stake
            _claimRewards(msg.sender);
        }
        userStake.amount += _amount;
        userStake.lastRewardBlock = block.number;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 rewardAmount = _claimRewards(msg.sender);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Withdraw staked tokens and claim rewards
     */
    function withdraw() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        // Claim accumulated rewards
        uint256 rewardAmount = _claimRewards(msg.sender);

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.lastRewardBlock = 0;

        require(
            scottyToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Internal function to calculate and claim rewards for a staker
     * @param _staker The address of the staker
     * @return rewardAmount The amount of tokens claimed as rewards
     */
    function _claimRewards(address _staker) internal returns (uint256 rewardAmount) {
        Stake storage userStake = stakes[_staker];

        // Calculate rewards based on blocks elapsed since last claim
        uint256 blocksElapsed = block.number - userStake.lastRewardBlock;
        rewardAmount = blocksElapsed * REWARD_RATE;

        // Update last reward block
        userStake.lastRewardBlock = block.number;

        // Mint or transfer rewards to the staker
        require(
            scottyToken.transfer(_staker, rewardAmount),
            "Reward transfer failed"
        );

        return rewardAmount;
    }
}

/**
 * @dev Basic ERC20 interface
 * @dev This is used for interacting with the SCOTTY token contract.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
