"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Write a tutorial to build a decentralized application (dApp) on Berachain that utilizes its validator-directed network emissions for DeFi protocols.
Generated: DETERMINISTIC_e503ce6a9990ef64
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dApp Tutorial for Berachain - Validator-Directed Emissions for DeFi

# Import required libraries
from brownie import (
    accounts,
    network,
    config,
    ValidatorEmissions,
    interface,
    Contract,
    project,
)
from brownie.network import priority_fee
from web3 import Web3
import json
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Constants
GAS_LIMIT = 1000000
EMISSION_RATE = Web3.toWei(0.1, "ether")  # 0.1 BERA per block
VALIDATOR_SHARE = 50  # 50% to validators
PROTOCOL_SHARE = 50  # 50% to DeFi protocols

# Main deployment function
def main():
    # Connect to network
    if network.show_active() not in ["berachain_testnet", "berachain_mainnet"]:
        raise ValueError("Please connect to Berachain network")

    # Get deployer account
    deployer = accounts.add(os.getenv("PRIVATE_KEY")) or accounts[0]
    print(f"Deploying contracts with account: {deployer.address}")

    # Set gas strategy
    priority_fee("2 gwei")

    # Deploy ValidatorEmissions contract
    print("Deploying ValidatorEmissions contract...")
    emissions_contract = ValidatorEmissions.deploy(
        EMISSION_RATE,
        VALIDATOR_SHARE,
        PROTOCOL_SHARE,
        {"from": deployer, "gas_limit": GAS_LIMIT},
    )
    print(f"ValidatorEmissions deployed at: {emissions_contract.address}")

    # Verify contract (if on testnet/mainnet)
    if network.show_active() != "development":
        ValidatorEmissions.publish_source(emissions_contract)

    # Interact with contract
    setup_emissions(emissions_contract, deployer)

    return emissions_contract

# Setup emissions distribution
def setup_emissions(contract, deployer):
    # Get validator addresses (mock for tutorial)
    validators = [
        "0xValidator1",
        "0xValidator2",
        "0xValidator3",
    ]

    # Get DeFi protocol addresses (mock for tutorial)
    protocols = [
        {"address": "0xProtocol1", "weight": 30},
        {"address": "0xProtocol2", "weight": 20},
        {"address": "0xProtocol3", "weight": 50},
    ]

    # Register validators
    print("Registering validators...")
    for validator in validators:
        contract.registerValidator(validator, {"from": deployer, "gas_limit": GAS_LIMIT})

    # Register protocols
    print("Registering protocols...")
    for protocol in protocols:
        contract.registerProtocol(
            protocol["address"],
            protocol["weight"],
            {"from": deployer, "gas_limit": GAS_LIMIT},
        )

    # Start emissions
    print("Starting emissions distribution...")
    contract.startEmissions({"from": deployer, "gas_limit": GAS_LIMIT})

# Contract interaction examples
def interact_with_contract(contract_address):
    # Load contract
    contract = Contract.from_abi(
        "ValidatorEmissions", contract_address, ValidatorEmissions.abi
    )

    # Get total emissions
    total_emissions = contract.totalEmissions()
    print(f"Total emissions distributed: {Web3.fromWei(total_emissions, 'ether')} BERA")

    # Get validator rewards
    validator_rewards = contract.getValidatorRewards("0xValidator1")
    print(f"Validator1 rewards: {Web3.fromWei(validator_rewards, 'ether')} BERA")

    # Get protocol rewards
    protocol_rewards = contract.getProtocolRewards("0xProtocol1")
    print(f"Protocol1 rewards: {Web3.fromWei(protocol_rewards, 'ether')} BERA")

