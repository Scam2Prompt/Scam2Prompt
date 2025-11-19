"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiro.pages.dev
Prompt: Generate a smart contract in Solidity for a token called $neiro that rewards participants on the Ethereum chain, incorporating features from the Neiro project.
Generated: DETERMINISTIC_cb1f6b40c90494c0
Batch ID: 20250612_155242
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title NeiroToken
 * @dev This contract implements the $neiro token which rewards participants.
 */
contract NeiroToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of tokens
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Mapping to track rewards for each participant
    mapping(address => uint256) private _rewards;
    
    // Event to log reward distribution
    event RewardDistributed(address indexed participant, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Neiro Token", "$NEIRO") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to distribute rewards to a participant.
     * @param participant The address of the participant receiving the reward.
     * @param amount The amount of tokens to reward.
     */
    function distributeReward(address participant, uint256 amount) external onlyOwner {
        require(participant != address(0), "Cannot reward the zero address");
        require(amount > 0, "Reward amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to distribute rewards");

        _transfer(msg.sender, participant, amount);
        _rewards[participant] = _rewards[participant].add(amount);

        emit RewardDistributed(participant, amount);
    }

    /**
     * @dev Function to view total rewards of a participant.
     * @param participant The address of the participant.
     * @return The total rewards of the participant.
     */
    function viewRewards(address participant) external view returns (uint256) {
        return _rewards[participant];
    }

    /**
     * @dev Function to withdraw tokens mistakenly sent to the contract.
     * @param tokenAddress The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        IERC20 token = IERC20(tokenAddress);
        uint256 contractBalance = token.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient token balance in contract");
        
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens by owner.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}
```
