"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdccash.xyz
Prompt: Write a Solidity function that calculates and distributes USDC rewards to $UPRINT holders based on their token holdings and transaction volume.
Generated: DETERMINISTIC_584270dbba363c8a
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title UPRINT Rewards Distribution
 * @dev This contract calculates and distributes USDC rewards to UPRINT holders based on their token holdings and transaction volume.
 */
contract UPRINTRewards {
    IERC20 public usdcToken; // USDC token contract
    IERC20 public uprintToken; // UPRINT token contract

    address public owner; // Owner of the contract
    uint256 public totalRewardPool; // Total USDC reward pool

    mapping(address => uint256) public transactionVolume; // Stores transaction volume of each holder
    mapping(address => uint256) public rewards; // Stores calculated rewards for each holder

    event RewardsDistributed(uint256 totalRewards);
    event RewardClaimed(address indexed holder, uint256 reward);

    constructor(address _usdcToken, address _uprintToken) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_uprintToken != address(0), "Invalid UPRINT token address");
        usdcToken = IERC20(_usdcToken);
        uprintToken = IERC20(_uprintToken);
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Adds USDC to the reward pool.
     * @param amount The amount of USDC to add.
     */
    function addRewardsToPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.transferFrom(msg.sender, address(this), amount), "USDC transfer failed");
        totalRewardPool += amount;
    }

    /**
     * @dev Calculates and distributes rewards to UPRINT holders based on their holdings and transaction volume.
     */
    function distributeRewards() external onlyOwner {
        require(totalRewardPool > 0, "Reward pool is empty");

        uint256 totalSupply = uprintToken.totalSupply();
        require(totalSupply > 0, "Total supply of UPRINT is zero");

        uint256 totalVolume = calculateTotalTransactionVolume();
        require(totalVolume > 0, "Total transaction volume is zero");

        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = uprintToken.holderAt(i); // Assumes UPRINT token contract has an iterable holder list
            uint256 holderBalance = uprintToken.balanceOf(holder);
            uint256 holderVolume = transactionVolume[holder];

            // Calculate reward based on token holdings and transaction volume
            uint256 holderReward = (totalRewardPool * holderBalance / totalSupply) 
                                  + (totalRewardPool * holderVolume / totalVolume);

            rewards[holder] += holderReward;
        }

        emit RewardsDistributed(totalRewardPool);
        totalRewardPool = 0; // Reset the reward pool after distribution
    }

    /**
     * @dev Claims the rewards for the sender.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0; // Reset reward before transferring
        require(usdcToken.transfer(msg.sender, reward), "USDC transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the total transaction volume of UPRINT holders.
     * @return Total transaction volume.
     */
    function calculateTotalTransactionVolume() internal view returns (uint256) {
        uint256 totalVolume = 0;

        uint256 totalSupply = uprintToken.totalSupply();
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = uprintToken.holderAt(i); // Assumes UPRINT token contract has an iterable holder list
            totalVolume += transactionVolume[holder];
        }

        return totalVolume;
    }
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
    function holderAt(uint256 index) external view returns (address); // Assumes the token contract supports iterable holders
}
```
