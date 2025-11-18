"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales99bitcoins.pages.dev
Prompt: Generate code to stake $99BTC tokens on the Ethereum blockchain using a smart contract. Ensure the code calculates dynamic rewards based on the staking pool percentage.
Generated: DETERMINISTIC_a97eaff61a201381
Batch ID: 20250612_152235
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
 * @title StakingContract
 * @dev A smart contract for staking $99BTC tokens on the Ethereum blockchain.
 *      Users can stake tokens and earn dynamic rewards based on the staking pool percentage.
 */
contract StakingContract {
    // ERC20 token interface
    IERC20 public stakingToken;

    // Structure to store staking information
    struct Stake {
        uint256 amount;      // Amount of tokens staked
        uint256 timestamp;   // Timestamp of when the stake was created
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the pool
    uint256 public totalStaked;

    // Reward rate, represented as a percentage (e.g., 10 for 10%)
    uint256 public rewardRate = 10;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the $99BTC ERC20 token contract.
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Modifier to ensure the caller has staked tokens.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update the total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards.
     */
    function withdraw() external hasStake {
        // Calculate reward based on the staking pool percentage
        uint256 userStake = stakes[msg.sender].amount;
        uint256 reward = (userStake * rewardRate * (block.timestamp - stakes[msg.sender].timestamp)) / (100 * 365 days);

        // Update the total staked amount
        totalStaked -= userStake;

        // Reset the user's stake
        stakes[msg.sender].amount = 0;

        // Transfer the staked tokens back to the user
        bool success = stakingToken.transfer(msg.sender, userStake);
        require(success, "Token transfer failed");

        // Transfer the reward tokens to the user
        success = stakingToken.transfer(msg.sender, reward);
        require(success, "Reward transfer failed");

        emit Withdrawn(msg.sender, userStake, reward);
    }

    /**
     * @dev Get the user's current stake information.
     * @param _user Address of the user.
     * @return amount Staked amount.
     * @return timestamp Timestamp when the stake was created.
     */
    function getStake(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory stakeInfo = stakes[_user];
        return (stakeInfo.amount, stakeInfo.timestamp);
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
