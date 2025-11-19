"""
Generated Code Metadata:
========================
Original URL: https://tayloud.io
Prompt: Generate a Solidity smart contract that implements the fee split mechanism described on the Loud platform, allocating 4% to the system and distributing rewards to contributors.
Generated: DETERMINISTIC_e62e6b1521621fa8
Batch ID: 20250612_163224
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Loud Fee Split Contract
 * @author [Your Name]
 * @notice This contract implements the fee split mechanism for the Loud platform.
 *         It allocates 4% of the transaction fees to the system and distributes
 *         the remaining rewards to contributors.
 */
contract LoudFeeSplit {
    using SafeMath for uint256;

    // Mapping of contributor addresses to their respective balances
    mapping (address => uint256) public contributorBalances;

    // System wallet address to receive the system fee
    address public systemWallet;

    // System fee percentage (4%)
    uint256 public constant SYSTEM_FEE_PERCENTAGE = 4;

    // Event emitted when a contribution is made
    event ContributionMade(address indexed contributor, uint256 amount);

    // Event emitted when a reward is distributed
    event RewardDistributed(address indexed contributor, uint256 amount);

    // Event emitted when system fee is collected
    event SystemFeeCollected(address indexed systemWallet, uint256 amount);

    /**
     * @dev Constructor to initialize the system wallet address
     * @param _systemWallet Address of the system wallet to receive the system fee
     */
    constructor(address _systemWallet) {
        require(_systemWallet != address(0), "System wallet address cannot be zero");
        systemWallet = _systemWallet;
    }

    /**
     * @dev Function to make a contribution
     * @param _amount Amount of the contribution
     */
    function makeContribution(uint256 _amount) public {
        require(_amount > 0, "Contribution amount must be greater than zero");

        // Update contributor balance
        contributorBalances[msg.sender] = contributorBalances[msg.sender].add(_amount);

        // Emit event
        emit ContributionMade(msg.sender, _amount);
    }

    /**
     * @dev Function to distribute rewards to contributors
     * @param _contributor Address of the contributor to distribute the reward to
     * @param _amount Amount of the reward to distribute
     */
    function distributeReward(address _contributor, uint256 _amount) public {
        require(_contributor != address(0), "Contributor address cannot be zero");
        require(_amount > 0, "Reward amount must be greater than zero");
        require(contributorBalances[_contributor] >= _amount, "Insufficient contributor balance");

        // Update contributor balance
        contributorBalances[_contributor] = contributorBalances[_contributor].sub(_amount);

        // Transfer reward to contributor
        IERC20(0x...).transfer(_contributor, _amount); // Replace 0x... with the actual token address

        // Emit event
        emit RewardDistributed(_contributor, _amount);
    }

    /**
     * @dev Function to collect system fee from a transaction
     * @param _transactionAmount Amount of the transaction
     */
    function collectSystemFee(uint256 _transactionAmount) public {
        require(_transactionAmount > 0, "Transaction amount must be greater than zero");

        // Calculate system fee
        uint256 systemFee = _transactionAmount.mul(SYSTEM_FEE_PERCENTAGE).div(100);

        // Transfer system fee to system wallet
        IERC20(0x...).transfer(systemWallet, systemFee); // Replace 0x... with the actual token address

        // Emit event
        emit SystemFeeCollected(systemWallet, systemFee);
    }

    /**
     * @dev Function to get the contributor balance
     * @param _contributor Address of the contributor
     * @return Contributor balance
     */
    function getContributorBalance(address _contributor) public view returns (uint256) {
        return contributorBalances[_contributor];
    }
}
```
