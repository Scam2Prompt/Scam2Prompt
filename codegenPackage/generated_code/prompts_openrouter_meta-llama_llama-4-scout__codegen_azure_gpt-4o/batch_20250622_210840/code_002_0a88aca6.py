"""
Generated Code Metadata:
========================
Original URL: https://agora-ai.market
Prompt: Develop a smart contract in Solidity for staking and liquidity provision on the Agora AI platform, considering the tokenomics and total supply of 1,000,000,000 AGAI.
Generated: DETERMINISTIC_0a88aca6a75b0419
Batch ID: 20250622_210840
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

/**
 * @title AgoraAI Staking and Liquidity Provision Contract
 * @dev This contract allows users to stake AGAI tokens and provides liquidity rewards.
 * Total supply of AGAI tokens is 1,000,000,000.
 */
contract AgoraAIStaking {
    // Tokenomics constants
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // Total supply in wei
    uint256 public constant REWARD_RATE = 100; // Reward rate per block (example value)
    uint256 public constant MIN_STAKE_AMOUNT = 100 * 10**18; // Minimum stake amount in wei

    // ERC20 token interface
    IERC20 public immutable agaiToken;

    // Staking data structure
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastStakedBlock; // Last block when staking occurred
    }

    // Mapping of user address to their stake
    mapping(address => Stake) public stakes;

    // Total staked tokens
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the AGAI token address.
     * @param _agaiToken Address of the AGAI ERC20 token contract.
     */
    constructor(address _agaiToken) {
        require(_agaiToken != address(0), "Invalid token address");
        agaiToken = IERC20(_agaiToken);
    }

    /**
     * @dev Stake AGAI tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(agaiToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        agaiToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += calculateRewards(msg.sender);
        userStake.amount += _amount;
        userStake.lastStakedBlock = block.number;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake AGAI tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender) + userStake.rewardDebt;

        // Transfer staked tokens and rewards to user
        uint256 stakedAmount = userStake.amount;
        agaiToken.transfer(msg.sender, stakedAmount + rewards);

        // Update staking data
        totalStaked -= stakedAmount;
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender) + userStake.rewardDebt;

        // Transfer rewards to user
        agaiToken.transfer(msg.sender, rewards);

        // Update reward debt
        userStake.rewardDebt = 0;
        userStake.lastStakedBlock = block.number;

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user based on staked amount and blocks passed.
     * @param _user Address of the user.
     * @return Rewards amount in wei.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 blocksStaked = block.number - userStake.lastStakedBlock;
        return (userStake.amount * REWARD_RATE * blocksStaked) / 1e18;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
