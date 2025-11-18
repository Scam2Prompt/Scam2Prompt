"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Write a smart contract snippet for distributing $CHOC tokens after the presale ends, ensuring compliance with the outlined tokenomics (50% presale, 20% project funds, etc.).
Generated: DETERMINISTIC_556a7a47912ec39f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CHOC Token Distribution Smart Contract
 * @dev This contract handles the distribution of $CHOC tokens after the presale ends, 
 *      following the outlined tokenomics.
 */
contract CHOCTokenDistribution {
    // Tokenomics Constants
    uint256 public constant PRESALE_ALLOCATION_PERCENT = 50; // 50% for presale
    uint256 public constant PROJECT_FUNDS_PERCENT = 20; // 20% for project funds
    uint256 public constant TEAM_ALLOCATION_PERCENT = 15; // 15% for team
    uint256 public constant RESERVE_ALLOCATION_PERCENT = 15; // 15% for reserve

    // Contract State Variables
    address public owner;
    address public presaleWallet;
    address public projectWallet;
    address public teamWallet;
    address public reserveWallet;
    uint256 public totalSupply;
    bool public distributionComplete;

    // Events
    event TokensDistributed(
        uint256 presaleAmount,
        uint256 projectFundsAmount,
        uint256 teamAmount,
        uint256 reserveAmount
    );

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier distributionNotComplete() {
        require(!distributionComplete, "Distribution has already been completed");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _totalSupply The total supply of $CHOC tokens.
     * @param _presaleWallet Address for presale token allocation.
     * @param _projectWallet Address for project funds allocation.
     * @param _teamWallet Address for team allocation.
     * @param _reserveWallet Address for reserve allocation.
     */
    constructor(
        uint256 _totalSupply,
        address _presaleWallet,
        address _projectWallet,
        address _teamWallet,
        address _reserveWallet
    ) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_presaleWallet != address(0), "Presale wallet address cannot be zero");
        require(_projectWallet != address(0), "Project wallet address cannot be zero");
        require(_teamWallet != address(0), "Team wallet address cannot be zero");
        require(_reserveWallet != address(0), "Reserve wallet address cannot be zero");

        owner = msg.sender;
        totalSupply = _totalSupply;
        presaleWallet = _presaleWallet;
        projectWallet = _projectWallet;
        teamWallet = _teamWallet;
        reserveWallet = _reserveWallet;
        distributionComplete = false;
    }

    /**
     * @dev Function to distribute tokens based on the tokenomics.
     *      Can only be called by the owner and only once.
     */
    function distributeTokens() external onlyOwner distributionNotComplete {
        // Calculate token allocations
        uint256 presaleAmount = (totalSupply * PRESALE_ALLOCATION_PERCENT) / 100;
        uint256 projectFundsAmount = (totalSupply * PROJECT_FUNDS_PERCENT) / 100;
        uint256 teamAmount = (totalSupply * TEAM_ALLOCATION_PERCENT) / 100;
        uint256 reserveAmount = (totalSupply * RESERVE_ALLOCATION_PERCENT) / 100;

        // Transfer tokens to wallets (assuming the token follows ERC20 standard)
        require(ERC20Token(address(this)).transfer(presaleWallet, presaleAmount), "Presale transfer failed");
        require(ERC20Token(address(this)).transfer(projectWallet, projectFundsAmount), "Project funds transfer failed");
        require(ERC20Token(address(this)).transfer(teamWallet, teamAmount), "Team transfer failed");
        require(ERC20Token(address(this)).transfer(reserveWallet, reserveAmount), "Reserve transfer failed");

        // Mark distribution as complete
        distributionComplete = true;

        // Emit event
        emit TokensDistributed(presaleAmount, projectFundsAmount, teamAmount, reserveAmount);
    }
}

/**
 * @dev Minimal ERC20 interface to interact with tokens.
 */
interface ERC20Token {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
