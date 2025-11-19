"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: Write a smart contract using Solidity that demonstrates a proof-of-concept (PoC) for a blockchain solution, as described by Proof of Work AG.
Generated: DETERMINISTIC_9bba34076f6e9109
Batch ID: 20250612_162050
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

/**
 * @title ProofOfWorkAG
 * @dev A proof-of-concept smart contract demonstrating a simple Proof of Work mechanism.
 */
contract ProofOfWorkAG {
    // State variables
    address public owner; // Contract owner
    uint256 public difficulty; // Difficulty level for the proof of work
    bytes32 public lastHash; // Last valid hash submitted
    uint256 public reward; // Reward for solving the proof of work

    // Events
    event ProofSubmitted(address indexed solver, bytes32 hash, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _difficulty Initial difficulty level for the proof of work.
     * @param _reward Initial reward for solving the proof of work.
     */
    constructor(uint256 _difficulty, uint256 _reward) {
        require(_difficulty > 0, "Difficulty must be greater than zero");
        require(_reward > 0, "Reward must be greater than zero");

        owner = msg.sender;
        difficulty = _difficulty;
        reward = _reward;
        lastHash = bytes32(0); // Initialize lastHash to zero
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to update the difficulty level.
     * @param _difficulty New difficulty level.
     */
    function updateDifficulty(uint256 _difficulty) external onlyOwner {
        require(_difficulty > 0, "Difficulty must be greater than zero");
        difficulty = _difficulty;
    }

    /**
     * @dev Function to update the reward amount.
     * @param _reward New reward amount.
     */
    function updateReward(uint256 _reward) external onlyOwner {
        require(_reward > 0, "Reward must be greater than zero");
        reward = _reward;
    }

    /**
     * @dev Function to submit a proof of work.
     * @param nonce The nonce used to generate the hash.
     */
    function submitProof(uint256 nonce) external {
        // Generate the hash using the nonce and the last hash
        bytes32 hash = keccak256(abi.encodePacked(lastHash, nonce));

        // Check if the hash meets the difficulty requirement
        require(uint256(hash) < (2**256 / difficulty), "Hash does not meet difficulty requirement");

        // Update the last hash
        lastHash = hash;

        // Emit the ProofSubmitted event
        emit ProofSubmitted(msg.sender, hash, reward);

        // Transfer the reward to the solver
        payable(msg.sender).transfer(reward);
    }

    /**
     * @dev Function to deposit Ether into the contract.
     * Allows the owner to fund the contract for rewards.
     */
    function deposit() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Allows the owner to withdraw funds.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
