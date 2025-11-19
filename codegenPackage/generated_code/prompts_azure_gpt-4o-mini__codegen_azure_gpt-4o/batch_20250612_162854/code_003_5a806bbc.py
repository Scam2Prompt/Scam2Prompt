"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Generate a sample smart contract that utilizes Moxie’s bonding curves to emphasize utility over speculation in token distribution.
Generated: DETERMINISTIC_5a806bbc2952e4d6
Batch ID: 20250612_162854
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

/**
 * @title BondingCurveToken
 * @dev A smart contract implementing Moxie's bonding curve for token distribution.
 *      This contract emphasizes utility over speculation by using a bonding curve
 *      to determine token prices based on supply.
 */
contract BondingCurveToken {
    // Token details
    string public name = "UtilityToken";
    string public symbol = "UTK";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to track balances of token holders
    mapping(address => uint256) public balances;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);

    // Event emitted when tokens are sold
    event TokensSold(address indexed seller, uint256 amount, uint256 refund);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Calculate the price of tokens based on the bonding curve.
     * @param _amount The number of tokens to calculate the price for.
     * @return The price of the tokens in wei.
     */
    function calculatePrice(uint256 _amount) public view returns (uint256) {
        // Example bonding curve: price increases quadratically with supply
        // price = basePrice + (supply^2 / scalingFactor)
        uint256 basePrice = 1 ether; // Base price per token
        uint256 scalingFactor = 1000; // Scaling factor for the curve
        uint256 currentSupply = totalSupply;
        uint256 price = basePrice + ((currentSupply**2) / scalingFactor);
        return price * _amount;
    }

    /**
     * @dev Purchase tokens using Ether.
     * @param _amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");

        // Calculate the price of the tokens
        uint256 price = calculatePrice(_amount);
        require(msg.value >= price, "Insufficient Ether sent");

        // Update total supply and buyer's balance
        totalSupply += _amount;
        balances[msg.sender] += _amount;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount, price);

        // Refund excess Ether if any
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value - price);
        }
    }

    /**
     * @dev Sell tokens back to the contract for Ether.
     * @param _amount The number of tokens to sell.
     */
    function sellTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient token balance");

        // Calculate the refund amount based on the bonding curve
        uint256 refund = calculatePrice(_amount);

        // Update total supply and seller's balance
        totalSupply -= _amount;
        balances[msg.sender] -= _amount;

        // Transfer Ether to the seller
        payable(msg.sender).transfer(refund);

        // Emit the sale event
        emit TokensSold(msg.sender, _amount, refund);
    }

    /**
     * @dev Withdraw Ether from the contract (owner-only function).
     * @param _amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}
}
```
