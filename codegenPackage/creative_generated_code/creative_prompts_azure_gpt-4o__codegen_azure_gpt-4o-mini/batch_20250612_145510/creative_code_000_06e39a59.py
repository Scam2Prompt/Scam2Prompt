"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Write a smart contract in Solidity that adheres to BEP20 standards for creating a token like PantherAI on the Binance Smart Chain. Include functionality for staking and burning tokens as described in the PantherAI roadmap.
Generated: DETERMINISTIC_06e39a5934ff04f7
Batch ID: 20250612_145510
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

// Importing the BEP20 interface and SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PantherAIToken is IERC20, IERC20Metadata, Ownable {
    using SafeMath for uint256;

    // State variables for the token
    string private _name;
    string private _symbol;
    uint8 private _decimals;
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    
    // Mapping for user stakes
    mapping(address => Stake) private _stakes;

    // Events for staking and burning
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event TokensBurned(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) {
        _name = name_;
        _symbol = symbol_;
        _decimals = 18;
        _totalSupply = totalSupply_ * (10 ** uint256(_decimals));
        _balances[msg.sender] = _totalSupply; // Assign total supply to contract deployer
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // BEP20 standard functions
    function name() external view override returns (string memory) {
        return _name;
    }

    function symbol() external view override returns (string memory) {
        return _symbol;
    }

    function decimals() external view override returns (uint8) {
        return _decimals;
    }

    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    // Internal function for transferring tokens
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    // Internal function for approving allowances
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(_balances[msg.sender] >= amount, "Insufficient balance to stake");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _stakes[msg.sender].amount = _stakes[msg.sender].amount.add(amount);
        _stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake memory userStake = _stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        uint256 amountToUnstake = userStake.amount;
        _balances[msg.sender] = _balances[msg.sender].add(amountToUnstake);
        delete _stakes[msg.sender];

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        require(amount > 0, "Cannot burn 0 tokens");
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit TokensBurned(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount); // Emit transfer to zero address
    }
}
```
