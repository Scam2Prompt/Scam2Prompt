"""
Generated Code Metadata:
========================
Original URL: https://fr-worldcoin.web.app
Prompt: Generate Solidity code for a smart contract that verifies wallet ownership and facilitates claiming $WLD tokens, referencing the distribution process mentioned on the Worldcoin site.
Generated: DETERMINISTIC_c9a44488b6170d5d
Batch ID: 20250612_151412
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WalletOwnershipVerifier
 * @dev A smart contract to verify wallet ownership and facilitate claiming $WLD tokens.
 */
contract WalletOwnershipVerifier is Ownable {
    // Token to be claimed
    IERC20 public wldToken;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to set the WLD token address.
     * @param _wldToken Address of the $WLD token contract.
     */
    constructor(address _wldToken) {
        require(_wldToken != address(0), "Invalid token address");
        wldToken = IERC20(_wldToken);
    }

    /**
     * @dev Function to claim $WLD tokens.
     * @param amount Amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than zero");
        require(wldToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        bool success = wldToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to deposit $WLD tokens into the contract.
     * @param amount Amount of tokens to deposit.
     */
    function depositTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(wldToken.transferFrom(msg.sender, address(this), amount), "Deposit failed");
    }

    /**
     * @dev Function to withdraw any tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(wldToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = wldToken.transfer(msg.sender, amount);
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to check if an address has claimed tokens.
     * @param claimant Address to check.
     * @return bool indicating if the address has claimed.
     */
    function hasClaimedTokens(address claimant) external view returns (bool) {
        return hasClaimed[claimant];
    }
}
```
