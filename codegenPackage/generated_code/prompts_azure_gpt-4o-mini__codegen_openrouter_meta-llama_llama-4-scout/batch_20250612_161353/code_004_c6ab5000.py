"""
Generated Code Metadata:
========================
Original URL: https://phoenixai-art.pages.dev
Prompt: Create a sample smart contract for the PXAI token, ensuring it includes features for buy-back and burn mechanisms as mentioned in the Phoenix AI tokenomics section.
Generated: DETERMINISTIC_c6ab5000ca69276e
Batch ID: 20250612_161353
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PXAI Token Contract
 * @author [Your Name]
 * @notice This contract represents the PXAI token with buy-back and burn mechanisms.
 */
contract PXAI is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // The address of the contract owner
    address private owner;

    // The address of the PXAI token treasury
    address private treasury;

    // The buy-back fee percentage
    uint256 public buyBackFee;

    // The total buy-back amount
    uint256 public totalBuyBackAmount;

    /**
     * @notice Constructor for the PXAI token contract
     * @param _name The name of the token
     * @param _symbol The symbol of the token
     * @param _treasury The address of the PXAI token treasury
     */
    constructor(string memory _name, string memory _symbol, address _treasury) ERC20(_name, _symbol) {
        owner = msg.sender;
        treasury = _treasury;
        buyBackFee = 500; // 5%
        totalBuyBackAmount = 0;
        _mint(msg.sender, 1000000 * 10**18); // Initial supply of 1,000,000 tokens with 18 decimals
    }

    /**
     * @notice Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @notice Modifier to restrict access to the treasury
     */
    modifier onlyTreasury() {
        require(msg.sender == treasury, "Only the treasury can perform this action");
        _;
    }

    /**
     * @notice Function to handle token transfers
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(buyBackFee).div(10000);
        uint256 sendAmount = amount.sub(fee);
        _transfer(msg.sender, to, sendAmount);
        _transfer(msg.sender, treasury, fee);
        totalBuyBackAmount = totalBuyBackAmount.add(fee);
        return true;
    }

    /**
     * @notice Function to handle token transfers with allowance
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(buyBackFee).div(10000);
        uint256 sendAmount = amount.sub(fee);
        _transfer(from, to, sendAmount);
        _transfer(from, treasury, fee);
        totalBuyBackAmount = totalBuyBackAmount.add(fee);
        _approve(from, msg.sender, allowances[from][msg.sender].sub(amount));
        return true;
    }

    /**
     * @notice Function to burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Function to trigger buy-back and burn mechanism
     * @param amount The amount of tokens to buy-back and burn
     */
    function triggerBuyBack(uint256 amount) public onlyTreasury {
        require(totalBuyBackAmount >= amount, "Insufficient buy-back amount");
        _burn(treasury, amount);
        totalBuyBackAmount = totalBuyBackAmount.sub(amount);
    }

    /**
     * @notice Function to update the buy-back fee
     * @param newFee The new buy-back fee percentage
     */
    function updateBuyBackFee(uint256 newFee) public onlyOwner {
        buyBackFee = newFee;
    }

    /**
     * @notice Function to update the treasury address
     * @param newTreasury The new treasury address
     */
    function updateTreasury(address newTreasury) public onlyOwner {
        treasury = newTreasury;
    }
}
```
