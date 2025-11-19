"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Generate a smart contract code in Solidity for a token with a similar tokenomics structure as $CAT, including allocations for presale investors, liquidity, and airdrops.
Generated: DETERMINISTIC_f505ea330b2f5e55
Batch ID: 20250622_204837
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
 * @title CATToken
 * @author [Your Name]
 * @notice A token with a similar tokenomics structure as $CAT.
 */
contract CATToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Presale investors allocation (10%)
    address[] public presaleInvestors;
    mapping(address => uint256) public presaleInvestorBalances;

    // Liquidity allocation (20%)
    address public liquidityProvider;
    uint256 public liquidityAllocation;

    // Airdrop allocation (5%)
    uint256 public airdropAllocation;
    address[] public airdropRecipients;
    mapping(address => uint256) public airdropRecipientBalances;

    // Tokenomics
    uint256 public constant TOTAL_SUPPLY = 100 * 10**6 * 10**18; // 100 million tokens
    uint256 public constant PRESALE_INVESTORS_ALLOCATION = TOTAL_SUPPLY * 10 / 100; // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = TOTAL_SUPPLY * 20 / 100; // 20%
    uint256 public constant AIRDROP_ALLOCATION = TOTAL_SUPPLY * 5 / 100; // 5%

    /**
     * @notice Constructor
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _totalSupply = TOTAL_SUPPLY;

        // Presale investors allocation
        _mint(msg.sender, PRESALE_INVESTORS_ALLOCATION);
        presaleInvestors.push(msg.sender);
        presaleInvestorBalances[msg.sender] = PRESALE_INVESTORS_ALLOCATION;

        // Liquidity allocation
        liquidityProvider = msg.sender;
        liquidityAllocation = LIQUIDITY_ALLOCATION;
        _mint(liquidityProvider, liquidityAllocation);

        // Airdrop allocation
        airdropAllocation = AIRDROP_ALLOCATION;
    }

    /**
     * @notice Add presale investor
     * @param investor The address of the presale investor
     * @param allocation The allocation for the presale investor
     */
    function addPresaleInvestor(address investor, uint256 allocation) public onlyOwner {
        require(investor != address(0), "Invalid investor address");
        require(presaleInvestorBalances[investor] == 0, "Investor already added");

        presaleInvestors.push(investor);
        presaleInvestorBalances[investor] = allocation;
        _mint(investor, allocation);
    }

    /**
     * @notice Add airdrop recipient
     * @param recipient The address of the airdrop recipient
     * @param allocation The allocation for the airdrop recipient
     */
    function addAirdropRecipient(address recipient, uint256 allocation) public onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(airdropRecipientBalances[recipient] == 0, "Recipient already added");

        airdropRecipients.push(recipient);
        airdropRecipientBalances[recipient] = allocation;
        _mint(recipient, allocation);
    }

    /**
     * @notice Transfer tokens
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 senderBalance = _balances[msg.sender];
        require(senderBalance >= amount, "Insufficient balance");

        _balances[msg.sender] = senderBalance - amount;
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approve tokens
     * @param spender The address of the spender
     * @param amount The amount of tokens to approve
     * @return A boolean indicating whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from
     * @param sender The address of the sender
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "Insufficient balance");
        uint256 allowance = _allowances[sender][msg.sender];
        require(allowance >= amount, "Insufficient allowance");

        _balances[sender] = senderBalance - amount;
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = allowance - amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Increase allowance
     * @param spender The address of the spender
     * @param addedValue The amount to increase the allowance by
     * @return A boolean indicating whether the increase was successful
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        _allowances[msg.sender][spender] = currentAllowance.add(addedValue);

        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decrease allowance
     * @param spender The address of the spender
     * @param subtractedValue The amount to decrease the allowance by
     * @return A boolean indicating whether the decrease was successful
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "Insufficient allowance");

        _allowances[msg.sender][spender] = currentAllowance - subtractedValue;

        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        uint256 accountBalance = _balances[msg.sender];
        require(accountBalance >= amount, "Insufficient balance");

        _balances[msg.sender] = accountBalance - amount;
        _totalSupply -= amount;

        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Mint tokens
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function mint(address account, uint256 amount) public onlyOwner {
        _mint(account, amount);
    }

    /**
     * @notice Mint tokens (internal)
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Invalid account");

        _totalSupply += amount;
        _balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    /**
     * @notice Get the balance of an account
     * @param account The address of the account
     * @return The balance of the account
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Get the allowance of a spender
     * @param owner The address of the owner
     * @param spender The address of the spender
     * @return The allowance of the spender
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
}
```
