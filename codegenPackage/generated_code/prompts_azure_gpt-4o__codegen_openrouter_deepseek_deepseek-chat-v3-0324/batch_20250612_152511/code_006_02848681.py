"""
Generated Code Metadata:
========================
Original URL: https://smart-5wk.pages.dev
Prompt: Develop a smart contract to manage dual-tier token allocation for the $SLN Smart Layer Airdrop, including active user rewards and lottery-based distribution.
Generated: DETERMINISTIC_02848681527a0216
Batch ID: 20250612_152511
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SmartLayerAirdrop is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract
    IERC20 public slnToken;

    // Airdrop parameters
    uint256 public constant TIER1_REWARD = 1000 * 10**18; // 1000 SLN
    uint256 public constant TIER2_REWARD = 500 * 10**18;  // 500 SLN
    uint256 public constant LOTTERY_REWARD = 10000 * 10**18; // 10,000 SLN
    uint256 public constant LOTTERY_WINNERS = 10;

    // Airdrop state
    uint256 public totalAllocated;
    uint256 public lotteryPool;
    uint256 public activeUserPool;
    bool public airdropActive;

    // User tracking
    mapping(address => bool) public hasClaimed;
    mapping(address => bool) public isWhitelisted;
    mapping(address => uint256) public userTier;
    address[] public lotteryParticipants;
    address[] public lotteryWinners;

    // Events
    event WhitelistAdded(address[] users, uint256 tier);
    event RewardClaimed(address user, uint256 amount);
    event LotteryParticipated(address user);
    event LotteryWinnersSelected(address[] winners);
    event AirdropStatusChanged(bool active);
    event TokensRecovered(address token, uint256 amount);

    constructor(address _slnToken) {
        require(_slnToken != address(0), "Invalid token address");
        slnToken = IERC20(_slnToken);
        airdropActive = false;
    }

    /**
     * @dev Add users to whitelist with tier
     * @param users Array of user addresses
     * @param tier Tier (1 or 2)
     */
    function addToWhitelist(address[] memory users, uint256 tier) external onlyOwner {
        require(tier == 1 || tier == 2, "Invalid tier");
        
        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid address");
            isWhitelisted[users[i]] = true;
            userTier[users[i]] = tier;
        }
        
        emit WhitelistAdded(users, tier);
    }

    /**
     * @dev Claim reward based on tier
     */
    function claimReward() external nonReentrant {
        require(airdropActive, "Airdrop not active");
        require(isWhitelisted[msg.sender], "Not whitelisted");
        require(!hasClaimed[msg.sender], "Already claimed");

        uint256 rewardAmount;
        if (userTier[msg.sender] == 1) {
            rewardAmount = TIER1_REWARD;
        } else {
            rewardAmount = TIER2_REWARD;
        }

        require(slnToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        
        hasClaimed[msg.sender] = true;
        activeUserPool = activeUserPool.add(rewardAmount);
        totalAllocated = totalAllocated.add(rewardAmount);

        bool success = slnToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Enter lottery (only for Tier 1 users)
     */
    function enterLottery() external {
        require(airdropActive, "Airdrop not active");
        require(isWhitelisted[msg.sender], "Not whitelisted");
        require(userTier[msg.sender] == 1, "Only Tier 1 can enter");
        require(!hasClaimed[msg.sender], "Already claimed reward");

        for (uint256 i = 0; i < lotteryParticipants.length; i++) {
            if (lotteryParticipants[i] == msg.sender) {
                revert("Already participated");
            }
        }

        lotteryParticipants.push(msg.sender);
        emit LotteryParticipated(msg.sender);
    }

    /**
     * @dev Select lottery winners (only owner)
     */
    function selectLotteryWinners() external onlyOwner {
        require(lotteryParticipants.length >= LOTTERY_WINNERS, "Not enough participants");
        require(lotteryWinners.length == 0, "Winners already selected");

        uint256 totalLotteryRewards = LOTTERY_REWARD.mul(LOTTERY_WINNERS);
        require(slnToken.balanceOf(address(this)) >= totalLotteryRewards, "Insufficient lottery pool");

        // Simple pseudo-random selection (not for production - use Chainlink VRF in real implementation)
        for (uint256 i = 0; i < LOTTERY_WINNERS; i++) {
            uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))) % lotteryParticipants.length;
            address winner = lotteryParticipants[randomIndex];
            
            // Ensure no duplicates
            for (uint256 j = 0; j < lotteryWinners.length; j++) {
                if (lotteryWinners[j] == winner) {
                    i--; // Retry
                    continue;
                }
            }
            
            lotteryWinners.push(winner);
        }

        // Distribute rewards
        for (uint256 i = 0; i < lotteryWinners.length; i++) {
            hasClaimed[lotteryWinners[i]] = true;
            bool success = slnToken.transfer(lotteryWinners[i], LOTTERY_REWARD);
            require(success, "Token transfer failed");
        }

        lotteryPool = lotteryPool.add(totalLotteryRewards);
        totalAllocated = totalAllocated.add(totalLotteryRewards);

        emit LotteryWinnersSelected(lotteryWinners);
    }

    /**
     * @dev Toggle airdrop status
     * @param _active New status
     */
    function setAirdropStatus(bool _active) external onlyOwner {
        airdropActive = _active;
        emit AirdropStatusChanged(_active);
    }

    /**
     * @dev Recover any ERC20 tokens sent to contract by mistake
     * @param tokenAddress Address of token to recover
     * @param amount Amount to recover
     */
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(slnToken) || !airdropActive, "Cannot withdraw SLN during airdrop");
        
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");
        
        bool success = token.transfer(owner(), amount);
        require(success, "Token transfer failed");
        
        emit TokensRecovered(tokenAddress, amount);
    }

    /**
     * @dev Get lottery participant count
     * @return count Number of participants
     */
    function getLotteryParticipantCount() external view returns (uint256) {
        return lotteryParticipants.length;
    }

    /**
     * @dev Get remaining contract balance
     * @return balance Remaining SLN balance
     */
    function getContractBalance() external view returns (uint256) {
        return slnToken.balanceOf(address(this));
    }
}
```
