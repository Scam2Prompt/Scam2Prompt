"""
Generated Code Metadata:
========================
Original URL: https://realio-bridge.web.app
Prompt: Create a smart contract that allows users to participate in governance on the Realio Network by delegating their voting rights to validators.
Generated: DETERMINISTIC_e68b9c7914796b1d
Batch ID: 20250612_161500
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title GovernanceContract
 * @dev A smart contract that allows users to delegate their voting rights to validators
 */
contract GovernanceContract is Ownable {
    // Struct to hold information about a delegate
    struct Delegate {
        address validator;
        uint256 votes;
    }

    // Mapping from user address to their delegate
    mapping(address => Delegate) public delegates;

    // Event emitted when a user delegates their votes
    event Delegated(address indexed user, address indexed validator, uint256 votes);

    // Event emitted when a user revokes their delegation
    event Revoked(address indexed user);

    // ERC20 token used for voting
    IERC20 public votingToken;

    /**
     * @dev Constructor to initialize the contract with the voting token address
     * @param _votingToken Address of the ERC20 token used for voting
     */
    constructor(IERC20 _votingToken) {
        votingToken = _votingToken;
    }

    /**
     * @dev Allows a user to delegate their voting rights to a validator
     * @param _validator Address of the validator to whom the votes are delegated
     * @param _votes Amount of votes to delegate
     */
    function delegate(address _validator, uint256 _votes) external {
        require(_votes > 0, "Votes must be greater than zero");
        require(votingToken.balanceOf(msg.sender) >= _votes, "Insufficient token balance");
        
        // Transfer tokens to the contract to ensure the user has delegated their votes
        votingToken.transferFrom(msg.sender, address(this), _votes);

        // Update the delegate mapping
        delegates[msg.sender] = Delegate({
            validator: _validator,
            votes: _votes
        });

        emit Delegated(msg.sender, _validator, _votes);
    }

    /**
     * @dev Allows a user to revoke their delegation
     */
    function revoke() external {
        require(delegates[msg.sender].votes > 0, "No delegation to revoke");

        // Transfer back the tokens to the user
        uint256 votes = delegates[msg.sender].votes;
        votingToken.transfer(msg.sender, votes);

        // Reset the delegate mapping
        delete delegates[msg.sender];

        emit Revoked(msg.sender);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(votingToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        votingToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Returns the current delegate of a user
     * @param _user Address of the user
     * @return validator Address of the validator to whom the user has delegated their votes
     * @return votes Amount of votes delegated
     */
    function getDelegate(address _user) external view returns (address validator, uint256 votes) {
        Delegate memory delegateInfo = delegates[_user];
        return (delegateInfo.validator, delegateInfo.votes);
    }
}
```
