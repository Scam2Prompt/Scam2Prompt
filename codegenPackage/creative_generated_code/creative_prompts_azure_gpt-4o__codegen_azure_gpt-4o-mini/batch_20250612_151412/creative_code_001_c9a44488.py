"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr-worldcoin.web.app
Prompt: Generate Solidity code for a smart contract that verifies wallet ownership and facilitates claiming $WLD tokens, referencing the distribution process mentioned on the Worldcoin site.
Generated: DETERMINISTIC_c9a44488b6170d5d
Batch ID: 20250612_151412
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WorldcoinTokenClaimer
 * @dev This contract allows users to verify wallet ownership and claim $WLD tokens.
 * The claim process is based on the distribution rules specified by the Worldcoin project.
 */
contract WorldcoinTokenClaimer is Ownable {
    // The ERC20 token being claimed
    IERC20 public wldToken;

    // Mapping to track claimed wallets
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Sets the WLD token address.
     * @param _wldToken Address of the WLD token contract.
     */
    constructor(address _wldToken) {
        require(_wldToken != address(0), "Invalid token address");
        wldToken = IERC20(_wldToken);
    }

    /**
     * @dev Function to claim WLD tokens.
     * Only wallets that haven't claimed can call this function.
     * @param amount The amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than zero");
        require(wldToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the sender as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer the tokens to the claimant
        bool success = wldToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit an event for the claim
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Owner can withdraw tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(wldToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        bool success = wldToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to check if an address has claimed tokens.
     * @param claimant The address to check.
     * @return A boolean indicating if the address has claimed.
     */
    function hasClaimedTokens(address claimant) external view returns (bool) {
        return hasClaimed[claimant];
    }
}
```
