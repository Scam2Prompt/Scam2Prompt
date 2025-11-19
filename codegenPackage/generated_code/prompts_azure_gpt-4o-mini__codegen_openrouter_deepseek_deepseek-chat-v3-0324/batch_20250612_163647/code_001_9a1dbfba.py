"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Generate a code example for creating a Decentralized Autonomous Organization (DAO) on Ethereum, highlighting its unique governance token features.
Generated: DETERMINISTIC_9a1dbfbaa93e1cdf
Batch ID: 20250612_163647
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

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/governance/Governor.sol";
import "@openzeppelin/contracts/governance/compatibility/GovernorCompatibilityBravo.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";

contract GovernanceToken is ERC20Votes, Ownable {
    uint256 public constant MAX_SUPPLY = 1000000 * 10**18;

    constructor() ERC20("GovernanceToken", "GT") ERC20Permit("GovernanceToken") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }
}

contract TimeLock is Ownable {
    uint256 public constant MIN_DELAY = 3600; // 1 hour
    uint256 public constant MAX_DELAY = 86400; // 1 day
    uint256 public constant GRACE_PERIOD = 86400; // 1 day

    mapping(bytes32 => bool) public queued;
    uint256 public delay;

    event QueueTransaction(
        bytes32 indexed txHash,
        address indexed target,
        uint256 value,
        string signature,
        bytes data,
        uint256 eta
    );
    event ExecuteTransaction(
        bytes32 indexed txHash,
        address indexed target,
        uint256 value,
        string signature,
        bytes data,
        uint256 eta
    );
    event CancelTransaction(
        bytes32 indexed txHash,
        address indexed target,
        uint256 value,
        string signature,
        bytes data,
        uint256 eta
    );

    constructor(uint256 _delay) {
        require(_delay >= MIN_DELAY && _delay <= MAX_DELAY, "Invalid delay");
        delay = _delay;
    }

    receive() external payable {}

    function queueTransaction(
        address target,
        uint256 value,
        string memory signature,
        bytes memory data,
        uint256 eta
    ) public onlyOwner returns (bytes32) {
        require(eta >= block.timestamp + delay, "ETA must satisfy delay");

        bytes32 txHash = keccak256(
            abi.encode(target, value, signature, data, eta)
        );
        queued[txHash] = true;

        emit QueueTransaction(txHash, target, value, signature, data, eta);
        return txHash;
    }

    function executeTransaction(
        address target,
        uint256 value,
        string memory signature,
        bytes memory data,
        uint256 eta
    ) public payable onlyOwner returns (bytes memory) {
        bytes32 txHash = keccak256(
            abi.encode(target, value, signature, data, eta)
        );
        require(queued[txHash], "Transaction hasn't been queued");
        require(block.timestamp >= eta, "Transaction hasn't surpassed time lock");
        require(block.timestamp <= eta + GRACE_PERIOD, "Transaction is stale");

        queued[txHash] = false;

        bytes memory callData;
        if (bytes(signature).length == 0) {
            callData = data;
        } else {
            callData = abi.encodePacked(
                bytes4(keccak256(bytes(signature))),
                data
            );
        }

        (bool success, bytes memory returnData) = target.call{value: value}(
            callData
        );
        require(success, "Transaction execution reverted");

        emit ExecuteTransaction(txHash, target, value, signature, data, eta);
        return returnData;
    }

    function cancelTransaction(
        address target,
        uint256 value,
        string memory signature,
        bytes memory data,
        uint256 eta
    ) public onlyOwner {
        bytes32 txHash = keccak256(
            abi.encode(target, value, signature, data, eta)
        );
        require(queued[txHash], "Transaction hasn't been queued");

        queued[txHash] = false;

        emit CancelTransaction(txHash, target, value, signature, data, eta);
    }
}

contract DAOGovernor is
    Governor,
    GovernorCompatibilityBravo,
    GovernorVotes,
    GovernorTimelockControl
{
    uint256 public constant VOTING_DELAY = 1;
    uint256 public constant VOTING_PERIOD = 50400; // 1 week in blocks
    uint256 public constant PROPOSAL_THRESHOLD = 1000 * 10**18; // 1000 tokens

    constructor(ERC20Votes _token, TimeLock _timelock)
        Governor("DAOGovernor")
        GovernorVotes(_token)
        GovernorTimelockControl(_timelock)
    {}

    function votingDelay() public pure override returns (uint256) {
        return VOTING_DELAY;
    }

    function votingPeriod() public pure override returns (uint256) {
        return VOTING_PERIOD;
    }

    function proposalThreshold() public pure override returns (uint256) {
        return PROPOSAL_THRESHOLD;
    }

    function quorum(uint256 blockNumber)
        public
        pure
        override
        returns (uint256)
    {
        return 4000 * 10**18; // 4000 tokens
    }

    function state(uint256 proposalId)
        public
        view
        override(Governor, GovernorTimelockControl)
        returns (ProposalState)
    {
        return super.state(proposalId);
    }

    function propose(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        string memory description
    ) public override(Governor, GovernorCompatibilityBravo) returns (uint256) {
        return super.propose(targets, values, calldatas, description);
    }

    function _execute(
        uint256 proposalId,
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor, GovernorTimelockControl) {
        super._execute(proposalId, targets, values, calldatas, descriptionHash);
    }

    function _cancel(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor, GovernorTimelockControl) returns (uint256) {
        return super._cancel(targets, values, calldatas, descriptionHash);
    }

    function _executor()
        internal
        view
        override(Governor, GovernorTimelockControl)
        returns (address)
    {
        return super._executor();
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(Governor, GovernorTimelockControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
