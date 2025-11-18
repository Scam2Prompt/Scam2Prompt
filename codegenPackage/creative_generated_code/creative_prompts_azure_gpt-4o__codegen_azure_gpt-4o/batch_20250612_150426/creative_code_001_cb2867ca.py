"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: Using the $UPRINT tokenomics, create a Solidity smart contract that implements a similar buy/sell tax mechanism (5% each) and distributes USDC reflections to token holders.
Generated: DETERMINISTIC_cb2867ca2fa87e69
Batch ID: 20250612_150426
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

// Importing required interfaces for USDC and SafeMath.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract UPrintToken is IERC20, Ownable {
    using SafeMath for uint256;

    // Token parameters
    string private constant NAME = "UPrintToken";
    string private constant SYMBOL = "UPRINT";
    uint8 private constant DECIMALS = 18;
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * (10 ** uint256(DECIMALS)); // 1 million tokens

    // Fees
    uint256 public constant BUY_TAX_PERCENT = 5; // 5% buy tax
    uint256 public constant SELL_TAX_PERCENT = 5; // 5% sell tax

    // Reflection token (USDC)
    IERC20 public usdcToken;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Reflection data
    mapping(address => uint256) private lastClaimed;
    uint256 public totalReflectionsDistributed;

    // Event declarations
    event ReflectionsDistributed(uint256 amount, uint256 timestamp);
    event ClaimedReflections(address indexed account, uint256 amount);

    constructor(address _usdcTokenAddress) {
        usdcToken = IERC20(_usdcTokenAddress);
        balances[msg.sender] = TOTAL_SUPPLY;
        emit Transfer(address(0), msg.sender, TOTAL_SUPPLY);
    }

    // ERC20 functions
    function name() external pure returns (string memory) {
        return NAME;
    }

    function symbol() external pure returns (string memory) {
        return SYMBOL;
    }

    function decimals() external pure returns (uint8) {
        return DECIMALS;
    }

    function totalSupply() external pure override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is prohibited");
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address is prohibited");
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is prohibited");
        require(recipient != address(0), "Transfer to the zero address is prohibited");
        require(allowances[sender][msg.sender] >= amount, "Transfer exceeds allowance");
        allowances[sender][msg.sender] = allowances[sender][msg.sender].sub(amount);
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal transfer function
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(balances[sender] >= amount, "Insufficient balance for transfer");

        uint256 taxAmount = amount.mul(BUY_TAX_PERCENT).div(100); // Apply buy/sell tax
        uint256 netAmount = amount.sub(taxAmount);

        // Update balances
        balances[sender] = balances[sender].sub(amount);
        balances[recipient] = balances[recipient].add(netAmount);

        // Distribute tax as reflections
        _distributeReflections(taxAmount);

        emit Transfer(sender, recipient, netAmount);
    }

    // Reflection distribution logic
    function _distributeReflections(uint256 amount) internal {
        totalReflectionsDistributed = totalReflectionsDistributed.add(amount);
        usdcToken.transfer(_calculateReflectionForAddress(msg.sender)); // Example reflection logic
    }

    ///""End configuration[
