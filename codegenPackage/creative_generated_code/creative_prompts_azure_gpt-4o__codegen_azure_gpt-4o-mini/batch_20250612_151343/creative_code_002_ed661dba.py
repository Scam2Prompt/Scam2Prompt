"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogeclaim.pages.dev
Prompt: Create a smart contract on Ethereum (ERC20) that facilitates the purchase of $0DOG tokens during the presale and ensures token transfer to a connected BRC20 wallet address.
Generated: DETERMINISTIC_ed661dba6e2b6fde
Batch ID: 20250612_151343
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

// Import ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the BRC20 token transfer
interface IBRC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// ERC20 token contract for $0DOG
contract DogToken is IERC20, Ownable {
    using SafeMath for uint256;

    // Token properties
    string public name = "$0DOG";
    string public symbol = "0DOG";
    uint8 public decimals = 18;
    uint256 private _totalSupply = 1_000_000 * (10 ** uint256(decimals)); // Total supply of 1 million tokens

    // Mappings for balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event for token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokenPrice; // Price in wei per token

    // Constructor to initialize presale parameters
    constructor(uint256 _tokenPrice, uint256 _presaleDuration) {
        tokenPrice = _tokenPrice; // Set token price
        presaleStart = block.timestamp; // Presale starts now
        presaleEnd = block.timestamp + _presaleDuration; // Presale duration
        _balances[address(this)] = _totalSupply; // Allocate total supply to contract
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 amount) external payable {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(msg.value == amount.mul(tokenPrice), "Incorrect ETH value sent");
        require(_balances[address(this)] >= amount, "Not enough tokens available");

        _balances[address(this)] = _balances[address(this)].sub(amount);
        _balances[msg.sender] = _balances[msg.sender].add(amount);

        emit TokensPurchased(msg.sender, amount);
    }

    // Function to transfer tokens to a BRC20 wallet
    function transferToBRC20(address brc20Address, address recipient, uint256 amount) external onlyOwner {
        IBRC20 brc20 = IBRC20(brc20Address);
        require(brc20.transfer(recipient, amount), "BRC20 transfer failed");
    }

    // ERC20 standard functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        return true;
    }

    // Fallback function to receive ETH
    receive() external payable {}
    
    // Function to withdraw ETH to the owner's address
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner()).transfer(amount);
    }
}
```
