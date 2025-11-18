"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokidongerapp.com
Prompt: Generate a Solidity-based token sale contract for FLOKIDONGER with parameters like presale price (0.0006 USD), launch price (0.0015 USD), and maximum entries (50 billion tokens).
Generated: DETERMINISTIC_aea77dfb4bdd0ea7
Batch ID: 20250612_145423
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
 * @title FLOKIDONGER Token Sale Contract
 * @dev This contract implements a token sale mechanism with presale and launch prices.
 * Presale price: 0.0006 USD
 * Launch price: 0.0015 USD
 * Maximum supply: 50 billion tokens
 */
contract FlokiDongerTokenSale {
    // Token and sale parameters
    string public constant name = "FLOKIDONGER";
    string public constant symbol = "FD";
    uint8 public constant decimals = 18;
    uint256 public constant maxSupply = 50_000_000_000 * (10 ** uint256(decimals)); // 50 billion tokens
    uint256 public constant presalePrice = 0.0006 * (10 ** uint256(decimals)); // 0.0006 USD in token's smallest unit
    uint256 public constant launchPrice = 0.0015 * (10 ** uint256(decimals)); // 0.0015 USD in token's smallest unit

    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total tokens minted
    uint256 public tokensSold; // Tokens sold in the sale
    bool public isPresale; // Flag to indicate if the sale is in presale phase

    // Mapping to store balances
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event SalePhaseUpdated(bool isPresale);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier validPurchase() {
        require(msg.value > 0, "Ether amount must be greater than zero");
        _;
    }

    constructor() {
        owner = msg.sender;
        isPresale = true; // Start with presale phase
    }

    /**
     * @dev Allows the contract owner to transfer ownership to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Toggle the sale phase (presale/launch).
     */
    function toggleSalePhase() external onlyOwner {
        isPresale = !isPresale;
        emit SalePhaseUpdated(isPresale);
    }

    /**
     * @dev Buy tokens by sending Ether.
     * Tokens will be priced based on the current sale phase (presale or launch).
     */
    function buyTokens() external payable validPurchase {
        // Determine the token price based on the phase
        uint256 tokenPrice = isPresale ? presalePrice : launchPrice;

        // Calculate the number of tokens to buy
        uint256 tokensToBuy = (msg.value * (10 ** uint256(decimals))) / tokenPrice;

        // Ensure maximum supply is not exceeded
        require(totalSupply + tokensToBuy <= maxSupply, "Exceeds maximum token supply");

        // Update state variables
        balances[msg.sender] += tokensToBuy;
        totalSupply += tokensToBuy;
        tokensSold += tokensToBuy;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensToBuy, msg.value);
    }

    /**
     * @dev Withdraw Ether from the contract to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to handle plain Ether transfers.
     */
    fallback() external payable {
        buyTokens();
    }

    /**
     * @dev Receive function to handle Ether transfers directly.
     */
    receive() external payable {
        buyTokens();
    }
}
```
