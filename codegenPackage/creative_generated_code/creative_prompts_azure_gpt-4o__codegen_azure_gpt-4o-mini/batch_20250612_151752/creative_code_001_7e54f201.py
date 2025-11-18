"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velodrome-7zz.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with Velodrome Finance to automate voting on pools using veVELO tokens and distribute rewards to voters.
Generated: DETERMINISTIC_7e54f20141182000
Batch ID: 20250612_151752
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Velodrome Finance to interact with veVELO tokens
interface IVelodrome {
    function vote(uint256 poolId, uint256 weight) external;
    function getReward() external;
}

// Smart contract for automated voting and reward distribution
contract AutoVoteAndReward is Ownable {
    // State variables
    IVelodrome public velodrome;
    IERC20 public veVELO; // veVELO token interface
    address public voter; // Address of the voter

    // Mapping to track pool votes
    mapping(uint256 => uint256) public poolVotes;

    // Event to log voting activity
    event Voted(uint256 indexed poolId, uint256 weight);
    event RewardsDistributed(address indexed voter, uint256 amount);

    // Constructor to set Velodrome and veVELO token addresses
    constructor(address _velodrome, address _veVELO) {
        velodrome = IVelodrome(_velodrome);
        veVELO = IERC20(_veVELO);
    }

    // Function to set the voter address
    function setVoter(address _voter) external onlyOwner {
        require(_voter != address(0), "Invalid voter address");
        voter = _voter;
    }

    // Function to automate voting on a pool
    function automateVote(uint256 poolId, uint256 weight) external {
        require(msg.sender == voter, "Only voter can call this function");
        require(weight > 0, "Weight must be greater than zero");

        // Update pool votes and cast the vote
        poolVotes[poolId] += weight;
        velodrome.vote(poolId, weight);
        
        emit Voted(poolId, weight);
    }

    // Function to distribute rewards to the voter
    function distributeRewards() external {
        require(msg.sender == voter, "Only voter can call this function");
        
        try velodrome.getReward() {
            uint256 rewardAmount = veVELO.balanceOf(address(this));
            require(rewardAmount > 0, "No rewards available");

            // Transfer rewards to the voter
            veVELO.transfer(voter, rewardAmount);

            emit RewardsDistributed(voter, rewardAmount);
        } catch {
            revert("Reward distribution failed");
        }
    }

    // Function to withdraw tokens from the contract (for emergencies)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(owner(), amount);
    }
}
```
