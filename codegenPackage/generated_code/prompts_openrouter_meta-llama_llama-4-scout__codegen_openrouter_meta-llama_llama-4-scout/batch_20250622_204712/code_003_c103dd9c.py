"""
Generated Code Metadata:
========================
Original URL: https://unicornmeme-clawback-claim.pages.dev
Prompt: "Generate a smart contract in Solidity for creating and distributing memecoins on the Ethereum blockchain, inspired by the Unicorn project's tokenomics."
Generated: DETERMINISTIC_c103dd9c0f157eb8
Batch ID: 20250622_204712
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
 * @title Memecoin
 * @author [Your Name]
 * @notice A smart contract for creating and distributing memecoins on the Ethereum blockchain.
 */
contract Memecoin is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of memecoins
    uint256 private _totalSupply;

    // Minting and burning events
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed burner, uint256 amount);

    /**
     * @notice Constructor for the Memecoin contract.
     * @param name_ The name of the memecoin.
     * @param symbol_ The symbol of the memecoin.
     * @param initialSupply The initial supply of memecoins.
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply) ERC20(name_, symbol_) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);
        _totalSupply = initialSupply;
    }

    /**
     * @notice Mints new memecoins and distributes them to the specified address.
     * @param to The address to distribute the memecoins to.
     * @param amount The amount of memecoins to mint and distribute.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
        _totalSupply += amount;
        emit Mint(to, amount);
    }

    /**
     * @notice Burns memecoins from the specified address.
     * @param amount The amount of memecoins to burn.
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @notice Transfers memecoins from the contract owner to the specified address.
     * @param to The address to transfer the memecoins to.
     * @param amount The amount of memecoins to transfer.
     */
    function distribute(address to, uint256 amount) public onlyOwner {
        // Check if the contract has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer memecoins
        _transfer(msg.sender, to, amount);
    }

    /**
     * @notice Increases the allowance of the specified address.
     * @param spender The address to increase the allowance for.
     * @param addedValue The amount to increase the allowance by.
     */
    function increaseAllowance(address spender, uint256 addedValue) public {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
    }

    /**
     * @notice Decreases the allowance of the specified address.
     * @param spender The address to decrease the allowance for.
     * @param subtractedValue The amount to decrease the allowance by.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "Decreased allowance below zero");
        _approve(msg.sender, spender, currentAllowance - subtractedValue);
    }

    /**
     * @notice Approves the specified address to spend the specified amount of memecoins.
     * @param spender The address to approve.
     * @param amount The amount of memecoins to approve.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers memecoins from the specified address to the recipient.
     * @param from The address to transfer memecoins from.
     * @param amount The amount of memecoins to transfer.
     * @param to The recipient address.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 currentAllowance = _allowances[from][msg.sender];
        require(currentAllowance >= amount, "Allowance insufficient");
        _approve(from, msg.sender, currentAllowance - amount);
        _transfer(from, to, amount);
        return true;
    }

    /**
     * @notice Internal function to handle memecoin transfers.
     * @param from The address to transfer memecoins from.
     * @param to The recipient address.
     * @param amount The amount of memecoins to transfer.
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        uint256 fromBalance = _balances[from];
        require(fromBalance >= amount, "Insufficient balance");
        _balances[from] = fromBalance - amount;
        _balances[to] += amount;
        emit Transfer(from, to, amount);
    }

    /**
     * @notice Internal function to handle memecoin minting.
     * @param account The address to mint memecoins to.
     * @param amount The amount of memecoins to mint.
     */
    function _mint(address account, uint256 amount) internal override {
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    /**
     * @notice Internal function to handle memecoin burning.
     * @param account The address to burn memecoins from.
     * @param amount The amount of memecoins to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "Insufficient balance");
        _balances[account] = accountBalance - amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @notice Internal function to handle allowance approvals.
     * @param owner The owner address.
     * @param spender The spender address.
     * @param amount The amount of memecoins to approve.
     */
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal override {
        require(owner != address(0), "Owner is zero");
        require(spender != address(0), "Spender is zero");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
