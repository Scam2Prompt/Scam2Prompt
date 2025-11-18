"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diamond-7n0.pages.dev
Prompt: Recommend best practices for ensuring security and transparency in Ethereum-based token projects, referencing the strategies outlined for Diamond Coin.
Generated: DETERMINISTIC_fb951b314eb1742c
Batch ID: 20250612_152620
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
 * @title DiamondCoin Best Practices
 * @dev This contract demonstrates recommended best practices for ensuring security and transparency in Ethereum-based token projects.
 */
contract DiamondCoin {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) private balances; // Mapping to track token balances

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract. Ensures transparency.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to mint tokens. Can only be called by the owner.
     * Ensures security by restricting access and logging the event.
     * @param to Address to mint tokens for.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Mint amount must be greater than zero");

        balances[to] += amount;
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to burn tokens. Can only be called by the owner.
     * Ensures security by logging the event and validating inputs.
     * @param from Address to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Address cannot be zero");
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[from] >= amount, "Insufficient balance");

        balances[from] -= amount;
        emit TokensBurned(from, amount);
    }

    /**
     * @dev Function to check the balance of an address.
     * Provides transparency for token holders.
     * @param account Address to query the balance of.
     * @return The balance of the queried address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function for fallback and receive to prevent accidental Ether transfers.
     */
    fallback() external {
        revert("Fallback function not allowed");
    }

    receive() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Follow best practices:
     * 1. Use `require` for input validation.
     * 2. Emit events for state changes to ensure transparency.
     * 3. Restrict sensitive functions using `onlyOwner`.
     * 4. Prevent accidental Ether transfers using fallback and receive functions.
     */
}
```
