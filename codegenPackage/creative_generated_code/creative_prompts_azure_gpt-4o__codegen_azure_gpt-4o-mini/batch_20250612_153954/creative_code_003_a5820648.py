"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upshift.fi
Prompt: Write a smart contract in Solidity that incorporates Upshift Finance's rewards boost mechanism (e.g., 1.25x upUSDC PT Boost) for users who participate in voting.
Generated: DETERMINISTIC_a5820648d9acdd11
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin contracts for ERC20 token standard and access control.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to manage voting and rewards boost mechanism
contract UpshiftVoting is Ownable {
    // State variables
    IERC20 public upUSDC; // Reference to the upUSDC token contract
    mapping(address => uint256) public userVotes; // Tracks votes per user
    mapping(address => uint256) public userBoostedRewards; // Tracks boosted rewards for users

    // Constants
    uint256 public constant BOOST_MULTIPLIER = 125; // 1.25x boost represented as 125
    uint256 public constant BOOST_DIVISOR = 100; // Used for calculating the boost

    // Event emitted when a user votes
    event Voted(address indexed user, uint256 votes);

    // Constructor to set the upUSDC token address
    constructor(address _upUSDC) {
        require(_upUSDC != address(0), "Invalid upUSDC address");
        upUSDC = IERC20(_upUSDC);
    }

    // Function for users to vote
    function vote(uint256 votes) external {
        require(votes > 0, "Must cast at least one vote");

        // Update user's votes
        userVotes[msg.sender] += votes;

        // Calculate boosted rewards
        uint256 boostedReward = (votes * BOOST_MULTIPLIER) / BOOST_DIVISOR;
        userBoostedRewards[msg.sender] += boostedReward;

        emit Voted(msg.sender, votes);
    }

    // Function to claim the rewards (this is a placeholder for actual reward claiming logic)
    function claimRewards() external {
        // Ensure the user has boosted rewards to claim
        uint256 rewardsToClaim = userBoostedRewards[msg.sender];
        require(rewardsToClaim > 0, "No rewards to claim");

        // Reset user's boosted rewards
        userBoostedRewards[msg.sender] = 0;

        // Transfer the boosted rewards to the user
        uint256 totalRewards = rewardsToClaim; // Placeholder for actual reward calculation
        require(upUSDC.balanceOf(address(this)) >= totalRewards, "Insufficient contract balance");
        
        // Transfer the rewards to the user
        bool success = upUSDC.transfer(msg.sender, totalRewards);
        require(success, "Transfer failed");

        // Emit an event for rewards claimed
        emit RewardsClaimed(msg.sender, totalRewards);
    }

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Allow the owner to withdraw any tokens sent to the contract accidentally
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(upUSDC), "Cannot withdraw upUSDC");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Fallback function to prevent ether from being sent to this contract
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
