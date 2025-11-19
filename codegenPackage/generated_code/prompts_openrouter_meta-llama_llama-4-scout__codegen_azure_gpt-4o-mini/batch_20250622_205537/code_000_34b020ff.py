"""
Generated Code Metadata:
========================
Original URL: https://bigeyetests.pages.dev
Prompt: Write a Solidity code snippet to verify the security of a memecoin platform's contract, similar to Big Eyes' audit by Solidity Finance.
Generated: DETERMINISTIC_34b020ff8737177a
Batch ID: 20250622_205537
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Memecoin
 * @dev A simple ERC20 token implementation for a memecoin platform.
 * This contract includes basic security features and follows best practices.
 */
contract Memecoin is ERC20, Ownable {
    // Mapping to track addresses that are allowed to mint tokens
    mapping(address => bool) private _minters;

    // Event emitted when a new minter is added
    event MinterAdded(address indexed minter);
    
    // Event emitted when a minter is removed
    event MinterRemoved(address indexed minter);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * The initial supply is allocated to the contract owner.
     */
    constructor() ERC20("Memecoin", "MEME") {
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to owner
    }

    /**
     * @dev Modifier to check if the caller is a minter.
     */
    modifier onlyMinter() {
        require(_minters[msg.sender], "Caller is not a minter");
        _;
    }

    /**
     * @dev Function to add a new minter.
     * @param minter The address to be added as a minter.
     */
    function addMinter(address minter) external onlyOwner {
        require(minter != address(0), "Invalid address");
        require(!_minters[minter], "Address is already a minter");

        _minters[minter] = true;
        emit MinterAdded(minter);
    }

    /**
     * @dev Function to remove a minter.
     * @param minter The address to be removed from minters.
     */
    function removeMinter(address minter) external onlyOwner {
        require(_minters[minter], "Address is not a minter");

        _minters[minter] = false;
        emit MinterRemoved(minter);
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyMinter {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(to, amount);
    }

    /**
     * @dev Function to check if an address is a minter.
     * @param account The address to check.
     * @return bool indicating if the address is a minter.
     */
    function isMinter(address account) external view returns (bool) {
        return _minters[account];
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
