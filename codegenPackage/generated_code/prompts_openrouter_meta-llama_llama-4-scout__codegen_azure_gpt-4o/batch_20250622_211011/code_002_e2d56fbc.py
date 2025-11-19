"""
Generated Code Metadata:
========================
Original URL: https://reg-bemorebasedxyz.pages.dev
Prompt: Generate a smart contract for minting tokens on the BASE chain using Transient innovations, with a pricing structure of 0.0042069 ETH or free.
Generated: DETERMINISTIC_e2d56fbc9f41a2de
Batch ID: 20250622_211011
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
 * @title TokenMinter
 * @dev A smart contract for minting tokens on the BASE chain with a pricing structure.
 * Users can mint tokens for either 0.0042069 ETH or free.
 */
contract TokenMinter {
    // Token details
    string public constant name = "TransientToken";
    string public constant symbol = "TTKN";
    uint256 public totalSupply;

    // Token price in wei (0.0042069 ETH)
    uint256 public constant TOKEN_PRICE = 4206900000000000;

    // Owner of the contract
    address public owner;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Events
    event TokenMinted(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Mint tokens by paying the required price or for free.
     * @param amount The number of tokens to mint.
     */
    function mint(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");

        // Check if the user is paying the required price or minting for free
        if (msg.value > 0) {
            require(msg.value == TOKEN_PRICE * amount, "Incorrect ETH value sent");
        }

        // Update the total supply and the user's balance
        totalSupply += amount;
        balances[msg.sender] += amount;

        // Emit the TokenMinted event
        emit TokenMinted(msg.sender, amount);
    }

    /**
     * @dev Withdraw the contract's balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer the contract's balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Transfer ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");

        // Emit the OwnershipTransferred event
        emit OwnershipTransferred(owner, newOwner);

        // Update the owner
        owner = newOwner;
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to retrieve the contract's balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
