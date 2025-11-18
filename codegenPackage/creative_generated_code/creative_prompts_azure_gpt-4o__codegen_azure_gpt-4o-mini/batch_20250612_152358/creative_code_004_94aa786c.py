"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogs-swap.pages.dev
Prompt: Develop a smart contract to facilitate $DOGS token transfers and airdrop distribution on the TON network.
Generated: DETERMINISTIC_94aa786ce87a6b61
Batch ID: 20250612_152358
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DogToken
 * @dev Smart contract for $DOGS token transfers and airdrop distribution
 */
contract DogToken is IERC20, Ownable {
    // State variables
    string private _name = "Dog Token";
    string private _symbol = "DOGS";
    uint8 private _decimals = 18;
    uint256 private _totalSupply;

    // Mapping from account addresses to their balances
    mapping(address => uint256) private _balances;

    // Mapping from account addresses to their allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event declarations (additional to the standard ones)
    event Airdrop(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that sets the initial total supply and assigns it to the creator
     * @param initialSupply initial supply of tokens to be created
     */
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * (10 ** uint256(_decimals));
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // ERC20 standard function implementations

    function name() public view returns (string memory) {
        return _name;
    }

    function symbol() public view returns (string memory) {
        return _symbol;
    }

    function decimals() public view returns (uint8) {
        return _decimals;
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
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

    /**
     * @dev Airdrop tokens to multiple recipients
     * @param recipients List of addresses to receive the airdrop
     * @param amounts List of corresponding amounts for each recipient
     */
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Cannot airdrop to the zero address");
            require(_balances[owner()] >= amounts[i], "Insufficient balance for airdrop");

            _balances[owner()] -= amounts[i];
            _balances[recipients[i]] += amounts[i];

            emit Transfer(owner(), recipients[i], amounts[i]);
            emit Airdrop(recipients[i], amounts[i]);
        }
    }
}
```
