"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-io.web.app
Prompt: Create a Solidity contract to manage the distribution of CRUDO tokens for ecosystem operations, marketing, and partnerships as outlined in the tokenomics section.
Generated: DETERMINISTIC_bfabce43facc6d14
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
 * @title CRUDO Token Distribution Contract
 * @notice This contract manages the distribution of CRUDO tokens for ecosystem operations, marketing, and partnerships.
 */
contract CRUDOTokenDistribution {
    // State variable to track total supply of tokens
    uint256 public totalSupply;
    
    // Mapping to track the balance of each address
    mapping(address => uint256) public balanceOf;
    
    // Events
    event TokensDistributed(address indexed to, uint256 amount);
    event Withdrawn(address indexed to, uint256 amount);
    
    // Percentage allocations for various purposes
    uint256 public constant ECOSYSTEM_ALLOCATION = 40; // 40% for ecosystem operations
    uint256 public constant MARKETING_ALLOCATION = 30; // 30% for marketing
    uint256 public constant PARTNERSHIP_ALLOCATION = 30; // 30% for partnerships

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the initial supply and owner of the contract.
     * @param initialSupply The initial supply of CRUDO tokens.
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        totalSupply = initialSupply;
        balanceOf[msg.sender] = initialSupply; // Assign initial supply to the contract owner
        owner = msg.sender;
    }

    /**
     * @dev Distributes tokens to a specified address for a specific purpose.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to distribute.
     * @param purpose The reason for the token distribution.
     */
    function distributeTokens(address recipient, uint256 amount, string memory purpose) external onlyOwner {
        require(recipient != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf[owner] >= amount, "Insufficient balance");

        balanceOf[owner] -= amount; // Deduct from owner's balance
        balanceOf[recipient] += amount; // Add to recipient's balance
        
        emit TokensDistributed(recipient, amount); // Emit distribution event
    }

    /**
     * @dev Withdraw tokens from the contract to a specified address.
     * @param to The address to withdraw tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf[owner] >= amount, "Insufficient balance");

        balanceOf[owner] -= amount; // Deduct from owner's balance
        balanceOf[to] += amount; // Add to recipient's balance
        
        emit Withdrawn(to, amount); // Emit withdrawal event
    }

    /**
     * @dev Function to get the owner's balance.
     * @return The balance of the owner.
     */
    function getOwnerBalance() external view returns (uint256) {
        return balanceOf[owner];
    }

    /**
     * @dev Function to get the total supply of tokens.
     * @return The total supply of tokens.
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }
}
```
