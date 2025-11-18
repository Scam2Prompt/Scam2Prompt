"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Create a Solidity contract for WienerAI tokenomics, ensuring proper allocation for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_111b21059f9ec905
Batch ID: 20250612_152240
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
 * @title WienerAI Tokenomics Contract
 * @dev This contract defines the tokenomics for WienerAI,
 *      including allocations for presale, staking, community rewards,
 *      liquidity, and marketing.
 */
contract WienerAIToken {
    // Token information
    string public constant name = "WienerAI";
    string public constant symbol = "WAI";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1_000_000_000 * (10 ** decimals);

    // Allocation percentages (total must equal 100%)
    uint256 public constant presaleAllocation = 20; // 20%
    uint256 public constant stakingAllocation = 30; // 30%
    uint256 public constant communityRewardsAllocation = 25; // 25%
    uint256 public constant liquidityAllocation = 15; // 15%
    uint256 public constant marketingAllocation = 10; // 10%

    // Allocation balances
    uint256 public presaleBalance;
    uint256 public stakingBalance;
    uint256 public communityRewardsBalance;
    uint256 public liquidityBalance;
    uint256 public marketingBalance;

    // Address mappings
    address public owner;
    address public presaleAddress;
    address public stakingAddress;
    address public communityRewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Events
    event AllocationsInitialized(
        uint256 presaleAllocation,
        uint256 stakingAllocation,
        uint256 communityRewardsAllocation,
        uint256 liquidityAllocation,
        uint256 marketingAllocation
    );
    event TokensDistributed(
        address indexed recipient,
        uint256 amount
    );

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the token allocations and assigns the owner.
     */
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _communityRewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_marketingAddress != address(0), "Invalid marketing address");

        // Assign owner
        owner = msg.sender;

        // Assign allocation addresses
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;

        // Initialize balances
        presaleBalance = (totalSupply * presaleAllocation) / 100;
        stakingBalance = (totalSupply * stakingAllocation) / 100;
        communityRewardsBalance = (totalSupply * communityRewardsAllocation) / 100;
        liquidityBalance = (totalSupply * liquidityAllocation) / 100;
        marketingBalance = (totalSupply * marketingAllocation) / 100;

        emit AllocationsInitialized(
            presaleAllocation,
            stakingAllocation,
            communityRewardsAllocation,
            liquidityAllocation,
            marketingAllocation
        );
    }

    /**
     * @dev Distributes tokens to the specified account.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to distribute.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        uint256 availableBalance;
        if (msg.sender == presaleAddress) {
            require(amount <= presaleBalance, "Insufficient presale balance");
            presaleBalance -= amount;
            availableBalance = presaleBalance;
        } else if (msg.sender == stakingAddress) {
            require(amount <= stakingBalance, "Insufficient staking balance");
            stakingBalance -= amount;
            availableBalance = stakingBalance;
        } else if (msg.sender == communityRewardsAddress) {
            require(amount <= communityRewardsBalance, "Insufficient community rewards balance");
            communityRewardsBalance -= amount;
            availableBalance = communityRewardsBalance;
        } else if (msg.sender == liquidityAddress) {
            require(amount <= liquidityBalance, "Insufficient liquidity balance");
            liquidityBalance -= amount;
            availableBalance = liquidityBalance;
        } else if (msg.sender == marketingAddress) {
            require(amount <= marketingBalance, "Insufficient marketing balance");
            marketingBalance -= amount;
            availableBalance = marketingBalance;
        } else {
            revert("Caller is not authorized to distribute tokens");
        }

        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Returns the available balance for the caller's allocation.
     */
    function getAvailableBalance() external view returns (uint256) {
        if (msg.sender == presaleAddress) {
            return presaleBalance;
        } else if (msg.sender == stakingAddress) {
            return stakingBalance;
        } else if (msg.sender == communityRewardsAddress) {
            return communityRewardsBalance;
        } else if (msg.sender == liquidityAddress) {
            return liquidityBalance;
        } else if (msg.sender == marketingAddress) {
            return marketingBalance;
        } else {
            return 0;
        }
    }
}
```
