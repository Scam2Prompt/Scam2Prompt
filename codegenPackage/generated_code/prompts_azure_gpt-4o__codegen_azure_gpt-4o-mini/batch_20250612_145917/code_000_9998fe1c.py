"""
Generated Code Metadata:
========================
Original URL: https://sonic-labs.vercel.app
Prompt: Write a Solidity smart contract that utilizes Sonic's Fee Monetization feature to maximize developer earnings by boosting on-chain traffic. Include examples of how fees are distributed.
Generated: DETERMINISTIC_9998fe1cd7aee74a
Batch ID: 20250612_145917
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract to implement Sonic's Fee Monetization feature
contract SonicFeeMonetization is Ownable {
    // Event to log fee distribution
    event FeesDistributed(address indexed recipient, uint256 amount);

    // Mapping to track the balance of each recipient
    mapping(address => uint256) public balances;

    // Total fees collected
    uint256 public totalFees;

    // Token used for fee distribution
    IERC20 public feeToken;

    // Constructor to initialize the contract with the fee token address
    constructor(address _feeToken) {
        require(_feeToken != address(0), "Invalid token address");
        feeToken = IERC20(_feeToken);
    }

    // Function to collect fees (to be called by the contract that generates fees)
    function collectFees(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalFees += amount;
        // Transfer the fees to this contract
        require(feeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }

    // Function to distribute fees to recipients
    function distributeFees(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            require(totalFees >= amounts[i], "Insufficient total fees");

            // Update the balance of the recipient
            balances[recipients[i]] += amounts[i];
            totalFees -= amounts[i];

            // Emit event for fee distribution
            emit FeesDistributed(recipients[i], amounts[i]);
        }
    }

    // Function for recipients to withdraw their fees
    function withdrawFees() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No fees to withdraw");

        // Reset the balance before transferring to prevent re-entrancy
        balances[msg.sender] = 0;

        // Transfer the fees to the recipient
        require(feeToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to check the total fees collected
    function getTotalFees() external view returns (uint256) {
        return totalFees;
    }

    // Function to check the balance of a specific recipient
    function getRecipientBalance(address recipient) external view returns (uint256) {
        return balances[recipient];
    }
}
```
