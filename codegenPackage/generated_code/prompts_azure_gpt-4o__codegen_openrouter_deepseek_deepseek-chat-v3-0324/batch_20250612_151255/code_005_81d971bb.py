"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Create a step-by-step guide for setting up a decentralized token presale similar to WienerAI, including tokenomics design and smart contract deployment.
Generated: DETERMINISTIC_81d971bb8ac39939
Batch ID: 20250612_151255
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PresaleToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    uint256 public constant PRESALE_PERCENTAGE = 30; // 30% for presale
    uint256 public constant LIQUIDITY_PERCENTAGE = 50; // 50% for liquidity
    uint256 public constant TEAM_PERCENTAGE = 10; // 10% for team
    uint256 public constant MARKETING_PERCENTAGE = 10; // 10% for marketing

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Tokens per ETH
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public hardCap;
    uint256 public totalContributed;
    bool public presaleFinalized;

    // Addresses
    address public liquidityWallet;
    address public teamWallet;
    address public marketingWallet;

    // Whitelist
    mapping(address => bool) public whitelist;
    bool public whitelistEnabled;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleFinalized(uint256 ethRaised, uint256 tokensSold);
    event WhitelistUpdated(address indexed account, bool status);

    constructor(
        string memory name,
        string memory symbol,
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _hardCap,
        uint256 _presaleDuration,
        address _liquidityWallet,
        address _teamWallet,
        address _marketingWallet
    ) ERC20(name, symbol) {
        require(_presaleRate > 0, "Presale rate must be > 0");
        require(_minContribution > 0, "Min contribution must be > 0");
        require(_maxContribution > _minContribution, "Max must be > min");
        require(_hardCap > 0, "Hard cap must be > 0");
        require(_presaleDuration > 0, "Presale duration must be > 0");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be 0");
        require(_teamWallet != address(0), "Team wallet cannot be 0");
        require(_marketingWallet != address(0), "Marketing wallet cannot be 0");

        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        hardCap = _hardCap;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp.add(_presaleDuration);
        liquidityWallet = _liquidityWallet;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;

        // Mint initial supply
        _mint(address(this), TOTAL_SUPPLY.mul(PRESALE_PERCENTAGE).div(100));
        _mint(liquidityWallet, TOTAL_SUPPLY.mul(LIQUIDITY_PERCENTAGE).div(100));
        _mint(teamWallet, TOTAL_SUPPLY.mul(TEAM_PERCENTAGE).div(100));
        _mint(marketingWallet, TOTAL_SUPPLY.mul(MARKETING_PERCENTAGE).div(100));
    }

    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        require(!presaleFinalized, "Presale already finalized");
        require(msg.value >= minContribution, "Contribution too low");
        require(msg.value <= maxContribution, "Contribution exceeds max");
        require(totalContributed.add(msg.value) <= hardCap, "Hard cap reached");
        if (whitelistEnabled) {
            require(whitelist[msg.sender], "Address not whitelisted");
        }

        uint256 tokens = msg.value.mul(presaleRate);
        require(balanceOf(address(this)) >= tokens, "Not enough tokens left");

        totalContributed = totalContributed.add(msg.value);
        _transfer(address(this), msg.sender, tokens);

        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalContributed == hardCap, "Presale not ended");
        require(!presaleFinalized, "Presale already finalized");

        presaleFinalized = true;

        // Transfer remaining tokens to liquidity wallet
        uint256 remainingTokens = balanceOf(address(this));
        if (remainingTokens > 0) {
            _transfer(address(this), liquidityWallet, remainingTokens);
        }

        emit PresaleFinalized(totalContributed, TOTAL_SUPPLY.mul(PRESALE_PERCENTAGE).div(100).sub(remainingTokens));
    }

    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        payable(owner()).transfer(address(this).balance);
    }

    function setWhitelistStatus(address[] calldata accounts, bool status) external onlyOwner {
        for (uint256 i = 0; i < accounts.length; i++) {
            whitelist[accounts[i]] = status;
            emit WhitelistUpdated(accounts[i], status);
        }
    }

    function toggleWhitelist() external onlyOwner {
        whitelistEnabled = !whitelistEnabled;
    }

    function extendPresale(uint256 additionalDuration) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale already ended");
        presaleEndTime = presaleEndTime.add(additionalDuration);
    }

    function getPresaleStatus() external view returns (
        uint256 startTime,
        uint256 endTime,
        uint256 rate,
        uint256 min,
        uint256 max,
        uint256 cap,
        uint256 contributed,
        bool finalized,
        bool isWhitelistEnabled
    ) {
        return (
            presaleStartTime,
            presaleEndTime,
            presaleRate,
            minContribution,
            maxContribution,
            hardCap,
            totalContributed,
            presaleFinalized,
            whitelistEnabled
        );
    }
}
```

```javascript
// Deployment script (using Hardhat)
const { ethers } = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString());

  // Token parameters
  const tokenName = "WienerAI";
  const tokenSymbol = "WAI";
  const presaleRate = ethers.utils.parseUnits("1000", 18); // 1000 tokens per ETH
  const minContribution = ethers.utils.parseEther("0.1"); // 0.1 ETH
  const maxContribution = ethers.utils.parseEther("5"); // 5 ETH
  const hardCap = ethers.utils.parseEther("100"); // 100 ETH
  const presaleDuration = 7 * 24 * 60 * 60; // 7 days in seconds

  // Wallet addresses
  const liquidityWallet = "0x123..."; // Replace with actual address
  const teamWallet = "0x456..."; // Replace with actual address
  const marketingWallet = "0x789..."; // Replace with actual address

  const PresaleToken = await ethers.getContractFactory("PresaleToken");
  const presaleToken = await PresaleToken.deploy(
    tokenName,
    tokenSymbol,
    presaleRate,
    minContribution,
    maxContribution,
    hardCap,
    presaleDuration,
    liquidityWallet,
    teamWallet,
    marketingWallet
  );

  await presaleToken.deployed();

  console.log("PresaleToken deployed to:", presaleToken.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// Verification script (for Etherscan)
const { run } = require("hardhat");

async function verify(contractAddress, args) {
  console.log("Verifying contract...");
  try {
    await run("verify:verify", {
      address: contractAddress,
      constructorArguments: args,
    });
  } catch (e) {
    if (e.message
