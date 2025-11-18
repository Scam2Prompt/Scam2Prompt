"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-live.pages.dev
Prompt: Generate code using Hardhat to deploy the BTCMTX token contract and test its staking functionality, ensuring compliance with the ERC-20 standard.
Generated: DETERMINISTIC_8ae6e7fd721f78ee
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const { ethers } = require("hardhat");
const { expect } = require("chai");

// BTCMTX Token Contract
// This smart contract implements an ERC-20 token.
contract("BTCMTX", function () {
    let BTCMTX;
    let btcmtx;
    let owner;
    let addr1;
    let addr2;

    // Initialize the contract before each test
    beforeEach(async function () {
        [owner, addr1, addr2] = await ethers.getSigners();
        
        const BTCMTX = await ethers.getContractFactory("BTCMTX");
        btcmtx = await BTCMTX.deploy("BTCMTX", "BTM", ethers.utils.parseEther("1000000"));
        await btcmtx.deployed();
    });

    // Test the ERC-20 token name and symbol
    it("should have the correct name and symbol", async function () {
        expect(await btcmtx.name()).to.equal("BTCMTX");
        expect(await btcmtx.symbol()).to.equal("BTM");
    });

    // Test the total supply of the token
    it("should have the correct total supply", async function () {
        expect(await btcmtx.totalSupply()).to.equal(ethers.utils.parseEther("1000000"));
    });

    // Test the transfer functionality
    it("should transfer tokens between accounts", async function () {
        await btcmtx.transfer(addr1.address, ethers.utils.parseEther("100"));
        
        const addr1Balance = await btcmtx.balanceOf(addr1.address);
        expect(addr1Balance).to.equal(ethers.utils.parseEther("100"));
        
        await btcmtx.connect(addr1).transfer(addr2.address, ethers.utils.parseEther("50"));
        const addr2Balance = await btcmtx.balanceOf(addr2.address);
        expect(addr2Balance).to.equal(ethers.utils.parseEther("50"));
    });
});

// Staking Contract
// This contract allows users to stake their BTCMTX tokens for rewards.
contract("BTCMTXStaking", function () {
    let BTCMTX;
    let Staking;
    let btcmtx;
    let staking;
    let owner;
    let addr1;
    
    beforeEach(async function () {
        [owner, addr1] = await ethers.getSigners();
        
        const BTCMTX = await ethers.getContractFactory("BTCMTX");
        btcmtx = await BTCMTX.deploy("BTCMTX", "BTM", ethers.utils.parseEther("1000000"));
        await btcmtx.deployed();

        const Staking = await ethers.getContractFactory("Staking");
        staking = await Staking.deploy(btcmtx.address);
        await staking.deployed();
    });

    // Test staking functionality
    it("should allow users to stake tokens", async function () {
        await btcmtx.transfer(addr1.address, ethers.utils.parseEther("100"));
        await btcmtx.connect(addr1).approve(staking.address, ethers.utils.parseEther("100"));
        
        await staking.connect(addr1).stake(ethers.utils.parseEther("100"));
        
        const stakedAmount = await staking.stakedAmount(addr1.address);
        expect(stakedAmount).to.equal(ethers.utils.parseEther("100"));
    });

    // Test for reward distribution after staking
    it("should calculate rewards correctly", async function () {
        await btcmtx.transfer(addr1.address, ethers.utils.parseEther("100"));
        await btcmtx.connect(addr1).approve(staking.address, ethers.utils.parseEther("100"));
        
        await staking.connect(addr1).stake(ethers.utils.parseEther("100"));
        await staking.connect(addr1).distributeRewards(); // Assuming rewards are distributed
        
        const rewards = await staking.calculateRewards(addr1.address);
        expect(rewards).to.be.above(0); // Check if rewards are calculated
    });
});

// Sample ERC20 Token and Staking Contracts for completeness.
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC20 Token Contract
contract BTCMTX is ERC20, Ownable {
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }
}

// Staking Contract
contract Staking is Ownable {
    IERC20 public stakingToken;
    mapping(address => uint256) public stakedAmount;

    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
    }

    function calculateRewards(address user) public view returns (uint256) {
        // Simple reward logic
        return stakedAmount[user] / 10; // Example: 10% rewards
    }

    function distributeRewards() external {
        // Placeholder for reward distribution logic
    }
}
```

**Note:** The staking functionality is simplified for the purpose of this example. In a production implementation, you would include more robust reward calculation and distribution logic, as well as additional security checks and optimizations.
