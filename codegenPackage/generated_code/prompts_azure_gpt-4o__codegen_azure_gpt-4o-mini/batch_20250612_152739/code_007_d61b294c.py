"""
Generated Code Metadata:
========================
Original URL: https://backup-ar.pages.dev
Prompt: Provide an example of a decentralized launchpad implementation using DTORO Studio for token creation and crowdpooling.
Generated: DETERMINISTIC_d61b294c68f9c2f2
Batch ID: 20250612_152739
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Launchpad
interface ILaunchpad {
    function createToken(string memory name, string memory symbol, uint256 totalSupply) external returns (address);
    function startCrowdPooling(address tokenAddress, uint256 amount, uint256 duration) external;
}

// Token contract implementation
contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        require(totalSupply > 0, "Total supply must be greater than zero");
        _mint(msg.sender, totalSupply);
    }
}

// Launchpad contract implementation
contract Launchpad is ILaunchpad, Ownable {
    using SafeMath for uint256;

    // Event emitted when a new token is created
    event TokenCreated(address indexed tokenAddress, string name, string symbol, uint256 totalSupply);
    // Event emitted when a crowd pooling starts
    event CrowdPoolingStarted(address indexed tokenAddress, uint256 amount, uint256 duration);

    // Function to create a new token
    function createToken(string memory name, string memory symbol, uint256 totalSupply) external override onlyOwner returns (address) {
        CustomToken newToken = new CustomToken(name, symbol, totalSupply);
        emit TokenCreated(address(newToken), name, symbol, totalSupply);
        return address(newToken);
    }

    // Function to start crowd pooling for a specific token
    function startCrowdPooling(address tokenAddress, uint256 amount, uint256 duration) external override onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        
        CustomToken token = CustomToken(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in the contract");

        // Logic to handle crowd pooling (e.g., locking tokens, managing contributions, etc.)
        // This is a placeholder for actual crowd pooling logic
        emit CrowdPoolingStarted(tokenAddress, amount, duration);
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        CustomToken token = CustomToken(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in the contract");
        token.transfer(msg.sender, amount);
    }
}
```
