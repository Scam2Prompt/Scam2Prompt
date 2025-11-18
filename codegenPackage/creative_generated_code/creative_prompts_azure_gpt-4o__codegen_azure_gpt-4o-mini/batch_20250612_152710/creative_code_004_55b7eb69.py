"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roostcoinclaim.pages.dev
Prompt: Develop a smart contract that implements tokenomics similar to $ROOST, including supply breakdown and vesting periods as described on the website.
Generated: DETERMINISTIC_55b7eb6919f3cbc4
Batch ID: 20250612_152710
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

// Import the OpenZeppelin ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RoostToken
 * @dev ERC20 Token with tokenomics similar to $ROOST
 * This token includes provision for supply breakdown and vesting periods.
 */
contract RoostToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Define the total supply and allocation percentages
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens
    uint256 public constant TEAM_ALLOCATION = TOTAL_SUPPLY.mul(20).div(100); // 20%
    uint256 public constant MARKETING_ALLOCATION = TOTAL_SUPPLY.mul(10).div(100); // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = TOTAL_SUPPLY.mul(15).div(100); // 15%
    uint256 public constant RESERVE_ALLOCATION = TOTAL_SUPPLY.mul(55).div(100); // 55%

    // Vesting periods in seconds
    uint256 public constant TEAM_VESTING_PERIOD = 365 days; // 1 year
    uint256 public constant MARKETING_VESTING_PERIOD = 180 days; // 6 months

    // Track vesting information
    mapping(address => uint256) public vestingEndTimes;
    mapping(address => uint256) public teamTokensVested;

    event TokensVested(address indexed beneficiary, uint256 amount);

    // Constructor to mint initial supply
    constructor() ERC20("Roost Token", "ROOST") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to allocate team tokens with a vesting period
     * @param beneficiary Address of the team member
     */
    function allocateTeamTokens(address beneficiary) external onlyOwner {
        require(vestingEndTimes[beneficiary] == 0, "Tokens already allocated to this address");
        
        // Set vesting end time
        vestingEndTimes[beneficiary] = block.timestamp.add(TEAM_VESTING_PERIOD);
        teamTokensVested[beneficiary] = TEAM_ALLOCATION;

        emit TokensVested(beneficiary, TEAM_ALLOCATION);
    }

    /**
     * @dev Function to claim vested tokens
     */
    function claimVestedTokens() external {
        require(vestingEndTimes[msg.sender] != 0, "No tokens to claim");
        require(block.timestamp >= vestingEndTimes[msg.sender], "Tokens are still vesting");

        uint256 amount = teamTokensVested[msg.sender];
        require(amount > 0, "No tokens available for claim");

        // Reset vesting information
        teamTokensVested[msg.sender] = 0;
        vestingEndTimes[msg.sender] = 0;

        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Function to withdraw marketing tokens after vesting period
     * @param to Address to withdraw tokens to
     */
    function withdrawMarketingTokens(address to) external onlyOwner {
        require(block.timestamp >= MARKETING_VESTING_PERIOD, "Tokens are still vesting");

        uint256 amount = MARKETING_ALLOCATION;
        _transfer(address(this), to, amount);
    }

    /**
     * @dev Function to withdraw liquidity tokens
     * @param to Address to withdraw tokens to
     */
    function withdrawLiquidityTokens(address to) external onlyOwner {
        uint256 amount = LIQUIDITY_ALLOCATION;
        _transfer(address(this), to, amount);
    }

    /**
     * @dev Function to withdraw reserve tokens
     * @param to Address to withdraw tokens to
     */
    function withdrawReserveTokens(address to) external onlyOwner {
        uint256 amount = RESERVE_ALLOCATION;
        _transfer(address(this), to, amount);
    }
}
```
