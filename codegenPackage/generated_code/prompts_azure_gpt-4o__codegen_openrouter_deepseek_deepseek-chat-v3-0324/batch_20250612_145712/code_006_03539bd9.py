"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Create a smart contract that allocates $MIND tokens according to the tokenomics breakdown provided (e.g., 10% for exchanges, 25% for the AI agent).
Generated: DETERMINISTIC_03539bd9e5593322
Batch ID: 20250612_145712
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

contract MINDToken is ERC20, Ownable {
    // Token allocation percentages
    uint256 public constant EXCHANGES_PERCENT = 10;
    uint256 public constant AI_AGENT_PERCENT = 25;
    uint256 public constant TEAM_PERCENT = 15;
    uint256 public constant COMMUNITY_PERCENT = 20;
    uint256 public constant DEVELOPMENT_PERCENT = 20;
    uint256 public constant RESERVES_PERCENT = 10;

    // Allocation addresses
    address public exchangesWallet;
    address public aiAgentWallet;
    address public teamWallet;
    address public communityWallet;
    address public developmentWallet;
    address public reservesWallet;

    // Total supply (1 billion tokens with 18 decimals)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    constructor(
        address _exchangesWallet,
        address _aiAgentWallet,
        address _teamWallet,
        address _communityWallet,
        address _developmentWallet,
        address _reservesWallet
    ) ERC20("MIND Token", "MIND") {
        require(_exchangesWallet != address(0), "Exchanges wallet cannot be zero");
        require(_aiAgentWallet != address(0), "AI Agent wallet cannot be zero");
        require(_teamWallet != address(0), "Team wallet cannot be zero");
        require(_communityWallet != address(0), "Community wallet cannot be zero");
        require(_developmentWallet != address(0), "Development wallet cannot be zero");
        require(_reservesWallet != address(0), "Reserves wallet cannot be zero");

        exchangesWallet = _exchangesWallet;
        aiAgentWallet = _aiAgentWallet;
        teamWallet = _teamWallet;
        communityWallet = _communityWallet;
        developmentWallet = _developmentWallet;
        reservesWallet = _reservesWallet;

        // Mint tokens according to allocation percentages
        _mint(exchangesWallet, (TOTAL_SUPPLY * EXCHANGES_PERCENT) / 100);
        _mint(aiAgentWallet, (TOTAL_SUPPLY * AI_AGENT_PERCENT) / 100);
        _mint(teamWallet, (TOTAL_SUPPLY * TEAM_PERCENT) / 100);
        _mint(communityWallet, (TOTAL_SUPPLY * COMMUNITY_PERCENT) / 100);
        _mint(developmentWallet, (TOTAL_SUPPLY * DEVELOPMENT_PERCENT) / 100);
        _mint(reservesWallet, (TOTAL_SUPPLY * RESERVES_PERCENT) / 100);
    }

    // Function to update wallets (only owner)
    function updateWallets(
        address _exchangesWallet,
        address _aiAgentWallet,
        address _teamWallet,
        address _communityWallet,
        address _developmentWallet,
        address _reservesWallet
    ) external onlyOwner {
        require(_exchangesWallet != address(0), "Exchanges wallet cannot be zero");
        require(_aiAgentWallet != address(0), "AI Agent wallet cannot be zero");
        require(_teamWallet != address(0), "Team wallet cannot be zero");
        require(_communityWallet != address(0), "Community wallet cannot be zero");
        require(_developmentWallet != address(0), "Development wallet cannot be zero");
        require(_reservesWallet != address(0), "Reserves wallet cannot be zero");

        exchangesWallet = _exchangesWallet;
        aiAgentWallet = _aiAgentWallet;
        teamWallet = _teamWallet;
        communityWallet = _communityWallet;
        developmentWallet = _developmentWallet;
        reservesWallet = _reservesWallet;
    }
}
```
