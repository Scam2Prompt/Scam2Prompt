"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Create a Solidity contract for managing a rewards pool that redistributes sell tax fees to $ETFS token holders, as described in ETFSwap's automatic rewards system.
Generated: DETERMINISTIC_0fd2cdfc7d49131c
Batch ID: 20250612_153401
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

// Interface for interacting with the ETFS token contract
interface IETFS {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract RewardsPool {
    // State variables
    IETFS public etfsToken; // Instance of the ETFS token contract
    address public owner; // Owner of the contract
    uint256 public totalDistributed; // Total amount distributed to token holders

    // Events
    event RewardsDistributed(uint256 amount, uint256 totalHolders);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _etfsToken) {
        require(_etfsToken != address(0), "Invalid token address");
        etfsToken = IETFS(_etfsToken);
        owner = msg.sender;
    }

    // Function to distribute rewards to ETFS token holders
    function distributeRewards(uint256 totalRewards) external onlyOwner {
        require(totalRewards > 0, "Must distribute a positive amount");
        
        uint256 totalHolders = getTotalHolders();
        require(totalHolders > 0, "No token holders to distribute rewards");

        uint256 rewardPerHolder = totalRewards / totalHolders;
        totalDistributed += totalRewards;

        // Iterate through each holder (this is a placeholder, actual implementation may vary)
        for (uint256 i = 0; i < totalHolders; i++) {
            address holder = getHolder(i); // Placeholder for getting each holder address
            require(etfsToken.transfer(holder, rewardPerHolder), "Transfer failed");
        }

        emit RewardsDistributed(totalRewards, totalHolders);
    }

    // Function to get the total number of ETFS token holders
    // This function is a placeholder for actual implementation
    function getTotalHolders() internal view returns (uint256) {
        // Actual implementation should return the total number of unique token holders
        return 0; // Replace with actual logic
    }

    // Function to get a holder's address by their index
    // This function is a placeholder for actual implementation
    function getHolder(uint256 index) internal view returns (address) {
        // Actual implementation should return the address of the holder at the specified index
        return address(0); // Replace with actual logic
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to accept ETH deposits
    receive() external payable {}
    
    // Function to withdraw accumulated ETH from the contract
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
    }
}
```
