"""
Generated Code Metadata:
========================
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Create a smart contract on Injective that supports structured DeFi products like liquid staking derivatives and real-world asset tokenization, as described in the Black Panther project.
Generated: DETERMINISTIC_de0a6fc6be9f373e
Batch ID: 20250612_150018
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BlackPantherDeFi
 * @dev A smart contract for structured DeFi products including:
 * - Liquid Staking Derivatives (LSD)
 * - Real-World Asset (RWA) Tokenization
 */
contract BlackPantherDeFi is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct for staking positions
    struct StakingPosition {
        uint256 amount;
        uint256 stakedAt;
        uint256 rewardDebt;
    }

    // Struct for RWA tokens
    struct RWAToken {
        address tokenAddress;
        string assetType;
        uint256 valuation;
        bool isActive;
    }

    // State variables
    IERC20 public stakingToken;
    IERC20 public rewardToken;
    uint256 public totalStaked;
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;

    // Mappings
    mapping(address => StakingPosition) public stakingPositions;
    mapping(uint256 => RWAToken) public rwaTokens;
    uint256 public rwaTokenCount;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RWATokenAdded(uint256 indexed tokenId, address tokenAddress, string assetType);
    event RWATokenUpdated(uint256 indexed tokenId, uint256 newValuation);
    event RWATokenDeactivated(uint256 indexed tokenId);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     * @param _rewardPerBlock Reward amount per block
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Updates reward variables
     */
    function updatePool() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }

        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksPassed = block.number - lastRewardBlock;
        uint256 reward = blocksPassed * rewardPerBlock;

        accRewardPerShare += (reward * 1e12) / totalStaked;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stakes tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        updatePool();

        StakingPosition storage position = stakingPositions[msg.sender];
        if (position.amount > 0) {
            uint256 pending = (position.amount * accRewardPerShare) / 1e12 - position.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        position.amount += amount;
        position.rewardDebt = (position.amount * accRewardPerShare) / 1e12;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes tokens and claims rewards
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        StakingPosition storage position = stakingPositions[msg.sender];
        require(position.amount >= amount, "Insufficient staked amount");
        require(amount > 0, "Amount must be greater than 0");

        updatePool();

        uint256 pending = (position.amount * accRewardPerShare) / 1e12 - position.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        position.amount -= amount;
        position.rewardDebt = (position.amount * accRewardPerShare) / 1e12;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims pending rewards
     */
    function claimRewards() external nonReentrant {
        updatePool();

        StakingPosition storage position = stakingPositions[msg.sender];
        uint256 pending = (position.amount * accRewardPerShare) / 1e12 - position.rewardDebt;
        require(pending > 0, "No rewards to claim");

        position.rewardDebt = (position.amount * accRewardPerShare) / 1e12;
        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Safely transfers rewards
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function safeRewardTransfer(address to, uint256 amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (amount > rewardBalance) {
            rewardToken.transfer(to, rewardBalance);
        } else {
            rewardToken.transfer(to, amount);
        }
    }

    // RWA Tokenization Functions

    /**
     * @dev Adds a new RWA token
     * @param tokenAddress Address of the RWA token
     * @param assetType Type of the real-world asset
     * @param valuation Valuation of the asset
     */
    function addRWAToken(
        address tokenAddress,
        string memory assetType,
        uint256 valuation
    ) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(bytes(assetType).length > 0, "Asset type cannot be empty");
        require(valuation > 0, "Valuation must be greater than 0");

        rwaTokenCount++;
        rwaTokens[rwaTokenCount] = RWAToken({
            tokenAddress: tokenAddress,
            assetType: assetType,
            valuation: valuation,
            isActive: true
        });

        emit RWATokenAdded(rwaTokenCount, tokenAddress, assetType);
    }

    /**
     * @dev Updates RWA token valuation
     * @param tokenId ID of the RWA token
     * @param newValuation New valuation amount
     */
    function updateRWAValuation(uint256 tokenId, uint256 newValuation) external onlyOwner {
        require(tokenId > 0 && tokenId <= rwaTokenCount, "Invalid token ID");
        require(newValuation > 0, "Valuation must be greater than 0");
        require(rwaTokens[tokenId].isActive, "Token is not active");

        rwaTokens[tokenId].valuation = newValuation;
        emit RWATokenUpdated(tokenId, newValuation);
    }

    /**
     * @dev Deactivates an RWA token
     * @param tokenId ID of the RWA token
     */
    function deactivateRWAToken(uint256 tokenId) external onlyOwner {
        require(tokenId > 0 && tokenId <= rwaTokenCount, "Invalid token ID");
        require(rwaTokens[tokenId].isActive, "Token already inactive");

        rwaTokens[tokenId].isActive = false;
        emit RWATokenDeactivated(tokenId);
    }

    /**
     * @dev Updates reward per block (only owner)
     * @param _rewardPerBlock New reward per block amount
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");
        updatePool();
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Emergency withdraw of reward tokens (only owner)
     */
    function emergencyRewardWithdraw(uint256 amount) external onlyOwner {
        require(amount <= rewardToken.balanceOf(address(this)), "Insufficient balance
