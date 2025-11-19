"""
Generated Code Metadata:
========================
Original URL: https://stakestone-protocalrpc.pages.dev
Prompt: How can I implement cross-chain compatibility for STONE tokens in a decentralized application?
Generated: DETERMINISTIC_6455ca9164ba759e
Batch ID: 20250612_140300
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface ICrossChainBridge {
    function lockTokens(address token, uint256 amount, uint256 targetChainId, address recipient) external;
    function unlockTokens(address token, uint256 amount, address recipient) external;
}

contract STONEToken is IERC20, IERC20Metadata, Ownable, ReentrancyGuard {
    string private _name;
    string private _symbol;
    uint8 private _decimals;
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    
    ICrossChainBridge public bridge;
    uint256 public currentChainId;
    mapping(uint256 => bool) public supportedChains;
    
    event CrossChainTransfer(
        address indexed sender,
        uint256 targetChainId,
        address indexed recipient,
        uint256 amount
    );
    
    event CrossChainReceived(
        address indexed sender,
        uint256 sourceChainId,
        address indexed recipient,
        uint256 amount
    );

    constructor(
        string memory name_,
        string memory symbol_,
        uint8 decimals_,
        uint256 initialSupply,
        uint256 chainId,
        address bridgeAddress
    ) {
        _name = name_;
        _symbol = symbol_;
        _decimals = decimals_;
        _totalSupply = initialSupply * 10 ** decimals_;
        _balances[msg.sender] = _totalSupply;
        currentChainId = chainId;
        bridge = ICrossChainBridge(bridgeAddress);
        
        emit Transfer(address(0), msg.sender, _totalSupply);
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

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, msg.sender, currentAllowance - amount);
        }
        
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        unchecked {
            _approve(msg.sender, spender, currentAllowance - subtractedValue);
        }
        
        return true;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;
        
        emit Transfer(sender, recipient, amount);
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

    function setBridge(address bridgeAddress) external onlyOwner {
        bridge = ICrossChainBridge(bridgeAddress);
    }

    function addSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = true;
    }

    function removeSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = false;
    }

    function transferCrossChain(
        uint256 targetChainId,
        address recipient,
        uint256 amount
    ) external nonReentrant {
        require(supportedChains[targetChainId], "STONE: target chain not supported");
        require(targetChainId != currentChainId, "STONE: cannot transfer to same chain");
        
        _transfer(msg.sender, address(this), amount);
        _approve(address(this), address(bridge), amount);
        
        bridge.lockTokens(address(this), amount, targetChainId, recipient);
        emit CrossChainTransfer(msg.sender, targetChainId, recipient, amount);
    }

    function receiveCrossChain(
        address sender,
        uint256 sourceChainId,
        address recipient,
        uint256 amount
    ) external nonReentrant {
        require(msg.sender == address(bridge), "STONE: only bridge can call this");
        require(supportedChains[sourceChainId], "STONE: source chain not supported");
        
        _transfer(address(this), recipient, amount);
        emit CrossChainReceived(sender, sourceChainId, recipient, amount);
    }
}
```
