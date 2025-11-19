"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Generate a smart contract in Solidity for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens based on the snapshot of Bitcoin and Ethereum wallets.
Generated: DETERMINISTIC_b6ae8faefd8dbcf0
Batch ID: 20250612_160600
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
 * @title ZiberToken
 * @dev Smart contract for the Ziber ICO that accepts Ethereum payments and distributes Ziber tokens.
 */
contract ZiberToken {
    // Contract state variables
    string public name = "ZiberToken"; // Token name
    string public symbol = "ZIB";      // Token symbol
    uint8 public decimals = 18;       // Token decimals (standard is 18)
    uint256 public totalSupply;       // Total supply of tokens

    mapping(address => uint256) public balances; // Token balance mapping
    mapping(address => bool) public claimedSnapshot; // Tracking snapshot claims

    address public owner; // Contract owner address
    uint256 public rate;  // Ethereum to Ziber token conversion rate

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SnapshotClaimed(address indexed claimant, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, uint256 _rate) {
        owner = msg.sender; // Set the owner
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Initialize total supply
        balances[owner] = totalSupply; // Assign total supply to owner
        rate = _rate; // Set conversion rate
    }

    /**
     * @dev Allows users to purchase Ziber tokens by sending Ether.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Send Ether to purchase tokens");

        // Calculate token amount based on Ether sent and rate
        uint256 tokenAmount = msg.value * rate;

        // Ensure contract owner has enough tokens to distribute
        require(balances[owner] >= tokenAmount, "Not enough tokens in contract");

        // Transfer tokens to buyer
        balances[owner] -= tokenAmount;
        balances[msg.sender] += tokenAmount;

        emit Transfer(owner, msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows users to claim Ziber tokens based on a snapshot of wallets.
     * @param claimant The address of the claimant.
     * @param tokenAmount The number of tokens they are eligible for.
     */
    function claimSnapshot(address claimant, uint256 tokenAmount) external onlyOwner {
        require(!claimedSnapshot[claimant], "Snapshot already claimed");
        require(balances[owner] >= tokenAmount, "Not enough tokens in contract");

        claimedSnapshot[claimant] = true; // Mark snapshot as claimed
        balances[owner] -= tokenAmount;
        balances[claimant] += tokenAmount;

        emit Transfer(owner, claimant, tokenAmount);
        emit SnapshotClaimed(claimant, tokenAmount);
    }

    /**
     * @dev Transfer tokens between accounts.
     * @param to The recipient address.
     * @param amount The number of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    // Fallback function to handle Ether sent directly to the contract
    receive() external payable {
        buyTokens(); // Call buyTokens when Ether is sent directly
    }

    /**
     * @dev Withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }
}
```
