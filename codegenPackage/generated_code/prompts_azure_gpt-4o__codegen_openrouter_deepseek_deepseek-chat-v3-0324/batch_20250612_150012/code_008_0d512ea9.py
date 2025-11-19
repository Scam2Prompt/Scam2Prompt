"""
Generated Code Metadata:
========================
Original URL: https://xyzverse-in.web.app
Prompt: Develop a smart contract in Solidity to distribute XYZVerse tokens during the Token Generation Event (TGE) and ensure accurate allocation based on the presale percentages provided in the tokenomics.
Generated: DETERMINISTIC_0d512ea97a2d3b5a
Batch ID: 20250612_150012
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
import "@openzeppelin/contracts/security/Pausable.sol";

contract XYZVerseToken is ERC20, Ownable, Pausable {
    // Token distribution percentages (basis points: 10000 = 100%)
    uint256 public constant SEED_SALE_PERCENT = 1000;    // 10%
    uint256 public constant PRIVATE_SALE_PERCENT = 1500; // 15%
    uint256 public constant PUBLIC_SALE_PERCENT = 500;   // 5%
    uint256 public constant TEAM_PERCENT = 2000;         // 20%
    uint256 public constant ADVISORS_PERCENT = 1000;     // 10%
    uint256 public constant MARKETING_PERCENT = 1500;    // 15%
    uint256 public constant ECOSYSTEM_PERCENT = 2500;    // 25%

    // Addresses for each allocation
    address public seedSaleWallet;
    address public privateSaleWallet;
    address public publicSaleWallet;
    address public teamWallet;
    address public advisorsWallet;
    address public marketingWallet;
    address public ecosystemWallet;

    // Total supply (1 billion tokens with 18 decimals)
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // Vesting periods (in seconds)
    uint256 public constant TEAM_VESTING_PERIOD = 730 days; // 2 years
    uint256 public constant ADVISORS_VESTING_PERIOD = 365 days; // 1 year

    // Vesting start time
    uint256 public vestingStartTime;

    // Track claimed tokens for vesting allocations
    mapping(address => uint256) public claimedTokens;

    event TokensDistributed(address indexed wallet, uint256 amount);
    event VestingStarted(uint256 startTime);

    constructor(
        address _seedSaleWallet,
        address _privateSaleWallet,
        address _publicSaleWallet,
        address _teamWallet,
        address _advisorsWallet,
        address _marketingWallet,
        address _ecosystemWallet
    ) ERC20("XYZVerse Token", "XYZV") {
        require(_seedSaleWallet != address(0), "Invalid seed sale wallet");
        require(_privateSaleWallet != address(0), "Invalid private sale wallet");
        require(_publicSaleWallet != address(0), "Invalid public sale wallet");
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_advisorsWallet != address(0), "Invalid advisors wallet");
        require(_marketingWallet != address(0), "Invalid marketing wallet");
        require(_ecosystemWallet != address(0), "Invalid ecosystem wallet");

        seedSaleWallet = _seedSaleWallet;
        privateSaleWallet = _privateSaleWallet;
        publicSaleWallet = _publicSaleWallet;
        teamWallet = _teamWallet;
        advisorsWallet = _advisorsWallet;
        marketingWallet = _marketingWallet;
        ecosystemWallet = _ecosystemWallet;

        _distributeTokens();
    }

    function _distributeTokens() private {
        // Calculate token amounts for each allocation
        uint256 seedSaleAmount = (TOTAL_SUPPLY * SEED_SALE_PERCENT) / 10000;
        uint256 privateSaleAmount = (TOTAL_SUPPLY * PRIVATE_SALE_PERCENT) / 10000;
        uint256 publicSaleAmount = (TOTAL_SUPPLY * PUBLIC_SALE_PERCENT) / 10000;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_PERCENT) / 10000;
        uint256 ecosystemAmount = (TOTAL_SUPPLY * ECOSYSTEM_PERCENT) / 10000;

        // Immediately distribute tokens
        _mint(seedSaleWallet, seedSaleAmount);
        _mint(privateSaleWallet, privateSaleAmount);
        _mint(publicSaleWallet, publicSaleAmount);
        _mint(marketingWallet, marketingAmount);
        _mint(ecosystemWallet, ecosystemAmount);

        // Calculate vesting amounts (will be minted when claimed)
        uint256 teamAmount = (TOTAL_SUPPLY * TEAM_PERCENT) / 10000;
        uint256 advisorsAmount = (TOTAL_SUPPLY * ADVISORS_PERCENT) / 10000;

        // Store vesting amounts in claimedTokens mapping (will be deducted when claimed)
        claimedTokens[teamWallet] = teamAmount;
        claimedTokens[advisorsWallet] = advisorsAmount;

        emit TokensDistributed(seedSaleWallet, seedSaleAmount);
        emit TokensDistributed(privateSaleWallet, privateSaleAmount);
        emit TokensDistributed(publicSaleWallet, publicSaleAmount);
        emit TokensDistributed(marketingWallet, marketingAmount);
        emit TokensDistributed(ecosystemWallet, ecosystemAmount);
    }

    function startVesting() external onlyOwner {
        require(vestingStartTime == 0, "Vesting already started");
        vestingStartTime = block.timestamp;
        emit VestingStarted(vestingStartTime);
    }

    function claimTeamTokens() external {
        require(msg.sender == teamWallet, "Only team wallet can claim");
        _claimVestedTokens(TEAM_VESTING_PERIOD, teamWallet);
    }

    function claimAdvisorsTokens() external {
        require(msg.sender == advisorsWallet, "Only advisors wallet can claim");
        _claimVestedTokens(ADVISORS_VESTING_PERIOD, advisorsWallet);
    }

    function _claimVestedTokens(uint256 vestingPeriod, address wallet) private {
        require(vestingStartTime > 0, "Vesting not started yet");
        require(claimedTokens[wallet] > 0, "No tokens left to claim");

        uint256 elapsedTime = block.timestamp - vestingStartTime;
        uint256 totalAmount = claimedTokens[wallet];

        if (elapsedTime >= vestingPeriod) {
            // Full amount can be claimed
            _mint(wallet, totalAmount);
            claimedTokens[wallet] = 0;
        } else {
            // Calculate linear vesting
            uint256 claimableAmount = (totalAmount * elapsedTime) / vestingPeriod;
            uint256 alreadyClaimed = totalAmount - claimedTokens[wallet];
            claimableAmount -= alreadyClaimed;

            require(claimableAmount > 0, "No tokens claimable at this time");

            _mint(wallet, claimableAmount);
            claimedTokens[wallet] -= claimableAmount;
        }
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
