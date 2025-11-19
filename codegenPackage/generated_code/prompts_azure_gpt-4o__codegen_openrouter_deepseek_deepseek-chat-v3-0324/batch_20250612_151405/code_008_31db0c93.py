"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-en.web.app
Prompt: Develop a Solidity smart contract for $SCOTTY token distribution based on the tokenomics provided (e.g., public sale, staking, development, marketing).
Generated: DETERMINISTIC_31db0c933cb7cffd
Batch ID: 20250612_151405
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

contract ScottyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PUBLIC_SALE_PERCENT = 30;
    uint256 public constant STAKING_PERCENT = 25;
    uint256 public constant DEVELOPMENT_PERCENT = 20;
    uint256 public constant MARKETING_PERCENT = 15;
    uint256 public constant TEAM_PERCENT = 10;

    // Addresses for different allocations
    address public publicSaleWallet;
    address public stakingWallet;
    address public developmentWallet;
    address public marketingWallet;
    address public teamWallet;

    // Total supply (1 billion tokens with 18 decimals)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18);

    // Flags for distribution completion
    bool public publicSaleDistributed;
    bool public stakingDistributed;
    bool public developmentDistributed;
    bool public marketingDistributed;
    bool public teamDistributed;

    event TokensDistributed(string allocation, uint256 amount, address wallet);

    constructor(
        address _publicSaleWallet,
        address _stakingWallet,
        address _developmentWallet,
        address _marketingWallet,
        address _teamWallet
    ) ERC20("Scotty Token", "SCOTTY") {
        require(_publicSaleWallet != address(0), "Public sale wallet cannot be zero");
        require(_stakingWallet != address(0), "Staking wallet cannot be zero");
        require(_developmentWallet != address(0), "Development wallet cannot be zero");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero");
        require(_teamWallet != address(0), "Team wallet cannot be zero");

        publicSaleWallet = _publicSaleWallet;
        stakingWallet = _stakingWallet;
        developmentWallet = _developmentWallet;
        marketingWallet = _marketingWallet;
        teamWallet = _teamWallet;
    }

    /**
     * @dev Distribute tokens according to tokenomics
     * Can only be called once by the owner
     */
    function distributeTokens() external onlyOwner {
        require(!publicSaleDistributed, "Public sale tokens already distributed");
        require(!stakingDistributed, "Staking tokens already distributed");
        require(!developmentDistributed, "Development tokens already distributed");
        require(!marketingDistributed, "Marketing tokens already distributed");
        require(!teamDistributed, "Team tokens already distributed");

        // Calculate token amounts for each allocation
        uint256 publicSaleAmount = TOTAL_SUPPLY.mul(PUBLIC_SALE_PERCENT).div(100);
        uint256 stakingAmount = TOTAL_SUPPLY.mul(STAKING_PERCENT).div(100);
        uint256 developmentAmount = TOTAL_SUPPLY.mul(DEVELOPMENT_PERCENT).div(100);
        uint256 marketingAmount = TOTAL_SUPPLY.mul(MARKETING_PERCENT).div(100);
        uint256 teamAmount = TOTAL_SUPPLY.mul(TEAM_PERCENT).div(100);

        // Mint tokens to respective wallets
        _mint(publicSaleWallet, publicSaleAmount);
        _mint(stakingWallet, stakingAmount);
        _mint(developmentWallet, developmentAmount);
        _mint(marketingWallet, marketingAmount);
        _mint(teamWallet, teamAmount);

        // Mark distributions as complete
        publicSaleDistributed = true;
        stakingDistributed = true;
        developmentDistributed = true;
        marketingDistributed = true;
        teamDistributed = true;

        // Emit events
        emit TokensDistributed("Public Sale", publicSaleAmount, publicSaleWallet);
        emit TokensDistributed("Staking", stakingAmount, stakingWallet);
        emit TokensDistributed("Development", developmentAmount, developmentWallet);
        emit TokensDistributed("Marketing", marketingAmount, marketingWallet);
        emit TokensDistributed("Team", teamAmount, teamWallet);
    }

    /**
     * @dev Override to prevent transfers until distributions are complete
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        if (from == address(0)) {
            // Minting is allowed during distribution
            return;
        }

        require(
            publicSaleDistributed &&
            stakingDistributed &&
            developmentDistributed &&
            marketingDistributed &&
            teamDistributed,
            "Token distribution not complete"
        );
    }
}
```
