"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidlrlbotyuulbnias66uqhqkoy7f4px26fibleghikvgo24hd7tje.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that integrates Moonwell's lending protocol for supplying assets and earning interest, ensuring compatibility with Moonbeam and Moonriver networks.
Generated: DETERMINISTIC_be0d47a0070c875d
Batch ID: 20250612_152358
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
 * @title MoonwellLendingIntegration
 * @dev This smart contract integrates Moonwell's lending protocol to allow users to supply assets and earn interest.
 * It is compatible with Moonbeam and Moonriver networks.
 */
interface IMoonwell {
    function mint(uint256 amount) external returns (uint256);
    function redeem(uint256 redeemTokens) external returns (uint256);
    function redeemUnderlying(uint256 redeemAmount) external returns (uint256);
    function balanceOfUnderlying(address owner) external returns (uint256);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MoonwellLendingIntegration {
    address public immutable moonwellToken; // Address of the Moonwell token (e.g., mToken)
    address public immutable underlyingToken; // Address of the underlying ERC20 token

    /**
     * @dev Sets the Moonwell token and underlying token addresses.
     * @param _moonwellToken Address of the Moonwell token (mToken).
     * @param _underlyingToken Address of the underlying ERC20 token.
     */
    constructor(address _moonwellToken, address _underlyingToken) {
        require(_moonwellToken != address(0), "Invalid Moonwell token address");
        require(_underlyingToken != address(0), "Invalid underlying token address");
        moonwellToken = _moonwellToken;
        underlyingToken = _underlyingToken;
    }

    /**
     * @dev Supplies the underlying asset to the Moonwell protocol to start earning interest.
     * @param amount The amount of underlying token to supply.
     */
    function supply(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        IERC20 token = IERC20(underlyingToken);
        IMoonwell moonwell = IMoonwell(moonwellToken);

        // Transfer the underlying token from the caller to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the Moonwell contract to spend the underlying token
        require(token.approve(moonwellToken, amount), "Approval failed");

        // Mint mTokens by supplying the underlying asset
        uint256 result = moonwell.mint(amount);
        require(result == 0, "Minting failed");
    }

    /**
     * @dev Redeems the supplied mTokens for the underlying asset.
     * @param redeemAmount The amount of underlying asset to redeem (in its native units).
     */
    function redeemUnderlying(uint256 redeemAmount) external {
        require(redeemAmount > 0, "Redeem amount must be greater than zero");

        IMoonwell moonwell = IMoonwell(moonwellToken);
        uint256 result = moonwell.redeemUnderlying(redeemAmount);
        require(result == 0, "Redeeming failed");

        // Transfer the redeemed tokens back to the caller
        IERC20 token = IERC20(underlyingToken);
        require(token.transferFrom(address(this), msg.sender, redeemAmount), "Token transfer failed");
    }

    /**
     * @dev Retrieves the balance of the underlying asset supplied by the user.
     * @param user The address of the user.
     * @return The balance of the underlying asset supplied by the user.
     */
    function getUserBalance(address user) external view returns (uint256) {
        IMoonwell moonwell = IMoonwell(moonwellToken);
        return moonwell.balanceOfUnderlying(user);
    }
}
```
