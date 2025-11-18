"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Write a function in Solidity to implement a "DEX Dog Park" feature where $POODL tokens can interact with other tokens, as described in the tokenomics section of the Poodl Inu website.
Generated: DETERMINISTIC_dce63f68659289a9
Batch ID: 20250612_153400
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

// Importing the IERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DEX Dog Park contract
contract DEXDogPark is Ownable {
    using SafeERC20 for IERC20;

    // Mapping to track how many $POODL tokens each user has staked
    mapping(address => uint256) private stakedPoodl;

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed user, uint256 amount);

    // Function to stake $POODL tokens
    function stakePoodl(uint256 amount, address poodlTokenAddress) external {
        require(amount > 0, "Amount must be greater than 0");
        require(poodlTokenAddress != address(0), "Invalid token address");

        // Interacting with the $POODL token contract
        IERC20 poodlToken = IERC20(poodlTokenAddress);
        
        // Transfer $POODL tokens from the user to this contract
        poodlToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update staked amount for the user
        stakedPoodl[msg.sender] += amount;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake $POODL tokens
    function unstakePoodl(uint256 amount, address poodlTokenAddress) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedPoodl[msg.sender] >= amount, "Insufficient staked amount");
        require(poodlTokenAddress != address(0), "Invalid token address");

        // Update staked amount for the user
        stakedPoodl[msg.sender] -= amount;

        // Interacting with the $POODL token contract to transfer back to the user
        IERC20 poodlToken = IERC20(poodlTokenAddress);
        poodlToken.safeTransfer(msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to check how much $POODL tokens a user has staked
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedPoodl[user];
    }

    // Function to withdraw any ERC20 tokens (other than $POODL) held by this contract
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        token.safeTransfer(msg.sender, amount);
    }
}
```
