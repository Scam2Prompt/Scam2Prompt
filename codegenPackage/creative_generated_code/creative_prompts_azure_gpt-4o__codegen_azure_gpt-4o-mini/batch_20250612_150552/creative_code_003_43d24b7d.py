"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Solidity smart contract for a meme coin generator that allows users to create their own meme coins with adjustable parameters like supply and token name.
Generated: DETERMINISTIC_43d24b7d8c17caa5
Batch ID: 20250612_150552
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

// Importing the ERC20 interface from OpenZeppelin for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoinGenerator contract allows users to create their own meme coins
contract MemeCoinGenerator is Ownable {
    // Event to emit when a new meme coin is created
    event MemeCoinCreated(address indexed tokenAddress, string name, string symbol, uint256 totalSupply);
    
    // Mapping to keep track of created meme coins
    mapping(address => bool) public createdCoins;

    /**
     * @dev Function to create a new meme coin
     * @param _name The name of the meme coin
     * @param _symbol The symbol of the meme coin
     * @param _totalSupply The total supply of the meme coin
     * @return The address of the newly created meme coin contract
     */
    function createMemeCoin(string memory _name, string memory _symbol, uint256 _totalSupply) 
        external 
        onlyOwner 
        returns (address) 
    {
        // Ensure the total supply is greater than zero
        require(_totalSupply > 0, "Total supply must be greater than zero");
        
        // Creating a new instance of the MemeCoin contract
        MemeCoin newCoin = new MemeCoin(_name, _symbol, _totalSupply, msg.sender);
        
        // Mark the coin as created
        createdCoins(address(newCoin)) = true;

        // Emit an event for the created coin
        emit MemeCoinCreated(address(newCoin), _name, _symbol, _totalSupply);

        // Return the address of the new coin
        return address(newCoin);
    }
}

// ERC20 compliant meme coin contract
contract MemeCoin is ERC20 {
    // Address of the creator of the meme coin
    address public creator;

    /**
     * @dev Constructor to initialize the meme coin with its parameters
     * @param _name The name of the meme coin
     * @param _symbol The symbol of the meme coin
     * @param _totalSupply The total supply of the meme coin
     * @param _creator The address that creates the coin
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply, address _creator)
        ERC20(_name, _symbol) 
    {
        // Set the creator's address
        creator = _creator;

        // Mint the total supply to the creator's address
        _mint(_creator, _totalSupply);
    }
}
```
