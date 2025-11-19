"""
Generated Code Metadata:
========================
Original URL: https://presale-srunexyz.pages.dev
Prompt: Generate a smart contract in Solidity to facilitate the presale of $SRUNE tokens, ensuring a cap of 1000 SOL.
Generated: DETERMINISTIC_93e72d261395b4f1
Batch ID: 20250612_162346
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
 * @title SRUNE Presale Contract
 * @dev This contract facilitates the presale of $SRUNE tokens with a cap of 1000 SOL.
 */
contract SRUNEPresale {
    // Address of the owner (contract deployer)
    address public owner;

    // Token price in wei (1 SOL = 10^18 wei)
    uint256 public constant TOKEN_PRICE = 0.01 ether;

    // Maximum cap in SOL (1000 SOL)
    uint256 public constant MAX_CAP = 1000 ether;

    // Total amount of SOL raised
    uint256 public totalRaised;

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 value);

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase $SRUNE tokens during the presale.
     *      Ensures the cap is not exceeded and the value sent is valid.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "You must send some SOL to purchase tokens");
        require(totalRaised + msg.value <= MAX_CAP, "Presale cap exceeded");

        // Calculate the number of tokens purchased
        uint256 tokensPurchased = msg.value / TOKEN_PRICE;

        // Update the total raised and contributions
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, tokensPurchased, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw the funds raised.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        // Emit the withdrawal event
        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to handle valid ETH transfers.
     */
    receive() external payable {
        purchaseTokens();
    }
}
```
