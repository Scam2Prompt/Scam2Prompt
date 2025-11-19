"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract code in Solidity that distributes Ziber tokens to Bitcoin and Ethereum owners as a bonus, based on the snapshot of the blockchain on July 26, 2017.
Generated: DETERMINISTIC_294d80a0246a1674
Batch ID: 20250622_205138
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for distributing Ziber tokens to Bitcoin and Ethereum owners
contract ZiberTokenDistributor is Ownable {
    // Address of the Ziber token contract
    IERC20 public ziberToken;

    // Mapping to track eligible addresses and their allocated Ziber tokens
    mapping(address => uint256) public allocations;

    // Event to log the distribution of tokens
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the Ziber token address
    constructor(address _ziberToken) {
        require(_ziberToken != address(0), "Invalid token address");
        ziberToken = IERC20(_ziberToken);
    }

    // Function to set allocations for eligible addresses
    function setAllocations(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            allocations[recipients[i]] = amounts[i];
        }
    }

    // Function to distribute Ziber tokens to eligible addresses
    function distributeTokens() external {
        uint256 amount = allocations[msg.sender];
        require(amount > 0, "No allocation for this address");

        // Reset allocation to prevent re-entrancy
        allocations[msg.sender] = 0;

        // Transfer Ziber tokens to the sender
        require(ziberToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensDistributed(msg.sender, amount);
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(ziberToken), "Cannot withdraw Ziber tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Function to check the allocation of a specific address
    function checkAllocation(address recipient) external view returns (uint256) {
        return allocations[recipient];
    }
}
```
