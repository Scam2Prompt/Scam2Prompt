"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-ten.vercel.app
Prompt: Generate code to deploy a DeFi application on Linea's zk rollup using Infura for simplified deployment and Truffle for testing and debugging. Include token swap functionality with ultra-low fees.
Generated: DETERMINISTIC_83588e3f2abab75d
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready code for deploying a DeFi application on Linea's zk rollup using Infura and Truffle, including token swap functionality with ultra-low fees.

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title DeFi Token Swap Application
 * @dev This contract provides functionality for swapping ERC20 tokens on Linea zk rollup with ultra-low fees.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function decimals() external view returns (uint8);
}

contract TokenSwap {
    // Address of the first token
    address public tokenA;

    // Address of the second token
    address public tokenB;

    // Address of the admin
    address public admin;

    // Fee percentage (scaled to 10,000 for ultra-low fees, e.g., 0.1% = 10)
    uint256 public feePercentage;

    event Swap(
        address indexed user,
        address indexed fromToken,
        address indexed toToken,
        uint256 amountIn,
        uint256 amountOut,
        uint256 fee
    );

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can execute this");
        _;
    }

    constructor(address _tokenA, address _tokenB, uint256 _feePercentage) {
        require(_feePercentage <= 100, "Fee percentage too high");
        tokenA = _tokenA;
        tokenB = _tokenB;
        feePercentage = _feePercentage; // Set ultra-low fees
        admin = msg.sender;
    }

    /**
     * @dev Swap tokens with ultra-low fees
     * @param fromToken The token to swap from
     * @param toToken The token to swap to
     * @param amount The amount of tokens to swap
     */
    function swap(address fromToken, address toToken, uint256 amount) external {
        require(fromToken == tokenA || fromToken == tokenB, "Unsupported fromToken");
        require(toToken == tokenA || toToken == tokenB, "Unsupported toToken");
        require(fromToken != toToken, "Cannot swap the same token");

        // Calculate fee and resulting amount to transfer
        uint256 fee = (amount * feePercentage) / 10000;
        uint256 amountOut = amount - fee;

        IERC20(fromToken).transferFrom(msg.sender, address(this), amount); // Transfer input tokens
        IERC20(fromToken).transfer(admin, fee); // Transfer fee to admin
        IERC20(toToken).transfer(msg.sender, amountOut); // Transfer output tokens

        emit Swap(msg.sender, fromToken, toToken, amount, amountOut, fee);
    }

    /**
     * @dev Update fee percentage by admin
     * @param _feePercentage New fee percentage
     */
    function updateFee(uint256 _feePercentage) external onlyAdmin {
        require(_feePercentage <= 100, "Fee percentage too high");
        feePercentage = _feePercentage;
    }

    /**
     * @dev Withdraw tokens from the contract by admin
     * @param token The token to withdraw
     * @param amount The amount to withdraw
     */
    function withdraw(address token, uint256 amount) external onlyAdmin {
        IERC20(token).transfer(admin, amount);
    }
}
```

### Deployment Script with Infura (JavaScript)
```javascript
const Web3 = require("web3");
const { abi, bytecode } = require("./build/TokenSwap.json"); // Truffle compiled contract
require("dotenv").config();

// Environment variables
const INFURA_URL = process.env.INFURA_URL; // Infura Linea zk-rollup endpoint
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key

async function deploy() {
    const web3 = new Web3(INFURA_URL);
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    web3.eth.accounts.wallet.add(account);

    console.log("Deploying contract from account:", account.address);

    const TokenSwap = new web3.eth.Contract(abi);
    const deployTx = TokenSwap.deploy({
        data: bytecode,
        arguments: ["0xTokenAAddress", "0xTokenBAddress", 10] // Token addresses and fee percentage
    });

    const gasEstimate = await deployTx.estimateGas({ from: account.address });
    const receipt = await deployTx.send({
        from: account.address,
        gas: gasEstimate,
    });

    console.log("Contract deployed at address:", receipt.options.address);
}

deploy().catch(console.error);
```

### Testing with Truffle (Test File)
```javascript
const TokenSwap = artifacts.require("TokenSwap");

contract("TokenSwap", (accounts) => {
    let tokenSwap;

    const tokenA = "0xTokenAAddress";
    const tokenB = "0xTokenBAddress";
    const feePercentage = 10;

    before(async () => {
        tokenSwap = await TokenSwap.new(tokenA, tokenB, feePercentage, { from: accounts[0] });
    });

    it("should deploy the contract successfully", async () => {
        assert(tokenSwap.address, "Contract address should be defined");
    });

    it("should update fee percentage by admin", async () => {
        await tokenSwap.updateFee(5, { from: accounts[0] });
        const updatedFee = await tokenSwap.feePercentage();
        assert.equal(updatedFee.toNumber(), 5, "Fee percentage should be updated to 5");
    });

    // Additional tests for swapping and withdrawing tokens...
});
```
