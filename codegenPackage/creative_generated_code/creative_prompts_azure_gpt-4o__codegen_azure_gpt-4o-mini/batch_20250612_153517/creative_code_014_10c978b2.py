"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Create a Solidity contract for multi-chain compatibility of $HEHE tokens, ensuring seamless transactions across Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_10c978b2929ffa0e
Batch ID: 20250612_153517
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

// Import OpenZeppelin's ERC20 implementation for standard token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with other chains
interface IBridge {
    function transferTo(address to, uint256 amount) external;
}

contract HEHEToken is ERC20, Ownable {
    // Mapping to track the bridge addresses for multi-chain compatibility
    mapping(uint256 => address) public bridges; // Chain ID -> Bridge Address
    
    // Event emitted when tokens are bridged
    event TokensBridged(address indexed to, uint256 amount, uint256 indexed chainId);

    // Constructor to initialize the token
    constructor() ERC20("HEHE Token", "HEHE") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to the deployer
    }

    // Function to add a bridge for a specific chain
    function setBridge(uint256 chainId, address bridgeAddress) external onlyOwner {
        require(bridgeAddress != address(0), "Invalid bridge address");
        bridges[chainId] = bridgeAddress;
    }

    // Function to bridge tokens to another chain
    function bridgeTokens(uint256 amount, uint256 chainId) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(bridges[chainId] != address(0), "Bridge not set for this chain");
        
        // Transfer tokens to the bridge contract
        _transfer(msg.sender, address(this), amount);
        
        // Call the bridge contract to handle the transfer
        IBridge(bridges[chainId]).transferTo(msg.sender, amount);
        
        emit TokensBridged(msg.sender, amount, chainId);
    }

    // Function to withdraw accidentally sent tokens
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");
        token.transfer(msg.sender, amount);
    }
}
```
