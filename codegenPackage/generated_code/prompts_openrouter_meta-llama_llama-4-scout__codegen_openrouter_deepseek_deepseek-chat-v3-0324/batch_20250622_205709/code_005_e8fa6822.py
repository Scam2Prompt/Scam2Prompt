"""
Generated Code Metadata:
========================
Original URL: https://dappadapp.pages.dev
Prompt: "Develop a smart contract for a launchpad that allows projects to raise funds in a fair and equitable manner, using a staking and distribution methodology like Dappad's."
Generated: DETERMINISTIC_e8fa6822bed04f14
Batch ID: 20250622_205709
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FairLaunchpad is Ownable, ReentrancyGuard {
    struct Project {
        address tokenAddress;
        uint256 totalTokens;
        uint256 tokensForSale;
        uint256 pricePerToken;
        uint256 minStakeAmount;
        uint256 startTime;
        uint256 endTime;
        uint256 totalRaised;
        bool isActive;
    }

    struct UserStake {
        uint256 amount;
        uint256 timestamp;
    }

    mapping(uint256 => Project) public projects;
    mapping(address => mapping(uint256 => UserStake)) public userStakes;
    mapping(address => mapping(uint256 => uint256)) public userContributions;
    mapping(address => uint256) public userTotalStaked;

    IERC20 public stakingToken;
    uint256 public projectCount;
    uint256 public constant MIN_DURATION = 1 days;
    uint256 public constant MAX_DURATION = 30 days;

    event ProjectCreated(
        uint256 indexed projectId,
        address indexed tokenAddress,
        uint256 totalTokens,
        uint256 tokensForSale,
        uint256 pricePerToken,
        uint256 minStakeAmount,
        uint256 startTime,
        uint256 endTime
    );
    event Staked(address indexed user, uint256 indexed projectId, uint256 amount);
    event Unstaked(address indexed user, uint256 indexed projectId, uint256 amount);
    event Contributed(address indexed user, uint256 indexed projectId, uint256 amount);
    event TokensClaimed(address indexed user, uint256 indexed projectId, uint256 amount);
    event ProjectStatusChanged(uint256 indexed projectId, bool isActive);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        stakingToken = IERC20(_stakingToken);
    }

    function createProject(
        address _tokenAddress,
        uint256 _totalTokens,
        uint256 _tokensForSale,
        uint256 _pricePerToken,
        uint256 _minStakeAmount,
        uint256 _startTime,
        uint256 _duration
    ) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_tokensForSale > 0 && _tokensForSale <= _totalTokens, "Invalid tokens for sale");
        require(_pricePerToken > 0, "Price per token must be greater than 0");
        require(_minStakeAmount > 0, "Min stake amount must be greater than 0");
        require(_startTime >= block.timestamp, "Start time must be in the future");
        require(_duration >= MIN_DURATION && _duration <= MAX_DURATION, "Invalid duration");

        uint256 projectId = projectCount++;
        uint256 endTime = _startTime + _duration;

        projects[projectId] = Project({
            tokenAddress: _tokenAddress,
            totalTokens: _totalTokens,
            tokensForSale: _tokensForSale,
            pricePerToken: _pricePerToken,
            minStakeAmount: _minStakeAmount,
            startTime: _startTime,
            endTime: endTime,
            totalRaised: 0,
            isActive: true
        });

        emit ProjectCreated(
            projectId,
            _tokenAddress,
            _totalTokens,
            _tokensForSale,
            _pricePerToken,
            _minStakeAmount,
            _startTime,
            endTime
        );
    }

    function stake(uint256 projectId, uint256 amount) external nonReentrant {
        Project storage project = projects[projectId];
        require(project.isActive, "Project is not active");
        require(block.timestamp < project.startTime, "Staking period has ended");
        require(amount > 0, "Amount must be greater than 0");

        userStakes[msg.sender][projectId].amount += amount;
        userStakes[msg.sender][projectId].timestamp = block.timestamp;
        userTotalStaked[msg.sender] += amount;

        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Staking transfer failed");

        emit Staked(msg.sender, projectId, amount);
    }

    function unstake(uint256 projectId, uint256 amount) external nonReentrant {
        Project storage project = projects[projectId];
        require(project.isActive, "Project is not active");
        require(block.timestamp < project.startTime, "Cannot unstake after sale starts");
        require(amount > 0, "Amount must be greater than 0");
        require(userStakes[msg.sender][projectId].amount >= amount, "Insufficient staked amount");

        userStakes[msg.sender][projectId].amount -= amount;
        userTotalStaked[msg.sender] -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Unstaking transfer failed");

        emit Unstaked(msg.sender, projectId, amount);
    }

    function contribute(uint256 projectId, uint256 amount) external payable nonReentrant {
        Project storage project = projects[projectId];
        require(project.isActive, "Project is not active");
        require(block.timestamp >= project.startTime && block.timestamp <= project.endTime, "Contribution period not active");
        require(amount > 0, "Amount must be greater than 0");
        require(userStakes[msg.sender][projectId].amount >= project.minStakeAmount, "Minimum stake not met");

        uint256 contributionValue = amount * project.pricePerToken;
        require(msg.value >= contributionValue, "Insufficient funds");

        userContributions[msg.sender][projectId] += amount;
        project.totalRaised += amount;

        emit Contributed(msg.sender, projectId, amount);
    }

    function claimTokens(uint256 projectId) external nonReentrant {
        Project storage project = projects[projectId];
        require(!project.isActive || block.timestamp > project.endTime, "Project is still active");
        require(userContributions[msg.sender][projectId] > 0, "No tokens to claim");

        uint256 tokensToClaim = userContributions[msg.sender][projectId];
        userContributions[msg.sender][projectId] = 0;

        IERC20 projectToken = IERC20(project.tokenAddress);
        require(projectToken.transfer(msg.sender, tokensToClaim), "Token transfer failed");

        emit TokensClaimed(msg.sender, projectId, tokensToClaim);
    }

    function setProjectStatus(uint256 projectId, bool isActive) external onlyOwner {
        projects[projectId].isActive = isActive;
        emit ProjectStatusChanged(projectId, isActive);
    }

    function withdrawFunds(uint256 projectId) external onlyOwner {
        Project storage project = projects[projectId];
        require(block.timestamp > project.endTime, "Project not ended yet");
        require(project.totalRaised > 0, "No funds to withdraw");

        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(owner(), balance);
    }
}
```