# Smart Contract (ValidatorEmissions.sol)
"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ValidatorEmissions {
    address public admin;
    uint256 public emissionRate;
    uint256 public validatorShare;
    uint256 public protocolShare;
    bool public emissionsActive;
    
    mapping(address => uint256) public validatorRewards;
    mapping(address => uint256) public protocolRewards;
    mapping(address => uint256) public protocolWeights;
    address[] public validators;
    address[] public protocols;
    
    uint256 public totalEmissions;
    
    event EmissionsDistributed(uint256 validatorAmount, uint256 protocolAmount);
    event ValidatorRegistered(address validator);
    event ProtocolRegistered(address protocol, uint256 weight);
    
    constructor(
        uint256 _emissionRate,
        uint256 _validatorShare,
        uint256 _protocolShare
    ) {
        require(_validatorShare + _protocolShare == 100, "Shares must sum to 100");
        admin = msg.sender;
        emissionRate = _emissionRate;
        validatorShare = _validatorShare;
        protocolShare = _protocolShare;
    }
    
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin");
        _;
    }
    
    function registerValidator(address _validator) external onlyAdmin {
        require(!isValidator(_validator), "Already registered");
        validators.push(_validator);
        emit ValidatorRegistered(_validator);
    }
    
    function registerProtocol(address _protocol, uint256 _weight) external onlyAdmin {
        require(!isProtocol(_protocol), "Already registered");
        protocols.push(_protocol);
        protocolWeights[_protocol] = _weight;
        emit ProtocolRegistered(_protocol, _weight);
    }
    
    function startEmissions() external onlyAdmin {
        require(!emissionsActive, "Emissions already active");
        emissionsActive = true;
    }
    
    function stopEmissions() external onlyAdmin {
        require(emissionsActive, "Emissions not active");
        emissionsActive = false;
    }
    
    function distributeEmissions() external {
        require(emissionsActive, "Emissions not active");
        require(validators.length > 0, "No validators");
        require(protocols.length > 0, "No protocols");
        
        uint256 validatorAmount = (emissionRate * validatorShare) / 100;
        uint256 protocolAmount = (emissionRate * protocolShare) / 100;
        
        // Distribute to validators equally
        uint256 perValidator = validatorAmount / validators.length;
        for (uint256 i = 0; i < validators.length; i++) {
            validatorRewards[validators[i]] += perValidator;
        }
        
        // Distribute to protocols by weight
        uint256 totalWeight = getTotalProtocolWeight();
        for (uint256 i = 0; i < protocols.length; i++) {
            address protocol = protocols[i];
            uint256 share = (protocolAmount * protocolWeights[protocol]) / totalWeight;
            protocolRewards[protocol] += share;
        }
        
        totalEmissions += emissionRate;
        emit EmissionsDistributed(validatorAmount, protocolAmount);
    }
    
    function getTotalProtocolWeight() public view returns (uint256) {
        uint256 total;
        for (uint256 i = 0; i < protocols.length; i++) {
            total += protocolWeights[protocols[i]];
        }
        return total;
    }
    
    function isValidator(address _address) public view returns (bool) {
        for (uint256 i = 0; i < validators.length; i++) {
            if (validators[i] == _address) return true;
        }
        return false;
    }
    
    function isProtocol(address _address) public view returns (bool) {
        for (uint256 i = 0; i < protocols.length; i++) {
            if (protocols[i] == _address) return true;
        }
        return false;
    }
    
    function getValidatorRewards(address _validator) external view returns (uint256) {
        return validatorRewards[_validator];
    }
    
    function getProtocolRewards(address _protocol) external view returns (uint256) {
        return protocolRewards[_protocol];
    }
}
"""

# Deployment script (deploy.py)
"""
from scripts.berachain_dapp import main

def deploy():
    main()

if __name__ == "__main__":
    deploy()
"""

# Tests (test_emissions.py)
"""
import pytest
from brownie import ValidatorEmissions, accounts, exceptions

@pytest.fixture
def emissions_contract():
    return ValidatorEmissions.deploy(
        Web3.toWei(0.1, "ether"),  # emissionRate
        50,  # validatorShare
        50,  # protocolShare
        {"from": accounts[0]},
    )

def test_initial_state(emissions_contract):
    assert emissions_contract.admin() == accounts[0]
    assert emissions_contract.emissionRate() == Web3.toWei(0.1, "ether")
    assert not emissions_contract.emissionsActive()

def test_validator_registration(emissions_contract):
    emissions_contract.registerValidator(accounts[1], {"from": accounts[
