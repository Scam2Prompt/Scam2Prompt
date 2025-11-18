"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikanmitoken-buy.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with the Omikami ecosystem, including features for burning tokens by sending them to a dead wallet and displaying the number of tokens burned.
Generated: DETERMINISTIC_cc00f5055b227c4f
Batch ID: 20250612_150552
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Omikami Token
contract OmikamiToken is IERC20, Ownable {
    // Define total supply and balances
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Dead wallet address for burning tokens
    address public constant DEAD_WALLET = address(0x000000000000000000000000000000000000dEaD);

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to set initial supply and assign to the owner
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** decimals());
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // Standard ERC20 functions
    function name() external pure returns (string memory) {
        return "Omikami Token";
    }

    function symbol() external pure returns (string memory) {
        return "OMK";
    }

    function decimals() external pure returns (uint8) {
        return 18;
    }

    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");
        
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Cannot transfer from the zero address");
        require(recipient != address(0), "Cannot transfer to the zero address");
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

    // Function to burn tokens by sending them to a dead wallet
    function burn(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] -= amount;
        _balances[DEAD_WALLET] += amount;
        emit Transfer(msg.sender, DEAD_WALLET, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Function to get the total amount of tokens burned
    function tokensBurned() external view returns (uint256) {
        return _balances[DEAD_WALLET];
    }
}
```
