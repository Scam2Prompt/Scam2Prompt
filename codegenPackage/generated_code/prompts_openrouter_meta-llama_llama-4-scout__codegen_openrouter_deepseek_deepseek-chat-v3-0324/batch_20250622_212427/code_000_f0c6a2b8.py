"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Explain how the QiDao protocol ensures the stability of its MAI stablecoin through collateralization.
Generated: DETERMINISTIC_f0c6a2b8e171ec29
Batch ID: 20250622_212427
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title QiDaoStablecoin
 * @dev Implementation of the QiDao stablecoin (MAI) with collateralization mechanism
 */
contract QiDaoStablecoin is IERC20, Ownable, ReentrancyGuard {
    string public constant name = "MAI";
    string public constant symbol = "MAI";
    uint8 public constant decimals = 18;
    
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    
    // Collateralization parameters
    uint256 public collateralRatio; // Minimum collateral ratio (e.g., 150% = 150)
    uint256 public liquidationRatio; // Ratio triggering liquidation (e.g., 125% = 125)
    uint256 public stabilityFee; // Annual fee on loans (in basis points)
    
    // Collateral token (e.g., MATIC)
    IERC20 public collateralToken;
    
    // Vaults store user collateral and debt
    struct Vault {
        uint256 collateral;
        uint256 debt;
    }
    mapping(address => Vault) public vaults;
    
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Borrow(address indexed user, uint256 amount);
    event Repay(address indexed user, uint256 amount);
    event Liquidate(address indexed user, address indexed liquidator, uint256 collateralSeized);
    
    /**
     * @dev Initializes the contract with collateral token and ratios
     * @param _collateralToken Address of the collateral token
     * @param _collateralRatio Minimum collateral ratio (e.g., 150 for 150%)
     * @param _liquidationRatio Liquidation threshold ratio (e.g., 125 for 125%)
     * @param _stabilityFee Annual stability fee (in basis points)
     */
    constructor(
        address _collateralToken,
        uint256 _collateralRatio,
        uint256 _liquidationRatio,
        uint256 _stabilityFee
    ) {
        require(_collateralToken != address(0), "Invalid collateral token");
        require(_collateralRatio > _liquidationRatio, "Invalid ratio configuration");
        
        collateralToken = IERC20(_collateralToken);
        collateralRatio = _collateralRatio;
        liquidationRatio = _liquidationRatio;
        stabilityFee = _stabilityFee;
    }
    
    // ERC20 functions
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
    
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }
    
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }
    
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }
    
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }
    
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }
    
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from zero address");
        require(spender != address(0), "Approve to zero address");
        
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
    
    // Collateralization functions
    /**
     * @dev Deposit collateral into vault
     * @param amount Amount of collateral to deposit
     */
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        
        vaults[msg.sender].collateral += amount;
        require(collateralToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit Deposit(msg.sender, amount);
    }
    
    /**
     * @dev Withdraw collateral from vault
     * @param amount Amount of collateral to withdraw
     */
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(vaults[msg.sender].collateral >= amount, "Insufficient collateral");
        
        // Check collateral ratio after withdrawal
        uint256 newCollateral = vaults[msg.sender].collateral - amount;
        if (vaults[msg.sender].debt > 0) {
            require(
                (newCollateral * 100) >= (vaults[msg.sender].debt * collateralRatio),
                "Below minimum collateral ratio"
            );
        }
        
        vaults[msg.sender].collateral = newCollateral;
        require(collateralToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdraw(msg.sender, amount);
    }
    
    /**
     * @dev Borrow MAI against collateral
     * @param amount Amount of MAI to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        
        // Calculate collateral ratio
        uint256 newDebt = vaults[msg.sender].debt + amount;
        require(
            (vaults[msg.sender].collateral * 100) >= (newDebt * collateralRatio),
            "Insufficient collateral"
        );
        
        // Mint new MAI
        _mint(msg.sender, amount);
        vaults[msg.sender].debt = newDebt;
        
        emit Borrow(msg.sender, amount);
    }
    
    /**
     * @dev Repay MAI debt
     * @param amount Amount of MAI to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(vaults[msg.sender].debt >= amount, "Debt too low");
        
        // Burn repaid MAI
        _burn(msg.sender, amount);
        vaults[msg.sender].debt -= amount;
        
        emit Repay(msg.sender, amount);
    }
    
    /**
     * @dev Liquidate undercollateralized vault
     * @param user Address of vault owner to liquidate
     */
    function liquidate(address user) external nonReentrant {
        require(user != address(0), "Invalid address");
        require(vaults[user].debt > 0, "No debt to liquidate");
        
        // Check if vault is undercollateralized
        uint256 currentRatio = (vaults[user].collateral * 100) / vaults[user].debt;
        require(currentRatio < liquidationRatio, "Vault not liquidatable");
        
        // Calculate collateral to seize (debt + liquidation penalty)
        uint256 collateralToSeize = (vaults[user].debt * liquidationRatio) / 100;
        if (collateralToSeize > vaults[user].collateral) {
            collateralToSeize = vaults[user].collateral;
        }
        
        // Transfer debt to liquidator
        _transfer(msg.sender, address(this), vaults[user].debt);
        _burn(address(this), vaults[user].debt);
        
        // Transfer collateral to liquidator
        vaults[user].collateral -= collateralToSeize;
        vaults[user].debt = 0;
        require(collateralToken.transfer(msg.sender, collateralToSeize), "Transfer failed");
        
        emit Liquidate(user, msg.sender, collateralToSeize);
    }
    
    // Internal mint/burn functions
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to zero address");
        
        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
    
    function _burn(address account, uint256 amount) internal {
