"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Create an example of an ERC-20 token contract in Solidity that implements a halving mechanism similar to BTC20, reducing rewards by 50% every four years.
Generated: DETERMINISTIC_9a7be96825288647
Batch ID: 20250612_151333
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
 * @title HalvingToken
 * @dev ERC-20 Token with a halving mechanism to reduce minting rewards by 50% every four years.
 */
contract HalvingToken {
    // ERC-20 token state variables
    string public name = "HalvingToken";
    string public symbol = "HTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping balances and allowances
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Halving mechanism variables
    uint256 public constant INITIAL_REWARD = 1000 * (10**18); // Initial reward in tokens
    uint256 public constant HALVING_PERIOD = 4 years; // Halving period in seconds
    uint256 public lastHalvingTimestamp;
    uint256 public currentReward;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event RewardHalved(uint256 newReward);

    // Constructor
    constructor() {
        currentReward = INITIAL_REWARD;
        lastHalvingTimestamp = block.timestamp;
    }

    /**
     * @dev Transfer tokens from the sender to a recipient.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     * @return success True if the transfer succeeds.
     */
    function transfer(address _to, uint256 _value) external returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid recipient");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner.
     * @param _spender Address of the spender.
     * @param _value Amount of tokens to approve.
     * @return success True if the approval succeeds.
     */
    function approve(address _spender, uint256 _value) external returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of the owner.
     * @param _from Address of the token owner.
     * @param _to Address of the recipient.
     * @param _value Amount of tokens to transfer.
     * @return success True if the transfer succeeds.
     */
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        require(balanceOf[_from] >= _value, "Insufficient balance");
        require(allowance[_from][msg.sender] >= _value, "Transfer not approved");
        require(_to != address(0), "Invalid recipient");

        balanceOf[_from] -= _value;
        allowance[_from][msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Mint new tokens to a recipient.
     * @param _to Address of the recipient.
     * @return success True if the minting succeeds.
     */
    function mint(address _to) external returns (bool success) {
        _updateReward(); // Check and apply halving if necessary
        require(_to != address(0), "Invalid recipient");

        balanceOf[_to] += currentReward;
        totalSupply += currentReward;

        emit Transfer(address(0), _to, currentReward);
        return true;
    }

    /**
     * @dev Internal function to update the current reward based on halving period.
     * Reduces the reward by 50% every four years.
     */
    function _updateReward() internal {
        if (block.timestamp >= lastHalvingTimestamp + HALVING_PERIOD) {
            currentReward /= 2; // Halve the reward
            lastHalvingTimestamp = block.timestamp; // Update the last halving timestamp

            emit RewardHalved(currentReward);
        }
    }
}
```
