"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Provide an example of a governance proposal for adjusting collateral factors at the Silo level in the Silo Finance protocol.
Generated: DETERMINISTIC_8a3ddc90d897cbe0
Batch ID: 20250612_150228
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

import "@openzeppelin/contracts/governance/Governor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorSettings.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";

interface ISiloManager {
    function setCollateralFactor(address silo, address asset, uint256 collateralFactor) external;
}

contract SiloGovernanceProposal is Governor, GovernorSettings, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction {
    ISiloManager public siloManager;
    address public targetSilo;
    address public targetAsset;
    uint256 public proposedCollateralFactor;

    constructor(
        IVotes _token,
        ISiloManager _siloManager,
        uint256 _initialVotingDelay,
        uint256 _initialVotingPeriod,
        uint256 _initialProposalThreshold,
        uint256 _quorumPercentage
    )
        Governor("SiloGovernanceProposal")
        GovernorSettings(
            _initialVotingDelay, // voting delay
            _initialVotingPeriod, // voting period
            _initialProposalThreshold // proposal threshold
        )
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(_quorumPercentage)
    {
        siloManager = _siloManager;
    }

    function proposeAdjustCollateralFactor(
        address silo,
        address asset,
        uint256 collateralFactor,
        string memory description
    ) public returns (uint256) {
        targetSilo = silo;
        targetAsset = asset;
        proposedCollateralFactor = collateralFactor;

        // Encode the function call to execute
        bytes memory data = abi.encodeWithSelector(
            this.executeAdjustCollateralFactor.selector,
            silo,
            asset,
            collateralFactor
        );

        // Create the proposal
        return Governor.propose(
            getProposalTargets(),
            getProposalValues(),
            getProposalCalldatas(data),
            description
        );
    }

    function executeAdjustCollateralFactor(
        address silo,
        address asset,
        uint256 collateralFactor
    ) public {
        require(
            state(proposalId()) == ProposalState.Succeeded,
            "Proposal must succeed first"
        );
        
        siloManager.setCollateralFactor(silo, asset, collateralFactor);
    }

    function getProposalTargets() private view returns (address[] memory) {
        address[] memory targets = new address[](1);
        targets[0] = address(this);
        return targets;
    }

    function getProposalValues() private pure returns (uint256[] memory) {
        uint256[] memory values = new uint256[](1);
        values[0] = 0;
        return values;
    }

    function getProposalCalldatas(bytes memory data) private pure returns (bytes[] memory) {
        bytes[] memory calldatas = new bytes[](1);
        calldatas[0] = data;
        return calldatas;
    }

    // The following functions are overrides required by Solidity.
    function votingDelay() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.votingDelay();
    }

    function votingPeriod() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.votingPeriod();
    }

    function quorum(uint256 blockNumber)
        public
        view
        override(Governor, GovernorVotesQuorumFraction)
        returns (uint256)
    {
        return super.quorum(blockNumber);
    }

    function proposalThreshold() public view override(Governor, GovernorSettings) returns (uint256) {
        return super.proposalThreshold();
    }
}
```
