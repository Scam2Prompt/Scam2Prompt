"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kishu.finance
Prompt: Create a function in Solidity that automatically redistributes rewards to $KISHU token holders in decentralized wallets, ensuring compliance with the token's reward mechanism.
Generated: DETERMINISTIC_d75b1ea89e81a0f8
Batch ID: 20250612_150602
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
 * @title RewardRedistributor
 * @dev A contract to redistribute rewards to KISHU token holders automatically.
 * The contract ensures compliance with the KISHU token's reward mechanism.
 */
contract RewardRedistributor {
    IERC20 public kishuToken; // The KISHU token contract address
    uint256 public totalDistributedRewards; // Tracks total rewards distributed
    address public owner; // Owner of the contract

    event RewardsDistributed(address indexed holder, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the KISHU token address and assign ownership.
     * @param _kishuTokenAddress Address of the KISHU token contract.
     */
    constructor(address _kishuTokenAddress) {
        require(_kishuTokenAddress != address(0), "Invalid token address");
        kishuToken = IERC20(_kishuTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Distributes rewards to KISHU token holders proportionally based on their token balance.
     * @param holders List of wallet addresses holding KISHU tokens.
     * @param totalRewardAmount Total reward amount to be distributed.
     */
    function distributeRewards(address[] calldata holders, uint256 totalRewardAmount) external onlyOwner {
        require(totalRewardAmount > 0, "Reward amount must be greater than zero");
        require(holders.length > 0, "No holders provided");

        uint256 totalSupply = kishuToken.totalSupply();
        require(totalSupply > 0, "Token supply must be greater than zero");

        // Transfer rewards to the contract for distribution
        require(kishuToken.transferFrom(msg.sender, address(this), totalRewardAmount), "Reward transfer failed");

        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            uint256 holderBalance = kishuToken.balanceOf(holder);

            if (holderBalance > 0) {
                // Calculate proportional reward
                uint256 reward = (holderBalance * totalRewardAmount) / totalSupply;

                // Transfer reward to the holder
                require(kishuToken.transfer(holder, reward), "Reward transfer failed");
                emit RewardsDistributed(holder, reward);

                totalDistributedRewards += reward;
            }
        }
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address is invalid");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param recipient Address to send the withdrawn tokens.
     */
    function withdrawTokens(address token, address recipient) external onlyOwner {
        require(recipient != address(0), "Recipient address is invalid");
        IERC20 tokenContract = IERC20(token);
        uint256 balance = tokenContract.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(tokenContract.transfer(recipient, balance), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token interaction.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function totalSupply() external view returns (uint256);
}
```
