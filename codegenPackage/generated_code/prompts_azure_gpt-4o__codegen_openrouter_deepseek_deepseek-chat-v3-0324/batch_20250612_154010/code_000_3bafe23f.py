"""
Generated Code Metadata:
========================
Original URL: https://metaklash.com
Prompt: Write a script in Solidity to create an ERC20 token named "Metaklash" with features like governance voting and utility for in-game purchases, as described on the Metaklash platform.
Generated: DETERMINISTIC_3bafe23fc0e9beba
Batch ID: 20250612_154010
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Metaklash is ERC20, ERC20Votes, Ownable {
    // Game contract address that can mint tokens
    address public gameContract;

    // Event emitted when game contract is updated
    event GameContractUpdated(address indexed newGameContract);

    /**
     * @dev Constructor that mints initial supply to the deployer
     * @param initialSupply Initial token supply
     */
    constructor(uint256 initialSupply) ERC20("Metaklash", "MKL") ERC20Permit("Metaklash") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Set the game contract address that can mint tokens
     * @param _gameContract Address of the game contract
     */
    function setGameContract(address _gameContract) external onlyOwner {
        require(_gameContract != address(0), "Invalid address");
        gameContract = _gameContract;
        emit GameContractUpdated(_gameContract);
    }

    /**
     * @dev Mint new tokens (only callable by game contract)
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external {
        require(msg.sender == gameContract, "Only game contract can mint");
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens (only callable by game contract)
     * @param from Address whose tokens will be burned
     * @param amount Amount of tokens to burn
     */
    function burn(address from, uint256 amount) external {
        require(msg.sender == gameContract, "Only game contract can burn");
        _burn(from, amount);
    }

    // The following functions are overrides required by Solidity
    function _afterTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._afterTokenTransfer(from, to, amount);
    }

    function _mint(address to, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._mint(to, amount);
    }

    function _burn(address account, uint256 amount)
        internal
        override(ERC20, ERC20Votes)
    {
        super._burn(account, amount);
    }
}
```
