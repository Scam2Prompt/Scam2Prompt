"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate code for a decentralized application (dApp) that allows users to purchase BTCMTX tokens using ETH, USDT, or BNB, and automatically stake them for mining credits.
Generated: DETERMINISTIC_85d6ee56c510a0f2
Batch ID: 20250612_151648
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

// Import standard OpenZeppelin contracts for safety and security
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the BTCMTX token contract
contract BTCMTX is IERC20, Ownable {
    using SafeERC20 for IERC20;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, string paymentMethod);
    event TokensStaked(address indexed staker, uint256 amount);

    // Token details
    string public constant name = "BTCMTX Token";
    string public constant symbol = "BTCMTX";
    uint8 public constant decimals = 18;

    // Token supply and balances
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;

    // Allowed allowances for transfer
    mapping(address => mapping(address => uint256)) private _allowances;

    // Staking tracking
    mapping(address => uint256) public stakedTokens;

    // Token purchase price in ETH (for simplicity)
    uint256 public tokenPriceInETH = 0.01 ether;

    // Supported payment tokens
    IERC20 public USDT;
    IERC20 public BNB;

    // Constructor to initialize the token and supported tokens
    constructor(address _usdt, address _bnb) {
        USDT = IERC20(_usdt);
        BNB = IERC20(_bnb);
    }

    // Function to return the total supply
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Function to return the balance of an account
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Function to purchase BTCMTX tokens
    function purchaseTokens(uint256 _amount, string calldata _paymentMethod) external payable {
        // Validate payment method
        require(keccak256(abi.encodePacked(_paymentMethod)) == keccak256("ETH") ||
                keccak256(abi.encodePacked(_paymentMethod)) == keccak256("USDT") ||
                keccak256(abi.encodePacked(_paymentMethod)) == keccak256("BNB"),
                "Invalid payment method");

        uint256 totalPrice = _amount * tokenPriceInETH;

        // Handle payment based on method
        if (keccak256(abi.encodePacked(_paymentMethod)) == keccak256("ETH")) {
            require(msg.value == totalPrice, "Incorrect ETH amount sent");
        } else if (keccak256(abi.encodePacked(_paymentMethod)) == keccak256("USDT")) {
            USDT.safeTransferFrom(msg.sender, address(this), totalPrice);
        } else { // BNB payment
            BNB.safeTransferFrom(msg.sender, address(this), totalPrice);
        }

        // Mint tokens to buyer
        _mint(msg.sender, _amount);

        emit TokensPurchased(msg.sender, _amount, _paymentMethod);
        stakeTokens(_amount);
    }

    // Internal function to mint tokens
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to the zero address");

        _totalSupply += amount;
        _balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    // Function to stake tokens for mining credits
    function stakeTokens(uint256 _amount) internal {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(_balances[msg.sender] >= _amount, "Insufficient token balance to stake");

        // Transfer tokens from user to contract
        _balances[msg.sender] -= _amount;
        stakedTokens[msg.sender] += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    // Allow the contract to receive ETH payments
    receive() external payable {}

    // Implement ERC20 functions
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "Transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);
        return true;
    }

    // Internal function to handle transfers
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    // Internal function to set allowances
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
