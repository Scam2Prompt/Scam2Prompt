"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servchains.com
Prompt: Create a smart contract in Solidity for managing ADAO token transactions, as described on servchains.com, with functionality for token purchase and transfer.
Generated: DETERMINISTIC_e5a274b97ed52a0f
Batch ID: 20250612_145711
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
 * @title ADAO Token Smart Contract
 * @notice This contract allows for the management of ADAO tokens, including token purchases and transfers.
 */
contract ADAO {
    // Token details
    string public name = "ADAO Token";
    string public symbol = "ADAO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Token balances
    mapping(address => uint256) private balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _initialSupply) {
        // Set the initial token supply and allocate it to the contract owner
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        owner = msg.sender;
    }

    /**
     * @notice Returns the token balance of a specific address.
     * @param account The address to query the balance for.
     * @return The token balance of the address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @notice Transfer tokens to another address.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool success) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit the transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @notice Purchase tokens by sending Ether to the contract.
     * @dev Token price is fixed at 1 Ether = 100 ADAO tokens for simplicity.
     */
    function purchaseTokens() public payable {
        require(msg.value > 0, "Ether value must be greater than zero");

        // Token price in wei
        uint256 tokenPrice = 1 ether / 100;

        // Calculate token amount based on Ether sent
        uint256 amountToPurchase = msg.value / tokenPrice;

        require(amountToPurchase > 0, "Unable to purchase tokens with the provided Ether");
        require(balances[owner] >= amountToPurchase, "Insufficient tokens available for sale");

        // Transfer tokens from the owner to the buyer
        balances[owner] -= amountToPurchase;
        balances[msg.sender] += amountToPurchase;

        // Emit the purchase event
        emit TokensPurchased(msg.sender, amountToPurchase);
    }

    /**
     * @notice Withdraw Ether from the contract.
     * @dev Only the contract owner can withdraw Ether.
     * @param amount The amount of Ether to withdraw in wei.
     */
    function withdrawEther(uint256 amount) public onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        // Transfer Ether to the owner
        payable(owner).transfer(amount);
    }

    /**
     * @notice Fallback function to receive Ether when no data is provided.
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @notice Fallback function to receive Ether when data is provided.
     */
    fallback() external payable {
        purchaseTokens();
    }
}
```
