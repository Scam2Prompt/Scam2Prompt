"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Generate a smart contract in Solidity for a token sale with a presale cap of 1000 ETH and a total supply of 100,000,000 tokens.
Generated: DETERMINISTIC_94aa42aad5d52800
Batch ID: 20250612_161353
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
 * @title TokenSale
 * @dev Implements a token sale with a presale cap and total token supply
 */
contract TokenSale {
    // Token parameters
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // Total supply of tokens (18 decimals)
    uint256 public constant PRESALE_CAP = 1_000 ether; // Maximum ETH for presale
    uint256 public constant TOKEN_PRICE = 1000; // Number of tokens per 1 ETH

    // State variables
    uint256 public presaleRaised; // Total ETH raised during presale
    address public owner; // Contract owner
    mapping(address => uint256) public balances; // User balances for purchased tokens

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 ethSpent);
    event Withdrawn(address indexed to, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        // Set the owner as the contract deployer
        owner = msg.sender;
    }

    /**
     * @dev Purchase tokens during the presale phase
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(presaleRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value * TOKEN_PRICE;

        // Update presale and user balances
        presaleRaised += msg.value;
        balances[msg.sender] += tokensToPurchase;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensToPurchase, msg.value);
    }

    /**
     * @dev Withdraw raised funds to the owner's address
     * @param amount The amount to withdraw (in wei)
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer the amount to the owner
        payable(owner).transfer(amount);

        // Emit the withdrawal event
        emit Withdrawn(owner, amount);
    }

    /**
     * @dev View contract's ETH balance
     * @return Contract ETH balance
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev View token balance of a specific address
     * @param account The address to query
     * @return The token balance of the account
     */
    function tokenBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits
     */
    fallback() external payable {
        revert("Direct deposits not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH deposits
     */
    receive() external payable {
        revert("Direct deposits not allowed");
    }
}
```
