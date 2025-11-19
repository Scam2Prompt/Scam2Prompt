"""
Generated Code Metadata:
========================
Original URL: https://ipmbway.pages.dev
Prompt: Design a smart contract in Solidity for a simple staking mechanism that allows users to stake GoldPro Tokens and receive a discount on redeemable physical gold through GEM NFTs.
Generated: DETERMINISTIC_77e8d975eeb565ff
Batch ID: 20250622_210145
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GoldProStaking is ReentrancyGuard, Ownable {
    // Token interfaces
    IERC20 public goldProToken;
    IERC721 public gemNFT;

    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public stakingDuration;
    uint256 public discountPercentage; // Basis points (e.g., 1000 = 10%)
    uint256 public totalStaked;

    // Stake tracking
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        bool claimed;
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event DiscountApplied(address indexed user, uint256 discountAmount);

    constructor(
        address _goldProToken,
        address _gemNFT,
        uint256 _minStakeAmount,
        uint256 _stakingDuration,
        uint256 _discountPercentage
    ) {
        require(_goldProToken != address(0), "Invalid GoldPro token address");
        require(_gemNFT != address(0), "Invalid GEM NFT address");
        require(_minStakeAmount > 0, "Minimum stake amount must be > 0");
        require(_stakingDuration > 0, "Staking duration must be > 0");
        require(_discountPercentage <= 10000, "Discount cannot exceed 100%");

        goldProToken = IERC20(_goldProToken);
        gemNFT = IERC721(_gemNFT);
        minStakeAmount = _minStakeAmount;
        stakingDuration = _stakingDuration;
        discountPercentage = _discountPercentage;
    }

    /**
     * @notice Stake GoldPro tokens to qualify for discount
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(stakes[msg.sender].amount == 0, "Already staked");

        stakes[msg.sender] = Stake({
            amount: amount,
            stakedAt: block.timestamp,
            claimed: false
        });

        totalStaked += amount;

        require(
            goldProToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens after staking period
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(
            block.timestamp >= userStake.stakedAt + stakingDuration,
            "Staking period not ended"
        );

        uint256 amount = userStake.amount;
        totalStaked -= amount;

        delete stakes[msg.sender];

        require(
            goldProToken.transfer(msg.sender, amount),
            "Transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Apply discount when redeeming physical gold with GEM NFT
     * @param nftId ID of the GEM NFT being used for redemption
     * @return discountAmount The calculated discount amount
     */
    function applyDiscount(uint256 nftId) external nonReentrant returns (uint256) {
        require(gemNFT.ownerOf(nftId) == msg.sender, "Not NFT owner");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(!userStake.claimed, "Discount already claimed");

        uint256 discountAmount = (userStake.amount * discountPercentage) / 10000;
        userStake.claimed = true;

        emit DiscountApplied(msg.sender, discountAmount);
        return discountAmount;
    }

    /**
     * @notice Update staking parameters (owner only)
     * @param _minStakeAmount New minimum stake amount
     * @param _stakingDuration New staking duration in seconds
     * @param _discountPercentage New discount percentage in basis points
     */
    function updateStakingParameters(
        uint256 _minStakeAmount,
        uint256 _stakingDuration,
        uint256 _discountPercentage
    ) external onlyOwner {
        require(_minStakeAmount > 0, "Minimum stake amount must be > 0");
        require(_stakingDuration > 0, "Staking duration must be > 0");
        require(_discountPercentage <= 10000, "Discount cannot exceed 100%");

        minStakeAmount = _minStakeAmount;
        stakingDuration = _stakingDuration;
        discountPercentage = _discountPercentage;
    }

    /**
     * @notice Emergency withdraw tokens (owner only)
     * @param tokenAddress Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
