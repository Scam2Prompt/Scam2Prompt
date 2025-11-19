"""
Generated Code Metadata:
========================
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Write a Solidity smart contract for a token similar to MAMO, including features for presale stages, token distribution percentages, and staking rewards as described on the Matmo platform.
Generated: DETERMINISTIC_b4c0a481270dbf8d
Batch ID: 20250612_150226
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MAMOToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PRESALE_PERCENTAGE = 30;
    uint256 public constant TEAM_PERCENTAGE = 15;
    uint256 public constant MARKETING_PERCENTAGE = 10;
    uint256 public constant DEVELOPMENT_PERCENTAGE = 15;
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 30;

    // Presale stages
    enum PresaleStage { NOT_STARTED, STAGE1, STAGE2, STAGE3, COMPLETED }
    PresaleStage public currentStage = PresaleStage.NOT_STARTED;

    // Token prices for each presale stage (in wei)
    mapping(PresaleStage => uint256) public stagePrices;
    
    // Total supply
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens

    // Allocation addresses
    address public presaleAddress;
    address public teamAddress;
    address public marketingAddress;
    address public developmentAddress;
    address public stakingAddress;

    // Staking rewards
    uint256 public stakingRewardsRate = 10; // 10% annual reward
    uint256 public lastRewardTime;
    uint256 public rewardInterval = 365 days;

    // Whitelist for presale
    mapping(address => bool) public whitelist;

    // Events
    event PresaleStageChanged(PresaleStage stage);
    event TokensPurchased(address buyer, uint256 amount);
    event StakingRewardsDistributed(uint256 amount);
    event WhitelistUpdated(address user, bool status);

    constructor(
        address _presaleAddress,
        address _teamAddress,
        address _marketingAddress,
        address _developmentAddress,
        address _stakingAddress
    ) ERC20("MAMO Token", "MAMO") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");
        require(_developmentAddress != address(0), "Development address cannot be zero");
        require(_stakingAddress != address(0), "Staking address cannot be zero");

        presaleAddress = _presaleAddress;
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
        stakingAddress = _stakingAddress;

        // Set stage prices
        stagePrices[PresaleStage.STAGE1] = 0.0001 ether;
        stagePrices[PresaleStage.STAGE2] = 0.0002 ether;
        stagePrices[PresaleStage.STAGE3] = 0.0003 ether;

        // Distribute initial supply
        _mint(presaleAddress, TOTAL_SUPPLY.mul(PRESALE_PERCENTAGE).div(100));
        _mint(teamAddress, TOTAL_SUPPLY.mul(TEAM_PERCENTAGE).div(100));
        _mint(marketingAddress, TOTAL_SUPPLY.mul(MARKETING_PERCENTAGE).div(100));
        _mint(developmentAddress, TOTAL_SUPPLY.mul(DEVELOPMENT_PERCENTAGE).div(100));
        _mint(stakingAddress, TOTAL_SUPPLY.mul(STAKING_REWARDS_PERCENTAGE).div(100));

        lastRewardTime = block.timestamp;
    }

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(
            currentStage != PresaleStage.NOT_STARTED && currentStage != PresaleStage.COMPLETED,
            "Presale is not active"
        );
        _;
    }

    // Modifier to check if address is whitelisted
    modifier onlyWhitelisted() {
        require(whitelist[msg.sender], "Address not whitelisted");
        _;
    }

    // Start a new presale stage
    function startPresaleStage(PresaleStage stage) external onlyOwner {
        require(stage != PresaleStage.NOT_STARTED, "Cannot set to NOT_STARTED");
        require(uint256(stage) > uint256(currentStage), "Cannot go to previous stage");
        
        currentStage = stage;
        emit PresaleStageChanged(stage);
    }

    // Buy tokens during presale
    function buyTokens() external payable presaleActive onlyWhitelisted {
        uint256 price = stagePrices[currentStage];
        require(msg.value > 0, "Must send ETH to buy tokens");
        require(price > 0, "Token price not set for this stage");

        uint256 tokenAmount = msg.value.mul(10**18).div(price);
        require(tokenAmount <= balanceOf(presaleAddress), "Not enough tokens left in presale");

        _transfer(presaleAddress, msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Distribute staking rewards
    function distributeStakingRewards() external {
        require(block.timestamp >= lastRewardTime.add(rewardInterval), "Reward interval not passed");
        
        uint256 rewardAmount = balanceOf(stakingAddress).mul(stakingRewardsRate).div(100);
        require(rewardAmount > 0, "No rewards to distribute");

        _transfer(stakingAddress, msg.sender, rewardAmount);
        lastRewardTime = block.timestamp;
        emit StakingRewardsDistributed(rewardAmount);
    }

    // Add/remove address from whitelist
    function updateWhitelist(address user, bool status) external onlyOwner {
        whitelist[user] = status;
        emit WhitelistUpdated(user, status);
    }

    // Withdraw ETH from contract
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Set staking rewards rate
    function setStakingRewardsRate(uint256 rate) external onlyOwner {
        require(rate <= 100, "Rate cannot exceed 100%");
        stakingRewardsRate = rate;
    }

    // Set reward interval
    function setRewardInterval(uint256 interval) external onlyOwner {
        require(interval > 0, "Interval must be greater than 0");
        rewardInterval = interval;
    }

    // Set staking address
    function setStakingAddress(address _stakingAddress) external onlyOwner {
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        stakingAddress = _stakingAddress;
    }
}
```
