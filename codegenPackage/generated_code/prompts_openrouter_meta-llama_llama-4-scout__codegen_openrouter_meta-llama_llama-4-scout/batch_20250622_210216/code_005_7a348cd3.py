"""
Generated Code Metadata:
========================
Original URL: https://aitech-c09.pages.dev
Prompt: Create a Solidity smart contract for AITECH staking, incorporating features such as NFT boosts, tier boosts, and support for multiple EVM chains.
Generated: DETERMINISTIC_7a348cd31fbb5b25
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AITECH Staking Contract
 * @author [Your Name]
 * @notice This contract manages AITECH staking with NFT boosts, tier boosts, and support for multiple EVM chains.
 */
contract AITECHStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of NFT boosts
    mapping(uint256 => NFTBoost) public nftBoosts;

    // Mapping of tier boosts
    mapping(uint256 => TierBoost) public tierBoosts;

    // Mapping of supported EVM chains
    mapping(uint256 => bool) public supportedChains;

    // AITECH token contract
    ERC20 public aitechToken;

    // NFT contract
    IERC721 public nftContract;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Total staked AITECH
    uint256 public totalStaked;

    // Event emitted when user stakes AITECH
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes AITECH
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when NFT boost is applied
    event NFTBoostApplied(address indexed user, uint256 nftId);

    // Event emitted when tier boost is applied
    event TierBoostApplied(address indexed user, uint256 tierId);

    /**
     * @param _aitechToken Address of AITECH token contract
     * @param _nftContract Address of NFT contract
     * @param _stakingStart Staking start timestamp
     * @param _stakingEnd Staking end timestamp
     */
    constructor(
        address _aitechToken,
        address _nftContract,
        uint256 _stakingStart,
        uint256 _stakingEnd
    ) public {
        aitechToken = ERC20(_aitechToken);
        nftContract = IERC721(_nftContract);
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
    }

    /**
     * @dev Stake AITECH tokens
     * @param _amount Amount of AITECH tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid user");
        require(_amount > 0, "Invalid amount");
        require(block.timestamp >= stakingStart && block.timestamp <= stakingEnd, "Staking period is over");

        // Transfer AITECH tokens from user to contract
        aitechToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].stakedAt = block.timestamp;

        // Update total staked AITECH
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake AITECH tokens
     */
    function unstake() external nonReentrant {
        require(msg.sender != address(0), "Invalid user");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has no staked AITECH");

        // Calculate unstaking reward
        uint256 reward = calculateReward(msg.sender);

        // Transfer AITECH tokens and reward to user
        aitechToken.transfer(msg.sender, userStakingInfos[msg.sender].stakedAmount.add(reward));

        // Reset user's staking information
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].stakedAt = 0;

        // Update total staked AITECH
        totalStaked = totalStaked.sub(userStakingInfos[msg.sender].stakedAmount);

        emit Unstaked(msg.sender, userStakingInfos[msg.sender].stakedAmount);
    }

    /**
     * @dev Apply NFT boost
     * @param _nftId ID of NFT to apply as boost
     */
    function applyNFTBoost(uint256 _nftId) external nonReentrant {
        require(msg.sender != address(0), "Invalid user");
        require(nftContract.ownerOf(_nftId) == msg.sender, "User does not own NFT");

        // Update NFT boost information
        nftBoosts[_nftId].boostedUser = msg.sender;
        nftBoosts[_nftId].boostMultiplier = 1.1; // Example boost multiplier

        emit NFTBoostApplied(msg.sender, _nftId);
    }

    /**
     * @dev Apply tier boost
     * @param _tierId ID of tier to apply as boost
     */
    function applyTierBoost(uint256 _tierId) external nonReentrant {
        require(msg.sender != address(0), "Invalid user");

        // Update tier boost information
        tierBoosts[_tierId].boostedUser = msg.sender;
        tierBoosts[_tierId].boostMultiplier = 1.2; // Example boost multiplier

        emit TierBoostApplied(msg.sender, _tierId);
    }

    /**
     * @dev Calculate staking reward
     * @param _user Address of user
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        // Example reward calculation
        uint256 stakedDuration = block.timestamp.sub(userStakingInfos[_user].stakedAt);
        uint256 baseReward = userStakingInfos[_user].stakedAmount.mul(stakedDuration).div(365 days);

        // Apply NFT boost
        for (uint256 i = 0; i < nftBoosts.length; i++) {
            if (nftBoosts[i].boostedUser == _user) {
                baseReward = baseReward.mul(nftBoosts[i].boostMultiplier);
            }
        }

        // Apply tier boost
        for (uint256 i = 0; i < tierBoosts.length; i++) {
            if (tierBoosts[i].boostedUser == _user) {
                baseReward = baseReward.mul(tierBoosts[i].boostMultiplier);
            }
        }

        return baseReward;
    }

    /**
     * @dev Add support for EVM chain
     * @param _chainId ID of EVM chain to support
     */
    function addSupportedChain(uint256 _chainId) external onlyOwner {
        supportedChains[_chainId] = true;
    }

    /**
     * @dev Remove support for EVM chain
     * @param _chainId ID of EVM chain to remove support for
     */
    function removeSupportedChain(uint256 _chainId) external onlyOwner {
        supportedChains[_chainId] = false;
    }

    // User staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakedAt;
    }

    // NFT boost information
    struct NFTBoost {
        address boostedUser;
        uint256 boostMultiplier;
    }

    // Tier boost information
    struct TierBoost {
        address boostedUser;
        uint256 boostMultiplier;
    }

    // Only owner modifier
    address private owner;
    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Initialize owner
    function initializeOwner() internal {
        owner = msg.sender;
    }

    // Fallback function
    receive() external payable {}
}
```
