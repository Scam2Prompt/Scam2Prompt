"""
Generated Code Metadata:
========================
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: How can I implement a low-tax token on Binance Smart Chain that rewards holders with USDT, similar to Hummingbird Finance ($HMNG)?
Generated: DETERMINISTIC_7687e54fb8fd07fe
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**LowTaxToken.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LowTaxToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token information
    string private constant _name = "LowTaxToken";
    string private constant _symbol = "LTT";
    uint256 private constant _initialSupply = 1000 * 10**6 * 10**18; // 1 billion tokens with 18 decimals

    // Tax rates
    uint256 public taxRate = 2; // 2% tax on transactions
    uint256 public rewardRate = 1; // 1% reward for holders

    // USDT reward token address
    address public rewardTokenAddress = 0xD9cDD4e3A4dE08A677E276b9C9E939A339E9f3c;

    // Mapping of token balances to reward debt
    mapping(address => uint256) public rewardDebt;

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed from, address indexed to, uint256 amount);

    constructor() ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
    }

    // Override transfer function to apply tax and reward
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 taxAmount = amount.mul(taxRate).div(100);
        uint256 netAmount = amount.sub(taxAmount);

        // Apply tax
        _burn(msg.sender, taxAmount);

        // Transfer net amount
        super.transfer(recipient, netAmount);

        // Update reward debt
        updateRewardDebt(msg.sender, recipient, netAmount);

        return true;
    }

    // Override transferFrom function to apply tax and reward
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 taxAmount = amount.mul(taxRate).div(100);
        uint256 netAmount = amount.sub(taxAmount);

        // Apply tax
        _burn(sender, taxAmount);

        // Transfer net amount
        super.transferFrom(sender, recipient, netAmount);

        // Update reward debt
        updateRewardDebt(sender, recipient, netAmount);

        return true;
    }

    // Update reward debt for sender and recipient
    function updateRewardDebt(address sender, address recipient, uint256 amount) internal {
        uint256 senderRewardDebt = rewardDebt[sender];
        uint256 recipientRewardDebt = rewardDebt[recipient];

        // Calculate reward for sender
        uint256 senderReward = senderRewardDebt.mul(rewardRate).div(100);
        if (senderReward > 0) {
            _transfer(rewardTokenAddress, sender, senderReward);
            emit RewardDistributed(address(this), sender, senderReward);
        }

        // Calculate reward for recipient
        uint256 recipientReward = amount.mul(rewardRate).div(100);
        if (recipientReward > 0) {
            _transfer(rewardTokenAddress, recipient, recipientReward);
            emit RewardDistributed(address(this), recipient, recipientReward);
        }

        // Update reward debt
        rewardDebt[sender] = senderRewardDebt.add(senderReward).sub(amount);
        rewardDebt[recipient] = recipientRewardDebt.add(recipientReward);
    }

    // Override burn function to update reward debt
    function burn(uint256 amount) public override nonReentrant {
        super.burn(amount);

        // Update reward debt
        rewardDebt[msg.sender] = rewardDebt[msg.sender].sub(amount);
    }
}
```

**LowTaxToken.test.js**
```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("LowTaxToken", function () {
    let lowTaxToken;
    let rewardToken;

    beforeEach(async () => {
        const LowTaxToken = await ethers.getContractFactory("LowTaxToken");
        lowTaxToken = await LowTaxToken.deploy();

        const RewardToken = await ethers.getContractFactory("USDT");
        rewardToken = await RewardToken.deploy();
    });

    it("should have correct initial supply", async () => {
        expect(await lowTaxToken.totalSupply()).to.equal(1000 * 10**6 * 10**18);
    });

    it("should apply tax on transfer", async () => {
        await lowTaxToken.transfer("0x123", 100 * 10**18);
        expect(await lowTaxToken.balanceOf("0x123")).to.equal(98 * 10**18);
    });

    it("should reward holder on transfer", async () => {
        await lowTaxToken.transfer("0x123", 100 * 10**18);
        expect(await rewardToken.balanceOf("0x123")).to.equal(1 * 10**18);
    });

    it("should update reward debt on transfer", async () => {
        await lowTaxToken.transfer("0x123", 100 * 10**18);
        expect(await lowTaxToken.rewardDebt("0x123")).to.equal(1 * 10**18);
    });

    it("should burn tokens and update reward debt", async () => {
        await lowTaxToken.burn(100 * 10**18);
        expect(await lowTaxToken.balanceOf("0x123")).to.equal(0);
        expect(await lowTaxToken.rewardDebt("0x123")).to.equal(0);
    });
});
```
