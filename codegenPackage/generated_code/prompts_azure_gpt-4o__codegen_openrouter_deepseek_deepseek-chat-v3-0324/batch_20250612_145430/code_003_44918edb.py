"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-fork-marekhauzr-main-419labs.vercel.app
Prompt: Provide an example of deploying a DAO on StarkNet L2, utilizing the governance-related resources from the StarkNet ecosystem.
Generated: DETERMINISTIC_44918edb17daa96f
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starknet.public.abi import get_selector_from_name
import asyncio
import os

# Define paths
CONTRACT_DIR = os.path.dirname(__file__)
DAO_CONTRACT_FILE = os.path.join(CONTRACT_DIR, "dao_contract.cairo")
PROPOSAL_CONTRACT_FILE = os.path.join(CONTRACT_DIR, "proposal_contract.cairo")

# Define constants
VOTING_PERIOD = 604800  # 7 days in seconds
QUORUM = 50  # 50% quorum required
VOTE_THRESHOLD = 50  # 50% approval threshold

async def deploy_dao():
    """
    Deploys a DAO with governance functionality on StarkNet.
    """
    try:
        # Initialize StarkNet
        starknet = await Starknet.empty()
        
        # Compile contracts
        dao_contract_definition = compile_starknet_files([DAO_CONTRACT_FILE], debug_info=True)
        proposal_contract_definition = compile_starknet_files([PROPOSAL_CONTRACT_FILE], debug_info=True)
        
        # Deploy DAO contract
        dao_contract = await starknet.deploy(
            contract_def=dao_contract_definition,
            constructor_calldata=[VOTING_PERIOD, QUORUM, VOTE_THRESHOLD]
        )
        
        # Deploy Proposal contract
        proposal_contract = await starknet.deploy(
            contract_def=proposal_contract_definition,
            constructor_calldata=[dao_contract.contract_address]
        )
        
        # Initialize DAO with Proposal contract address
        await dao_contract.initialize(
            proposal_contract_address=proposal_contract.contract_address
        ).invoke()
        
        print(f"DAO Contract deployed at: {hex(dao_contract.contract_address)}")
        print(f"Proposal Contract deployed at: {hex(proposal_contract.contract_address)}")
        
        return dao_contract, proposal_contract
        
    except Exception as e:
        print(f"Error deploying DAO: {str(e)}")
        raise

async def create_proposal(dao_contract, proposal_contract, proposer_address, description):
    """
    Creates a new proposal in the DAO.
    """
    try:
        # Create proposal
        await proposal_contract.create_proposal(
            proposer=proposer_address,
            description=description
        ).invoke()
        
        # Get proposal count
        proposal_count = await dao_contract.get_proposal_count().call()
        print(f"New proposal created. Total proposals: {proposal_count.result[0]}")
        
    except Exception as e:
        print(f"Error creating proposal: {str(e)}")
        raise

async def vote_on_proposal(dao_contract, voter_address, proposal_id, support):
    """
    Votes on a proposal in the DAO.
    """
    try:
        # Vote on proposal
        await dao_contract.vote(
            voter=voter_address,
            proposal_id=proposal_id,
            support=support
        ).invoke()
        
        print(f"Vote cast by {hex(voter_address)} on proposal {proposal_id}")
        
    except Exception as e:
        print(f"Error voting on proposal: {str(e)}")
        raise

async def execute_proposal(dao_contract, proposal_id):
    """
    Executes a proposal if it has passed.
    """
    try:
        # Check if proposal can be executed
        can_execute = await dao_contract.can_execute(proposal_id=proposal_id).call()
        if not can_execute.result[0]:
            print("Proposal cannot be executed yet")
            return False
        
        # Execute proposal
        await dao_contract.execute_proposal(proposal_id=proposal_id).invoke()
        print(f"Proposal {proposal_id} executed successfully")
        return True
        
    except Exception as e:
        print(f"Error executing proposal: {str(e)}")
        raise

