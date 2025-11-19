"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawthereum.pages.dev
Prompt: Create a Solidity smart contract that integrates with the $PAWTH token for animal welfare initiatives, referencing the community's mission.
Generated: DETERMINISTIC_2f7cf7c85b85dcf4
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the AnimalWelfareInitiatives contract
contract AnimalWelfareInitiatives is Ownable {
    // State variable to hold the address of the $PAWTH token
    IERC20 public pawthToken;

    // Event emitted when a donation is made
    event DonationReceived(address indexed donor, uint256 amount);

    // Event emitted when funds are withdrawn by the owner
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Constructor to initialize the $PAWTH token address
    constructor(address _pawthTokenAddress) {
        require(_pawthTokenAddress != address(0), "Invalid token address");
        pawthToken = IERC20(_pawthTokenAddress);
    }

    // Function to donate $PAWTH tokens to the initiative
    function donate(uint256 amount) external {
        require(amount > 0, "Donation amount must be greater than zero");

        // Transfer $PAWTH tokens from the donor to this contract
        bool success = pawthToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit DonationReceived(msg.sender, amount);
    }

    // Function to withdraw funds from the contract
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(pawthToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer $PAWTH tokens from this contract to the owner's address
        bool success = pawthToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit FundsWithdrawn(msg.sender, amount);
    }

    // Function to check the balance of the contract
    function checkBalance() external view returns (uint256) {
        return pawthToken.balanceOf(address(this));
    }
}
```
