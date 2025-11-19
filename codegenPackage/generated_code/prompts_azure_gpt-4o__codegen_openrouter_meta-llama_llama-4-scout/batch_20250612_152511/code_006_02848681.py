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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SmartLayerAirdrop is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user activity status
    mapping(address => bool) public activeUsers;

    // Mapping of user reward claims
    mapping(address => bool) public rewardClaims;

    // Mapping of lottery tickets
    mapping(address => uint256) public lotteryTickets;

    // Token contract instance
    ERC20 public $SLN;

    // Total active user rewards
    uint256 public totalActiveUserRewards;

    // Total lottery-based distribution rewards
    uint256 public totalLotteryRewards;

    // Active user reward per user
    uint256 public activeUserReward;

    // Lottery ticket price
    uint256 public lotteryTicketPrice;

    // Lottery draw timestamp
    uint256 public lotteryDrawTimestamp;

    // Event emitted when user becomes active
    event UserActivated(address indexed user);

    // Event emitted when user claims reward
    event RewardClaimed(address indexed user, uint256 amount);

    // Event emitted when lottery ticket purchased
    event LotteryTicketPurchased(address indexed user, uint256 ticketId);

    // Event emitted when lottery draw occurs
    event LotteryDrawn(address indexed winner, uint256 amount);

    /**
     * @dev Initializes the Smart Layer Airdrop contract.
     * @param _slnTokenAddress Address of the $SLN token contract.
     * @param _activeUserReward Active user reward per user.
     * @param _lotteryTicketPrice Lottery ticket price.
     * @param _totalActiveUserRewards Total active user rewards.
     * @param _totalLotteryRewards Total lottery-based distribution rewards.
     */
    constructor(
        address _slnTokenAddress,
        uint256 _activeUserReward,
        uint256 _lotteryTicketPrice,
        uint256 _totalActiveUserRewards,
        uint256 _totalLotteryRewards
    ) public {
        require(_slnTokenAddress != address(0), "Invalid $SLN token address");
        $SLN = ERC20(_slnTokenAddress);
        activeUserReward = _activeUserReward;
        lotteryTicketPrice = _lotteryTicketPrice;
        totalActiveUserRewards = _totalActiveUserRewards;
        totalLotteryRewards = _totalLotteryRewards;
        lotteryDrawTimestamp = block.timestamp.add(30 days);
    }

    /**
     * @dev Activates a user for the airdrop.
     */
    function activateUser() public {
        require(!activeUsers[msg.sender], "User already active");
        activeUsers[msg.sender] = true;
        emit UserActivated(msg.sender);
    }

    /**
     * @dev Claims active user reward.
     */
    function claimReward() public nonReentrant {
        require(activeUsers[msg.sender], "User not active");
        require(!rewardClaims[msg.sender], "Reward already claimed");
        rewardClaims[msg.sender] = true;
        $SLN.transfer(msg.sender, activeUserReward);
        emit RewardClaimed(msg.sender, activeUserReward);
    }

    /**
     * @dev Purchases a lottery ticket.
     * @param _numTickets Number of tickets to purchase.
     */
    function purchaseLotteryTickets(uint256 _numTickets) public nonReentrant {
        require(_numTickets > 0, "Invalid number of tickets");
        require($SLN.balanceOf(msg.sender) >= _numTickets.mul(lotteryTicketPrice), "Insufficient $SLN balance");
        require(block.timestamp < lotteryDrawTimestamp, "Lottery draw already occurred");
        $SLN.transferFrom(msg.sender, address(this), _numTickets.mul(lotteryTicketPrice));
        lotteryTickets[msg.sender] = lotteryTickets[msg.sender].add(_numTickets);
        for (uint256 i = 0; i < _numTickets; i++) {
            emit LotteryTicketPurchased(msg.sender, lotteryTickets[msg.sender].sub(i));
        }
    }

    /**
     * @dev Draws the lottery winner.
     */
    function drawLottery() public nonReentrant {
        require(block.timestamp >= lotteryDrawTimestamp, "Lottery draw not yet due");
        require(totalLotteryRewards > 0, "No lottery rewards available");
        address winner = getRandomAddress();
        uint256 winnerTickets = lotteryTickets[winner];
        lotteryTickets[winner] = 0;
        $SLN.transfer(winner, totalLotteryRewards.mul(winnerTickets).div(getTotalLotteryTickets()));
        emit LotteryDrawn(winner, totalLotteryRewards.mul(winnerTickets).div(getTotalLotteryTickets()));
    }

    /**
     * @dev Gets a random address from the list of users with lottery tickets.
     * @return The address of the winner.
     */
    function getRandomAddress() internal view returns (address) {
        // Simple implementation for demonstration purposes
        // Consider using a secure random number generator in production
        uint256 random = uint256(keccak256(abi.encodePacked(block.timestamp))) % getNumUsersWithTickets();
        uint256 i = 0;
        for (address user in lotteryTickets) {
            if (i == random) {
                return user;
            }
            i++;
        }
        // Should never happen
        revert("No users with lottery tickets");
    }

    /**
     * @dev Gets the total number of lottery tickets.
     * @return The total number of lottery tickets.
     */
    function getTotalLotteryTickets() public view returns (uint256) {
        uint256 totalTickets = 0;
        for (address user in lotteryTickets) {
            totalTickets = totalTickets.add(lotteryTickets[user]);
        }
        return totalTickets;
    }

    /**
     * @dev Gets the number of users with lottery tickets.
     * @return The number of users with lottery tickets.
     */
    function getNumUsersWithTickets() public view returns (uint256) {
        uint256 numUsers = 0;
        for (address user in lotteryTickets) {
            if (lotteryTickets[user] > 0) {
                numUsers++;
            }
        }
        return numUsers;
    }
}
```
