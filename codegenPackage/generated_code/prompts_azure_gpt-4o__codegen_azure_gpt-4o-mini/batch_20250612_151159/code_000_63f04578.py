"""
Generated Code Metadata:
========================
Original URL: https://web-wienerdog.pages.dev
Prompt: Write a smart contract in Solidity that mimics the tokenomics of WienerAI ($WAI), including presale allocation, staking rewards, and community rewards distribution.
Generated: DETERMINISTIC_63f045785716ec70
Batch ID: 20250612_151159
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WienerAIToken is ERC20, Ownable, ReentrancyGuard {
    // Presale allocation variables
    uint256 public presaleAllocation;
    uint256 public presaleStart;
    uint256 public presaleEnd;
    mapping(address => uint256) public presaleContributions;

    // Staking rewards variables
    uint256 public stakingRewardRate; // Reward rate per block
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public lastClaimedBlock;

    // Community rewards variables
    uint256 public communityRewardPool;
    uint256 public communityRewardRate; // Rate of distribution

    // Events
    event PresaleContribution(address indexed contributor, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 _presaleAllocation, uint256 _stakingRewardRate, uint256 _communityRewardRate) 
        ERC20("WienerAI", "WAI") {
        presaleAllocation = _presaleAllocation * (10 ** decimals());
        stakingRewardRate = _stakingRewardRate;
        communityRewardRate = _communityRewardRate;
        _mint(address(this), presaleAllocation); // Mint presale tokens to the contract
    }

    // Function to start presale
    function startPresale(uint256 duration) external onlyOwner {
        presaleStart = block.timestamp;
        presaleEnd = block.timestamp + duration;
    }

    // Function to contribute to presale
    function contributeToPresale(uint256 amount) external nonReentrant {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Not enough tokens in presale");

        presaleContributions[msg.sender] += amount;
        _transfer(address(this), msg.sender, amount);
        emit PresaleContribution(msg.sender, amount);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Update rewards before staking
        claimRewards();

        stakedAmount[msg.sender] += amount;
        lastClaimedBlock[msg.sender] = block.number;
        _transfer(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        claimRewards();

        stakedAmount[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim staking rewards
    function claimRewards() public {
        uint256 reward = calculateRewards(msg.sender);
        if (reward > 0) {
            lastClaimedBlock[msg.sender] = block.number;
            _mint(msg.sender, reward);
            emit RewardsClaimed(msg.sender, reward);
        }
    }

    // Function to calculate rewards based on staked amount and blocks
    function calculateRewards(address user) public view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 blocksStaked = block.number - lastClaimedBlock[user];
        return staked * stakingRewardRate * blocksStaked;
    }

    // Function to distribute community rewards
    function distributeCommunityRewards() external onlyOwner {
        require(communityRewardPool > 0, "No rewards to distribute");
        uint256 totalSupply = totalSupply();
        for (uint256 i = 0; i < totalSupply; i++) {
            address recipient = address(uint160(i)); // This is a placeholder; implement actual logic to get recipients
            uint256 reward = communityRewardPool * communityRewardRate / totalSupply;
            _mint(recipient, reward);
        }
        communityRewardPool = 0; // Reset the pool after distribution
    }

    // Function to fund community rewards
    function fundCommunityRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _transfer(msg.sender, address(this), amount);
        communityRewardPool += amount;
    }
}
```
