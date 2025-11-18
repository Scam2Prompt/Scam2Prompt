"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Suggest tools or APIs for deploying and managing a token presale on the Ethereum blockchain, including tracking contributions and enforcing the total supply limit of 100,000,000 ALIEN tokens.
Generated: DETERMINISTIC_2066e9165a58fa4d
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
pragma solidity ^0.8.18;

/**
 * @title TokenPresale
 * @dev A contract for managing a token presale on the Ethereum blockchain. Enforces
 *      a supply limit of 100,000,000 ALIEN tokens and tracks contributions.
 */
contract TokenPresale {
    // Token supply limit
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimal places
    uint256 public totalTokensSold; // Tracks total tokens sold during presale

    // Token price in wei (e.g., 1 token = 0.001 ETH)
    uint256 public constant TOKEN_PRICE = 0.001 ether;

    // Owner's address
    address public owner;

    // Mapping to track individual contributions
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event WithdrawnFunds(address indexed owner, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor: Sets the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Handles the purchase of tokens during the presale. Ensures that the
     *      supply limit is not exceeded and the contribution amount is valid.
     */
    function purchaseTokens() external payable {
        // Ensure the sent ETH is enough to purchase at least one token
        require(msg.value > 0, "You must send ETH to purchase tokens");
        require(msg.value >= TOKEN_PRICE, "Insufficient ETH to purchase tokens");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = (msg.value * 10**18) / TOKEN_PRICE;

        // Ensure the purchase does not exceed the max supply
        require(totalTokensSold + tokensToPurchase <= MAX_SUPPLY, "Purchase exceeds max supply");

        // Update state variables
        contributions[msg.sender] += tokensToPurchase;
        totalTokensSold += tokensToPurchase;

        // Emit an event for token purchase
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Allows the owner to withdraw the collected ETH funds from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer the contract's balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");

        // Emit an event for fund withdrawal
        emit WithdrawnFunds(owner, contractBalance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```

Make sure to deploy this contract on the Ethereum network to conduct the presale. Proper UI and integrations with wallets like MetaMask are recommended for participant interaction.
