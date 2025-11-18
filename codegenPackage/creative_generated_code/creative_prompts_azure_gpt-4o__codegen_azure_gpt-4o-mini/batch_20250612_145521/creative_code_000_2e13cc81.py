"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Write a smart contract in Solidity for a token similar to $GEGG, including features for presale stages, token distribution percentages (e.g., liquidity, marketing, ecosystem), and staking functionality.
Generated: DETERMINISTIC_2e13cc8143cc093e
Batch ID: 20250612_145521
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GEGGToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public liquidityPercentage = 20; // 20% for liquidity
    uint256 public marketingPercentage = 10; // 10% for marketing
    uint256 public ecosystemPercentage = 15; // 15% for ecosystem
    uint256 public presalePercentage = 55; // 55% for presale

    // Total supply of tokens
    uint256 public totalSupplyTokens = 1_000_000 * (10 ** decimals());
    uint256 public presaleEndTime;

    // Staking variables
    mapping(address => uint256) private _stakedTokens;
    mapping(address => uint256) private _stakingStartTime;
    uint256 public rewardRate = 10; // 10% reward on staking
    uint256 public totalStaked;

    // Presale configuration
    bool public presaleActive = false;
    uint256 public presalePrice; // Price per token during presale
    uint256 public tokensSold;

    event TokensDistributed(address indexed recipient, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);

    constructor() ERC20("GEGG Token", "GEGG") {
        // Allocate initial tokens based on distribution percentages
        uint256 liquidityTokens = totalSupplyTokens.mul(liquidityPercentage).div(100);
        uint256 marketingTokens = totalSupplyTokens.mul(marketingPercentage).div(100);
        uint256 ecosystemTokens = totalSupplyTokens.mul(ecosystemPercentage).div(100);
        uint256 presaleTokens = totalSupplyTokens.mul(presalePercentage).div(100);

        // Mint tokens for liquidity, marketing, ecosystem, and presale
        _mint(msg.sender, liquidityTokens);
        _mint(msg.sender, marketingTokens);
        _mint(msg.sender, ecosystemTokens);
        _mint(address(this), presaleTokens); // Mint presale tokens to the contract

        // Start presale in inactive state
        presaleEndTime = block.timestamp + 30 days; // Presale lasts for 30 days
    }

    // Activate presale with a specified price
    function startPresale(uint256 _presalePrice) external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleActive = true;
        presalePrice = _presalePrice;
    }

    // Stop presale
    function stopPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
    }

    // Purchase tokens during the presale
    function buyTokens(uint256 amount) external payable nonReentrant {
        require(presaleActive, "Presale is not active");
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value == amount.mul(presalePrice), "Incorrect Ether sent");
        require(tokensSold.add(amount) <= balanceOf(address(this)), "Not enough tokens in presale");

        tokensSold = tokensSold.add(amount);
        _transfer(address(this), msg.sender, amount);

        emit TokensDistributed(msg.sender, amount);
    }

    // Stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakedTokens[msg.sender] = _stakedTokens[msg.sender].add(amount);
        _stakingStartTime[msg.sender] = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens and claim rewards
    function unstakeTokens() external nonReentrant {
        uint256 stakedAmount = _stakedTokens[msg.sender];
        require(stakedAmount > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);
        
        // Reset staked amount
        _stakedTokens[msg.sender] = 0;
        totalStaked = totalStaked.sub(stakedAmount);

        // Transfer staked amount and rewards back to the user
        _transfer(address(this), msg.sender, stakedAmount);
        if (reward > 0) {
            _mint(msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    // Calculate rewards based on staked amount and duration
    function calculateRewards(address staker) public view returns (uint256) {
        uint256 stakedAmount = _stakedTokens[staker];
        if (stakedAmount == 0) return 0;

        uint256 stakingDuration = block.timestamp.sub(_stakingStartTime[staker]);
        return stakedAmount.mul(stakingDuration).mul(rewardRate).div(365 days).div(100); // Annual reward rate
    }

    // Withdraw Ether from the contract (owner only)
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
