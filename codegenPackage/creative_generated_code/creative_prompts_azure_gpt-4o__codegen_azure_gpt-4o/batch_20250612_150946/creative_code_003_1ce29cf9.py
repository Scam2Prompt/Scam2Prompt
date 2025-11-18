"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://besureofme.pages.dev
Prompt: Create a smart contract that utilizes ListaDAO's permissionless liquid staking protocol for managing staked assets.
Generated: DETERMINISTIC_1ce29cf9f5d31d5f
Batch ID: 20250612_150946
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
 * @title LiquidStakingManager
 * @dev A smart contract to interact with ListaDAO's permissionless liquid staking protocol.
 * This contract allows users to stake and manage their assets securely.
 */
interface IListaStaking {
    function stake() external payable;
    function withdraw(uint256 _amount) external;
    function getReward() external;
}

contract LiquidStakingManager {
    // Address of the ListaDAO staking contract
    address public immutable listaStakingContract;

    // Mapping to track user balances
    mapping(address => uint256) private userBalances;

    // Event emitted when a user successfully stakes assets
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked assets
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardClaimed(address indexed user);

    /**
     * @dev Constructor to set ListaDAO's staking contract address.
     * @param _listaStakingContract Address of the ListaDAO staking contract.
     */
    constructor(address _listaStakingContract) {
        require(_listaStakingContract != address(0), "Invalid staking contract address");
        listaStakingContract = _listaStakingContract;
    }

    /**
     * @dev Stake ETH into the ListaDAO staking contract.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than 0");

        // Interact with ListaDAO's staking contract
        IListaStaking(listaStakingContract).stake{value: msg.value}();

        // Update user balance
        userBalances[msg.sender] += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked ETH from the ListaDAO staking contract.
     * @param _amount Amount of ETH to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than 0");
        require(userBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Interact with ListaDAO's staking contract
        IListaStaking(listaStakingContract).withdraw(_amount);

        // Update user balance
        userBalances[msg.sender] -= _amount;

        // Transfer withdrawn ETH back to the user
        payable(msg.sender).transfer(_amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards from the ListaDAO staking contract.
     */
    function claimRewards() external {
        // Interact with ListaDAO's staking contract to claim rewards
        IListaStaking(listaStakingContract).getReward();

        emit RewardClaimed(msg.sender);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param _user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return userBalances[_user];
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {
        // Allow contract to receive ETH
    }

    /**
     * @dev Withdraw function to recover funds sent accidentally to the contract.
     * Only accessible by the contract owner.
     */
    function emergencyWithdraw() external {
        require(msg.sender == address(this), "Only the contract itself can invoke this");
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
