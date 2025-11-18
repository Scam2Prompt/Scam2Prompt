"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Generate a smart contract for launching a new token on the HyperEVM Native Dex, incorporating liquidity management features.
Generated: DETERMINISTIC_40e6f76cf8320080
Batch ID: 20250612_154057
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

// Importing the required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the contract for the Token
contract MyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Liquidity management parameters
    uint256 public liquidityFee; // Liquidity fee as a percentage
    uint256 public totalSupplyLimit; // Maximum total supply
    mapping(address => bool) private _isExcludedFromFee;

    // Events
    event LiquidityAdded(uint256 amountToken, uint256 amountETH);
    
    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _liquidityFee, uint256 _totalSupplyLimit) 
        ERC20(name, symbol) 
    {
        require(initialSupply <= _totalSupplyLimit, "Initial supply exceeds total supply limit");
        _mint(msg.sender, initialSupply);
        liquidityFee = _liquidityFee;
        totalSupplyLimit = _totalSupplyLimit;
        _isExcludedFromFee[msg.sender] = true; // Exclude owner from fees
    }

    // Function to set liquidity fee
    function setLiquidityFee(uint256 fee) external onlyOwner {
        liquidityFee = fee;
    }

    // Function to add liquidity to the DEX
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Transfer tokens from owner to contract
        _transfer(msg.sender, address(this), tokenAmount);

        // Emit event for liquidity addition
        emit LiquidityAdded(tokenAmount, msg.value);
    }

    // Function to exclude addresses from liquidity fees
    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    // Function to include addresses back in liquidity fees
    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    // Overriding the transfer function to include liquidity fee logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        if(!_isExcludedFromFee[sender] && !_isExcludedFromFee[recipient]) {
            uint256 feeAmount = amount.mul(liquidityFee).div(100);
            amount = amount.sub(feeAmount);
            super._transfer(sender, address(this), feeAmount); // Transfer fee to contract
        }
        super._transfer(sender, recipient, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
