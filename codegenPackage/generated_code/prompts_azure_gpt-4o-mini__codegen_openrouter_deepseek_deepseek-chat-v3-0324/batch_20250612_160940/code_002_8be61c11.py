"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to create their own meme coin on the Oracle Meme's Meme Coin Generator.
Generated: DETERMINISTIC_8be61c11772ef7af
Batch ID: 20250612_160940
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

contract MemeCoinGenerator is ERC20, Ownable {
    uint256 public constant INITIAL_SUPPLY = 1000000 * 10**18;
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18;
    uint256 public constant MINT_FEE = 0.01 ether;
    
    string private _memeName;
    string private _memeSymbol;
    uint8 private _decimals;
    
    event MemeCoinCreated(
        string name,
        string symbol,
        address creator,
        uint256 initialSupply
    );
    
    event TokensMinted(
        address minter,
        uint256 amount,
        uint256 newTotalSupply
    );
    
    constructor(
        string memory name_,
        string memory symbol_,
        uint8 decimals_
    ) ERC20(name_, symbol_) {
        _memeName = name_;
        _memeSymbol = symbol_;
        _decimals = decimals_;
        
        _mint(msg.sender, INITIAL_SUPPLY);
        
        emit MemeCoinCreated(
            _memeName,
            _memeSymbol,
            msg.sender,
            INITIAL_SUPPLY
        );
    }
    
    function mint(address to, uint256 amount) external payable {
        require(msg.value >= MINT_FEE, "MemeCoinGenerator: Insufficient mint fee");
        require(totalSupply() + amount <= MAX_SUPPLY, "MemeCoinGenerator: Exceeds max supply");
        
        _mint(to, amount);
        
        emit TokensMinted(to, amount, totalSupply());
    }
    
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    function decimals() public view override returns (uint8) {
        return _decimals;
    }
    
    function memeName() public view returns (string memory) {
        return _memeName;
    }
    
    function memeSymbol() public view returns (string memory) {
        return _memeSymbol;
    }
    
    receive() external payable {
        revert("MemeCoinGenerator: Direct payments not allowed");
    }
}
```
