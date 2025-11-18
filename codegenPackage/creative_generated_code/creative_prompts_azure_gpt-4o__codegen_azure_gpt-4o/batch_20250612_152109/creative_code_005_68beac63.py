"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metagalaxyland-migration-v2.pages.dev
Prompt: Develop a smart contract in Solidity that handles the migration of $MEGALAND tokens to $MEGALAND V2 tokens, ensuring the conversion rate of 1380000:1 is enforced.
Generated: DETERMINISTIC_68beac63baa2ab35
Batch ID: 20250612_152109
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
 * @title TokenMigration
 * @dev Smart contract to handle $MEGALAND token migration to $MEGALAND V2 tokens
 *      with a conversion rate of 1,380,000:1.
 */
contract TokenMigration {
    IERC20 public megalandToken; // Address of the $MEGALAND token contract
    IERC20 public megalandV2Token; // Address of the $MEGALAND V2 token contract
    uint256 public constant CONVERSION_RATE = 1380000; // Conversion rate: 1,380,000 to 1
    address public owner; // Contract owner address

    event Migration(address indexed user, uint256 oldTokensBurned, uint256 newTokensMinted);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(address _megalandToken, address _megalandV2Token) {
        require(_megalandToken != address(0), "Invalid $MEGALAND token address");
        require(_megalandV2Token != address(0), "Invalid $MEGALAND V2 token address");

        megalandToken = IERC20(_megalandToken);
        megalandV2Token = IERC20(_megalandV2Token);
        owner = msg.sender;
    }

    /**
     * @notice Migrate $MEGALAND tokens to $MEGALAND V2 tokens
     * @param amount The amount of $MEGALAND tokens to migrate
     */
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(megalandToken.balanceOf(msg.sender) >= amount, "Insufficient $MEGALAND balance");
        require(megalandToken.allowance(msg.sender, address(this)) >= amount, "Token allowance too low");

        // Calculate the amount of $MEGALAND V2 tokens to mint
        uint256 v2Tokens = amount / CONVERSION_RATE;
        require(v2Tokens > 0, "Amount too small for conversion");

        // Burn the user's $MEGALAND tokens
        bool burnSuccess = megalandToken.transferFrom(msg.sender, address(this), amount);
        require(burnSuccess, "$MEGALAND token transfer failed");

        // Mint $MEGALAND V2 tokens to the user
        bool mintSuccess = megalandV2Token.transfer(msg.sender, v2Tokens);
        require(mintSuccess, "$MEGALAND V2 token transfer failed");

        emit Migration(msg.sender, amount, v2Tokens);
    }

    /**
     * @notice Allow the owner to withdraw any leftover tokens
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = token.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
