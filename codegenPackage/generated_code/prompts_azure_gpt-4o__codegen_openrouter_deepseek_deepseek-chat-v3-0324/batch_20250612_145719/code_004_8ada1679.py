"""
Generated Code Metadata:
========================
Original URL: https://multichain-sol.vercel.app
Prompt: Create a step-by-step guide for deploying a smart contract that utilizes Multichain's MPC-based cross-chain bridging mechanism.
Generated: DETERMINISTIC_8ada1679845ffb98
Batch ID: 20250612_145719
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
 * @title CrossChainBridge
 * @dev A smart contract for cross-chain token transfers using Multichain's MPC bridge
 */
contract CrossChainBridge is Ownable, ReentrancyGuard {
    // Token to be bridged
    IERC20 public token;
    
    // Bridge fee percentage (1 = 0.01%)
    uint256 public bridgeFee;
    
    // Minimum and maximum bridge amounts
    uint256 public minBridgeAmount;
    uint256 public maxBridgeAmount;
    
    // Supported destination chains and their IDs
    mapping(string => uint256) public supportedChains;
    
    // Events
    event BridgeInitiated(
        address indexed sender,
        uint256 amount,
        string destinationChain,
        uint256 timestamp
    );
    
    event BridgeCompleted(
        address indexed recipient,
        uint256 amount,
        string sourceChain,
        uint256 timestamp
    );
    
    event FeesWithdrawn(
        address indexed owner,
        uint256 amount,
        uint256 timestamp
    );
    
    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token to bridge
     * @param _bridgeFee Bridge fee percentage (1 = 0.01%)
     * @param _minBridgeAmount Minimum bridge amount
     * @param _maxBridgeAmount Maximum bridge amount
     */
    constructor(
        address _token,
        uint256 _bridgeFee,
        uint256 _minBridgeAmount,
        uint256 _maxBridgeAmount
    ) {
        require(_token != address(0), "Invalid token address");
        require(_bridgeFee <= 10000, "Fee cannot exceed 100%");
        require(_minBridgeAmount < _maxBridgeAmount, "Invalid amount range");
        
        token = IERC20(_token);
        bridgeFee = _bridgeFee;
        minBridgeAmount = _minBridgeAmount;
        maxBridgeAmount = _maxBridgeAmount;
        
        // Initialize supported chains (example values)
        supportedChains["Ethereum"] = 1;
        supportedChains["Binance"] = 56;
        supportedChains["Polygon"] = 137;
    }
    
    /**
     * @dev Initiate a cross-chain transfer
     * @param amount Amount of tokens to bridge
     * @param destinationChain Name of the destination chain
     */
    function initiateBridge(
        uint256 amount,
        string memory destinationChain
    ) external nonReentrant {
        require(amount >= minBridgeAmount, "Amount below minimum");
        require(amount <= maxBridgeAmount, "Amount exceeds maximum");
        require(supportedChains[destinationChain] != 0, "Chain not supported");
        
        uint256 fee = (amount * bridgeFee) / 10000;
        uint256 amountAfterFee = amount - fee;
        
        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        // In a real implementation, this would trigger the Multichain MPC bridge
        // For this example, we just emit an event
        emit BridgeInitiated(
            msg.sender,
            amountAfterFee,
            destinationChain,
            block.timestamp
        );
    }
    
    /**
     * @dev Complete a cross-chain transfer (to be called by MPC nodes)
     * @param recipient Address to receive tokens
     * @param amount Amount of tokens to receive
     * @param sourceChain Name of the source chain
     */
    function completeBridge(
        address recipient,
        uint256 amount,
        string memory sourceChain
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient");
        require(amount > 0, "Invalid amount");
        require(supportedChains[sourceChain] != 0, "Chain not supported");
        
        require(
            token.transfer(recipient, amount),
            "Transfer failed"
        );
        
        emit BridgeCompleted(
            recipient,
            amount,
            sourceChain,
            block.timestamp
        );
    }
    
    /**
     * @dev Add or update a supported chain
     * @param chainName Name of the chain
     * @param chainId Chain ID
     */
    function updateSupportedChain(
        string memory chainName,
        uint256 chainId
    ) external onlyOwner {
        require(chainId != 0, "Invalid chain ID");
        supportedChains[chainName] = chainId;
    }
    
    /**
     * @dev Update bridge fee
     * @param newFee New bridge fee percentage (1 = 0.01%)
     */
    function updateBridgeFee(uint256 newFee) external onlyOwner {
        require(newFee <= 10000, "Fee cannot exceed 100%");
        bridgeFee = newFee;
    }
    
    /**
     * @dev Update bridge amount limits
     * @param newMin Minimum bridge amount
     * @param newMax Maximum bridge amount
     */
    function updateBridgeLimits(
        uint256 newMin,
        uint256 newMax
    ) external onlyOwner {
        require(newMin < newMax, "Invalid amount range");
        minBridgeAmount = newMin;
        maxBridgeAmount = newMax;
    }
    
    /**
     * @dev Withdraw accumulated fees
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No fees to withdraw");
        
        require(
            token.transfer(owner(), balance),
            "Transfer failed"
        );
        
        emit FeesWithdrawn(owner(), balance, block.timestamp);
    }
    
    /**
     * @dev Emergency withdraw tokens (only for emergencies)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        require(
            token.transfer(owner(), balance),
            "Transfer failed"
        );
    }
}
```

```javascript
// Deployment script (using Hardhat)
const { ethers } = require("hardhat");

async function main() {
  // Contract parameters
  const tokenAddress = "0xYourTokenAddress"; // Replace with actual token address
  const bridgeFee = 10; // 0.1% fee
  const minBridgeAmount = ethers.utils.parseUnits("10", 18); // 10 tokens
  const maxBridgeAmount = ethers.utils.parseUnits("10000", 18); // 10,000 tokens

  // Deploy the contract
  const CrossChainBridge = await ethers.getContractFactory("CrossChainBridge");
  const bridge = await CrossChainBridge.deploy(
    tokenAddress,
    bridgeFee,
    minBridgeAmount,
    maxBridgeAmount
  );

  await bridge.deployed();

  console.log("CrossChainBridge deployed to:", bridge.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Test script (using Hardhat)
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CrossChainBridge", function () {
  let owner, user, token, bridge;
  const initialSupply = ethers.utils.parseUnits("1000000", 18);

  beforeEach(async function () {
    [owner, user] = await ethers.getSigners();

    // Deploy test token
    const Token = await ethers.getContractFactory("ERC20Mock");
    token = await Token.deploy("Test Token", "TEST", owner.address, initialSupply);
    await token.deployed();

    // Deploy bridge
    const Bridge = await ethers.getContractFactory("CrossChainBridge");
    bridge = await Bridge.deploy(
      token.address,
      10, // 0.1% fee
      ethers.utils.parseUnits("10", 18), // min 10 tokens
      ethers.utils.parseUnits("10000", 18) // max 10,000 tokens
    );
    await bridge.deployed();

    // Approve bridge to spend tokens
    await token.connect(user).approve(
      bridge.address,
      ethers.utils.parseUnits("10000", 18)
    );
  });

  it("Should deploy with correct parameters", async function () {
    expect(await bridge.token()).to.equal(token.address);
    expect(await bridge.bridgeFee()).to.equal(10);
    expect(await bridge.minBridgeAmount()).to.equal(ethers.utils.parseUnits("10", 18));
    expect(await bridge.maxBridgeAmount()).to.equal(ethers.utils.parseUnits("10000", 18));
  });

  it("Should initiate bridge transfer", async function () {
    const amount = ethers.utils.parseUnits("100", 18);
    await expect(bridge.connect(user).initiateBridge(amount, "Ethereum"))
      .to.emit(bridge, "BridgeInitiated")
      .withArgs(user.address, amount.sub(amount.mul(10).div(10000)), "E
