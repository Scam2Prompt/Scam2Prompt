"""
Generated Code Metadata:
========================
Original URL: https://synthethicdapp.pages.dev
Prompt: "Generate a basic implementation of a bridge for staking and recovery in a Dapp ecosystem, considering KYC validation and NFT staking."
Generated: DETERMINISTIC_e37fe86a991a591f
Batch ID: 20250622_210300
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IKYCValidator {
    function isKYCVerified(address user) external view returns (bool);
}

contract StakingBridge is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC721 public nftToken;
    IKYCValidator public kycValidator;

    struct StakeInfo {
        uint256 amount;
        uint256 stakedAt;
        uint256 nftTokenId;
    }

    mapping(address => StakeInfo) public stakes;
    mapping(uint256 => bool) public stakedNfts;

    uint256 public minStakeAmount;
    uint256 public stakingDuration;
    uint256 public rewardRate;

    event Staked(address indexed user, uint256 amount, uint256 nftTokenId);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event Recovered(address indexed user, uint256 amount, uint256 nftTokenId);

    constructor(
        address _stakingToken,
        address _nftToken,
        address _kycValidator,
        uint256 _minStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        nftToken = IERC721(_nftToken);
        kycValidator = IKYCValidator(_kycValidator);
        minStakeAmount = _minStakeAmount;
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;
    }

    function stake(uint256 amount, uint256 nftTokenId) external nonReentrant {
        require(kycValidator.isKYCVerified(msg.sender), "KYC not verified");
        require(amount >= minStakeAmount, "Amount below minimum");
        require(nftToken.ownerOf(nftTokenId) == msg.sender, "Not NFT owner");
        require(!stakedNfts[nftTokenId], "NFT already staked");

        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount == 0, "Already staked");

        stakingToken.transferFrom(msg.sender, address(this), amount);
        nftToken.transferFrom(msg.sender, address(this), nftTokenId);

        userStake.amount = amount;
        userStake.stakedAt = block.timestamp;
        userStake.nftTokenId = nftTokenId;
        stakedNfts[nftTokenId] = true;

        emit Staked(msg.sender, amount, nftTokenId);
    }

    function unstake() external nonReentrant {
        StakeInfo memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.stakedAt + stakingDuration, "Staking period not ended");

        uint256 reward = calculateReward(userStake.amount, userStake.stakedAt);
        uint256 totalAmount = userStake.amount + reward;

        stakingToken.transfer(msg.sender, totalAmount);
        nftToken.transferFrom(address(this), msg.sender, userStake.nftTokenId);

        delete stakes[msg.sender];
        stakedNfts[userStake.nftTokenId] = false;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    function recoverStake(address user) external onlyOwner {
        StakeInfo memory userStake = stakes[user];
        require(userStake.amount > 0, "No stake found");

        stakingToken.transfer(user, userStake.amount);
        nftToken.transferFrom(address(this), user, userStake.nftTokenId);

        delete stakes[user];
        stakedNfts[userStake.nftTokenId] = false;

        emit Recovered(user, userStake.amount, userStake.nftTokenId);
    }

    function calculateReward(uint256 amount, uint256 stakedAt) public view returns (uint256) {
        uint256 stakingTime = block.timestamp - stakedAt;
        return (amount * rewardRate * stakingTime) / (stakingDuration * 100);
    }

    function updateStakingParams(
        uint256 _minStakeAmount,
        uint256 _stakingDuration,
        uint256 _rewardRate
    ) external onlyOwner {
        minStakeAmount = _minStakeAmount;
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;
    }

    function updateKYCValidator(address _kycValidator) external onlyOwner {
        kycValidator = IKYCValidator(_kycValidator);
    }
}
```
