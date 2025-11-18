"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-unnfinance.pages.dev
Prompt: Create a smart contract that integrates UNION Finance's U-CDS (Crypto Default Swaps) to protect against event risks like smart contract hacks or oracle attacks.
Generated: DETERMINISTIC_83869a720fcb4a9a
Batch ID: 20250612_145731
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

// Importing the necessary interfaces for the U-CDS
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// A smart contract that integrates UNION Finance's U-CDS for protection against event risks
contract EventRiskProtector is Ownable {
    using SafeMath for uint256;

    // Address of the U-CDS contract
    address public uCdsAddress;

    // Mapping to keep track of user cover amounts
    mapping(address => uint256) public coverAmounts;

    // Event emitted when coverage is purchased
    event CoveragePurchased(address indexed user, uint256 amount);

    // Event emitted when coverage is claimed
    event CoverageClaimed(address indexed user, uint256 amount);

    // Modifier to check if the user has coverage
    modifier hasCoverage(address user) {
        require(coverAmounts[user] > 0, "No coverage purchased");
        _;
    }

    // Constructor to set the U-CDS address
    constructor(address _uCdsAddress) {
        require(_uCdsAddress != address(0), "Invalid U-CDS address");
        uCdsAddress = _uCdsAddress;
    }

    // Function to purchase coverage
    function purchaseCoverage(uint256 amount) external payable {
        require(amount > 0, "Coverage amount must be greater than 0");
        require(msg.value >= amount, "Insufficient funds sent");

        // Updating cover amounts
        coverAmounts[msg.sender] = coverAmounts[msg.sender].add(amount);

        // Emit event for coverage purchase
        emit CoveragePurchased(msg.sender, amount);
    }

    // Function to claim coverage in case of an event (e.g. hack or oracle attack)
    function claimCoverage() external hasCoverage(msg.sender) {
        uint256 amount = coverAmounts[msg.sender];

        // Resetting the cover amount to prevent re-entrancy
        coverAmounts[msg.sender] = 0;

        // Sending the cover amount back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit event for coverage claim
        emit CoverageClaimed(msg.sender, amount);
    }

    // Function to withdraw funds in case of contract emergencies
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer funds to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Function to receive Ether. Allows the contract to accept Ether transfers.
    receive() external payable {}
}
```
