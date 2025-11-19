"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: Write a Java smart contract for Neo N3 that includes functionality for on-chain governance, allowing NEO token holders to vote for council members and consensus nodes.
Generated: DETERMINISTIC_53ac859be88c0cfc
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using System;
using System.Collections.Generic;

namespace NeoGovernance
{
    public class GovernanceContract : SmartContract
    {
        // Struct to represent a council member
        public struct CouncilMember
        {
            public byte[] Address;
            public string Name;
            public int Votes;
        }

        // List of council members
        private static List<CouncilMember> councilMembers;

        // Mapping of addresses to their voting status
        private static Dictionary<byte[], bool> hasVoted;

        // Event to notify when a new council member is added
        public static event Action<byte[], string> CouncilMemberAdded;

        // Event to notify when a vote is cast
        public static event Action<byte[], byte[]> VoteCast;

        // Initialize the contract
        static GovernanceContract()
        {
            councilMembers = new List<CouncilMember>();
            hasVoted = new Dictionary<byte[], bool>();
        }

        // Function to add a new council member
        public static void AddCouncilMember(byte[] address, string name)
        {
            // Ensure only the contract owner can add members
            if (!Runtime.CheckWitness(OwnerAddress))
                throw new Exception("Unauthorized access");

            // Create a new council member and add to the list
            CouncilMember newMember = new CouncilMember
            {
                Address = address,
                Name = name,
                Votes = 0
            };
            councilMembers.Add(newMember);
            CouncilMemberAdded(address, name);
        }

        // Function to cast a vote for a council member
        public static void Vote(byte[] memberAddress)
        {
            // Ensure the voter has not voted before
            if (hasVoted.ContainsKey(Runtime.CallingScriptHash))
                throw new Exception("You have already voted");

            // Find the council member to vote for
            for (int i = 0; i < councilMembers.Count; i++)
            {
                if (councilMembers[i].Address == memberAddress)
                {
                    // Increment the vote count
                    councilMembers[i].Votes++;
                    hasVoted[Runtime.CallingScriptHash] = true;
                    VoteCast(Runtime.CallingScriptHash, memberAddress);
                    return;
                }
            }

            throw new Exception("Council member not found");
        }

        // Function to get the current council members
        public static CouncilMember[] GetCouncilMembers()
        {
            return councilMembers.ToArray();
        }

        // Function to get the vote count for a specific council member
        public static int GetVoteCount(byte[] memberAddress)
        {
            foreach (var member in councilMembers)
            {
                if (member.Address == memberAddress)
                {
                    return member.Votes;
                }
            }
            throw new Exception("Council member not found");
        }

        // Function to reset the voting status (for new voting rounds)
        public static void ResetVoting()
        {
            hasVoted.Clear();
            foreach (var member in councilMembers)
            {
                member.Votes = 0;
            }
        }

        // Owner address for authorization
        private static byte[] OwnerAddress => (byte[])Storage.Get(Storage.CurrentContext, "owner");

        // Function to set the owner address (only callable once)
        public static void SetOwner(byte[] owner)
        {
            if (OwnerAddress != null)
                throw new Exception("Owner already set");

            Storage.Put(Storage.CurrentContext, "owner", owner);
        }
    }
}
```
