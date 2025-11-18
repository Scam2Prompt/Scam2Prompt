"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofinance.blogspot.com
Prompt: Provide an example of a smart contract that integrates Lido Finance's liquid staking model to allow users to stake fractions of ETH and receive stETH tokens.
Generated: DETERMINISTIC_bff38c7a56dfa92c
Batch ID: 20250612_142640
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

// Importing OpenZeppelin Contracts for ownership and safety checks
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for Lido's Staking Mechanism
interface ILido {
    function submit(address _referral) external payable returns (uint256);
    function getPooledEthByShares(uint256 _sharesAmount) external view returns (uint256);
    function getSharesByPooledEth(uint256 _ethAmount) external view returns (uint256);
}

// Smart Contract for integrating Lido Finance's liquid staking model
contract LidoStakingIntegration is Ownable, ReentrancyGuard {
    // Address for the Lido Staking contract
    ILido public lido;

    // Event emitted when a user stakes ETH
    event Staked(address indexed user, uint256 ethAmount, uint256 stEthAmount);

    /**
     * @dev Constructor that initializes the Lido contract address.
     * @param _lido Address of the Lido staking contract.
     */
    constructor(address _lido) {
        require(_lido != address(0), "Lido address cannot be zero");
        lido = ILido(_lido);
    }

    /**
     * @dev Allows users to stake ETH and receive stETH (Lido's liquid staking token).
     * Emits a Staked event upon success.
     */
    function stakeETH() external payable nonReentrant {
        require(msg.value > 0, "You must send ETH to stake");

        // Interact with Lido's submit function to stake ETH
        // The referral address is set to `address(0)` for no referral
        uint256 stEthAmount = lido.submit{value: msg.value}(address(0));

        // Emit the staking event
        emit Staked(msg.sender, msg.value, stEthAmount);
    }

    /**
     * @dev Allows the owner to update the Lido contract address if needed.
     * @param _lido New address of the Lido staking contract.
     */
    function updateLidoAddress(address _lido) external onlyOwner {
        require(_lido != address(0), "Lido address cannot be zero");
        lido = ILido(_lido);
    }

    /**
     * @dev Fallback function to accept ETH directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw accidentally sent ETH.
     * Can only be called by the owner.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available for withdrawal");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }
}
```
