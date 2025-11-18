"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverse-com.pages.dev
Prompt: Write a smart contract in Solidity that facilitates staking $DOGEVERSE tokens on the Ethereum blockchain, allowing users to lock their tokens and earn rewards over time.
Generated: DETERMINISTIC_391900f8f3f165d4
Batch ID: 20250612_153606
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
 * @title DogeverseStakeContract
 * @dev A smart contract for staking $DOGEVERSE tokens and earning rewards.
 */
contract DogeverseStakeContract {
    // ERC20 interface for interacting with the $DOGEVERSE token contract
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public dogeverseToken; // Reference to the $DOGEVERSE token contract
    uint256 public rewardRate; // Reward rate in percentage (e.g., 10% = 10)
    uint256 public lockDuration; // Lock duration in seconds

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp when the stake was created
        bool withdrawn; // Whether the stake was withdrawn
    }

    mapping(address => Stake) public stakes; // Mapping to store stakes for each user

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward, uint256 timestamp);

    /**
     * @dev Constructor to initialize the contract with token address, reward rate, and lock duration.
     * @param _tokenAddress Address of the $DOGEVERSE token contract.
     * @param _rewardRate Reward rate in percentage.
     * @param _lockDuration Lock duration in seconds.
     */
    constructor(address _tokenAddress, uint256 _rewardRate, uint256 _lockDuration) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");
        require(_lockDuration > 0, "Lock duration must be positive");

        dogeverseToken = IERC20(_tokenAddress);
        rewardRate = _rewardRate;
        lockDuration = _lockDuration;
    }

    /**
     * @dev Function to allow users to stake $DOGEVERSE tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Already staking");

        // Transfer tokens from the user to the contract
        require(dogeverseToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record the stake
        stakes[msg.sender] = Stake(_amount, block.timestamp, false);

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Function to withdraw staked tokens and claim rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No active stake");
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.timestamp + lockDuration, "Stake is still locked");

        uint256 reward = calculateReward(userStake.amount, block.timestamp - userStake.timestamp);
        uint256 totalAmount = userStake.amount + reward;

        userStake.withdrawn = true;

        // Transfer staked tokens and reward back to the user
        require(dogeverseToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, reward, block.timestamp);
    }

    /**
     * @dev Helper function to calculate rewards based on staked amount and duration.
     * @param _amount Staked amount.
     * @param _duration Duration of staking in seconds.
     * @return Calculated reward.
     */
    function calculateReward(uint256 _amount, uint256 _duration) public view returns (uint256) {
        return (_amount * rewardRate * _duration) / (100 * 365 * 24 * 60 * 60); // Assuming reward rate is annualized
    }

    /**
     * @dev Function to check the staked amount and status for a user.
     * @param _user Address of the user.
     * @return Stake information for the user.
     */
    function getStake(address _user) external view returns (Stake memory) {
        return stakes[_user];
    }
}
```
