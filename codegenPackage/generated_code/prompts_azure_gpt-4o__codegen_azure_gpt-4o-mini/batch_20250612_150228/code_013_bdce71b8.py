"""
Generated Code Metadata:
========================
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Write a smart contract to enable cross-chain staking of uniTokens (uniETH, uniBTC, uniIOTX) on Bedrock, ensuring compatibility with IoTeX and DePIN.
Generated: DETERMINISTIC_bdce71b8eabe900d
Batch ID: 20250612_150228
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the cross-chain staking functionality
interface ICrossChainStaking {
    function stakeTokens(address token, uint256 amount) external;
    function unstakeTokens(address token, uint256 amount) external;
}

// Smart contract for cross-chain staking of uniTokens
contract CrossChainStaking is Ownable, ICrossChainStaking {
    // Mapping to track staked balances for each user
    mapping(address => mapping(address => uint256)) private stakedBalances;

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, address indexed token, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed user, address indexed token, uint256 amount);

    // Function to stake tokens
    function stakeTokens(address token, uint256 amount) external override {
        require(amount > 0, "Amount must be greater than zero");
        require(token == address(0x1234567890abcdef1234567890abcdef12345678) || // uniETH
                token == address(0xabcdef1234567890abcdef1234567890abcdef12) || // uniBTC
                token == address(0x7890abcdef1234567890abcdef1234567890abcd), // uniIOTX
                "Invalid token");

        // Transfer tokens from the user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update the staked balance
        stakedBalances[msg.sender][token] += amount;

        // Emit the staking event
        emit TokensStaked(msg.sender, token, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(address token, uint256 amount) external override {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender][token] >= amount, "Insufficient staked balance");

        // Update the staked balance
        stakedBalances[msg.sender][token] -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        // Emit the unstaking event
        emit TokensUnstaked(msg.sender, token, amount);
    }

    // Function to check the staked balance of a user
    function getStakedBalance(address user, address token) external view returns (uint256) {
        return stakedBalances[user][token];
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
