"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-claiim.pages.dev
Prompt: Provide an example of a Solidity contract that allows users to stake $GBTC and participate in weekly prediction challenges.
Generated: DETERMINISTIC_2e9db83f8835af92
Batch ID: 20250612_160940
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

// Importing OpenZeppelin's ERC20 interface for $GBTC token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PredictionChallenge is Ownable {
    // State variables
    IERC20 public gbtcToken; // Interface for the $GBTC token
    uint256 public challengeId; // Unique identifier for each prediction challenge
    uint256 public stakedAmount; // Total amount of $GBTC staked in the current challenge

    struct Challenge {
        uint256 id; // Challenge ID
        uint256 endTime; // Challenge end time
        bool resolved; // Whether the challenge has been resolved
        mapping(address => uint256) stakes; // User stakes
        address winner; // Address of the challenge winner
    }

    // Mapping to store challenges
    mapping(uint256 => Challenge) public challenges;

    // Events
    event ChallengeCreated(uint256 indexed challengeId, uint256 endTime);
    event Staked(address indexed user, uint256 indexed challengeId, uint256 amount);
    event ChallengeResolved(uint256 indexed challengeId, address indexed winner, uint256 amount);

    // Constructor to set the $GBTC token address
    constructor(address _gbtcToken) {
        gbtcToken = IERC20(_gbtcToken);
    }

    // Function to create a new prediction challenge
    function createChallenge(uint256 duration) external onlyOwner {
        challengeId++;
        uint256 endTime = block.timestamp + duration;
        challenges[challengeId] = Challenge({
            id: challengeId,
            endTime: endTime,
            resolved: false,
            winner: address(0)
        });
        emit ChallengeCreated(challengeId, endTime);
    }

    // Function to stake $GBTC in a challenge
    function stake(uint256 _challengeId, uint256 amount) external {
        // Ensure the challenge exists and is still active
        require(challenges[_challengeId].id == _challengeId, "Challenge does not exist");
        require(block.timestamp < challenges[_challengeId].endTime, "Challenge has ended");

        // Transfer $GBTC from user to this contract
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update stakes and total staked amount
        challenges[_challengeId].stakes[msg.sender] += amount;
        stakedAmount += amount;

        emit Staked(msg.sender, _challengeId, amount);
    }

    // Function to resolve a challenge and declare a winner
    function resolveChallenge(uint256 _challengeId, address winner) external onlyOwner {
        // Ensure the challenge exists and has not been resolved
        require(challenges[_challengeId].id == _challengeId, "Challenge does not exist");
        require(!challenges[_challengeId].resolved, "Challenge already resolved");
        require(block.timestamp >= challenges[_challengeId].endTime, "Challenge has not ended");

        // Mark the challenge as resolved and declare the winner
        challenges[_challengeId].resolved = true;
        challenges[_challengeId].winner = winner;

        // Distribute the total staked amount to the winner
        uint256 prizeAmount = stakedAmount;
        stakedAmount = 0;
        require(gbtcToken.transfer(winner, prizeAmount), "Transfer to winner failed");

        emit ChallengeResolved(_challengeId, winner, prizeAmount);
    }

    // Function to withdraw $GBTC if a user does not win
    function withdraw(uint256 _challengeId) external {
        // Ensure the challenge exists and has been resolved
        require(challenges[_challengeId].id == _challengeId, "Challenge does not exist");
        require(challenges[_challengeId].resolved, "Challenge not yet resolved");

        uint256 userStake = challenges[_challengeId].stakes[msg.sender];
        require(userStake > 0, "No stake found for user");

        // Reset user's stake before transferring to prevent re-entrancy
        challenges[_challengeId].stakes[msg.sender] = 0;

        // Transfer the user's stake back
        require(gbtcToken.transfer(msg.sender, userStake), "Transfer failed");
    }
}
```
