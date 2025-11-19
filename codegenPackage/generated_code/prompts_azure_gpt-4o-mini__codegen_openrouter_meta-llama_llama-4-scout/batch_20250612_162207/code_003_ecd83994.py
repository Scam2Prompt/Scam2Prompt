"""
Generated Code Metadata:
========================
Original URL: https://too1m.pages.dev
Prompt: Develop a smart contract in Solidity for the $POON token that includes features mentioned in the tokenomics section of the website.
Generated: DETERMINISTIC_ecd83994b02449c5
Batch ID: 20250612_162207
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PoonToken
 * @author [Your Name]
 * @notice The $POON token smart contract.
 */
contract PoonToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Tokenomics parameters
    uint256 public _totalSupply;
    uint256 public _maxSupply;
    uint256 public _mintingRate;

    // Events
    event Mint(address indexed to, uint256 amount);
    event TokenomicsUpdated(uint256 maxSupply, uint256 mintingRate);

    /**
     * @notice Initializes the PoonToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param maxSupply The maximum supply of the token.
     * @param mintingRate The rate at which new tokens are minted.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 maxSupply,
        uint256 mintingRate
    ) ERC20(name, symbol) {
        _totalSupply = initialSupply;
        _maxSupply = maxSupply;
        _mintingRate = mintingRate;

        // Mint initial supply to the contract creator
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Updates the tokenomics parameters.
     * @param maxSupply The new maximum supply of the token.
     * @param mintingRate The new minting rate of the token.
     */
    function updateTokenomics(uint256 maxSupply, uint256 mintingRate) public onlyOwner {
        _maxSupply = maxSupply;
        _mintingRate = mintingRate;

        emit TokenomicsUpdated(maxSupply, mintingRate);
    }

    /**
     * @notice Mints new tokens to the specified address.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(_totalSupply + amount <= _maxSupply, "Mint: Exceeds maximum supply");

        _totalSupply += amount;
        _mint(to, amount);

        emit Mint(to, amount);
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        super.burn(amount);
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Increases the allowance of the specified address.
     * @param spender The address to increase the allowance of.
     * @param addedValue The amount to increase the allowance by.
     */
    function increaseAllowance(address spender, uint256 addedValue) public override nonReentrant returns (bool) {
        return super.increaseAllowance(spender, addedValue);
    }

    /**
     * @notice Decreases the allowance of the specified address.
     * @param spender The address to decrease the allowance of.
     * @param subtractedValue The amount to decrease the allowance by.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override nonReentrant returns (bool) {
        return super.decreaseAllowance(spender, subtractedValue);
    }

    /**
     * @notice Returns the total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of the specified address.
     * @param account The address to retrieve the balance of.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Returns the allowance of the specified address.
     * @param owner The address to retrieve the allowance of.
     * @param spender The address to retrieve the allowance for.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
