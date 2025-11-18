"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeofelon-swap-1.dexkit.app
Prompt: Generate Solidity code for creating a custom ERC-20 token, referencing the token creation functionality of Pepeofelon Swap.
Generated: DETERMINISTIC_ed1be8537b2237b2
Batch ID: 20250612_151247
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

// Importing OpenZeppelin's ERC20 contract and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CustomERC20Token
 * @dev This contract implements an ERC20 token with basic functionalities and ownership control.
 */
contract CustomERC20Token is ERC20, Ownable {

    // Mapping to keep track of token balances for each address
    mapping(address => bool) public minters;

    // Event to emit when a new minter is added
    event MinterAdded(address indexed minter);

    // Event to emit when a minter is removed
    event MinterRemoved(address indexed minter);

    /**
     * @dev Constructor that gives msg.sender all existing tokens.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token, in wei (smallest unit).
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to add a new minter.
     * @param minter The address to be added as a minter.
     */
    function addMinter(address minter) external onlyOwner {
        require(minter != address(0), "Minter cannot be the zero address");
        minters[minter] = true;
        emit MinterAdded(minter);
    }

    /**
     * @dev Function to remove a minter.
     * @param minter The address to be removed as a minter.
     */
    function removeMinter(address minter) external onlyOwner {
        require(minter != address(0), "Minter cannot be the zero address");
        minters[minter] = false;
        emit MinterRemoved(minter);
    }

    /**
     * @dev Mint new tokens.
     * @param to The address to receive the newly minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external {
        require(minters[msg.sender], "Only minters can mint");
        require(to != address(0), "Cannot mint to the zero address");

        // Mint tokens
        _mint(to, amount);
    }

    /**
     * @dev Override the _beforeTokenTransfer function to include checks or custom logic if needed.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Add any custom logic here, if needed
    }
}
```
