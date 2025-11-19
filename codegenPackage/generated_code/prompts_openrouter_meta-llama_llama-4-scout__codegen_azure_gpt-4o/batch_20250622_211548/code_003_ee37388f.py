"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate a smart contract code in Solidity to facilitate Ethereum governance token evolution, specifically for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_ee37388f331fd019
Batch ID: 20250622_211548
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
 * @title GovernanceToken
 * @dev A smart contract for an ERC20-based governance token designed for DeFi applications.
 *      This contract includes minting, burning, and delegation functionality for governance purposes.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GovernanceToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping for delegation
    mapping(address => address) private _delegates;

    // Checkpoints for vote balances
    struct Checkpoint {
        uint32 fromBlock;
        uint256 votes;
    }

    mapping(address => Checkpoint[]) private _checkpoints;

    // Total supply cap for the governance token
    uint256 public immutable maxSupply;

    // Events
    event DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate);
    event DelegateVotesChanged(address indexed delegate, uint256 previousBalance, uint256 newBalance);

    /**
     * @dev Constructor to initialize the governance token.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param _maxSupply Maximum supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 _maxSupply) ERC20(name, symbol) {
        require(_maxSupply > 0, "Max supply must be greater than zero");
        maxSupply = _maxSupply;
    }

    /**
     * @dev Mint new tokens. Only the owner can mint tokens.
     * @param to Address to receive the minted tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply().add(amount) <= maxSupply, "Minting exceeds max supply");
        _mint(to, amount);
        _moveDelegates(address(0), _delegates[to], amount);
    }

    /**
     * @dev Burn tokens. Only the owner can burn tokens.
     * @param from Address from which tokens will be burned.
     * @param amount Amount of tokens to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
        _moveDelegates(_delegates[from], address(0), amount);
    }

    /**
     * @dev Delegate votes from the sender to a delegatee.
     * @param delegatee The address to delegate votes to.
     */
    function delegate(address delegatee) external {
        address currentDelegate = _delegates[msg.sender];
        uint256 delegatorBalance = balanceOf(msg.sender);
        _delegates[msg.sender] = delegatee;

        emit DelegateChanged(msg.sender, currentDelegate, delegatee);

        _moveDelegates(currentDelegate, delegatee, delegatorBalance);
    }

    /**
     * @dev Get the current delegate for an account.
     * @param account The address of the account.
     * @return The address of the delegate.
     */
    function delegates(address account) external view returns (address) {
        return _delegates[account];
    }

    /**
     * @dev Get the current votes balance for a delegate.
     * @param account The address of the delegate.
     * @return The number of votes.
     */
    function getVotes(address account) external view returns (uint256) {
        uint256 nCheckpoints = _checkpoints[account].length;
        return nCheckpoints > 0 ? _checkpoints[account][nCheckpoints - 1].votes : 0;
    }

    /**
     * @dev Internal function to move delegates and update vote balances.
     * @param from The address of the previous delegate.
     * @param to The address of the new delegate.
     * @param amount The amount of votes to move.
     */
    function _moveDelegates(address from, address to, uint256 amount) internal {
        if (from != to && amount > 0) {
            if (from != address(0)) {
                uint256 fromVotes = _getVotes(from);
                uint256 newFromVotes = fromVotes.sub(amount);
                _writeCheckpoint(from, newFromVotes);
                emit DelegateVotesChanged(from, fromVotes, newFromVotes);
            }

            if (to != address(0)) {
                uint256 toVotes = _getVotes(to);
                uint256 newToVotes = toVotes.add(amount);
                _writeCheckpoint(to, newToVotes);
                emit DelegateVotesChanged(to, toVotes, newToVotes);
            }
        }
    }

    /**
     * @dev Internal function to write a checkpoint for vote balances.
     * @param delegate The address of the delegate.
     * @param newVotes The new vote balance.
     */
    function _writeCheckpoint(address delegate, uint256 newVotes) internal {
        uint32 blockNumber = safe32(block.number, "Block number exceeds 32 bits");
        uint256 nCheckpoints = _checkpoints[delegate].length;

        if (nCheckpoints > 0 && _checkpoints[delegate][nCheckpoints - 1].fromBlock == blockNumber) {
            _checkpoints[delegate][nCheckpoints - 1].votes = newVotes;
        } else {
            _checkpoints[delegate].push(Checkpoint(blockNumber, newVotes));
        }
    }

    /**
     * @dev Internal function to get the current votes for a delegate.
     * @param delegate The address of the delegate.
     * @return The number of votes.
     */
    function _getVotes(address delegate) internal view returns (uint256) {
        uint256 nCheckpoints = _checkpoints[delegate].length;
        return nCheckpoints > 0 ? _checkpoints[delegate][nCheckpoints - 1].votes : 0;
    }

    /**
     * @dev Safe casting of uint256 to uint32.
     * @param n The number to cast.
     * @param errorMessage Error message if casting fails.
     * @return The casted number.
     */
    function safe32(uint256 n, string memory errorMessage) internal pure returns (uint32) {
        require(n < 2**32, errorMessage);
        return uint32(n);
    }
}
```
