"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Develop a smart contract in Solidity to manage entry fees and prize distribution for the competitive mode of WhelpS: Slipstream, including a mechanism to burn a portion of the Dragon tokens.
Generated: DETERMINISTIC_d974ea6e8b2b70ad
Batch ID: 20250612_151539
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
 * @title SlipstreamCompetition
 * @dev This smart contract manages entry fees, prize distribution, and token burning
 * for the competitive mode of WhelpS: Slipstream.
 */
contract SlipstreamCompetition {
    // Address of the token contract
    address public dragonTokenAddress;

    // Address of the contract owner
    address public owner;

    // Entry fee in Dragon tokens
    uint256 public entryFee;

    // Percentage of the entry fee to burn
    uint256 public burnPercentage;

    // Event to log prize distribution
    event PrizeDistributed(address indexed winner, uint256 prizeAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _dragonTokenAddress,
        uint256 _entryFee,
        uint256 _burnPercentage
    ) {
        require(_burnPercentage <= 100, "Burn percentage must be <= 100");
        dragonTokenAddress = _dragonTokenAddress;
        entryFee = _entryFee;
        burnPercentage = _burnPercentage;
        owner = msg.sender;
    }

    /**
     * @dev Updates the entry fee. Restricted to the owner.
     * @param _entryFee New entry fee in Dragon tokens.
     */
    function updateEntryFee(uint256 _entryFee) external onlyOwner {
        entryFee = _entryFee;
    }

    /**
     * @dev Updates the burn percentage. Restricted to the owner.
     * @param _burnPercentage New burn percentage (must be <= 100).
     */
    function updateBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage <= 100, "Burn percentage must be <= 100");
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Handles player entry, burns a portion of the entry fee, and stores remaining tokens for prize distribution.
     */
    function enterCompetition() external {
        IERC20 dragonToken = IERC20(dragonTokenAddress);

        // Ensure the player has approved the entry fee transfer
        require(
            dragonToken.allowance(msg.sender, address(this)) >= entryFee,
            "Insufficient allowance for entry fee"
        );

        // Transfer entry fee from player to contract
        require(
            dragonToken.transferFrom(msg.sender, address(this), entryFee),
            "Token transfer failed"
        );

        // Calculate burn amount and remaining amount
        uint256 burnAmount = (entryFee * burnPercentage) / 100;
        uint256 remainingAmount = entryFee - burnAmount;

        // Burn the specified portion of Dragon tokens
        require(
            dragonToken.transfer(address(0), burnAmount),
            "Burn failed"
        );

        // Remaining tokens are held for prize distribution
        // These tokens stay in contract balance
    }

    /**
     * @dev Distributes the prize to the winner. Restricted to the owner.
     * @param winner Address of the winner.
     * @param prizeAmount Amount of Dragon tokens to distribute as prize.
     */
    function distributePrize(address winner, uint256 prizeAmount)
        external
        onlyOwner
    {
        IERC20 dragonToken = IERC20(dragonTokenAddress);

        // Ensure the contract has sufficient balance
        require(
            dragonToken.balanceOf(address(this)) >= prizeAmount,
            "Insufficient contract balance for prize"
        );

        // Transfer prize to the winner
        require(
            dragonToken.transfer(winner, prizeAmount),
            "Prize transfer failed"
        );

        emit PrizeDistributed(winner, prizeAmount);
    }
}

/**
 * @dev Interface for ERC20 token. Minimal implementation for integration.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function allowance(address owner, address spender)
        external
        view
        returns (uint256);
}
```
