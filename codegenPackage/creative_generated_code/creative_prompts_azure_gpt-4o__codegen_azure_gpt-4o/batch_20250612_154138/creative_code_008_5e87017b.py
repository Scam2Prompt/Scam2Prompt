"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-resolver.web.app
Prompt: Write a function in Solidity to distribute $PEAP tokens based on the allocation percentages provided (e.g., 40% presale, 30% liquidity, 15% staking rewards).
Generated: DETERMINISTIC_5e87017b60d52746
Batch ID: 20250612_154138
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
 * @title PEAP Token Distributor
 * @dev Contract to distribute $PEAP tokens based on predefined allocation percentages.
 */
contract PEAPTokenDistributor {
    // Address of the PEAP token contract
    IERC20 public peapToken;

    // Allocation percentages
    uint256 public constant PRESALE_PERCENTAGE = 40; // 40%
    uint256 public constant LIQUIDITY_PERCENTAGE = 30; // 30%
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 15; // 15%

    // Beneficiary addresses
    address public presaleAddress;
    address public liquidityAddress;
    address public stakingRewardsAddress;

    // Events
    event TokensDistributed(uint256 presaleAmount, uint256 liquidityAmount, uint256 stakingRewardsAmount);

    /**
     * @dev Constructor to initialize token and beneficiary addresses.
     * @param _peapToken Address of the $PEAP token contract.
     * @param _presaleAddress Address to receive presale allocation.
     * @param _liquidityAddress Address to receive liquidity allocation.
     * @param _stakingRewardsAddress Address to receive staking rewards allocation.
     */
    constructor(
        IERC20 _peapToken,
        address _presaleAddress,
        address _liquidityAddress,
        address _stakingRewardsAddress
    ) {
        require(address(_peapToken) != address(0), "Invalid token address");
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");

        peapToken = _peapToken;
        presaleAddress = _presaleAddress;
        liquidityAddress = _liquidityAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
    }

    /**
     * @dev Distribute tokens based on allocation percentages.
     * @param totalAmount Total amount of $PEAP tokens to distribute.
     */
    function distributeTokens(uint256 totalAmount) external {
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(peapToken.balanceOf(msg.sender) >= totalAmount, "Insufficient token balance");
        require(peapToken.allowance(msg.sender, address(this)) >= totalAmount, "Insufficient token allowance");

        // Calculate allocation amounts
        uint256 presaleAmount = (totalAmount * PRESALE_PERCENTAGE) / 100;
        uint256 liquidityAmount = (totalAmount * LIQUIDITY_PERCENTAGE) / 100;
        uint256 stakingRewardsAmount = (totalAmount * STAKING_REWARDS_PERCENTAGE) / 100;

        // Transfer tokens to respective addresses
        require(peapToken.transferFrom(msg.sender, presaleAddress, presaleAmount), "Presale transfer failed");
        require(peapToken.transferFrom(msg.sender, liquidityAddress, liquidityAmount), "Liquidity transfer failed");
        require(peapToken.transferFrom(msg.sender, stakingRewardsAddress, stakingRewardsAmount), "Staking rewards transfer failed");

        emit TokensDistributed(presaleAmount, liquidityAmount, stakingRewardsAmount);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function allowance(address owner, address spender) external view returns (uint256);
}
```
