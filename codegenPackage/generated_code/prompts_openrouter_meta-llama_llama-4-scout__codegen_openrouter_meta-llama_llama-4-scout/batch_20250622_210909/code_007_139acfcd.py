"""
Generated Code Metadata:
========================
Original URL: https://memeindex-ie.web.app
Prompt: Write a Solidity smart contract for managing the Meme Index platform's tokenomics, including the distribution of presale tokens, staking rewards, and community incentives.
Generated: DETERMINISTIC_139acfcde8420531
Batch ID: 20250622_210909
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

/**
 * @title MemeIndexTokenomics
 * @author [Your Name]
 * @notice Manages the Meme Index platform's tokenomics, including presale token distribution, 
 *         staking rewards, and community incentives.
 */
contract MemeIndexTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective roles
    mapping(address => bool) public isPresaleParticipant;
    mapping(address => bool) public isCommunityIncentiveRecipient;

    // Presale token distribution details
    uint256 public presaleTokenSupply;
    uint256 public presaleTokenPrice;

    // Staking rewards details
    uint256 public stakingRewardRate;
    mapping(address => uint256) public stakingRewards;

    // Community incentives details
    uint256 public communityIncentiveRate;
    mapping(address => uint256) public communityIncentives;

    // Event emitted when presale tokens are distributed
    event PresaleTokensDistributed(address indexed participant, uint256 amount);

    // Event emitted when staking rewards are claimed
    event StakingRewardsClaimed(address indexed staker, uint256 amount);

    // Event emitted when community incentives are claimed
    event CommunityIncentivesClaimed(address indexed recipient, uint256 amount);

    /**
     * @notice Initializes the MemeIndexTokenomics contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param initialSupply The initial supply of tokens
     * @param presaleTokenSupply_ The total supply of presale tokens
     * @param presaleTokenPrice_ The price of presale tokens
     * @param stakingRewardRate_ The rate of staking rewards
     * @param communityIncentiveRate_ The rate of community incentives
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 presaleTokenSupply_,
        uint256 presaleTokenPrice_,
        uint256 stakingRewardRate_,
        uint256 communityIncentiveRate_
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);

        presaleTokenSupply = presaleTokenSupply_;
        presaleTokenPrice = presaleTokenPrice_;
        stakingRewardRate = stakingRewardRate_;
        communityIncentiveRate = communityIncentiveRate_;
    }

    /**
     * @notice Distributes presale tokens to participants
     * @param participant The address of the participant
     * @param amount The amount of tokens to distribute
     */
    function distributePresaleTokens(address participant, uint256 amount) external onlyOwner {
        require(participant != address(0), "Invalid participant address");
        require(amount > 0, "Invalid token amount");
        require(presaleTokenSupply >= amount, "Insufficient presale token supply");

        presaleTokenSupply = presaleTokenSupply.sub(amount);
        _mint(participant, amount);
        isPresaleParticipant[participant] = true;

        emit PresaleTokensDistributed(participant, amount);
    }

    /**
     * @notice Claims staking rewards
     */
    function claimStakingRewards() external nonReentrant {
        uint256 rewards = stakingRewards[msg.sender];
        require(rewards > 0, "No staking rewards to claim");

        stakingRewards[msg.sender] = 0;
        _mint(msg.sender, rewards);

        emit StakingRewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Updates staking rewards for a staker
     * @param staker The address of the staker
     * @param amount The amount of rewards to update
     */
    function updateStakingRewards(address staker, uint256 amount) external onlyOwner {
        require(staker != address(0), "Invalid staker address");
        require(amount > 0, "Invalid reward amount");

        stakingRewards[staker] = stakingRewards[staker].add(amount);
    }

    /**
     * @notice Claims community incentives
     */
    function claimCommunityIncentives() external nonReentrant {
        uint256 incentives = communityIncentives[msg.sender];
        require(incentives > 0, "No community incentives to claim");

        communityIncentives[msg.sender] = 0;
        _mint(msg.sender, incentives);

        emit CommunityIncentivesClaimed(msg.sender, incentives);
    }

    /**
     * @notice Updates community incentives for a recipient
     * @param recipient The address of the recipient
     * @param amount The amount of incentives to update
     */
    function updateCommunityIncentives(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Invalid incentive amount");

        communityIncentives[recipient] = communityIncentives[recipient].add(amount);
        isCommunityIncentiveRecipient[recipient] = true;
    }

    /**
     * @notice Burns tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        super.burn(amount);
    }

    /**
     * @notice Burns tokens from a specified address
     * @param account The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        super.burnFrom(account, amount);
    }
}
```
