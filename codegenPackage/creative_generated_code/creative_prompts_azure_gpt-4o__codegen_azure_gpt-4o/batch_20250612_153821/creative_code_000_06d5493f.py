"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocket-pool.xyz
Prompt: Write a smart contract in Solidity that integrates Rocket Pool's rETH token into a DeFi protocol, allowing users to stake rETH and earn rewards. Include functionality for calculating rETH/ETH exchange rates based on Rocket Pool's reward distribution mechanism.
Generated: DETERMINISTIC_06d5493fe64c50a2
Batch ID: 20250612_153821
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
 * @title rETH Staking Contract
 * @notice A smart contract to allow users to stake rETH and earn rewards.
 * Integrates Rocket Pool's rETH token and calculates exchange rates based on reward mechanisms.
 */
interface IRocketTokenRETH {
    /**
     * @dev Returns the current exchange rate between rETH and ETH.
     * This is calculated based on Rocket Pool's reward distribution mechanism.
     */
    function getExchangeRate() external view returns (uint256);
}

contract rETHStaking {
    // State variables
    address public owner; // Contract owner
    IRocketTokenRETH public rETH; // Reference to the rETH token contract

    mapping(address => uint256) public userStakes; // Tracks how much rETH each user has staked
    mapping(address => uint256) public userRewards; // Tracks rewards earned by each user

    uint256 public totalStaked; // Total rETH staked in the contract

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor to initialize the contract.
     * @param _rETHAddress The address of the Rocket Pool rETH token contract.
     */
    constructor(address _rETHAddress) {
        require(_rETHAddress != address(0), "Invalid rETH address");
        owner = msg.sender;
        rETH = IRocketTokenRETH(_rETHAddress);
    }

    /**
     * @notice Modifier to restrict certain functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @notice Allows a user to stake rETH into the contract.
     * @param _amount Amount of rETH to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer rETH from the user to the contract
        require(
            IERC20(address(rETH)).transferFrom(msg.sender, address(this), _amount),
            "rETH transfer failed"
        );

        // Update state
        userStakes[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows a user to withdraw their staked rETH.
     * @param _amount Amount of rETH to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(userStakes[msg.sender] >= _amount, "Insufficient staked balance");

        // Update state
        userStakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer rETH back to the user
        require(IERC20(address(rETH)).transfer(msg.sender, _amount), "rETH transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Allows a user to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update state
        userRewards[msg.sender] = 0;

        // Transfer ETH rewards to the user
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculates the rewards for a given user based on their staked rETH.
     * @param _user The address of the user.
     * @return The amount of ETH rewards the user is entitled to.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakedAmount = userStakes[_user];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 exchangeRate = rETH.getExchangeRate(); // Fetch current rETH/ETH exchange rate
        return (stakedAmount * exchangeRate) / 1e18; // Convert to ETH rewards
    }

    /**
     * @notice Allows the contract owner to withdraw any excess ETH in the contract.
     * @param _amount Amount of ETH to withdraw.
     */
    function withdrawExcessETH(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient balance");
        payable(owner).transfer(_amount);
    }

    /**
     * @notice Fallback function to accept ETH transfers into the contract.
     */
    receive() external payable {}

    /**
     * @notice Allows the contract owner to update the rETH token contract address.
     * @param _newRETHAddress The new address for the rETH token contract.
     */
    function updateRETHAddress(address _newRETHAddress) external onlyOwner {
        require(_newRETHAddress != address(0), "Invalid rETH address");
        rETH = IRocketTokenRETH(_newRETHAddress);
    }
}

/**
 * @dev Interface for ERC20 token functionality.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
