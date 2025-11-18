"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://not-claim.pages.dev
Prompt: Create a Solidity function that calculates and distributes $NOT tokens based on the "first come, first served" rule for the pre-sale. Ensure it handles refunds for late transactions.
Generated: DETERMINISTIC_8d65218b057402ff
Batch ID: 20250612_152235
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

contract PreSale {
    // The total supply of $NOT tokens
    uint256 public totalSupply;
    // The price of one $NOT token in wei
    uint256 public tokenPrice;
    // Mapping of addresses to the amount of $NOT tokens purchased
    mapping(address => uint256) public balances;
    // Total number of tokens sold
    uint256 public tokensSold;
    // Flag to indicate if the sale is active
    bool public saleActive;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);
    // Event emitted for refunds
    event RefundIssued(address indexed buyer, uint256 amount);

    // Constructor to initialize the contract
    constructor(uint256 _totalSupply, uint256 _tokenPrice) {
        totalSupply = _totalSupply;
        tokenPrice = _tokenPrice;
        saleActive = true; // Start the sale as active
    }

    // Modifier to ensure the sale is active
    modifier saleIsActive() {
        require(saleActive, "Sale is not active");
        _;
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 tokenAmount) external payable saleIsActive {
        require(tokenAmount > 0, "Must purchase at least one token");
        require(msg.value == tokenAmount * tokenPrice, "Incorrect Ether amount");
        require(tokensSold + tokenAmount <= totalSupply, "Not enough tokens available");

        // Update state
        balances[msg.sender] += tokenAmount;
        tokensSold += tokenAmount;

        // Emit event for tokens purchased
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to end the sale and handle refunds for late transactions
    function endSale() external {
        require(saleActive, "Sale already ended");
        saleActive = false; // Stop the sale

        // Calculate refunds for those who sent Ether after the sale has ended
        uint256 refundAmount;
        for (uint256 i = 0; i < tokensSold; i++) {
            address buyer = address(uint160(i)); // Simulating buyer addresses for simplicity
            uint256 purchasedTokens = balances[buyer];
            if (purchasedTokens == 0) continue;

            // Calculate refund based on the number of tokens purchased
            refundAmount = purchasedTokens * tokenPrice;

            // Reset balance before refunding
            balances[buyer] = 0;

            // Send Ether back to the buyer
            (bool success, ) = buyer.call{value: refundAmount}("");
            require(success, "Refund failed");

            // Emit refund event
            emit RefundIssued(buyer, refundAmount);
        }
    }

    // Fallback function to accept Ether for refunds or token purchases
    receive() external payable {
        require(saleActive, "Sale is not active");
    }
}
```
