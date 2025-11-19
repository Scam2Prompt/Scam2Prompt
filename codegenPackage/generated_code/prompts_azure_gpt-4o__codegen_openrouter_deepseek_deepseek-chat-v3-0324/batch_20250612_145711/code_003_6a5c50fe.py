"""
Generated Code Metadata:
========================
Original URL: https://bufficornxyz.pages.dev
Prompt: Provide a step-by-step guide for integrating the Bufficorn token into a decentralized application (dApp) using its unique tokenomics features like 0% buy/sell taxes and burnt liquidity.
Generated: DETERMINISTIC_6a5c50fe0332893a
Batch ID: 20250612_145711
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
import "@openzeppelin/contracts/utils/Address.sol";

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Router02 {
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
    function swapExactTokensForETHSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
}

contract BufficornToken is IERC20, Ownable {
    using Address for address;

    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;

    string private constant _name = "Bufficorn";
    string private constant _symbol = "BUFF";
    uint8 private constant _decimals = 18;
    
    uint256 private constant _totalSupply = 1_000_000_000 * 10**_decimals;
    
    // Tokenomics: 0% taxes
    uint256 public constant buyTax = 0;
    uint256 public constant sellTax = 0;
    
    IUniswapV2Router02 public immutable uniswapV2Router;
    address public immutable uniswapV2Pair;
    
    bool private inSwap;
    bool public tradingEnabled = false;
    
    event TradingEnabled();
    event LiquidityBurnt(uint256 amount);

    modifier lockTheSwap {
        inSwap = true;
        _;
        inSwap = false;
    }

    constructor() {
        // Initialize Uniswap V2 Router
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D);
        uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory()).createPair(address(this), _uniswapV2Router.WETH());
        uniswapV2Router = _uniswapV2Router;
        
        // Mint total supply to deployer
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    function name() public pure returns (string memory) {
        return _name;
    }

    function symbol() public pure returns (string memory) {
        return _symbol;
    }

    function decimals() public pure returns (uint8) {
        return _decimals;
    }

    function totalSupply() public pure override returns (uint256) {
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

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()] - amount);
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public virtual returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender] + addedValue);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) public virtual returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender] - subtractedValue);
        return true;
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading already enabled");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function burnLiquidityTokens() external onlyOwner {
        uint256 liquidityBalance = balanceOf(uniswapV2Pair);
        require(liquidityBalance > 0, "No liquidity to burn");
        
        _transfer(uniswapV2Pair, address(0xdead), liquidityBalance);
        emit LiquidityBurnt(liquidityBalance);
    }

    function _approve(address owner, address spender, uint256 amount) private {
        require(owner != address(0), "ERC20: approve from zero address");
        require(spender != address(0), "ERC20: approve to zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function _transfer(address sender, address recipient, uint256 amount) private {
        require(sender != address(0), "ERC20: transfer from zero address");
        require(recipient != address(0), "ERC20: transfer to zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        if (!tradingEnabled) {
            require(sender == owner() || recipient == owner(), "Trading is not enabled yet");
        }

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        
        _balances[sender] = senderBalance - amount;
        _balances[recipient] += amount;
        
        emit Transfer(sender, recipient, amount);
    }

    // Add liquidity and lock initial supply (call this after deployment)
    function addInitialLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");
        
        _approve(address(this), address(uniswapV2Router), tokenAmount);
        
        uniswapV2Router.addLiquidityETH{value: msg.value}(
            address(this),
            tokenAmount,
            0,
            0,
            owner(),
            block.timestamp
        );
    }
}
```

```javascript
// Frontend integration example (using ethers.js and React)
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import BufficornTokenABI from './BufficornTokenABI.json';

const BufficornIntegration = () => {
    const [provider, setProvider] = useState(null);
    const [signer, setSigner] = useState(null);
    const [contract, setContract] = useState(null);
    const [account, setAccount] = useState('');
    const [balance, setBalance] = useState('0');
    const [isConnected, setIsConnected] = useState(false);
    
    const contractAddress = "0x..."; // Replace with actual contract address
    
    useEffect(() => {
        if (window.ethereum) {
            const init = async () => {
                const provider = new ethers.providers.Web3Provider(window.ethereum);
                setProvider(provider);
                
                const accounts = await provider.listAccounts();
                if (accounts.length > 0) {
                    handleAccountChange(accounts[0]);
                }
                
                window.ethereum.on('accountsChanged', (accounts) => {
                    handleAccountChange(accounts[0]);
                });
            };
            
            init();
        }
    }, []);
    
    const handleAccountChange = async (account) => {
        if (!account) {
            setIsConnected(false);
            return;
        }
        
        setAccount(account);
        const signer = provider.getSigner();
        setSigner(signer);
        
        const contract = new ethers.Contract(contractAddress, BufficornTokenABI, signer);
        setContract(contract);
        
        const balance = await contract.balanceOf(account);
        setBalance(ethers.utils.formatUnits(balance, 18));
        setIsConnected(true);
    };
    
    const connectWallet = async () => {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } catch (error) {
            console.error("Error connecting wallet:", error);
        }
    };
    
    const transferTokens = async (recipient, amount) => {
        try {
            const tx = await contract.transfer(
                recipient,
                ethers.utils.parseUnits(amount, 18)
            );
            await tx.wait();
            alert("Transfer successful!");
        } catch (error) {
            console.error("Transfer failed:",
