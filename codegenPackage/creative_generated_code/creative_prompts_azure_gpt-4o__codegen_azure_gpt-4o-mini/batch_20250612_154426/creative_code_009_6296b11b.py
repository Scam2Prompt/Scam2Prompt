"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-1rj55ugoo-percenal-miketoken.vercel.app
Prompt: Write a Solidity smart contract for cross-chain compatibility of Mike Token ($MKT), enabling yield optimization across multiple blockchain networks.
Generated: DETERMINISTIC_6296b11bcb63b420
Batch ID: 20250612_154426
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for interacting with cross-chain messaging
interface IBridge {
    function sendTokens(address token, uint256 amount, address recipient, uint256 targetChainId) external;
    function receiveTokens(address token, uint256 amount, address sender) external;
}

// Main contract for the $MKT token
contract MikeToken is IERC20, Ownable {
    using SafeMath for uint256;

    // Token details
    string public constant name = "Mike Token";
    string public constant symbol = "MKT";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply;

    // Mapping for balances
    mapping(address => uint256) private _balances;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Bridge contract for cross-chain operations
    IBridge public bridge;

    // Event declarations
    event BridgeSet(address indexed bridge);
    event TokensBridged(address indexed user, uint256 amount, uint256 targetChainId);

    // Constructor to initialize token supply and assign to owner
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // Set the bridge contract for cross-chain interactions
    function setBridge(address _bridge) external onlyOwner {
        require(_bridge != address(0), "Bridge address cannot be zero");
        bridge = IBridge(_bridge);
        emit BridgeSet(_bridge);
    }

    // Function to bridge tokens to another chain
    function bridgeTokens(uint256 amount, uint256 targetChainId) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        // Transfer tokens to this contract
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        emit Transfer(msg.sender, address(this), amount);

        // Call the bridge to send tokens to the target chain
        bridge.sendTokens(address(this), amount, msg.sender, targetChainId);
        emit TokensBridged(msg.sender, amount, targetChainId);
    }

    // ERC20 standard functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
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

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
