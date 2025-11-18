"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airyd.pages.dev
Prompt: Provide code to implement permissionless token listings on a blockchain platform, inspired by Avalaunch's emphasis on permissionless fundraising.
Generated: DETERMINISTIC_c18dedf31668301a
Batch ID: 20250612_151141
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

// Import required OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PermissionlessToken
 * @dev This contract allows users to create and list tokens for fundraising.
 *      Inspired by the concept of permissionless fundraising.
 */
contract PermissionlessToken is ERC20, Ownable {
    // Event emitted when a new token is created
    event TokenCreated(address indexed creator, string name, string symbol, uint256 totalSupply);
    
    // Mapping to keep track of listed tokens
    mapping(address => bool) public listedTokens;
    
    // Error messages
    error TokenAlreadyListed(address tokenAddress);
    error TokenNotListed(address tokenAddress);

    /**
     * @dev Constructor for the PermissionlessToken contract.
     * @param name The name of the token.
     * @param symbol The symbol for the token.
     * @param totalSupply The total supply of tokens to be created.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) 
        ERC20(name, symbol) 
    {
        _mint(msg.sender, totalSupply);
        listedTokens[address(this)] = true; // Mark the deployed token as listed
        emit TokenCreated(msg.sender, name, symbol, totalSupply);
    }

    /**
     * @dev Allows users to create a new token.
     * @param name The name of the new token.
     * @param symbol The symbol for the new token.
     * @param totalSupply The total supply of the new token.
     */
    function createToken(string memory name, string memory symbol, uint256 totalSupply) external {
        // Validate the input parameters
        require(totalSupply > 0, "Total supply must be greater than zero");
        
        // Create new token contract
        PermissionlessToken newToken = new PermissionlessToken(name, symbol, totalSupply);
        
        // Check if the token is already listed
        if (listedTokens[address(newToken)]) {
            revert TokenAlreadyListed(address(newToken));
        }
        
        // Mark the new token as listed
        listedTokens[address(newToken)] = true;
        
        emit TokenCreated(msg.sender, name, symbol, totalSupply);
    }

    /**
     * @dev Allows users to check if a token is listed.
     * @param tokenAddress The address of the token to check.
     * @return bool indicating whether the token is listed.
     */
    function isTokenListed(address tokenAddress) external view returns (bool) {
        return listedTokens[tokenAddress];
    }
    
    /**
     * @dev Allows the owner to withdraw any Ether sent to the contract.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
