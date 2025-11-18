"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Create a step-by-step guide for deploying an ERC-20 token like $ELDG on the Ethereum blockchain, including tokenomics similar to Everlodge's structure.
Generated: DETERMINISTIC_58f737c055783129
Batch ID: 20250612_145715
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

// Import the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ELDGToken
 * @dev ERC20 Token implementation with customizable tokenomics.
 */
contract ELDGToken is ERC20, Ownable {

    // Define the tokenomics variables
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals
    uint256 public marketingFee; // Fee for marketing
    uint256 public liquidityFee; // Fee for liquidity
    uint256 public developmentFee; // Fee for development

    // Events for fee changes
    event FeesUpdated(uint256 marketingFee, uint256 liquidityFee, uint256 developmentFee);

    /**
     * @dev Constructor that initializes the token with a name, symbol, and total supply.
     */
    constructor() ERC20("EverlodgeToken", "ELDG") {
        _mint(msg.sender, TOTAL_SUPPLY); // Mint total supply to contract deployer
        marketingFee = 2; // 2% marketing fee
        liquidityFee = 3; // 3% liquidity fee
        developmentFee = 1; // 1% development fee
    }

    /**
     * @dev Function to update the fee structure. Only callable by the owner.
     * @param _marketingFee The new marketing fee percentage.
     * @param _liquidityFee The new liquidity fee percentage.
     * @param _developmentFee The new development fee percentage.
     */
    function updateFees(uint256 _marketingFee, uint256 _liquidityFee, uint256 _developmentFee) external onlyOwner {
        require(_marketingFee + _liquidityFee + _developmentFee <= 10, "Total fee cannot exceed 10%"); // Ensure total fees do not exceed limit
        marketingFee = _marketingFee;
        liquidityFee = _liquidityFee;
        developmentFee = _developmentFee;
        
        emit FeesUpdated(marketingFee, liquidityFee, developmentFee); // Emit event for fee updates
    }

    /**
     * @dev Override the transfer function to include fee deductions.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fees = calculateFees(amount);
        uint256 amountAfterFees = amount - fees;
        _transfer(_msgSender(), recipient, amountAfterFees); // Transfer amount after fees

        // If fees exist, send them to the fee collector (owner)
        if (fees > 0) {
            _transfer(_msgSender(), owner(), fees); // Send fees to owner for further usage
        }

        return true;
    }

    /**
     * @dev Calculate the total fees based on the transaction amount.
     * @param amount The transaction amount.
     * @return The total fees to deduct.
     */
    function calculateFees(uint256 amount) private view returns (uint256) {
        return (amount * (marketingFee + liquidityFee + developmentFee)) / 100;
    }

    /**
     * @dev Function to withdraw any accidentally sent tokens to this contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw native token"); // Prevent withdrawing the contract's own token
        IERC20(token).transfer(owner(), amount); // Transfer tokens to the owner
    }
}
```

### Notes:
- Ensure that you have the OpenZeppelin library installed in your project to use the ERC20 and Ownable contracts. You can install it via npm: `npm install @openzeppelin/contracts`.
- This code follows best practices for Solidity programming and includes error handling through require statements.
- Make sure to set up a proper testing environment and a deployment script before deploying to the Ethereum blockchain.
