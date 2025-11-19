"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for distributing Scotty AI token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_edc235beda88e7ef
Batch ID: 20250622_210914
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
 * @title ScottyAIRewardDistributor
 * @dev Smart contract for distributing Scotty AI token rewards to users based on their share of the staking pool and annual returns percentage.
 */
contract ScottyAIRewardDistributor {
    // Scotty AI token contract address
    address public tokenAddress;

    // Total staked amount in the pool
    uint256 public totalStaked;

    // Annual return percentage (e.g., 5% = 500)
    uint256 public annualReturnPercentage;

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Modifier to ensure valid token address
    modifier validTokenAddress() {
        require(tokenAddress != address(0), "Token address is not set");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the Scotty AI token contract.
     * @param _annualReturnPercentage Annual return percentage (e.g., 5% = 500).
     */
    constructor(address _tokenAddress, uint256 _annualReturnPercentage) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_annualReturnPercentage > 0, "Annual return percentage must be greater than 0");

        tokenAddress = _tokenAddress;
        annualReturnPercentage = _annualReturnPercentage;
    }

    /**
     * @dev Function to allow users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external validTokenAddress {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens from the user to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Update user stake and total staked amount
        userStakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate and distribute rewards to users.
     */
    function distributeRewards() external validTokenAddress {
        require(totalStaked > 0, "No tokens staked in the pool");

        // Iterate through all users and calculate rewards
        for (address user : getAllStakers()) {
            uint256 userStake = userStakes[user];
            uint256 reward = (userStake * annualReturnPercentage) / 10000;

            // Update user rewards
            userRewards[user] += reward;

            // Transfer reward tokens to the user
            IERC20(tokenAddress).transfer(user, reward);

            emit RewardsDistributed(user, reward);
        }
    }

    /**
     * @dev Helper function to get all stakers (not implemented in this snippet).
     * @return List of staker addresses.
     */
    function getAllStakers() internal view returns (address[] memory) {
        // This function should return the list of all stakers.
        // Implementation depends on how stakers are tracked in the contract.
        // For simplicity, this is left as a placeholder.
        return new address[](0);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
