"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greens-bitcoins.pages.dev
Prompt: Create a Solidity smart contract that allows users to participate in the Green Bitcoin presale and stake their tokens for rewards.
Generated: DETERMINISTIC_61f216e15d87894a
Batch ID: 20250612_161427
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

/// @title Green Bitcoin Presale and Staking Contract
/// @notice This smart contract allows users to participate in a token presale and stake their tokens for rewards
contract GreenBitcoinPresaleAndStaking {
    // Address of the owner (deployer of the contract)
    address public owner;

    // Presale token price in wei (e.g., 1 token = 0.01 ETH)
    uint256 public tokenPrice = 0.01 ether;

    // Total tokens available for presale
    uint256 public presaleTokenSupply = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Total tokens sold during the presale
    uint256 public tokensSold;

    // Token balances of users
    mapping(address => uint256) public tokenBalances;

    // Staking balances of users
    mapping(address => uint256) public stakingBalances;

    // Rewards earned by users
    mapping(address => uint256) public rewards;

    // Staking reward rate (e.g., 10%)
    uint256 public rewardRate = 10; // 10%

    // Tracks whether staking is active
    bool public stakingActive = false;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when tokens are staked
    event TokensStaked(address indexed staker, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed claimer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /// @notice Constructor to initialize the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /// @notice Allows users to purchase tokens during the presale
    /// @param _amount The number of tokens to purchase
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than 0");
        uint256 cost = _amount * tokenPrice;
        require(msg.value == cost, "Incorrect ETH amount sent");
        require(tokensSold + _amount <= presaleTokenSupply, "Not enough tokens left for presale");

        tokensSold += _amount;
        tokenBalances[msg.sender] += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /// @notice Allows users to stake their tokens to earn rewards
    /// @param _amount The number of tokens to stake
    function stakeTokens(uint256 _amount) external {
        require(stakingActive, "Staking is not active");
        require(_amount > 0, "Amount must be greater than 0");
        require(tokenBalances[msg.sender] >= _amount, "Insufficient token balance");

        tokenBalances[msg.sender] -= _amount;
        stakingBalances[msg.sender] += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /// @notice Allows users to claim their staking rewards
    function claimRewards() external {
        uint256 staked = stakingBalances[msg.sender];
        require(staked > 0, "No staked tokens to claim rewards");

        uint256 reward = (staked * rewardRate) / 100;
        rewards[msg.sender] += reward;

        emit RewardsClaimed(msg.sender, reward);
    }

    /// @notice Activates or deactivates the staking functionality
    /// @param _active Boolean to set staking activity
    function setStakingActive(bool _active) external onlyOwner {
        stakingActive = _active;
    }

    /// @notice Updates the token price for the presale
    /// @param _newPrice The new token price in wei
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than 0");
        tokenPrice = _newPrice;
    }

    /// @notice Withdraws the contract's ETH balance to the owner's address
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /// @notice Fallback function to prevent accidental ETH transfers without data
    receive() external payable {
        revert("ETH transfers not allowed without presale participation");
    }
}
```
