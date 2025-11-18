"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-com.pages.dev
Prompt: Provide a step-by-step tutorial for deploying a token presale smart contract on Ethereum, including features for staking and reward claiming as described in the $SCOTTY presale.
Generated: DETERMINISTIC_a603eda889082660
Batch ID: 20250612_152109
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
 * @title TokenPresaleWithStaking
 * @dev A token presale with staking and reward claiming functionality.
 */
contract TokenPresaleWithStaking {
    // Token variables
    address public tokenAddress;
    uint256 public presalePrice; // Price per token in wei
    uint256 public startTime;
    uint256 public endTime;

    // Staking variables
    uint256 public rewardRate; // Reward rate in percentage
    mapping(address => uint256) public stakingBalance;
    mapping(address => uint256) public stakingStartTime;
    mapping(address => uint256) public rewardsClaimed;

    // Access control
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Constructor
    constructor(
        address _tokenAddress,
        uint256 _presalePrice,
        uint256 _rewardRate,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_startTime < _endTime, "Start time must be before end time");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        tokenAddress = _tokenAddress;
        presalePrice = _presalePrice;
        rewardRate = _rewardRate;
        startTime = _startTime;
        endTime = _endTime;
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to ensure presale is active
    modifier presaleActive() {
        require(block.timestamp >= startTime, "Presale has not started");
        require(block.timestamp <= endTime, "Presale has ended");
        _;
    }

    // Function to purchase tokens during presale
    function purchaseTokens(uint256 tokenAmount) external payable presaleActive {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        uint256 requiredEther = tokenAmount * presalePrice;
        require(msg.value == requiredEther, "Incorrect Ether value sent");

        // Transfer tokens to buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to stake tokens
    function stakeTokens(uint256 tokenAmount) external {
        require(tokenAmount > 0, "Token amount must be greater than 0");

        // Transfer tokens from staker to contract
        require(
            IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount),
            "Token transfer failed"
        );

        stakingBalance[msg.sender] += tokenAmount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, tokenAmount);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address staker) public view returns (uint256) {
        uint256 stakedTime = block.timestamp - stakingStartTime[staker];
        uint256 reward = (stakingBalance[staker] * rewardRate * stakedTime) /
            (100 * 365 days);
        return reward - rewardsClaimed[staker];
    }

    // Function to claim staking rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        rewardsClaimed[msg.sender] += rewards;

        // Transfer rewards to staker
        require(
            IERC20(tokenAddress).transfer(msg.sender, rewards),
            "Token transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw tokens from the presale contract (Owner only)
    function withdrawTokens(uint256 tokenAmount) external onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than 0");

        require(
            IERC20(tokenAddress).transfer(owner, tokenAmount),
            "Token transfer failed"
        );
    }

    // Function to withdraw Ether collected during presale (Owner only)
    function withdrawEther() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Ether transfer failed");
    }
}

// Interface for ERC20 token interactions
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool);
}
```
