"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Create a smart contract to manage USDT prize distribution for participants in the $PLENA Quest, ensuring compliance with Plena Finance's rules.
Generated: DETERMINISTIC_26e8aa186a908050
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
 * @title PrizeDistribution
 * @dev Smart contract to manage USDT prize distribution for participants in the $PLENA Quest.
 */
contract PrizeDistribution {
    // Address of the USDT token contract
    address public usdtToken;

    // Address of the contract owner
    address public owner;

    // Event emitted when a prize is distributed
    event PrizeDistributed(address indexed participant, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _usdtToken Address of the USDT token contract.
     */
    constructor(address _usdtToken) {
        require(_usdtToken != address(0), "Invalid USDT token address");
        usdtToken = _usdtToken;
        owner = msg.sender;
    }

    /**
     * @dev Distribute prize to a participant.
     * @param participant Address of the participant.
     * @param amount Amount of USDT to distribute (in smallest units, e.g., wei).
     */
    function distributePrize(address participant, uint256 amount) external onlyOwner {
        require(participant != address(0), "Invalid participant address");
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the USDT token contract to transfer tokens
        bool success = IERC20(usdtToken).transfer(participant, amount);
        require(success, "USDT transfer failed");

        // Emit the prize distribution event
        emit PrizeDistributed(participant, amount);
    }

    /**
     * @dev Withdraw remaining USDT tokens from the contract (owner-only).
     * @param to Address to send the withdrawn tokens.
     * @param amount Amount of USDT to withdraw (in smallest units, e.g., wei).
     */
    function withdraw(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Interact with the USDT token contract to transfer tokens
        bool success = IERC20(usdtToken).transfer(to, amount);
        require(success, "USDT withdrawal failed");
    }

    /**
     * @dev Change the USDT token contract address (owner-only).
     * @param newUsdtToken Address of the new USDT token contract.
     */
    function updateUsdtTokenAddress(address newUsdtToken) external onlyOwner {
        require(newUsdtToken != address(0), "Invalid USDT token address");
        usdtToken = newUsdtToken;
    }

    /**
     * @dev Change the contract owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

// Interface for interacting with ERC20 tokens (USDT in this case)
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
