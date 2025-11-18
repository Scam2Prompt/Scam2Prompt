"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreifcnpktapdtapj76jqfg5h4rszqmvsurv5ynmixd4gjkfrhunxfiu.ipfs.dweb.link
Prompt: Generate a smart contract snippet for distributing $ARROW tokens to IDO participants on Arrow Markets.
Generated: DETERMINISTIC_8e767aa04e7ade6f
Batch ID: 20250612_152249
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
 * @title TokenDistributor
 * @dev A smart contract to distribute $ARROW tokens to IDO participants
 */
contract TokenDistributor is Ownable {
    // The address of the $ARROW token contract
    IERC20 public arrowToken;

    // Mapping to track the distribution status of each participant
    mapping(address => bool) public hasClaimed;

    // Event to log the distribution of tokens
    event TokensDistributed(address indexed participant, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $ARROW token address
     * @param _arrowTokenAddress The address of the $ARROW token contract
     */
    constructor(address _arrowTokenAddress) {
        require(_arrowTokenAddress != address(0), "Invalid token address");
        arrowToken = IERC20(_arrowTokenAddress);
    }

    /**
     * @dev Distribute tokens to a list of participants
     * @param participants The addresses of the participants to distribute tokens to
     * @param amounts The amounts of tokens to distribute to each participant
     */
    function distributeTokens(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Participants and amounts length mismatch");

        for (uint256 i = 0; i < participants.length; i++) {
            require(participants[i] != address(0), "Invalid participant address");
            require(!hasClaimed[participants[i]], "Tokens already claimed");

            uint256 amount = amounts[i];
            require(arrowToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

            // Transfer tokens to the participant
            hasClaimed[participants[i]] = true;
            arrowToken.transfer(participants[i], amount);
            emit TokensDistributed(participants[i], amount);
        }
    }

    /**
     * @dev Withdraw any remaining tokens from the contract
     * @param _to The address to withdraw tokens to
     * @param _amount The amount of tokens to withdraw
     */
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(arrowToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Transfer remaining tokens to the owner's address
        arrowToken.transfer(_to, _amount);
    }
}
```
