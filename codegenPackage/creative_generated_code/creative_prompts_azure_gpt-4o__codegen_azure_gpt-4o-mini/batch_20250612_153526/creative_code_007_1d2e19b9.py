"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-iio.pages.dev
Prompt: Using Solidity, design a smart contract that prevents inflation by enforcing a fixed token supply, similar to DOGE20's approach.
Generated: DETERMINISTIC_1d2e19b93d0498a9
Batch ID: 20250612_153526
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FixedSupplyToken
 * @dev A simple ERC20 token with a fixed supply to prevent inflation.
 */
contract FixedSupplyToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 private constant _totalSupply = 1_000_000 * 10 ** decimals(); // 1 million tokens

    /**
     * @dev Constructor that gives msg.sender all of the initial tokens.
     */
    constructor() ERC20("FixedSupplyToken", "FST") {
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev This function overrides the _mint function to prevent any further tokens from being created.
     * @param account The address to which tokens are being minted.
     * @param amount The number of tokens to mint.
     * Only the owner can call this function, but it will revert if called.
     */
    function _mint(address account, uint256 amount) internal override {
        require(totalSupply() + amount <= _totalSupply, "FixedSupplyToken: minting exceeds total supply");
        super._mint(account, amount);
    }

    /**
     * @dev Function to retrieve the total supply of the token.
     * @return The total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Function to safely transfer tokens from one address to another.
     * @param to The recipient address.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success or failure of the transfer.
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        require(to != address(0), "FixedSupplyToken: transfer to the zero address");
        return super.transfer(to, amount);
    }

    /**
     * @dev Function to safely approve another address to spend tokens on behalf of the owner.
     * @param spender The address which will spend the funds.
     * @param amount The amount of tokens to be spent.
     * @return A boolean indicating success or failure of the approval.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "FixedSupplyToken: approve to the zero address");
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another using the allowance mechanism.
     * @param from The address of the token owner.
     * @param to The address of the recipient.
     * @param amount The amount of tokens to be transferred.
     * @return A boolean indicating success or failure of the transfer.
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        require(from != address(0), "FixedSupplyToken: transfer from the zero address");
        require(to != address(0), "FixedSupplyToken: transfer to the zero address");
        return super.transferFrom(from, to, amount);
    }
}
```
