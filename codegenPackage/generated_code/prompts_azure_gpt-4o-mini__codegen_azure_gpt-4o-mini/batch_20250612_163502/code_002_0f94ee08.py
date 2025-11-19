"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Generate a code snippet for a decentralized application (dApp) that allows users to buy and sell $FOMO tokens on a DEX.
Generated: DETERMINISTIC_0f94ee08d05e0d16
Batch ID: 20250612_163502
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DEX (Decentralized Exchange)
interface IDex {
    function buyTokens(address token, uint256 amount) external payable;
    function sellTokens(address token, uint256 amount) external;
}

// FOMO Token Contract
contract FomoToken is IERC20, Ownable {
    string public constant name = "FOMO Token";
    string public constant symbol = "FOMO";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events for Transfer and Approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // ERC20 Functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Function to mint new tokens (only owner)
    function mint(uint256 amount) external onlyOwner {
        _totalSupply += amount * (10 ** uint256(decimals));
        _balances[msg.sender] += amount * (10 ** uint256(decimals));
        emit Transfer(address(0), msg.sender, amount * (10 ** uint256(decimals)));
    }
}

// DEX Contract for buying and selling FOMO tokens
contract FomoDex is IDex, Ownable {
    FomoToken public fomoToken;

    constructor(address tokenAddress) {
        fomoToken = FomoToken(tokenAddress);
    }

    // Buy tokens with Ether
    function buyTokens(address token, uint256 amount) external payable override {
        require(msg.value > 0, "Ether value must be greater than 0");
        require(token == address(fomoToken), "Invalid token");

        uint256 tokenAmount = msg.value; // Assuming 1 ETH = 1 FOMO for simplicity
        require(fomoToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in the reserve");

        fomoToken.transfer(msg.sender, tokenAmount);
    }

    // Sell tokens for Ether
    function sellTokens(address token, uint256 amount) external override {
        require(token == address(fomoToken), "Invalid token");
        require(fomoToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        fomoToken.transferFrom(msg.sender, address(this), amount);
        payable(msg.sender).transfer(amount); // Assuming 1 FOMO = 1 ETH for simplicity
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
