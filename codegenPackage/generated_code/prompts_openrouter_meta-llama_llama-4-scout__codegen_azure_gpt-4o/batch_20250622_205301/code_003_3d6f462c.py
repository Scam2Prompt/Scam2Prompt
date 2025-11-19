"""
Generated Code Metadata:
========================
Original URL: https://taiyoil.web.app
Prompt: Design a simple smart contract using Solidity to manage the minting and distribution of Taiyo Oil, including the logic for rewarding Taiyo Pilots based on oil purchased.
Generated: DETERMINISTIC_3d6f462cc407f9d4
Batch ID: 20250622_205301
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

/**
 * @title TaiyoOilContract
 * @dev A smart contract to manage the minting and distribution of Taiyo Oil,
 *      including rewarding Taiyo Pilots based on oil purchased.
 */
contract TaiyoOilContract {
    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total supply of Taiyo Oil
    uint256 public rewardRate; // Reward rate for Taiyo Pilots

    mapping(address => uint256) public balances; // Balances of Taiyo Oil for each address
    mapping(address => uint256) public rewards; // Rewards for Taiyo Pilots

    // Events
    event Mint(address indexed to, uint256 amount);
    event Purchase(address indexed buyer, uint256 amount);
    event RewardDistributed(address indexed pilot, uint256 reward);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, uint256 _rewardRate) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        rewardRate = _rewardRate;
        balances[owner] = _initialSupply; // Assign initial supply to the owner
    }

    /**
     * @dev Mint new Taiyo Oil tokens.
     * @param _to Address to receive the minted tokens.
     * @param _amount Amount of tokens to mint.
     */
    function mint(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Cannot mint to the zero address");
        require(_amount > 0, "Mint amount must be greater than zero");

        totalSupply += _amount;
        balances[_to] += _amount;

        emit Mint(_to, _amount);
    }

    /**
     * @dev Purchase Taiyo Oil tokens.
     * @param _amount Amount of tokens to purchase.
     */
    function purchase(uint256 _amount) external payable {
        require(_amount > 0, "Purchase amount must be greater than zero");
        require(balances[owner] >= _amount, "Insufficient supply for purchase");

        uint256 cost = _amount; // Assuming 1 token = 1 wei for simplicity
        require(msg.value >= cost, "Insufficient payment for purchase");

        // Transfer tokens from owner to buyer
        balances[owner] -= _amount;
        balances[msg.sender] += _amount;

        // Calculate and distribute rewards to the buyer (Taiyo Pilot)
        uint256 reward = (_amount * rewardRate) / 100; // Reward based on reward rate
        rewards[msg.sender] += reward;

        emit Purchase(msg.sender, _amount);
        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @dev Check the balance of Taiyo Oil for a specific address.
     * @param _account Address to check the balance for.
     * @return Balance of Taiyo Oil.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Check the reward balance for a specific Taiyo Pilot.
     * @param _pilot Address of the Taiyo Pilot.
     * @return Reward balance.
     */
    function rewardBalanceOf(address _pilot) external view returns (uint256) {
        return rewards[_pilot];
    }

    /**
     * @dev Withdraw contract funds (only owner).
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }
}
```
