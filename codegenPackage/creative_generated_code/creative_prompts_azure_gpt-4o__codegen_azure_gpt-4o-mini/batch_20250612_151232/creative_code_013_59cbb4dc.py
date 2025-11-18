"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-en.pages.dev
Prompt: Create a Solidity function to calculate transaction fees for Pushd token holders, applying lower rates for users who hold and use Pushd tokens.
Generated: DETERMINISTIC_59cbb4dcbd7c3446
Batch ID: 20250612_151232
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

contract PushdToken {
    
    // Mapping to store token balances of each address
    mapping(address => uint256) private balances;
    
    // Transaction fee percentages
    uint256 public constant DEFAULT_FEE_PERCENTAGE = 5; // 5%
    uint256 public constant DISCOUNTED_FEE_PERCENTAGE = 2; // 2%
    
    // Event for logging fee calculations
    event FeeCalculated(address indexed user, uint256 amount, uint256 fee);

    // Modifier to check if the user has enough tokens
    modifier hasSufficientTokens(address user, uint256 amount) {
        require(balances[user] >= amount, "Insufficient token balance");
        _;
    }

    // Function to calculate transaction fee based on token holdings
    function calculateTransactionFee(address user, uint256 transactionAmount) 
        public 
        view 
        hasSufficientTokens(user, transactionAmount) 
        returns (uint256) 
    {
        uint256 feePercentage;

        // Determine the fee percentage based on token holdings
        if (balances[user] > 0) {
            feePercentage = DISCOUNTED_FEE_PERCENTAGE; // Discounted fee for token holders
        } else {
            feePercentage = DEFAULT_FEE_PERCENTAGE; // Default fee for non-holders
        }

        // Calculate the transaction fee
        uint256 fee = (transactionAmount * feePercentage) / 100;

        // Emit the fee calculated event
        emit FeeCalculated(user, transactionAmount, fee);

        return fee;
    }

    // Function to allow users to deposit tokens (for demonstration purposes)
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += amount; // Update user balance
    }

    // Function to get the balance of a user
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
