"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Write a Solidity function for a token presale that enforces a cap of 1,000 BASE for purchases, as described in the JESSE presale.
Generated: DETERMINISTIC_aff4b90297739686
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

// Importing ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for the presale of a token
contract JessePresale {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public baseToken; // The token being sold
    uint256 public constant MAX_PURCHASE = 1000 * (10 ** 18); // Maximum purchase limit in BASE tokens

    // Mapping to track purchases by each user
    mapping(address => uint256) public purchases;

    // Event to log purchase activity
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the presale contract with the token address
    constructor(address _baseToken) {
        require(_baseToken != address(0), "Token address cannot be zero");
        baseToken = IERC20(_baseToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 amount) external {
        require(amount > 0, "Purchase amount must be greater than zero");
        require(amount <= MAX_PURCHASE, "Cannot purchase more than 1000 BASE tokens");
        
        uint256 totalPurchased = purchases[msg.sender] + amount;
        require(totalPurchased <= MAX_PURCHASE, "Total purchase exceeds limit");

        // Update the purchaser's total amount
        purchases[msg.sender] = totalPurchased;

        // Transfer the purchased tokens from the contract to the buyer
        require(baseToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit event to log purchase
        emit TokensPurchased(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(baseToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the owner
        require(baseToken.transfer(owner, amount), "Token transfer failed");
    }

    // Function to check the contract's token balance
    function contractBalance() external view returns (uint256) {
        return baseToken.balanceOf(address(this));
    }
}
```
