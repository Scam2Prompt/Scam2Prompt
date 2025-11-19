"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogleonidas.pages.dev
Prompt: Provide a code example for a smart contract that manages the presale of DOG tokens, including the cap and total supply.
Generated: DETERMINISTIC_906bb1450870aeb2
Batch ID: 20250612_163751
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
 * @title DOGTokenPresale
 * @dev A smart contract to manage the presale of DOG tokens with a cap and total supply.
 */
contract DOGTokenPresale {
    // Token details
    string public constant name = "DOG Token";
    string public constant symbol = "DOG";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public constant totalSupply = 1_000_000 * (10 ** uint256(decimals));

    // Presale cap
    uint256 public constant presaleCap = 200_000 * (10 ** uint256(decimals));

    // Token price in wei
    uint256 public tokenPrice = 0.001 ether;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Total tokens sold during presale
    uint256 public tokensSold;

    // Address of the contract owner
    address public owner;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Purchase DOG tokens during the presale.
     * @param _amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        // Calculate the total cost of tokens being purchased
        uint256 cost = _amount * tokenPrice;

        // Ensure the buyer has sent enough Ether
        require(msg.value >= cost, "Insufficient ether sent");

        // Ensure the presale cap has not been exceeded
        require(tokensSold + _amount <= presaleCap, "Presale cap exceeded");

        // Update the buyer's balance and tokensSold
        balances[msg.sender] += _amount;
        tokensSold += _amount;

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, _amount);

        // Refund excess Ether, if any
        uint256 excess = msg.value - cost;
        if (excess > 0) {
            payable(msg.sender).transfer(excess);
        }
    }

    /**
     * @dev Withdraw Ether collected from token sales to the owner's address.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Update the price of the token.
     * @param _newPrice The new price per token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be greater than zero");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Get the contract's balance.
     * @return The contract's Ether balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
