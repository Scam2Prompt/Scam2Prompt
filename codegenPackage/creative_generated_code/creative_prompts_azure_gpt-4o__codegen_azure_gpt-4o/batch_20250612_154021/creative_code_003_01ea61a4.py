"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiiway.com
Prompt: Create a smart contract for staking cryptocurrency with an APY of up to 12%, and integrate it with Defiway's staking functionality across 10+ blockchains.
Generated: DETERMINISTIC_01ea61a41e38db44
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready code for a Solidity smart contract that supports staking cryptocurrency with an APY of up to 12%. Note that integration with third-party staking solutions like Defiway across multiple blockchains requires off-chain mechanisms, but the contract provides the core functionality.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A smart contract for staking cryptocurrency with an APY of up to 12%.
 *      This contract allows users to stake tokens, earn rewards, and withdraw their staked tokens and rewards.
 */
contract StakingContract {
    // Variables
    uint256 public constant APY = 12; // Annual Percentage Yield (fixed at 12%)
    uint256 public constant SECONDS_IN_YEAR = 365 days; // Number of seconds in a year

    address public owner; // Contract owner
    ERC20 public stakingToken; // ERC20 token to be staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the staking started
        uint256 lastClaimedTime; // Timestamp when rewards were last claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found.");
        _;
    }

    // Constructor
    constructor(address _stakingToken) {
        owner = msg.sender; // Set the contract deployer as the owner
        stakingToken = ERC20(_stakingToken); // Initialize the staking token
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens.");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed.");

        Stake storage userStake = stakes[msg.sender];

        // If the user already has an active stake, claim their rewards first
        if (userStake.amount > 0) {
            claimRewards();
        }

        userStake.amount += _amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimedTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() public hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        // Calculate rewards based on staked amount, APY, and staking duration
        uint256 stakingDuration = block.timestamp - userStake.lastClaimedTime;
        uint256 reward = (userStake.amount * APY * stakingDuration) / (100 * SECONDS_IN_YEAR);

        require(reward > 0, "No rewards available to claim.");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed.");

        userStake.lastClaimedTime = block.timestamp;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to withdraw their staked tokens and rewards.
     */
    function withdraw() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];

        // Claim rewards before withdrawing
        claimRewards();

        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;

        require(stakingToken.transfer(msg.sender, stakedAmount), "Withdrawal transfer failed.");

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows the owner to recover any tokens accidentally sent to the contract.
     * @param _token The address of the token to recover.
     * @param _amount The amount of tokens to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(stakingToken), "Cannot recover staking tokens.");
        ERC20(_token).transfer(owner, _amount);
    }
}

/**
 * @title ERC20
 * @dev Simplified ERC20 interface. Replace with the actual ERC20 interface in production.
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

Make sure to replace `ERC20` with the actual ERC20 interface when deploying the contract. Additionally, multi-chain integration with Defiway would usually require oracle services or off-chain components, which are not implemented purely in Solidity.
