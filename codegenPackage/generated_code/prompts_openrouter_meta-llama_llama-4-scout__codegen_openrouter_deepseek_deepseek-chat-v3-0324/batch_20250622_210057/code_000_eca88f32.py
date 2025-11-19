"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogs.pages.dev
Prompt: Write a smart contract in Solidity for a token sale on the Bitcoin blockchain, similar to the $0DOG token sale described on the Bitcoin Dogs website.
Generated: DETERMINISTIC_eca88f3236d61504
Batch ID: 20250622_210057
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

contract BitcoinDogsToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token sale parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_SUPPLY = 200_000_000 * 10**18; // 20% of total supply
    uint256 public constant PUBLIC_SALE_SUPPLY = 300_000_000 * 10**18; // 30% of total supply
    uint256 public constant TEAM_SUPPLY = 100_000_000 * 10**18; // 10% of total supply
    uint256 public constant RESERVE_SUPPLY = 400_000_000 * 10**18; // 40% of total supply

    // Sale phases
    enum SalePhase { NONE, PRESALE, PUBLIC_SALE, COMPLETED }
    SalePhase public currentPhase = SalePhase.NONE;

    // Token pricing
    uint256 public presalePrice = 0.0001 ether; // Price per token in presale
    uint256 public publicSalePrice = 0.0002 ether; // Price per token in public sale

    // Sale tracking
    uint256 public presaleTokensSold = 0;
    uint256 public publicSaleTokensSold = 0;

    // Vesting for team tokens
    uint256 public teamTokensReleased = 0;
    uint256 public constant TEAM_VESTING_PERIOD = 365 days; // 1 year vesting
    uint256 public constant TEAM_VESTING_CLIFF = 90 days; // 3 month cliff
    uint256 public vestingStartTime;

    // Addresses
    address public reserveWallet;
    address public teamWallet;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event SalePhaseChanged(SalePhase newPhase);
    event TeamTokensReleased(address indexed teamWallet, uint256 amount);

    constructor(
        address _reserveWallet,
        address _teamWallet
    ) ERC20("Bitcoin Dogs Token", "0DOG") {
        require(_reserveWallet != address(0), "Reserve wallet cannot be zero address");
        require(_teamWallet != address(0), "Team wallet cannot be zero address");

        reserveWallet = _reserveWallet;
        teamWallet = _teamWallet;

        // Mint reserve tokens
        _mint(reserveWallet, RESERVE_SUPPLY);
        
        // Mint team tokens (vested)
        _mint(address(this), TEAM_SUPPLY);
    }

    /**
     * @dev Start a new sale phase
     * @param phase The new sale phase to start
     */
    function startSalePhase(SalePhase phase) external onlyOwner {
        require(phase != SalePhase.NONE, "Cannot set phase to NONE");
        require(phase != currentPhase, "Already in this phase");
        
        if (phase == SalePhase.PRESALE) {
            require(currentPhase == SalePhase.NONE, "Presale must be first phase");
        } else if (phase == SalePhase.PUBLIC_SALE) {
            require(currentPhase == SalePhase.PRESALE || currentPhase == SalePhase.NONE, 
                "Public sale must follow presale");
        } else if (phase == SalePhase.COMPLETED) {
            require(currentPhase != SalePhase.NONE, "Cannot complete before starting");
        }

        currentPhase = phase;
        
        if (phase == SalePhase.PUBLIC_SALE) {
            vestingStartTime = block.timestamp;
        }
        
        emit SalePhaseChanged(phase);
    }

    /**
     * @dev Buy tokens during active sale
     */
    function buyTokens() external payable nonReentrant {
        require(currentPhase == SalePhase.PRESALE || currentPhase == SalePhase.PUBLIC_SALE, 
            "Sale is not active");
        
        uint256 amount;
        uint256 cost;
        
        if (currentPhase == SalePhase.PRESALE) {
            amount = msg.value.div(presalePrice);
            require(presaleTokensSold.add(amount) <= PRESALE_SUPPLY, "Exceeds presale supply");
            cost = amount.mul(presalePrice);
            presaleTokensSold = presaleTokensSold.add(amount);
        } else {
            amount = msg.value.div(publicSalePrice);
            require(publicSaleTokensSold.add(amount) <= PUBLIC_SALE_SUPPLY, "Exceeds public sale supply");
            cost = amount.mul(publicSalePrice);
            publicSaleTokensSold = publicSaleTokensSold.add(amount);
        }
        
        require(amount > 0, "Amount must be greater than 0");
        require(cost <= msg.value, "Insufficient payment");
        
        _mint(msg.sender, amount);
        
        // Refund any excess payment
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value.sub(cost));
        }
        
        emit TokensPurchased(msg.sender, amount, cost);
    }

    /**
     * @dev Release vested team tokens
     */
    function releaseTeamTokens() external nonReentrant {
        require(currentPhase == SalePhase.COMPLETED, "Sale must be completed");
        require(vestingStartTime > 0, "Vesting not started");
        require(block.timestamp >= vestingStartTime.add(TEAM_VESTING_CLIFF), "Cliff period not passed");
        
        uint256 elapsedTime = block.timestamp.sub(vestingStartTime);
        uint256 totalVested = TEAM_SUPPLY;
        
        if (elapsedTime < TEAM_VESTING_PERIOD) {
            totalVested = TEAM_SUPPLY.mul(elapsedTime).div(TEAM_VESTING_PERIOD);
        }
        
        uint256 unreleased = totalVested.sub(teamTokensReleased);
        require(unreleased > 0, "No tokens to release");
        
        teamTokensReleased = teamTokensReleased.add(unreleased);
        _transfer(address(this), teamWallet, unreleased);
        
        emit TeamTokensReleased(teamWallet, unreleased);
    }

    /**
     * @dev Withdraw collected ETH from token sales
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Set new token prices
     * @param newPresalePrice New price for presale tokens (in wei)
     * @param newPublicSalePrice New price for public sale tokens (in wei)
     */
    function setPrices(uint256 newPresalePrice, uint256 newPublicSalePrice) external onlyOwner {
        require(currentPhase != SalePhase.COMPLETED, "Sale is completed");
        require(newPresalePrice > 0, "Presale price must be greater than 0");
        require(newPublicSalePrice > 0, "Public sale price must be greater than 0");
        
        presalePrice = newPresalePrice;
        publicSalePrice = newPublicSalePrice;
    }

    /**
     * @dev Update reserve wallet address
     * @param newReserveWallet New reserve wallet address
     */
    function updateReserveWallet(address newReserveWallet) external onlyOwner {
        require(newReserveWallet != address(0), "Reserve wallet cannot be zero address");
        reserveWallet = newReserveWallet;
    }

    /**
     * @dev Update team wallet address
     * @param newTeamWallet New team wallet address
     */
    function updateTeamWallet(address newTeamWallet) external onlyOwner {
        require(newTeamWallet != address(0), "Team wallet cannot be zero address");
        teamWallet = newTeamWallet;
    }
}
```
