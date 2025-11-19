"""
Generated Code Metadata:
========================
Original URL: https://panther-ai.pages.dev
Prompt: Generate a smart contract for the PantherAI token using BEP20 standards, ensuring it includes features for staking and liquidity management.
Generated: DETERMINISTIC_4daaa70eb87f350d
Batch ID: 20250612_155446
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/IERC20Metadata.sol";
import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PantherAI is Context, IERC20, IERC20Metadata, Ownable {
    using SafeMath for uint256;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    mapping(address => bool) private _isExcludedFromFee;
    mapping(address => bool) private _isStaker;

    uint256 private _totalSupply;
    string private _name;
    string private _symbol;
    uint8 private _decimals;

    uint256 public liquidityFee = 2; // 2% liquidity fee
    uint256 public stakingFee = 3;   // 3% staking fee
    uint256 public totalFees = liquidityFee.add(stakingFee);

    address public liquidityWallet;
    address public stakingWallet;

    bool public feesEnabled = true;

    event StakerAdded(address indexed account);
    event StakerRemoved(address indexed account);
    event FeesUpdated(uint256 liquidityFee, uint256 stakingFee);
    event FeesToggled(bool enabled);
    event WalletsUpdated(address liquidityWallet, address stakingWallet);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        address liquidityWallet_,
        address stakingWallet_
    ) {
        _name = name_;
        _symbol = symbol_;
        _decimals = 18;
        _totalSupply = initialSupply_ * 10 ** _decimals;
        _balances[_msgSender()] = _totalSupply;
        liquidityWallet = liquidityWallet_;
        stakingWallet = stakingWallet_;

        // Exclude owner and wallets from fees
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[liquidityWallet] = true;
        _isExcludedFromFee[stakingWallet] = true;

        emit Transfer(address(0), _msgSender(), _totalSupply);
    }

    function name() public view override returns (string memory) {
        return _name;
    }

    function symbol() public view override returns (string memory) {
        return _symbol;
    }

    function decimals() public view override returns (uint8) {
        return _decimals;
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender].add(addedValue));
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender].sub(subtractedValue, "ERC20: decreased allowance below zero"));
        return true;
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }

    function excludeFromFee(address account) public onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    function includeInFee(address account) public onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    function isStaker(address account) public view returns (bool) {
        return _isStaker[account];
    }

    function addStaker(address account) public onlyOwner {
        _isStaker[account] = true;
        emit StakerAdded(account);
    }

    function removeStaker(address account) public onlyOwner {
        _isStaker[account] = false;
        emit StakerRemoved(account);
    }

    function setFees(uint256 _liquidityFee, uint256 _stakingFee) external onlyOwner {
        require(_liquidityFee.add(_stakingFee) <= 10, "Fees cannot exceed 10%");
        liquidityFee = _liquidityFee;
        stakingFee = _stakingFee;
        totalFees = _liquidityFee.add(_stakingFee);
        emit FeesUpdated(_liquidityFee, _stakingFee);
    }

    function toggleFees(bool _enabled) external onlyOwner {
        feesEnabled = _enabled;
        emit FeesToggled(_enabled);
    }

    function setWallets(address _liquidityWallet, address _stakingWallet) external onlyOwner {
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        require(_stakingWallet != address(0), "Staking wallet cannot be zero address");
        liquidityWallet = _liquidityWallet;
        stakingWallet = _stakingWallet;
        emit WalletsUpdated(_liquidityWallet, _stakingWallet);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");

        bool takeFee = feesEnabled;
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            takeFee = false;
        }

        if (takeFee) {
            uint256 liquidityAmount = amount.mul(liquidityFee).div(100);
            uint256 stakingAmount = amount.mul(stakingFee).div(100);
            uint256 transferAmount = amount.sub(liquidityAmount).sub(stakingAmount);

            _balances[sender] = senderBalance.sub(amount);
            _balances[recipient] = _balances[recipient].add(transferAmount);
            _balances[liquidityWallet] = _balances[liquidityWallet].add(liquidityAmount);
            _balances[stakingWallet] = _balances[stakingWallet].add(stakingAmount);

            emit Transfer(sender, recipient, transferAmount);
            emit Transfer(sender, liquidityWallet, liquidityAmount);
            emit Transfer(sender, stakingWallet, stakingAmount);
        } else {
            _balances[sender] = senderBalance.sub(amount);
            _balances[recipient] = _balances[recipient].add(amount);
            emit Transfer(sender, recipient, amount);
        }
    }

    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "ERC20: mint to the zero address");
        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }

    function burn(uint256 amount) public {
        _burn(_msgSender(), amount);
    }

    function burnFrom(address account, uint256 amount) public {
        uint256 currentAllowance = allowance(account, _msgSender());
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        _approve(account, _msgSender(), currentAllowance.sub(amount));
        _burn(account, amount);
    }

    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");
        uint256 accountBalance = _balances[
