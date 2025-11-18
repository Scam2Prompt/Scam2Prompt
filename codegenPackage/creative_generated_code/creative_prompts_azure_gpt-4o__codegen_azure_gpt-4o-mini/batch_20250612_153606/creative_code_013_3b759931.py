"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Generate a smart contract function in Solidity to allow users to burn non-transferable mining credits and receive Bitcoin cloud mining power, as outlined in Bitcoin Minetrix's Stake-to-Mine concept.
Generated: DETERMINISTIC_3b7599313e835484
Batch ID: 20250612_153606
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

// Interface for the Bitcoin cloud mining power contract
interface IBitcoinMiningPower {
    function allocateMiningPower(address user, uint256 amount) external;
}

contract MiningCredits {
    // State variables
    address public owner; // Owner of the contract
    IBitcoinMiningPower public bitcoinMiningPowerContract; // Contract for Bitcoin mining power allocation

    // Mapping to track non-transferable mining credits for each user
    mapping(address => uint256) public miningCredits;

    // Event to emit when credits are burned
    event CreditsBurned(address indexed user, uint256 amount, uint256 miningPowerAllocated);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _bitcoinMiningPowerContract) {
        owner = msg.sender; // Set the contract deployer as the owner
        bitcoinMiningPowerContract = IBitcoinMiningPower(_bitcoinMiningPowerContract);
    }

    // Function to burn mining credits and receive Bitcoin cloud mining power
    function burnCredits(uint256 amount) external {
        require(amount > 0, "Invalid amount: must be greater than zero");
        require(miningCredits[msg.sender] >= amount, "Insufficient credits: user does not have enough mining credits");

        // Decrease the user's mining credits
        miningCredits[msg.sender] -= amount;

        // Allocate corresponding Bitcoin cloud mining power
        bitcoinMiningPowerContract.allocateMiningPower(msg.sender, amount);

        // Emit the CreditsBurned event
        emit CreditsBurned(msg.sender, amount, amount);
    }

    // Function to allow the owner to mint mining credits to a user
    function mintCredits(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address: cannot mint to the zero address");
        require(amount > 0, "Invalid amount: must be greater than zero");

        // Increase the user's mining credits
        miningCredits[user] += amount;
    }

    // Function to retrieve the mining credits of a user
    function getMiningCredits(address user) external view returns (uint256) {
        return miningCredits[user];
    }
}
```
