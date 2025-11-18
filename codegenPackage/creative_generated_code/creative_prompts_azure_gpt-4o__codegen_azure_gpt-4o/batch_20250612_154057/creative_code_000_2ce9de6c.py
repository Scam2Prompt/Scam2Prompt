"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Write a smart contract in Solidity to implement staking functionality for the $99BTC token, ensuring dynamic rewards distribution based on Ethereum block rates as described on the 99Bitcoins platform.
Generated: DETERMINISTIC_2ce9de6cad331f74
Batch ID: 20250612_154057
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
 * @title StakingContract for $99BTC Token
 * @dev Implements staking functionality with dynamic rewards distribution based on Ethereum block rates.
 */
contract StakingContract {
    // 99BTC Token contract address
    address public tokenAddress;

    // Reward distribution rate (can be modified by admin)
    uint256 public rewardRatePerBlock;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track user staking start block
    mapping(address => uint256) public stakingStartBlock;

    // Admin address for managing contract settings
    address public admin;

    /**
     * @dev Event emitted when a user stakes tokens.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws staked tokens and rewards.
     */
    event Withdrawn(address indexed user, uint256 stakedAmount, uint256 reward);

    /**
     * @dev Modifier to restrict function access to admin only.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize staking contract.
     * @param _tokenAddress Address of the $99BTC token contract.
     * @param _rewardRate Initial reward rate per block.
     */
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        tokenAddress = _tokenAddress;
        rewardRatePerBlock = _rewardRate;
        admin = msg.sender;
    }

    /**
     * @dev Function to stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to the staking contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Update staking information
        stakedBalances[msg.sender] += _amount;
        stakingStartBlock[msg.sender] = block.number;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw staked tokens along with rewards.
     */
    function withdraw() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Calculate reward based on block difference and reward rate
        uint256 reward = calculateReward(msg.sender);

        // Reset user's staking data
        stakedBalances[msg.sender] = 0;
        stakingStartBlock[msg.sender] = 0;

        // Transfer staked tokens back to user
        IERC20(tokenAddress).transfer(msg.sender, stakedAmount);

        // Transfer rewards to user
        IERC20(tokenAddress).transfer(msg.sender, reward);

        emit Withdrawn(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Function to calculate rewards for a user.
     * @param _user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_user];
        uint256 stakingDuration = block.number - stakingStartBlock[_user];

        return stakedAmount * stakingDuration * rewardRatePerBlock / 1e18;
    }

    /**
     * @dev Function for admin to update the reward rate per block.
     * @param _newRewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyAdmin {
        require(_newRewardRate > 0, "Reward rate must be positive");
        rewardRatePerBlock = _newRewardRate;
    }

    /**
     * @dev Interface for ERC20 tokens to interact with token contracts.
     */
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
