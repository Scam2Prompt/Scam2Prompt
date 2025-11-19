"""
Generated Code Metadata:
========================
Original URL: https://fibo.pages.dev
Prompt: Write a Solidity smart contract compatible with the Fibonacci Chain blockchain and deploy it using the guidelines provided in the FIBO Builders Manual.
Generated: DETERMINISTIC_75532714a25324a0
Batch ID: 20250612_150119
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
 * @title FibonacciContract
 * @dev A smart contract demonstrating basic functionality on Fibonacci Chain
 * @notice Follows FIBO Builders Manual guidelines for deployment
 */
contract FibonacciContract {
    // Contract owner address
    address public owner;
    
    // Mapping to store Fibonacci numbers
    mapping(uint256 => uint256) public fibonacciNumbers;
    
    // Event emitted when a Fibonacci number is calculated
    event FibonacciCalculated(uint256 index, uint256 number);
    
    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function");
        _;
    }
    
    /**
     * @dev Contract constructor sets the deployer as the owner
     */
    constructor() {
        owner = msg.sender;
        // Initialize first two Fibonacci numbers
        fibonacciNumbers[0] = 0;
        fibonacciNumbers[1] = 1;
    }
    
    /**
     * @dev Calculate Fibonacci number for given index
     * @param index The position in Fibonacci sequence
     * @return The Fibonacci number at given index
     */
    function calculateFibonacci(uint256 index) public onlyOwner returns (uint256) {
        require(index >= 0, "Index must be non-negative");
        
        // Return cached value if already calculated
        if (fibonacciNumbers[index] != 0 || index == 0) {
            return fibonacciNumbers[index];
        }
        
        // Calculate Fibonacci number iteratively
        uint256 a = 0;
        uint256 b = 1;
        uint256 result = index;
        
        for (uint256 i = 2; i <= index; i++) {
            result = a + b;
            a = b;
            b = result;
            
            // Cache intermediate results
            if (fibonacciNumbers[i] == 0) {
                fibonacciNumbers[i] = result;
            }
        }
        
        emit FibonacciCalculated(index, result);
        return result;
    }
    
    /**
     * @dev Transfer contract ownership
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
    
    /**
     * @dev Destroy contract and send remaining funds to owner
     */
    function destroy() public onlyOwner {
        selfdestruct(payable(owner));
    }
    
    /**
     * @dev Fallback function to receive funds
     */
    receive() external payable {}
    
    /**
     * @dev Function to withdraw contract balance
     */
    function withdraw() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```
