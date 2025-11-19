"""
Generated Code Metadata:
========================
Original URL: https://a292d5c1.docs-62t.pages.dev
Prompt: Explain how Código ensures the security of generated smart contracts and provide an example of the testing process.
Generated: DETERMINISTIC_5cff337f403765d8
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's an example of a secure smart contract in Solidity with test cases using Hardhat and Chai. The example demonstrates security best practices and testing methodology:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SecurePaymentContract
 * @dev Implements secure payment functionality with withdrawal pattern,
 * access control, and protection against common vulnerabilities.
 */
contract SecurePaymentContract {
    address payable public owner;
    mapping(address => uint256) private _balances;
    bool private _locked;

    // Events for transaction logging
    event Deposit(address indexed sender, uint256 amount);
    event Withdrawal(address indexed receiver, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier nonReentrant() {
        require(!_locked, "Reentrant call detected");
        _locked = true;
        _;
        _locked = false;
    }

    constructor() {
        owner = payable(msg.sender);
    }

    /**
     * @dev Deposit funds into contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        _balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds from contract (protected against reentrancy)
     * @param amount The amount to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        
        _balances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Emergency stop function for owner
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        owner.transfer(balance);
    }

    /**
     * @dev Get user's balance
     * @param user The address to query
     */
    function balanceOf(address user) external view returns (uint256) {
        return _balances[user];
    }
}
```

Here are the corresponding tests:

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("SecurePaymentContract", function () {
  let contract;
  let owner, user1, user2, attacker;

  beforeEach(async function () {
    [owner, user1, user2, attacker] = await ethers.getSigners();
    
    const SecurePaymentContract = await ethers.getContractFactory("SecurePaymentContract");
    contract = await SecurePaymentContract.deploy();
    await contract.deployed();
  });

  describe("Deposit functionality", function () {
    it("Should accept deposits and update balances", async function () {
      const depositAmount = ethers.utils.parseEther("1.0");
      await contract.connect(user1).deposit({ value: depositAmount });
      
      expect(await contract.balanceOf(user1.address)).to.equal(depositAmount);
    });

    it("Should reject zero value deposits", async function () {
      await expect(
        contract.connect(user1).deposit({ value: 0 })
      ).to.be.revertedWith("Deposit amount must be greater than 0");
    });
  });

  describe("Withdrawal functionality", function () {
    const depositAmount = ethers.utils.parseEther("1.0");

    beforeEach(async function () {
      await contract.connect(user1).deposit({ value: depositAmount });
    });

    it("Should allow valid withdrawals", async function () {
      const initialBalance = await ethers.provider.getBalance(user1.address);
      
      const tx = await contract.connect(user1).withdraw(depositAmount);
      const receipt = await tx.wait();
      const gasUsed = receipt.gasUsed.mul(tx.gasPrice);
      
      const finalBalance = await ethers.provider.getBalance(user1.address);
      expect(finalBalance).to.be.closeTo(
        initialBalance.add(depositAmount).sub(gasUsed),
        ethers.utils.parseEther("0.01")
      );
    });

    it("Should prevent overwithdrawal", async function () {
      await expect(
        contract.connect(user1).withdraw(depositAmount.add(1))
      ).to.be.revertedWith("Insufficient balance");
    });

    it("Should prevent reentrancy attacks", async function () {
      // Deploy malicious contract
      const ReentrancyAttacker = await ethers.getContractFactory("ReentrancyAttacker");
      const attackerContract = await ReentrancyAttacker.deploy(contract.address);
      await attackerContract.deployed();
      
      // Deposit funds to attacker contract
      await attacker.connect(attacker).sendTransaction({
        to: attackerContract.address,
        value: depositAmount
      });
      
      // Perform attack
      await expect(
        attackerContract.connect(attacker).attack()
      ).to.be.revertedWith("Transfer failed");
    });
  });

  describe("Access control", function () {
    it("Should allow only owner to emergency withdraw", async function () {
      await expect(
        contract.connect(user1).emergencyWithdraw()
      ).to.be.revertedWith("Caller is not the owner");
    });

    it("Should allow owner to emergency withdraw", async function () {
      const depositAmount = ethers.utils.parseEther("1.0");
      await contract.connect(user1).deposit({ value: depositAmount });
      
      const ownerBalanceBefore = await ethers.provider.getBalance(owner.address);
      const tx = await contract.connect(owner).emergencyWithdraw();
      const receipt = await tx.wait();
      const gasUsed = receipt.gasUsed.mul(tx.gasPrice);
      
      const ownerBalanceAfter = await ethers.provider.getBalance(owner.address);
      expect(ownerBalanceAfter).to.be.closeTo(
        ownerBalanceBefore.add(depositAmount).sub(gasUsed),
        ethers.utils.parseEther("0.01")
      );
    });
  });
});
```

And the malicious contract for reentrancy testing:

```solidty
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface ISecurePaymentContract {
    function deposit() external payable;
    function withdraw(uint256 amount) external;
}

contract ReentrancyAttacker {
    ISecurePaymentContract public victim;
    uint256 public attackAmount;

    constructor(address _victim) {
        victim = ISecurePaymentContract(_victim);
    }

    receive() external payable {
        if (address(victim).balance >= attackAmount) {
            victim.withdraw(attackAmount);
        }
    }

    function attack() external payable {
        require(msg.value > 0, "Need funds to attack");
        attackAmount = msg.value;
        
        victim.deposit{value: attackAmount}();
        victim.withdraw(attackAmount);
    }
}
```
