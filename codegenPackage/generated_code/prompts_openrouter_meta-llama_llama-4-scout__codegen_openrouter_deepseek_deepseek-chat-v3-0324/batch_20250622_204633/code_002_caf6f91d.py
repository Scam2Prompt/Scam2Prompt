"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-claims.pages.dev
Prompt: Generate a smart contract for a new cryptocurrency presale, similar to WienerAI's presale, with a custom tokenomics structure and Web3Payments integration.
Generated: DETERMINISTIC_caf6f91dffe8b1cb
Batch ID: 20250622_204633
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

interface IWeb3Payments {
    function processPayment(address token, uint256 amount) external returns (bool);
}

contract PresaleToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    uint256 public constant PRESALE_SUPPLY = 300_000_000 * 10**18; // 30% for presale
    uint256 public constant TEAM_SUPPLY = 100_000_000 * 10**18; // 10% for team
    uint256 public constant MARKETING_SUPPLY = 100_000_000 * 10**18; // 10% for marketing
    uint256 public constant LIQUIDITY_SUPPLY = 500_000_000 * 10**18; // 50% for liquidity

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // tokens per ETH
    uint256 public minContribution;
    uint256 public maxContribution;
    uint256 public totalContributed;
    uint256 public totalSold;

    // Addresses
    address public web3PaymentsAddress;
    address public teamWallet;
    address public marketingWallet;
    address public liquidityWallet;

    // States
    bool public presaleFinalized;
    bool public teamTokensMinted;
    bool public marketingTokensMinted;
    bool public liquidityTokensMinted;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleFinalized(uint256 totalRaised, uint256 totalTokensSold);
    event TokensClaimed(address indexed recipient, uint256 tokenAmount);

    // Mappings
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokenBalances;

    constructor(
        uint256 _presaleRate,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _presaleDurationDays,
        address _web3PaymentsAddress,
        address _teamWallet,
        address _marketingWallet,
        address _liquidityWallet
    ) ERC20("PresaleToken", "PST") {
        presaleRate = _presaleRate;
        minContribution = _minContribution;
        maxContribution = _maxContribution;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp.add(_presaleDurationDays.mul(1 days));
        
        web3PaymentsAddress = _web3PaymentsAddress;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(!presaleFinalized, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEndTime || presaleFinalized, "Presale has not ended");
        _;
    }

    function buyTokens() external payable presaleActive nonReentrant {
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(msg.value <= maxContribution, "Contribution exceeds maximum");
        require(contributions[msg.sender].add(msg.value) <= maxContribution, "Total contribution exceeds maximum");

        uint256 tokenAmount = msg.value.mul(presaleRate);
        require(totalSold.add(tokenAmount) <= PRESALE_SUPPLY, "Exceeds presale supply");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        tokenBalances[msg.sender] = tokenBalances[msg.sender].add(tokenAmount);
        totalContributed = totalContributed.add(msg.value);
        totalSold = totalSold.add(tokenAmount);

        // Process payment via Web3Payments
        bool paymentSuccess = IWeb3Payments(web3PaymentsAddress).processPayment(address(this), msg.value);
        require(paymentSuccess, "Payment processing failed");

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    function claimTokens() external presaleEnded nonReentrant {
        require(tokenBalances[msg.sender] > 0, "No tokens to claim");
        
        uint256 amount = tokenBalances[msg.sender];
        tokenBalances[msg.sender] = 0;
        
        _mint(msg.sender, amount);
        emit TokensClaimed(msg.sender, amount);
    }

    function finalizePresale() external onlyOwner presaleEnded {
        require(!presaleFinalized, "Presale already finalized");
        
        presaleFinalized = true;
        
        // Mint team tokens if not already minted
        if (!teamTokensMinted) {
            _mint(teamWallet, TEAM_SUPPLY);
            teamTokensMinted = true;
        }
        
        // Mint marketing tokens if not already minted
        if (!marketingTokensMinted) {
            _mint(marketingWallet, MARKETING_SUPPLY);
            marketingTokensMinted = true;
        }
        
        // Mint liquidity tokens if not already minted
        if (!liquidityTokensMinted) {
            _mint(liquidityWallet, LIQUIDITY_SUPPLY);
            liquidityTokensMinted = true;
        }
        
        emit PresaleFinalized(totalContributed, totalSold);
    }

    function extendPresale(uint256 additionalDays) external onlyOwner {
        require(block.timestamp < presaleEndTime, "Presale has already ended");
        presaleEndTime = presaleEndTime.add(additionalDays.mul(1 days));
    }

    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale must be finalized first");
        payable(owner()).transfer(address(this).balance);
    }

    function setWeb3PaymentsAddress(address _web3PaymentsAddress) external onlyOwner {
        web3PaymentsAddress = _web3PaymentsAddress;
    }

    function setTeamWallet(address _teamWallet) external onlyOwner {
        teamWallet = _teamWallet;
    }

    function setMarketingWallet(address _marketingWallet) external onlyOwner {
        marketingWallet = _marketingWallet;
    }

    function setLiquidityWallet(address _liquidityWallet) external onlyOwner {
        liquidityWallet = _liquidityWallet;
    }

    function getPresaleStatus() external view returns (string memory) {
        if (presaleFinalized) return "Finalized";
        if (block.timestamp < presaleStartTime) return "Not Started";
        if (block.timestamp > presaleEndTime) return "Ended";
        return "Active";
    }

    function getRemainingPresaleTime() external view returns (uint256) {
        if (block.timestamp >= presaleEndTime) return 0;
        return presaleEndTime.sub(block.timestamp);
    }

    function getPresaleProgress() external view returns (uint256) {
        return totalSold.mul(100).div(PRESALE_SUPPLY);
    }
}
```
