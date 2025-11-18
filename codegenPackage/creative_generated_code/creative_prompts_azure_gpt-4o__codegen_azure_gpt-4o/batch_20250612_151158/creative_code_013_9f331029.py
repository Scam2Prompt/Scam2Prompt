"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appwienerclaim.pages.dev
Prompt: Recommend security best practices for implementing custom Web3 smart contracts for token presales and staking, as described in WienerAI.
Generated: DETERMINISTIC_9f331029836eb011
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Solidity code implementation of security best practices for a custom Web3 smart contract that includes token presales and staking functionality. The code includes comments explaining each section and adheres to security best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TokenPresaleAndStaking
 * @dev A secure smart contract for token presale and staking functionality.
 */
contract TokenPresaleAndStaking {
    // State variables
    address public owner; // Contract owner
    uint256 public presalePrice; // Token price during presale
    uint256 public presaleEndTime; // Timestamp for presale end
    uint256 public stakingRewardRate; // Reward rate for staking
    uint256 public constant MINIMUM_STAKE_DURATION = 1 weeks; // Minimum staking duration

    mapping(address => uint256) public balances; // User token balances
    mapping(address => uint256) public stakedAmounts; // User staked amounts
    mapping(address => uint256) public stakingStartTimes; // User staking start timestamps

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier stakingActive() {
        require(stakedAmounts[msg.sender] > 0, "No tokens staked");
        _;
    }

    constructor(uint256 _presalePrice, uint256 _presaleDuration, uint256 _stakingRewardRate) {
        require(_presalePrice > 0, "Presale price must be greater than zero");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");
        require(_stakingRewardRate > 0, "Staking reward rate must be greater than zero");

        owner = msg.sender;
        presalePrice = _presalePrice;
        presaleEndTime = block.timestamp + _presaleDuration;
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable presaleActive {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * presalePrice, "Incorrect Ether value sent");

        balances[msg.sender] += amount;
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient token balance");

        balances[msg.sender] -= amount;
        stakedAmounts[msg.sender] += amount;
        stakingStartTimes[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstakeTokens() external stakingActive {
        require(block.timestamp >= stakingStartTimes[msg.sender] + MINIMUM_STAKE_DURATION, "Staking duration not met");

        uint256 stakedAmount = stakedAmounts[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        // Reset staking data
        stakedAmounts[msg.sender] = 0;
        stakingStartTimes[msg.sender] = 0;

        balances[msg.sender] += stakedAmount + reward;

        emit TokensUnstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculate staking rewards for a user.
     * @param user The address of the user.
     * @return reward The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        uint256 duration = block.timestamp - stakingStartTimes[user];
        reward = (stakedAmounts[user] * stakingRewardRate * duration) / 1 weeks;
    }

    /**
     * @dev Update presale price. Only owner can call this function.
     * @param _presalePrice The new presale price.
     */
    function setPresalePrice(uint256 _presalePrice) external onlyOwner {
        require(_presalePrice > 0, "Presale price must be greater than zero");
        presalePrice = _presalePrice;
    }

    /**
     * @dev Withdraw contract balance (Ether). Only owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfer not allowed");
    }

    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```

This contract includes security best practices such as:
- Using `require` for input validation and preventing invalid actions.
- Proper access control with the `onlyOwner` modifier.
- Preventing reentrancy by following the checks-effects-interactions pattern.
- Handling Ether transfers securely with fallback and receive functions.
- Enforcing a minimum staking duration to discourage premature withdrawal.
