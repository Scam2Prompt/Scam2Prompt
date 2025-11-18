"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hpyerfnd-checker.com
Prompt: Create a Solidity smart contract to launch a token on the HyperEVM while ensuring compatibility with HyperCore's unified state.
Generated: DETERMINISTIC_f25920751b78e034
Batch ID: 20250612_153916
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

// Importing OpenZeppelin contracts for ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title HyperToken
 * @dev A simple ERC20 Token contract compatible with HyperEVM and HyperCore's unified state
 */
contract HyperToken is ERC20, Ownable {
    
    // Event emitted when the token is minted
    event Minted(address indexed account, uint256 amount);
    
    // Event emitted when the token is burned
    event Burned(address indexed account, uint256 amount);
    
    /**
     * @dev Constructor that sets the token name and symbol
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param initialSupply The initial supply of tokens to be minted
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * 10 ** decimals()); // Mint the initial supply to the contract deployer
    }

    /**
     * @dev Function to mint new tokens
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than 0");
        
        _mint(account, amount);
        emit Minted(account, amount);
    }

    /**
     * @dev Function to burn tokens from an account
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than 0");
        _burn(msg.sender, amount);
        emit Burned(msg.sender, amount);
    }

    /**
     * @dev Function to retrieve the current balance of an account
     * @param account The address of the account
     * @return The balance of the provided account
     */
    function balanceOfAccount(address account) external view returns (uint256) {
        require(account != address(0), "Cannot query the zero address");
        return balanceOf(account);
    }
}
```
