"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-dapp.web.app
Prompt: Write a smart contract in Solidity that integrates the Proof of Intelligence (PoI) consensus mechanism described in Lightchain AI, rewarding nodes for performing AI computations like model training or inference.
Generated: DETERMINISTIC_8d6ec2c14f186e7c
Batch ID: 20250612_154820
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

// Smart contract that implements Proof of Intelligence (PoI) consensus mechanism
contract ProofOfIntelligence is Ownable {
    // Token used for rewarding nodes
    IERC20 public rewardToken;

    // Struct to hold information about each node's computation
    struct Computation {
        address node;
        uint256 reward;
        bool completed;
        uint256 timestamp;
    }

    // Mapping to store computations by their ID
    mapping(uint256 => Computation) public computations;
    uint256 public computationCount;

    // Event to notify about new computations
    event ComputationSubmitted(uint256 indexed computationId, address indexed node, uint256 reward);

    // Event to notify about rewards distributed
    event RewardDistributed(address indexed node, uint256 amount);

    // Constructor to initialize the token
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        rewardToken = IERC20(tokenAddress);
    }

    // Function to submit a computation for validation
    function submitComputation(uint256 reward) external {
        require(reward > 0, "Reward must be greater than zero");

        // Create a new computation entry
        computationCount++;
        computations[computationCount] = Computation({
            node: msg.sender,
            reward: reward,
            completed: false,
            timestamp: block.timestamp
        });

        emit ComputationSubmitted(computationCount, msg.sender, reward);
    }

    // Function to mark a computation as completed and distribute rewards
    function completeComputation(uint256 computationId) external {
        Computation storage computation = computations[computationId];

        // Ensure the computation exists and has not been completed
        require(computation.node != address(0), "Computation does not exist");
        require(!computation.completed, "Computation already completed");

        // Mark computation as completed
        computation.completed = true;

        // Transfer the reward to the node
        require(rewardToken.balanceOf(address(this)) >= computation.reward, "Insufficient contract balance");
        rewardToken.transfer(computation.node, computation.reward);

        emit RewardDistributed(computation.node, computation.reward);
    }

    // Function to withdraw tokens from the contract (only callable by the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        rewardToken.transfer(owner(), amount);
    }

    // Function to check the status of a computation
    function getComputationStatus(uint256 computationId) external view returns (Computation memory) {
        return computations[computationId];
    }
}
```
