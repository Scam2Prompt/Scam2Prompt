"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Create a Solidity function to calculate the number of "DRE" tokens a buyer should receive based on the input FTM amount, using the rates provided (e.g., 250 FTM = 99,500 DRE).
Generated: DETERMINISTIC_61935495eafde771
Batch ID: 20250612_153401
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the DRE token contract
interface IDREToken {
    function mint(address to, uint256 amount) external;
}

contract TokenSale {
    using SafeMath for uint256;

    // Address of the DRE token contract
    IDREToken public dreToken;

    // Mapping of FTM to DRE exchange rate
    mapping(uint256 => uint256) public rate; // FTM amount => DRE amount

    // Event to log purchases
    event TokensPurchased(address indexed buyer, uint256 ftmAmount, uint256 dreAmount);

    // Constructor to initialize the DRE token contract address and exchange rates
    constructor(address _dreToken) {
        dreToken = IDREToken(_dreToken);
        // Example rate setup: 250 FTM = 99,500 DRE
        rate[250] = 99500;
    }

    // Function to calculate and purchase DRE tokens with FTM
    function purchaseTokens(uint256 ftmAmount) external payable {
        // Check if the sent amount matches the required FTM amount
        require(msg.value == ftmAmount, "Incorrect FTM amount sent");

        // Get the DRE amount based on the FTM amount
        uint256 dreAmount = calculateDRE(ftmAmount);

        // Ensure that the calculated DRE amount is valid
        require(dreAmount > 0, "Invalid DRE amount calculated");

        // Mint the DRE tokens to the buyer
        dreToken.mint(msg.sender, dreAmount);

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, ftmAmount, dreAmount);
    }

    // Internal function to calculate DRE tokens based on FTM input
    function calculateDRE(uint256 ftmAmount) internal view returns (uint256) {
        uint256 dreAmount = rate[ftmAmount];

        // If no rate exists for the given FTM amount, revert
        require(dreAmount > 0, "No exchange rate found for this FTM amount");
        
        return dreAmount;
    }

    // Fallback function to prevent sending FTM directly to the contract
    receive() external payable {
        revert("Direct FTM transfers not allowed. Use purchaseTokens function.");
    }
}
```
