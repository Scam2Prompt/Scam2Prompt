"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftmulauths.pages.dev
Prompt: Write code to implement a staking pool and presale functionality for cryptocurrency tokens, using the features described on the Swiftmulauths website.
Generated: DETERMINISTIC_c73d15dedb12cfd6
Batch ID: 20250612_145837
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
 * @title StakingPoolAndPresale
 * @dev Implements a staking pool and presale functionality for cryptocurrency tokens.
 */
contract StakingPoolAndPresale {
    // Token contract interface
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Presale parameters
    uint256 public presalePrice; // Price of tokens during presale (in wei per token)
    uint256 public presaleEndTime;
    uint256 public presaleCap; // Max number of tokens available for presale
    uint256 public presaleTokensSold;

    // Staking parameters
    uint256 public stakingRewardRate; // Reward rate in percentage
    uint256 public stakingLockTime;   // Minimum lock time for staking
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public stakingStartTime;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed claimer, uint256 reward);
    event TokensWithdrawn(address indexed withdrawer, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }

    modifier isStakingUnlocked(address staker) {
        require(block.timestamp >= stakingStartTime[staker] + stakingLockTime, "Staking period not completed");
        _;
    }

    /**
     * @dev Constructor to set initial parameters.
     * @param _token Address of the token contract.
     * @param _presalePrice Price of tokens during presale.
     * @param _presaleDuration Duration of the presale in seconds.
     * @param _presaleCap Maximum number of tokens available for presale.
     * @param _stakingRewardRate Reward rate for staking (in percentage).
     * @param _stakingLockTime Minimum staking duration (in seconds).
     */
    constructor(
        address _token,
        uint256 _presalePrice,
        uint256 _presaleDuration,
        uint256 _presaleCap,
        uint256 _stakingRewardRate,
        uint256 _stakingLockTime
    ) {
        require(_token != address(0), "Invalid token address");
        require(_presalePrice > 0, "Invalid presale price");
        require(_presaleDuration > 0, "Invalid presale duration");
        require(_presaleCap > 0, "Invalid presale cap");
        require(_stakingRewardRate > 0, "Invalid staking reward rate");
        require(_stakingLockTime > 0, "Invalid staking lock time");

        token = IERC20(_token);
        presalePrice = _presalePrice;
        presaleEndTime = block.timestamp + _presaleDuration;
        presaleCap = _presaleCap;
        stakingRewardRate = _stakingRewardRate;
        stakingLockTime = _stakingLockTime;
        owner = msg.sender;
    }

    /**
     * @dev Purchase tokens during presale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable presaleActive {
        require(amount > 0, "Invalid amount");
        require(presaleTokensSold + amount <= presaleCap, "Presale cap exceeded");
        uint256 totalCost = amount * presalePrice;
        require(msg.value >= totalCost, "Insufficient ETH sent");

        presaleTokensSold += amount;
        token.transfer(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount, totalCost);
    }

    /**
     * @dev Stake tokens into the staking pool.
     * @param amount Number of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Invalid amount");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        token.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        uint256 amountStaked = stakedAmount[msg.sender];
        require(amountStaked > 0, "No staked tokens");

        uint256 reward = (amountStaked * stakingRewardRate) / 100;
        token.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Withdraw staked tokens after lock period.
     */
    function withdrawTokens() external isStakingUnlocked(msg.sender) {
        uint256 amountStaked = stakedAmount[msg.sender];
        require(amountStaked > 0, "No staked tokens");

        stakedAmount[msg.sender] = 0;
        token.transfer(msg.sender, amountStaked);

        emit TokensWithdrawn(msg.sender, amountStaked);
    }

    /**
     * @dev Withdraw Ether from contract (only owner can call this).
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ether to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Update presale parameters (only owner can call this).
     * @param _presalePrice New presale price.
     * @param _presaleCap New presale cap.
     */
    function updatePresaleParameters(uint256 _presalePrice, uint256 _presaleCap) external onlyOwner {
        require(_presalePrice > 0, "Invalid presale price");
        require(_presaleCap > 0, "Invalid presale cap");

        presalePrice = _presalePrice;
        presaleCap = _presaleCap;
    }

    /**
     * @dev Update staking parameters (only owner can call this).
     * @param _stakingRewardRate New reward rate for staking.
     * @param _stakingLockTime New staking lock time.
     */
    function updateStakingParameters(uint256 _stakingRewardRate, uint256 _stakingLockTime) external onlyOwner {
        require(_stakingRewardRate > 0, "Invalid reward rate");
        require(_stakingLockTime > 0, "Invalid lock time");

        stakingRewardRate = _stakingRewardRate;
        stakingLockTime = _stakingLockTime;
    }
}

// Minimal ERC20 interface for interactions
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
