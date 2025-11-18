"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Write a smart contract to enable builders to offer product trials as rewards for Farcaster Members using the Moxie Protocol.
Generated: DETERMINISTIC_0aab4d7c7e523234
Batch ID: 20250612_150715
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

// Importing OpenZeppelin's ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract to manage product trials as rewards for Farcaster Members using the Moxie Protocol
contract ProductTrialReward {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public rewardToken; // Token used for rewards

    // Event emitted when a new trial is offered
    event TrialOffered(address indexed builder, uint256 indexed trialId, string productName);
    
    // Event emitted when a trial is redeemed
    event TrialRedeemed(address indexed member, uint256 indexed trialId);

    // Struct to represent a product trial
    struct Trial {
        string productName; // Name of the product
        uint256 rewardAmount; // Amount of tokens rewarded for the trial
        bool isActive; // Indicates if the trial is active
    }

    // Mapping to store trials by ID
    mapping(uint256 => Trial) public trials;
    uint256 public trialCount; // Counter for trial IDs

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with the reward token
    constructor(IERC20 _rewardToken) {
        owner = msg.sender; // Set the contract deployer as the owner
        rewardToken = _rewardToken; // Set the reward token
    }

    // Function to offer a new product trial
    function offerTrial(string memory _productName, uint256 _rewardAmount) external onlyOwner {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        // Create a new trial and increment the trial count
        trials[trialCount] = Trial({
            productName: _productName,
            rewardAmount: _rewardAmount,
            isActive: true
        });

        emit TrialOffered(msg.sender, trialCount, _productName); // Emit event for the new trial
        trialCount++; // Increment the trial counter
    }

    // Function for members to redeem a trial
    function redeemTrial(uint256 _trialId) external {
        Trial storage trial = trials[_trialId]; // Get the trial by ID
        require(trial.isActive, "Trial is not active"); // Ensure the trial is active

        // Transfer reward tokens to the member
        bool success = rewardToken.transfer(msg.sender, trial.rewardAmount);
        require(success, "Transfer failed");

        trial.isActive = false; // Mark trial as redeemed
        emit TrialRedeemed(msg.sender, _trialId); // Emit event for the redeemed trial
    }

    // Function for the owner to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");

        bool success = rewardToken.transfer(owner, amount);
        require(success, "Transfer failed");
    }
}
```
