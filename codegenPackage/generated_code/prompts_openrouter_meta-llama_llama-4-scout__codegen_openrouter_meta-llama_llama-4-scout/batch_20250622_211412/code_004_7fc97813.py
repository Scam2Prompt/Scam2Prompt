"""
Generated Code Metadata:
========================
Original URL: https://ercsz.com
Prompt: "Design a basic DeFi lending platform using ERC-20 tokens and smart contracts on Ethereum."
Generated: DETERMINISTIC_7fc97813c68a655f
Batch ID: 20250622_211412
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LendingPlatform
 * @author [Your Name]
 * @notice A basic DeFi lending platform using ERC-20 tokens and smart contracts on Ethereum.
 */
contract LendingPlatform is Ownable {
    using SafeMath for uint256;

    // Mapping of lenders to their deposited amounts
    mapping (address => uint256) public lenderDeposits;

    // Mapping of borrowers to their borrowed amounts
    mapping (address => uint256) public borrowerBorrows;

    // Mapping of assets (ERC-20 tokens) to their corresponding lending rates
    mapping (address => uint256) public lendingRates;

    // List of supported assets (ERC-20 tokens)
    address[] public supportedAssets;

    // Event emitted when a lender deposits assets
    event Deposit(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower borrows assets
    event Borrow(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a lender withdraws assets
    event Withdraw(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower repays assets
    event Repay(address indexed borrower, address indexed asset, uint256 amount);

    /**
     * @notice Constructor
     * @param _supportedAssets List of supported assets (ERC-20 tokens)
     * @param _lendingRates Mapping of assets to their corresponding lending rates
     */
    constructor(address[] memory _supportedAssets, uint256[] memory _lendingRates) {
        require(_supportedAssets.length == _lendingRates.length, "Invalid input lengths");

        for (uint256 i = 0; i < _supportedAssets.length; i++) {
            supportedAssets.push(_supportedAssets[i]);
            lendingRates[_supportedAssets[i]] = _lendingRates[i];
        }
    }

    /**
     * @notice Deposit assets as a lender
     * @param _asset Address of the asset to deposit
     * @param _amount Amount of assets to deposit
     */
    function deposit(address _asset, uint256 _amount) public {
        require(lendingRates[_asset] > 0, "Asset not supported");
        require(ERC20(_asset).transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        lenderDeposits[msg.sender] = lenderDeposits[msg.sender].add(_amount);

        emit Deposit(msg.sender, _asset, _amount);
    }

    /**
     * @notice Borrow assets as a borrower
     * @param _asset Address of the asset to borrow
     * @param _amount Amount of assets to borrow
     */
    function borrow(address _asset, uint256 _amount) public {
        require(lendingRates[_asset] > 0, "Asset not supported");
        require(lenderDeposits[msg.sender] >= _amount, "Insufficient deposits");

        borrowerBorrows[msg.sender] = borrowerBorrows[msg.sender].add(_amount);
        lenderDeposits[msg.sender] = lenderDeposits[msg.sender].sub(_amount);

        require(ERC20(_asset).transfer(msg.sender, _amount), "Transfer failed");

        emit Borrow(msg.sender, _asset, _amount);
    }

    /**
     * @notice Withdraw assets as a lender
     * @param _asset Address of the asset to withdraw
     * @param _amount Amount of assets to withdraw
     */
    function withdraw(address _asset, uint256 _amount) public {
        require(lendingRates[_asset] > 0, "Asset not supported");
        require(lenderDeposits[msg.sender] >= _amount, "Insufficient deposits");

        lenderDeposits[msg.sender] = lenderDeposits[msg.sender].sub(_amount);

        require(ERC20(_asset).transfer(msg.sender, _amount), "Transfer failed");

        emit Withdraw(msg.sender, _asset, _amount);
    }

    /**
     * @notice Repay assets as a borrower
     * @param _asset Address of the asset to repay
     * @param _amount Amount of assets to repay
     */
    function repay(address _asset, uint256 _amount) public {
        require(lendingRates[_asset] > 0, "Asset not supported");
        require(borrowerBorrows[msg.sender] >= _amount, "Insufficient borrows");

        borrowerBorrows[msg.sender] = borrowerBorrows[msg.sender].sub(_amount);

        require(ERC20(_asset).transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        emit Repay(msg.sender, _asset, _amount);
    }

    /**
     * @notice Update lending rate for an asset
     * @param _asset Address of the asset to update
     * @param _newRate New lending rate for the asset
     */
    function updateLendingRate(address _asset, uint256 _newRate) public onlyOwner {
        lendingRates[_asset] = _newRate;
    }

    /**
     * @notice Add a new supported asset
     * @param _asset Address of the asset to add
     * @param _lendingRate Initial lending rate for the asset
     */
    function addSupportedAsset(address _asset, uint256 _lendingRate) public onlyOwner {
        supportedAssets.push(_asset);
        lendingRates[_asset] = _lendingRate;
    }

    /**
     * @notice Remove a supported asset
     * @param _asset Address of the asset to remove
     */
    function removeSupportedAsset(address _asset) public onlyOwner {
        for (uint256 i = 0; i < supportedAssets.length; i++) {
            if (supportedAssets[i] == _asset) {
                supportedAssets[i] = supportedAssets[supportedAssets.length - 1];
                supportedAssets.pop();
                delete lendingRates[_asset];
                break;
            }
        }
    }
}
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  const LendingPlatform = await ethers.getContractFactory("LendingPlatform");

  const supportedAssets = ["0x...Asset1...", "0x...Asset2..."];
  const lendingRates = [100, 200];

  const lendingPlatform = await LendingPlatform.create(supportedAssets, lendingRates);
  await lendingPlatform.deployed();

  console.log("Lending Platform deployed to:", lendingPlatform.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

```javascript
// scripts/interact.js
const { ethers } = require("hardhat");
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function main() {
  const lendingPlatformAddress = "0x...LendingPlatform...";
  const lendingPlatform = await ethers.getContractAt("LendingPlatform", lendingPlatformAddress);

  rl.question("Enter your account address: ", async (account) => {
    const accountAddress = account;

    rl.question("Enter the asset address: ", async (asset) => {
      const assetAddress = asset;

      rl.question("Enter the amount: ", async (amount) => {
        const amountValue = ethers.utils.parseEther(amount);

        // Deposit
        console.log("Depositing...");
        await lendingPlatform.deposit(assetAddress, amountValue);
        console.log("Deposited!");

        // Borrow
        // console.log("Borrowing...");
        // await lendingPlatform.borrow(assetAddress, amountValue);
        // console.log("Borrowed!");

        // Withdraw
        // console.log("Withdrawing...");
        // await lendingPlatform.withdraw(assetAddress, amountValue);
        // console.log("Withdrawn!");

        // Repay
        // console.log("Repaying...");
        // await lendingPlatform.repay(assetAddress, amountValue);
        // console.log("Repaid!");

        rl.close();
      });
    });
  });
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
