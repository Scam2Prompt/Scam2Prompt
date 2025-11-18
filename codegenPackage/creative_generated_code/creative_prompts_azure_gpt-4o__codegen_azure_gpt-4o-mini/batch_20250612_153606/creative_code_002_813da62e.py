"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockycoinbase.pages.dev
Prompt: Provide code in Solidity to verify wallet eligibility for airdrops based on the $ROCKY token smart contract specifications mentioned on the Rocky on Base website.
Generated: DETERMINISTIC_813da62e84916dd8
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract AirdropEligibility {

    // State variables
    IERC20 public rockyToken; // Instance of the $ROCKY token contract
    mapping(address => bool) public eligibleAddresses; // Mapping to track eligible addresses
    address public owner; // Owner of the contract

    // Events
    event AirdropEligibilityChecked(address indexed wallet, bool isEligible);

    // Constructor to set the $ROCKY token address
    constructor(address _rockyTokenAddress) {
        require(_rockyTokenAddress != address(0), "Invalid token address!");
        rockyToken = IERC20(_rockyTokenAddress);
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner!");
        _;
    }

    // Function to check wallet eligibility based on token balance
    function checkEligibility(address wallet) external returns (bool) {
        require(wallet != address(0), "Invalid wallet address!");
        
        // Get the balance of the $ROCKY token for the wallet
        uint256 balance = rockyToken.balanceOf(wallet);
        
        // Determine eligibility based on a predefined balance threshold
        // Example threshold: 100 $ROCKY tokens
        bool isEligible = balance >= 100 * 10**rockyToken.decimals();
        
        // Update the mapping and emit an event
        eligibleAddresses[wallet] = isEligible;
        emit AirdropEligibilityChecked(wallet, isEligible);

        return isEligible;
    }

    // Function to withdraw tokens (owner only)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid withdrawal address!");
        require(amount > 0, "Amount must be greater than zero!");
        
        // Check that the contract has enough tokens to withdraw
        uint256 contractBalance = rockyToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient token balance!");

        // Transfer the tokens to the specified address
        bool success = rockyToken.transfer(to, amount);
        require(success, "Token transfer failed!");
    }

    // Function to update the token address (owner only)
    function updateTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid token address!");
        
        rockyToken = IERC20(newTokenAddress);
    }
}
```
