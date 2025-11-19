"""
Generated Code Metadata:
========================
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: "Generate a smart contract code for an NFT launchpad that includes staking $SFUND and $SNFTS for early access to project tokens and NFTs, with functionalities for team mint, lottery phases, and FCFS allocation."
Generated: DETERMINISTIC_f6a3d559a342684d
Batch ID: 20250622_210502
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTLaunchpad is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token contracts
    IERC20 public sfundToken;
    IERC20 public projectToken;
    IERC721 public snftsToken;

    // Launchpad parameters
    struct Launchpad {
        uint256 startTime;
        uint256 endTime;
        uint256 teamMintTime;
        uint256 lotteryPhaseTime;
        uint256 fcfsPhaseTime;
        uint256 totalTokens;
        uint256 tokensAllocated;
        uint256 pricePerToken;
        uint256 maxPerUser;
        bool isActive;
    }

    // User stakes
    struct UserStake {
        uint256 sfundAmount;
        uint256 snftsAmount;
        uint256 lastStakeTime;
    }

    // Allocation details
    struct UserAllocation {
        uint256 tokensBought;
        bool hasTeamMintAccess;
        bool hasLotteryAccess;
        bool hasFCFSAccess;
    }

    // Launchpad details
    Launchpad public currentLaunchpad;
    
    // Mappings
    mapping(address => UserStake) public userStakes;
    mapping(address => UserAllocation) public userAllocations;
    mapping(address => bool) public whitelistedTeams;

    // Events
    event Staked(address indexed user, uint256 sfundAmount, uint256 snftsAmount);
    event Unstaked(address indexed user, uint256 sfundAmount, uint256 snftsAmount);
    event TokensPurchased(address indexed user, uint256 amount);
    event TeamMinted(address indexed teamMember, uint256 amount);
    event LotteryParticipated(address indexed user);
    event FCFSParticipated(address indexed user);

    constructor(
        address _sfundToken,
        address _snftsToken
    ) {
        sfundToken = IERC20(_sfundToken);
        snftsToken = IERC721(_snftsToken);
    }

    // Set project token for current launchpad
    function setProjectToken(address _projectToken) external onlyOwner {
        projectToken = IERC20(_projectToken);
    }

    // Setup new launchpad
    function setupLaunchpad(
        uint256 _startTime,
        uint256 _endTime,
        uint256 _teamMintTime,
        uint256 _lotteryPhaseTime,
        uint256 _fcfsPhaseTime,
        uint256 _totalTokens,
        uint256 _pricePerToken,
        uint256 _maxPerUser
    ) external onlyOwner {
        require(_startTime < _endTime, "Invalid time range");
        require(_teamMintTime < _lotteryPhaseTime, "Team mint must be before lottery");
        require(_lotteryPhaseTime < _fcfsPhaseTime, "Lottery must be before FCFS");
        require(_fcfsPhaseTime < _endTime, "FCFS must be before end");

        currentLaunchpad = Launchpad({
            startTime: _startTime,
            endTime: _endTime,
            teamMintTime: _teamMintTime,
            lotteryPhaseTime: _lotteryPhaseTime,
            fcfsPhaseTime: _fcfsPhaseTime,
            totalTokens: _totalTokens,
            tokensAllocated: 0,
            pricePerToken: _pricePerToken,
            maxPerUser: _maxPerUser,
            isActive: true
        });
    }

    // Stake SFUND tokens
    function stakeSFUND(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        require(sfundToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        UserStake storage stake = userStakes[msg.sender];
        stake.sfundAmount = stake.sfundAmount.add(amount);
        stake.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, amount, 0);
    }

    // Stake SNFTs tokens
    function stakeSNFTS(uint256 tokenId) external nonReentrant {
        snftsToken.transferFrom(msg.sender, address(this), tokenId);

        UserStake storage stake = userStakes[msg.sender];
        stake.snftsAmount = stake.snftsAmount.add(1);
        stake.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, 0, 1);
    }

    // Unstake SFUND tokens
    function unstakeSFUND(uint256 amount) external nonReentrant {
        UserStake storage stake = userStakes[msg.sender];
        require(stake.sfundAmount >= amount, "Insufficient staked");

        stake.sfundAmount = stake.sfundAmount.sub(amount);
        require(sfundToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount, 0);
    }

    // Unstake SNFTs tokens
    function unstakeSNFTS(uint256 tokenId) external nonReentrant {
        UserStake storage stake = userStakes[msg.sender];
        require(stake.snftsAmount > 0, "No SNFTs staked");

        stake.snftsAmount = stake.snftsAmount.sub(1);
        snftsToken.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, 0, 1);
    }

    // Whitelist team members
    function whitelistTeam(address[] memory teamMembers) external onlyOwner {
        for (uint256 i = 0; i < teamMembers.length; i++) {
            whitelistedTeams[teamMembers[i]] = true;
        }
    }

    // Team mint function
    function teamMint(uint256 amount) external nonReentrant {
        require(block.timestamp >= currentLaunchpad.teamMintTime && block.timestamp < currentLaunchpad.lotteryPhaseTime, "Not team mint phase");
        require(whitelistedTeams[msg.sender], "Not whitelisted");
        require(userAllocations[msg.sender].tokensBought.add(amount) <= currentLaunchpad.maxPerUser, "Exceeds max allocation");
        require(currentLaunchpad.tokensAllocated.add(amount) <= currentLaunchpad.totalTokens, "Exceeds total supply");

        uint256 cost = amount.mul(currentLaunchpad.pricePerToken);
        require(projectToken.transferFrom(msg.sender, address(this), cost), "Payment failed");

        userAllocations[msg.sender].tokensBought = userAllocations[msg.sender].tokensBought.add(amount);
        userAllocations[msg.sender].hasTeamMintAccess = true;
        currentLaunchpad.tokensAllocated = currentLaunchpad.tokensAllocated.add(amount);

        emit TeamMinted(msg.sender, amount);
    }

    // Enter lottery phase
    function enterLottery() external nonReentrant {
        require(block.timestamp >= currentLaunchpad.lotteryPhaseTime && block.timestamp < currentLaunchpad.fcfsPhaseTime, "Not lottery phase");
        UserStake memory stake = userStakes[msg.sender];
        require(stake.sfundAmount > 0 || stake.snftsAmount > 0, "No stake");

        userAllocations[msg.sender].hasLotteryAccess = true;
        emit LotteryParticipated(msg.sender);
    }

    // Purchase tokens during FCFS phase
    function purchaseTokensFCFS(uint256 amount) external nonReentrant {
        require(block.timestamp >= currentLaunchpad.fcfsPhaseTime && block.timestamp < currentLaunchpad.endTime, "Not FCFS phase");
        require(userAllocations[msg.sender].hasLotteryAccess, "Not eligible");
        require(userAllocations[msg.sender].tokensBought.add(amount) <= currentLaunchpad.maxPerUser, "Exceeds max allocation");
        require(currentLaunchpad.tokensAllocated.add(amount) <= currentLaunchpad.totalTokens, "Exceeds total supply");

        uint256 cost = amount.mul(currentLaunchpad.pricePerToken);
        require(projectToken.transferFrom(msg.sender, address(this), cost), "Payment failed");

        userAllocations[msg.sender].tokensBought = userAllocations[msg.sender].tokensBought.add(amount);
        userAllocations[msg.sender].hasFCFSAccess = true;
        currentLaunchpad.tokensAllocated = currentLaunchpad.tokensAllocated.add(amount);

        emit FCFSParticipated(msg.sender);
        emit TokensPurchased(msg.sender, amount);
    }

    // Withdraw funds (owner only)
    function withdrawFunds() external onlyOwner {
        require(block.timestamp >= currentLaunchpad.endTime, "Launchpad not ended");
        uint
