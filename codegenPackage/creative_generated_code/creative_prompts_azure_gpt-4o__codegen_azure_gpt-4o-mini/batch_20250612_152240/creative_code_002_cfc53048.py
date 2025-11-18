"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastairdropclaim.pages.dev
Prompt: Generate a smart contract snippet for managing airdrop claims on Blast Mainnet, ensuring wallet registration and reward distribution.
Generated: DETERMINISTIC_cfc530480aa82ba0
Batch ID: 20250612_152240
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

// Import the Ownable contract from OpenZeppelin to manage ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// AirdropManager contract to handle wallet registrations and reward distributions
contract AirdropManager is Ownable {
    // Mapping to track if an address is registered
    mapping(address => bool) public registeredAddresses;
    // Mapping to track the claimed status of rewards
    mapping(address => bool) public claimedRewards;

    // Event emitted when a wallet is registered
    event WalletRegistered(address indexed wallet);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed wallet, uint256 amount);

    // Reward amount
    uint256 public rewardAmount;

    // Constructor to initialize the reward amount
    constructor(uint256 _rewardAmount) {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = _rewardAmount;
    }

    // Modifier to check if the wallet is registered
    modifier onlyRegistered() {
        require(registeredAddresses[msg.sender], "Wallet not registered");
        _;
    }

    // Function to register a wallet for airdrop
    function registerWallet() external {
        require(!registeredAddresses[msg.sender], "Wallet already registered");
        registeredAddresses[msg.sender] = true;
        emit WalletRegistered(msg.sender);
    }

    // Function for registered wallets to claim their rewards
    function claimReward() external onlyRegistered {
        require(!claimedRewards[msg.sender], "Reward already claimed");

        // Mark the reward as claimed
        claimedRewards[msg.sender] = true;

        // Transfer the reward amount to the caller
        payable(msg.sender).transfer(rewardAmount);
        
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw contract balance by the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
