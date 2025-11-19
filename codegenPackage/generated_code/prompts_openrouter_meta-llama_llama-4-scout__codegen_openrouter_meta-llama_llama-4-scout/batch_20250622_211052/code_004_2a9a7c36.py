"""
Generated Code Metadata:
========================
Original URL: https://starknet-quest-fnjdubph5-lfglabs.vercel.app
Prompt: "Design a smart contract for a custom Starknet Quest that issues exclusive tokens upon completion."
Generated: DETERMINISTIC_2a9a7c36111467b1
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IERC20 } from "./IERC20.sol";
import { Ownable } from "./Ownable.sol";

/**
 * @title Starknet Quest Token Contract
 * @author [Your Name]
 * @notice This contract issues exclusive tokens upon completion of a custom Starknet Quest.
 */
contract StarknetQuestToken {
    // Mapping of quest completions to token recipients
    mapping(address => bool) public questCompletions;

    // Mapping of token balances
    mapping(address => uint256) public tokenBalances;

    // Total token supply
    uint256 public totalSupply;

    // Token name and symbol
    string public name;
    string public symbol;

    // Event emitted when a quest is completed and tokens are issued
    event QuestCompleted(address indexed recipient, uint256 amount);

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    /**
     * @notice Initializes the contract with token name, symbol, and total supply.
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _totalSupply Total token supply
     */
    constructor(string memory _name, string memory _symbol, uint256 _totalSupply) {
        name = _name;
        symbol = _symbol;
        totalSupply = _totalSupply;
        tokenBalances[msg.sender] = _totalSupply; // Mint tokens to contract owner
    }

    /**
     * @notice Completes the quest and issues exclusive tokens to the recipient.
     * @param _recipient Address of the recipient
     * @param _amount Amount of tokens to issue
     */
    function completeQuest(address _recipient, uint256 _amount) public onlyOwner {
        require(_amount > 0, "Invalid token amount");
        require(tokenBalances[msg.sender] >= _amount, "Insufficient token balance");

        // Mark quest as completed for recipient
        questCompletions[_recipient] = true;

        // Transfer tokens to recipient
        tokenBalances[msg.sender] -= _amount;
        tokenBalances[_recipient] += _amount;

        emit QuestCompleted(_recipient, _amount);
        emit Transfer(msg.sender, _recipient, _amount);
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param _from Address of the sender
     * @param _to Address of the recipient
     * @param _amount Amount of tokens to transfer
     */
    function transfer(address _from, address _to, uint256 _amount) public {
        require(tokenBalances[_from] >= _amount, "Insufficient token balance");

        tokenBalances[_from] -= _amount;
        tokenBalances[_to] += _amount;

        emit Transfer(_from, _to, _amount);
    }

    /**
     * @notice Returns the token balance of an address.
     * @param _owner Address of the owner
     * @return uint256 Token balance
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return tokenBalances[_owner];
    }

    // Restrict functions to contract owner
    modifier onlyOwner() {
        require(msg.sender == tokenBalances[address(0)], "Only contract owner can call this function");
        _;
    }
}
```

However, I realized you requested a Starknet smart contract. Starknet uses Cairo, not Solidity. Here is the Cairo code:

```cairo
// SPDX-License-Identifier: MIT
// This file is written in Cairo, a programming language used for Starknet smart contracts.

use starknet::Contract;
use starknet::ContractError;

#[starknet::contract]
mod starknet_quest_token {
    #[contract]
    struct StarknetQuestToken {
        quest_completions: Mapping<Address, bool>,
        token_balances: Mapping<Address, Uint256>,
        total_supply: Uint256,
        name: String,
        symbol: String,
    }

    #[external]
    impl StarknetQuestToken {
        fn constructor(name: String, symbol: String, total_supply: Uint256) {
            let mut instance = StarknetQuestToken {
                quest_completions: Mapping::new(),
                token_balances: Mapping::new(),
                total_supply,
                name,
                symbol,
            };
            instance.token_balances.insert(
                ContractAddress::default(),
                &total_supply,
            );
        }

        fn complete_quest(
            &mut self,
            recipient: Address,
            amount: Uint256,
        ) -> Result<(), ContractError> {
            require!(amount > 0, "Invalid token amount");
            require!(
                self.token_balances.get(&ContractAddress::default()).unwrap() >= amount,
                "Insufficient token balance"
            );

            self.quest_completions.insert(recipient, &true);

            self.token_balances
                .insert(ContractAddress::default(), &(self.token_balances.get(&ContractAddress::default()).unwrap() - amount));
            self.token_balances.insert(recipient, &(self.token_balances.get(&recipient).unwrap_or(Uint256::zero()) + amount));

            Ok(())
        }

        fn transfer(&mut self, from: Address, to: Address, amount: Uint256) -> Result<(), ContractError> {
            require!(
                self.token_balances.get(&from).unwrap_or(Uint256::zero()) >= amount,
                "Insufficient token balance"
            );

            self.token_balances
                .insert(from, &(self.token_balances.get(&from).unwrap() - amount));
            self.token_balances.insert(to, &(self.token_balances.get(&to).unwrap_or(Uint256::zero()) + amount));

            Ok(())
        }

        fn balance_of(&self, owner: Address) -> Uint256 {
            self.token_balances.get(&owner).unwrap_or(Uint256::zero())
        }
    }
}
```
