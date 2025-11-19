"""
Generated Code Metadata:
========================
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Write a smart contract in Solidity for a token similar to $GEGG, including features for presale stages, token distribution percentages (e.g., liquidity, marketing, ecosystem), and staking functionality.
Generated: DETERMINISTIC_2e13cc8143cc093e
Batch ID: 20250612_145521
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GEGGToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant LIQUIDITY_PERCENTAGE = 20;
    uint256 public constant MARKETING_PERCENTAGE = 30;
    uint256 public constant ECOSYSTEM_PERCENTAGE = 50;

    // Presale stages
    enum PresaleStage { 
        NotStarted, 
        Whitelist, 
        PublicSale 
    }

    PresaleStage public currentStage = PresaleStage.NotStarted;

    // Mapping of whitelisted addresses
    mapping(address => bool) public whitelist;

    // Mapping of stakers
    mapping(address => uint256) public stakers;

    // Mapping of staking rewards
    mapping(address => uint256) public stakingRewards;

    // Total token supply
    uint256 public totalTokens;

    // Token distribution addresses
    address public liquidityAddress;
    address public marketingAddress;
    address public ecosystemAddress;

    // Staking start and end timestamps
    uint256 public stakingStartTimestamp;
    uint256 public stakingEndTimestamp;

    // Reward token per block
    uint256 public rewardPerBlock;

    // Flag to check if staking is active
    bool public isStakingActive;

    constructor(
        uint256 _totalTokens,
        address _liquidityAddress,
        address _marketingAddress,
        address _ecosystemAddress,
        uint256 _stakingStartTimestamp,
        uint256 _stakingEndTimestamp,
        uint256 _rewardPerBlock
    ) ERC20("GEGG Token", "GEGG") {
        totalTokens = _totalTokens;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
        ecosystemAddress = _ecosystemAddress;
        stakingStartTimestamp = _stakingStartTimestamp;
        stakingEndTimestamp = _stakingEndTimestamp;
        rewardPerBlock = _rewardPerBlock;

        // Mint tokens for distribution
        _mint(address(this), totalTokens);

        // Distribute tokens
        distributeTokens();
    }

    // Distribute tokens to liquidity, marketing, and ecosystem addresses
    function distributeTokens() internal {
        uint256 liquidityTokens = totalTokens.mul(LIQUIDITY_PERCENTAGE).div(100);
        uint256 marketingTokens = totalTokens.mul(MARKETING_PERCENTAGE).div(100);
        uint256 ecosystemTokens = totalTokens.mul(ECOSYSTEM_PERCENTAGE).div(100);

        _transfer(address(this), liquidityAddress, liquidityTokens);
        _transfer(address(this), marketingAddress, marketingTokens);
        _transfer(address(this), ecosystemAddress, ecosystemTokens);
    }

    // Start presale
    function startPresale(PresaleStage _stage) external onlyOwner {
        require(_stage > currentStage, "Invalid presale stage");

        currentStage = _stage;

        if (_stage == PresaleStage.Whitelist) {
            // Whitelist logic
        } else if (_stage == PresaleStage.PublicSale) {
            // Public sale logic
        }
    }

    // Add address to whitelist
    function addToWhitelist(address _address) external onlyOwner {
        require(currentStage == PresaleStage.Whitelist, "Whitelist stage not started");

        whitelist[_address] = true;
    }

    // Start staking
    function startStaking() external onlyOwner {
        require(!isStakingActive, "Staking already active");
        require(block.timestamp >= stakingStartTimestamp, "Staking not started yet");

        isStakingActive = true;
    }

    // Stake tokens
    function stake(uint256 _amount) external {
        require(isStakingActive, "Staking not active");
        require(_amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        stakers[msg.sender] = stakers[msg.sender].add(_amount);
        _transfer(msg.sender, address(this), _amount);
    }

    // Claim staking rewards
    function claimRewards() external {
        require(isStakingActive, "Staking not active");
        require(stakers[msg.sender] > 0, "No staked tokens");

        uint256 rewards = stakingRewards[msg.sender];
        stakingRewards[msg.sender] = 0;

        _transfer(address(this), msg.sender, rewards);
    }

    // Update staking rewards
    function updateStakingRewards() external {
        // Update staking rewards logic
    }

    // Fallback function
    receive() external payable {}

    // Modifier for only owner
    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner");
        _;
    }

    // Owner function to update reward per block
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }
}
```
