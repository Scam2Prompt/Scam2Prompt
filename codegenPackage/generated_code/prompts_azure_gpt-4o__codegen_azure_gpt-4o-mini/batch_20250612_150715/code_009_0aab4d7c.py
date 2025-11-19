"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Write a smart contract to enable builders to offer product trials as rewards for Farcaster Members using the Moxie Protocol.
Generated: DETERMINISTIC_0aab4d7c7e523234
Batch ID: 20250612_150715
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for managing product trials as rewards for Farcaster Members
contract MoxieProtocol {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public rewardToken; // Token used for rewards

    // Struct to represent a product trial
    struct ProductTrial {
        uint256 id; // Unique identifier for the trial
        address builder; // Address of the builder offering the trial
        string productName; // Name of the product
        uint256 rewardAmount; // Amount of tokens rewarded for the trial
        bool isActive; // Status of the trial
    }

    // Mapping to store product trials by their ID
    mapping(uint256 => ProductTrial) public productTrials;
    uint256 public trialCount; // Counter for the number of trials

    // Events for logging
    event ProductTrialCreated(uint256 indexed trialId, address indexed builder, string productName, uint256 rewardAmount);
    event ProductTrialClaimed(uint256 indexed trialId, address indexed member);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _rewardToken) {
        owner = msg.sender; // Set the contract deployer as the owner
        rewardToken = IERC20(_rewardToken); // Set the reward token
    }

    // Function to create a new product trial
    function createProductTrial(string memory _productName, uint256 _rewardAmount) external onlyOwner {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        trialCount++; // Increment the trial count
        productTrials[trialCount] = ProductTrial(trialCount, msg.sender, _productName, _rewardAmount, true); // Create a new trial

        emit ProductTrialCreated(trialCount, msg.sender, _productName, _rewardAmount); // Emit event
    }

    // Function for members to claim a product trial reward
    function claimProductTrial(uint256 _trialId) external {
        ProductTrial storage trial = productTrials[_trialId]; // Retrieve the trial

        require(trial.isActive, "Trial is not active"); // Check if the trial is active
        require(rewardToken.balanceOf(address(this)) >= trial.rewardAmount, "Insufficient reward balance"); // Check contract balance

        // Transfer the reward to the member
        rewardToken.transfer(msg.sender, trial.rewardAmount);

        // Emit event for claiming the trial
        emit ProductTrialClaimed(_trialId, msg.sender);
    }

    // Function to deactivate a product trial (only callable by the owner)
    function deactivateProductTrial(uint256 _trialId) external onlyOwner {
        ProductTrial storage trial = productTrials[_trialId]; // Retrieve the trial
        require(trial.isActive, "Trial is already inactive"); // Check if the trial is active

        trial.isActive = false; // Deactivate the trial
    }

    // Function to withdraw tokens from the contract (only callable by the owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer tokens to the owner
        rewardToken.transfer(owner, _amount);
    }
}
```
