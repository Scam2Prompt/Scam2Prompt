"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimehere.pages.dev
Prompt: Create a Solidity smart contract that integrates with the Verse Burn Engine to automate the burning of VERSE tokens.
Generated: DETERMINISTIC_05c0de0bf06f4d6b
Batch ID: 20250612_151759
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

// Interface for the Verse Burn Engine contract
interface IVerseBurnEngine {
    function burn(uint256 amount) external;
    function getBurnRate() external view returns (uint256);
}

// VerseToken interface for interacting with the VERSE token contract
interface IVerseToken {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract VerseTokenBurner {
    // State variables
    address public owner; // Owner of the contract
    IVerseToken public verseToken; // VERSE token contract instance
    IVerseBurnEngine public verseBurnEngine; // Verse Burn Engine contract instance

    // Events
    event TokensBurned(address indexed from, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with required addresses
    constructor(address _verseToken, address _verseBurnEngine) {
        require(_verseToken != address(0), "Invalid VERSE token address");
        require(_verseBurnEngine != address(0), "Invalid Verse Burn Engine address");
        
        owner = msg.sender;
        verseToken = IVerseToken(_verseToken);
        verseBurnEngine = IVerseBurnEngine(_verseBurnEngine);
    }

    // Function to automate burning of VERSE tokens
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer VERSE tokens from the sender to this contract
        bool success = verseToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        // Call the burn function in Verse Burn Engine
        verseBurnEngine.burn(amount);

        emit TokensBurned(msg.sender, amount);
    }

    // Function to retrieve the current burn rate from Verse Burn Engine
    function getBurnRate() external view returns (uint256) {
        return verseBurnEngine.getBurnRate();
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to prevent accidental Ether transfers
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
