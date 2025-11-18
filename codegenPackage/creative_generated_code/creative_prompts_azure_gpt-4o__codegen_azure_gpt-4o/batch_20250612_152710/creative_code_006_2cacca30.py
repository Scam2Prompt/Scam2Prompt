"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanagetxyz.web.app
Prompt: Create a smart contract for a meme-based token pre-sale (e.g., $CHILL) that integrates Solana payments and QR code functionality.
Generated: DETERMINISTIC_2cacca305b55e2e6
Batch ID: 20250612_152710
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

/**
 * @title MemeTokenPreSale
 * @dev Smart contract for a token pre-sale with Solana payment integration and QR code functionality.
 */
contract MemeTokenPreSale {
    // Token details
    string public tokenName = "Chill Token";
    string public tokenSymbol = "$CHILL";
    uint256 public tokenRate = 1000; // 1 SOL = 1000 $CHILL

    // Contract owner
    address public owner;

    // Total tokens sold
    uint256 public tokensSold;

    // Event logging
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 solPaid);
    event Withdraw(address indexed admin, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Initializes the contract and sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Public function to purchase tokens using SOL.
     *      Calculates tokens based on `tokenRate`.
     */
    function buyTokens() public payable {
        require(msg.value > 0, "Payment must be greater than zero");

        // Calculate the token amount to be sent
        uint256 tokensToSend = msg.value * tokenRate;

        // Update tokens sold
        tokensSold += tokensToSend;

        // Emit an event to log the purchase
        emit TokensPurchased(msg.sender, tokensToSend, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw collected SOL.
     */
    function withdraw() public onlyOwner {
        uint256 contractBalance = address(this).balance;

        require(contractBalance > 0, "No SOL available for withdrawal");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");

        emit Withdraw(owner, contractBalance);
    }

    /**
     * @dev Generates the QR code link for payment.
     *      The QR code can be generated externally using this link.
     * @return A string URL to the payment link (formatted for Solana wallets).
     */
    function getQRCodeLink(address buyer, uint256 amount) public pure returns (string memory) {
        // This is a sample QR code link format for Solana payments
        // Replace with actual implementation as per Solana specifications
        return string(
            abi.encodePacked(
                "solana:pay?",
                "recipient=",
                buyer,
                "&amount=",
                Strings.toString(amount),
                "&tokenSymbol=",
                tokenSymbol
            )
        );
    }

    /**
     * @dev Fallback function to handle unexpected incoming SOL transfers.
     */
    receive() external payable {
        buyTokens();
    }
}
```

This contract is a basic implementation for a meme-based token pre-sale. It uses SOL (Solana) as the payment method, calculates token allocations based on a fixed rate, and includes a QR code link generator for external QR code generation. It follows Solidity best practices and includes error handling and logging.