async def main():
    """
    Main function to demonstrate DAO deployment and usage.
    """
    # Deploy DAO
    dao_contract, proposal_contract = await deploy_dao()
    
    # Example addresses
    proposer = 0x12345
    voter1 = 0x67890
    voter2 = 0xABCDE
    
    # Create a proposal
    await create_proposal(
        dao_contract,
        proposal_contract,
        proposer,
        "Upgrade protocol parameters"
    )
    
    # Vote on proposal
    await vote_on_proposal(dao_contract, voter1, 0, True)  # For
    await vote_on_proposal(dao_contract, voter2, 0, False) # Against
    
    # Execute proposal (after voting period)
    await execute_proposal(dao_contract, 0)

if __name__ == "__main__":
    asyncio.run(main())
```

```cairo
// dao_contract.cairo
%lang starknet

from starkware.starknet.common.syscalls import get_caller_address
from starkware.cairo.common.uint256 import Uint256, uint256_add, uint256_sub

// Storage variables
@storage_var
func proposal_count() -> (count: felt) {
}

@storage_var
func voting_period() -> (period: felt) {
}

@storage_var
func quorum() -> (quorum: felt) {
}

@storage_var
func vote_threshold() -> (threshold: felt) {
}

@storage_var
func proposal_contract() -> (address: felt) {
}

@storage_var
func proposals(id: felt) -> (
    proposer: felt,
    description: felt,
    start_time: felt,
    end_time: felt,
    for_votes: Uint256,
    against_votes: Uint256,
    executed: felt
) {
}

@storage_var
func has_voted(proposal_id: felt, voter: felt) -> (voted: felt) {
}

// Events
@event
func ProposalCreated(
    proposal_id: felt,
    proposer: felt,
    description: felt,
    start_time: felt,
    end_time: felt
) {
}

@event
func VoteCast(
    voter: felt,
    proposal_id: felt,
    support: felt,
    weight: Uint256
) {
}

@event
func ProposalExecuted(proposal_id: felt) {
}

// Constructor
@constructor
func constructor{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    voting_period_param: felt,
    quorum_param: felt,
    vote_threshold_param: felt
) {
    voting_period.write(voting_period_param);
    quorum.write(quorum_param);
    vote_threshold.write(vote_threshold_param);
    return ();
}

// Initialize with proposal contract address
@external
func initialize{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(proposal_contract_address: felt) {
    proposal_contract.write(proposal_contract_address);
    return ();
}

// Create a new proposal (only callable by proposal contract)
@external
func create_proposal{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    proposer: felt,
    description: felt
) {
    // Only proposal contract can create proposals
    let caller = get_caller_address();
    let proposal_contract_address = proposal_contract.read();
    assert caller = proposal_contract_address;
    
    // Get current time (simplified for example)
    let start_time = 0;  // In production, use block timestamp
    let end_time = start_time + voting_period.read();
    
    // Get new proposal ID
    let (proposal_id) = proposal_count.read();
    proposal_count.write(proposal_id + 1);
    
    // Store proposal
    proposals.write(
        proposal_id,
        proposer,
        description,
        start_time,
        end_time,
        Uint256(0, 0),
        Uint256(0, 0),
        0
    );
    
    // Emit event
    ProposalCreated.emit(proposal_id, proposer, description, start_time, end_time);
    return ();
}

// Vote on a proposal
@external
func vote{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr
}(
    voter: felt,
    proposal_id: felt,
    support: felt
) {
    // Check if voting period is active
    let (_, _, start_time, end_time, _, _, executed) = proposals.read(proposal_id);
    assert executed = 0;  // Proposal not executed
    // assert current_time >= start_time and current_time <= end_time;
    
    // Check if voter has already voted
    let (has_voted_before) = has_voted.read(proposal_id, voter);
    assert has_voted_before = 0;
    
    // Mark as voted
    has_v
