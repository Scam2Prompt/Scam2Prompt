"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftsolutionchain.web.app
Prompt: Generate a smart contract for staking tokens, including APR activation functionality, based on the features highlighted on Swift Solution Chain.
Generated: DETERMINISTIC_b99efdddd5789168
Batch ID: 20250612_151506
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
 * @title TokenStaking
 * @notice A smart contract for staking tokens with APR activation functionality.
 * @dev This contract supports staking, calculating rewards based on APR, and withdrawal of tokens and rewards.
 */
contract TokenStaking {
    // Struct to store information about a staker
    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 rewardDebt;      // Accumulated rewards before the last action
        uint256 stakeTimestamp;  // Timestamp when the stake was created
    }

    // State variables
    address public owner;                    // Owner of the contract
    address public token;                    // Address of the staking token
    uint256 public apr;                      // Annual Percentage Rate (APR) for staking rewards
    uint256 public totalStaked;              // Total amount of tokens staked in the contract
    mapping(address => Stake) public stakes; // Mapping of user address to their staking information

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);
    event APRUpdated(uint256 newApr);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the token to be staked.
     * @param _apr Initial APR value.
     */
    constructor(address _token, uint256 _apr) {
        require(_token != address(0), "Token address cannot be zero");
        token = _token;
        apr = _apr;
        owner = msg.sender;
    }

    /**
     * @notice Allows users to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer the staking tokens to the contract
        bool success = IERC20(token).transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += calculateRewards(msg.sender);
        userStake.amount += _amount;
        userStake.stakeTimestamp = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to withdraw their staked tokens along with rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update contract state
        uint256 totalWithdrawal = userStake.amount + rewards;
        totalStaked -= userStake.amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        // Transfer tokens and rewards
        bool success = IERC20(token).transfer(msg.sender, totalWithdrawal);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    /**
     * @notice Sets a new APR value.
     * @param _newApr New APR value.
     */
    function setAPR(uint256 _newApr) external onlyOwner {
        require(_newApr > 0, "APR must be greater than zero");
        apr = _newApr;

        emit APRUpdated(_newApr);
    }

    /**
     * @notice Calculates the rewards for a user based on their stake and the APR.
     * @param _user Address of the user.
     * @return Rewards amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakeTimestamp;
        uint256 yearlyReward = (userStake.amount * apr) / 100;
        return (yearlyReward * stakingDuration) / 365 days;
    }
}

// Interface for interacting with the ERC20 token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
