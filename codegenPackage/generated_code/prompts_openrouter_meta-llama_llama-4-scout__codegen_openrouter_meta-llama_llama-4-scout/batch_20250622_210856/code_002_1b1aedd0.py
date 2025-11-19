"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Generate a Solidity (or Rust, if applicable) code snippet for a smart contract that implements a token distribution mechanism similar to PUNDU's, with 45% of tokens going to LP and 45% to presale participants.
Generated: DETERMINISTIC_1b1aedd03d0b1f6e
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the Solidity code for the smart contract:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenDistributionContract
 * @author [Your Name]
 * @notice This contract distributes tokens to LP and presale participants.
 */
contract TokenDistributionContract is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their presale allocation
    mapping(address => uint256) public presaleAllocations;

    // Address of the LP wallet
    address public lpWallet;

    // Total token supply
    uint256 public totalSupply;

    // Token distribution percentages
    uint256 public constant LP_PERCENTAGE = 45;
    uint256 public constant PRESALE_PERCENTAGE = 45;

    /**
     * @notice Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _lpWallet LP wallet address
     */
    constructor(string memory _name, string memory _symbol, address _lpWallet) ERC20(_name, _symbol) {
        lpWallet = _lpWallet;

        // Initialize total supply
        totalSupply = 10000 * 10**18; // 10,000 tokens with 18 decimals

        // Validate distribution percentages
        require(LP_PERCENTAGE + PRESALE_PERCENTAGE <= 100, "Distribution percentages exceed 100%");

        // Mint tokens for LP and presale participants
        _mint(lpWallet, totalSupply * LP_PERCENTAGE / 100);
        _mint(address(this), totalSupply * PRESALE_PERCENTAGE / 100);

        // Emit event for token distribution
        emit TokenDistributed(lpWallet, totalSupply * LP_PERCENTAGE / 100);
    }

    /**
     * @notice Distributes tokens to presale participants
     * @param _participants Presale participant addresses
     * @param _amounts Presale participant token amounts
     */
    function distributePresaleTokens(address[] memory _participants, uint256[] memory _amounts) external onlyOwner {
        require(_participants.length == _amounts.length, "Participant and amount arrays must be the same length");

        for (uint256 i = 0; i < _participants.length; i++) {
            presaleAllocations[_participants[i]] = _amounts[i];
            _transfer(address(this), _participants[i], _amounts[i]);
        }
    }

    /**
     * @notice Transfers tokens from the contract to an address
     * @param _to Address to transfer tokens to
     * @param _amount Token amount to transfer
     */
    function transferTokens(address _to, uint256 _amount) external onlyOwner {
        _transfer(address(this), _to, _amount);
    }

    /**
     * @notice Event emitted when tokens are distributed
     * @param _to Address that received tokens
     * @param _amount Token amount received
     */
    event TokenDistributed(address indexed _to, uint256 _amount);

    /**
     * @notice Modifier for only owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /**
     * @notice Owner of the contract
     */
    address public owner;

    /**
     * @notice Constructor modifier for setting the owner
     */
    modifier onlyOwnerConstructor() {
        require(owner == address(0), "Owner already set");
        _;
        owner = msg.sender;
    }

    /**
     * @notice Fallback for receiving Ether
     */
    receive() external payable {}
}
```

To compile and deploy the contract, ensure you have OpenZeppelin installed:

```bash
npm install @openzeppelin/contracts
```

Then use Hardhat or Truffle to compile and deploy the contract.

Here is an example using Hardhat:

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  const TokenDistributionContract = await ethers.getContractFactory("TokenDistributionContract");
  const contract = await TokenDistributionContract.deploy("Token Name", "TKN", "0x... lp wallet address");

  await contract.deployed();

  console.log(`Contract deployed to ${contract.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
