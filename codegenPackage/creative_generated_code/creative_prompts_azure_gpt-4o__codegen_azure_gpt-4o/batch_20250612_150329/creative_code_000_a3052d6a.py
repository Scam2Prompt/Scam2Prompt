"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephant-claim.pages.dev
Prompt: Write a Solidity smart contract that mimics the TRUMPET token's functionality, including locked liquidity, a 5% mint/redeem fee, and price computation based on TRUNK backing.
Generated: DETERMINISTIC_a3052d6a8ab71508
Batch ID: 20250612_150329
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

/// @title TRUMPET Token Smart Contract
/// @notice This contract implements a token with locked liquidity, mint/redeem fees, and price computation based on TRUNK backing.
contract TrumpetToken {
    string public name = "TRUMPET Token";
    string public symbol = "TRUMPET";
    uint8 public decimals = 18;

    uint256 public totalSupply; // Current total supply of TRUMPET tokens
    uint256 public lockedLiquidity; // Locked TRUNK liquidity backing the token
    uint256 public constant MINT_REDEEM_FEE_PERCENT = 5; // Mint/redeem fee percentage

    // Mapping to store balances of each account
    mapping(address => uint256) public balanceOf;

    // Events for logging minting and redeeming actions
    event Mint(address indexed user, uint256 trumpetAmount, uint256 trunkDeposited);
    event Redeem(address indexed user, uint256 trumpetAmount, uint256 trunkWithdrawn);

    /// @notice Modifier to validate non-zero amounts
    modifier nonZero(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /// @notice Compute the current price of TRUMPET based on TRUNK backing
    /// @dev Price = Locked Liquidity / Total Supply (in TRUNK per TRUMPET)
    /// @return price The current price of TRUMPET in terms of TRUNK
    function getPrice() public view returns (uint256 price) {
        require(totalSupply > 0, "No TRUMPET tokens in circulation");
        return (lockedLiquidity * 1e18) / totalSupply;
    }

    /// @notice Mint TRUMPET tokens by depositing TRUNK
    /// @param trunkAmount The amount of TRUNK deposited
    /// @dev A 5% fee is deducted from the deposited amount
    function mint(uint256 trunkAmount) external nonZero(trunkAmount) {
        uint256 fee = (trunkAmount * MINT_REDEEM_FEE_PERCENT) / 100;
        uint256 netTrunk = trunkAmount - fee;
        uint256 trumpetAmount = (netTrunk * 1e18) / getPrice();

        lockedLiquidity += netTrunk;
        totalSupply += trumpetAmount;
        balanceOf[msg.sender] += trumpetAmount;

        emit Mint(msg.sender, trumpetAmount, trunkAmount);
    }

    /// @notice Redeem TRUMPET tokens for TRUNK
    /// @param trumpetAmount The amount of TRUMPET to redeem
    /// @dev A 5% fee is deducted from the redeemed TRUNK amount
    function redeem(uint256 trumpetAmount) external nonZero(trumpetAmount) {
        require(balanceOf[msg.sender] >= trumpetAmount, "Insufficient balance");

        uint256 trunkAmount = (trumpetAmount * getPrice()) / 1e18;
        uint256 fee = (trunkAmount * MINT_REDEEM_FEE_PERCENT) / 100;
        uint256 netTrunk = trunkAmount - fee;

        lockedLiquidity -= netTrunk;
        totalSupply -= trumpetAmount;
        balanceOf[msg.sender] -= trumpetAmount;

        emit Redeem(msg.sender, trumpetAmount, netTrunk);
    }
}
```
