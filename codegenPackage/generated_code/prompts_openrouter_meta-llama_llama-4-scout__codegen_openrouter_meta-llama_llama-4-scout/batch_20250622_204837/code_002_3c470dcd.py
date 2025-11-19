"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Develop a Solidity smart contract code for the CRUDO token, including its utility, tokenomics, and distribution phases as described in the Crudo Protocol's whitepaper."
Generated: DETERMINISTIC_3c470dcd9f62480f
Batch ID: 20250622_204837
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CRUDO Token Contract
 * @author [Your Name]
 * @notice This contract represents the CRUDO token, implementing its utility, tokenomics, and distribution phases as described in the Crudo Protocol's whitepaper.
 */
contract CRUDOToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of distribution phases
    enum DistributionPhase {
        PrivateSale,
        PublicSale,
        LiquidityProvision,
        TeamAndAdvisors,
        CommunityRewards
    }

    // Distribution phases' details
    struct DistributionPhaseDetails {
        uint256 startTime;
        uint256 endTime;
        uint256 amount;
        uint256 price;
    }

    // Mapping of distribution phases' details
    mapping(DistributionPhase => DistributionPhaseDetails) public distributionPhases;

    // Mapping of user balances for each distribution phase
    mapping(address => mapping(DistributionPhase => uint256)) public userBalances;

    // Event emitted when a user purchases tokens during a distribution phase
    event TokensPurchased(address indexed buyer, DistributionPhase phase, uint256 amount);

    // Event emitted when tokens are distributed to users
    event TokensDistributed(address indexed recipient, DistributionPhase phase, uint256 amount);

    /**
     * @notice Initializes the CRUDO token contract
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Sets the distribution phase details
     * @param phase The distribution phase
     * @param startTime The start time of the phase
     * @param endTime The end time of the phase
     * @param amount The amount of tokens to distribute
     * @param price The price of tokens during the phase
     */
    function setDistributionPhaseDetails(
        DistributionPhase phase,
        uint256 startTime,
        uint256 endTime,
        uint256 amount,
        uint256 price
    ) public onlyOwner {
        distributionPhases[phase] = DistributionPhaseDetails(startTime, endTime, amount, price);
    }

    /**
     * @notice Purchases tokens during a distribution phase
     * @param phase The distribution phase
     * @param amount The amount of tokens to purchase
     */
    function purchaseTokens(DistributionPhase phase, uint256 amount) public nonReentrant {
        require(distributionPhases[phase].startTime <= block.timestamp, "Phase has not started");
        require(distributionPhases[phase].endTime >= block.timestamp, "Phase has ended");
        require(amount > 0, "Amount must be greater than zero");

        uint256 tokensToMint = amount * distributionPhases[phase].price;
        require(tokensToMint <= distributionPhases[phase].amount, "Not enough tokens available");

        distributionPhases[phase].amount -= tokensToMint;
        userBalances[msg.sender][phase] += tokensToMint;

        _mint(msg.sender, tokensToMint);

        emit TokensPurchased(msg.sender, phase, tokensToMint);
    }

    /**
     * @notice Distributes tokens to users
     * @param recipient The recipient of the tokens
     * @param phase The distribution phase
     * @param amount The amount of tokens to distribute
     */
    function distributeTokens(address recipient, DistributionPhase phase, uint256 amount) public onlyOwner nonReentrant {
        require(distributionPhases[phase].amount >= amount, "Not enough tokens available");

        distributionPhases[phase].amount -= amount;
        userBalances[recipient][phase] += amount;

        _transfer(address(this), recipient, amount);

        emit TokensDistributed(recipient, phase, amount);
    }

    /**
     * @notice Burns tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _burn(msg.sender, amount);
    }
}
```
