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
import io.neow3j.devpack.Storage;
import io.neow3j.devpack.StorageContext;
import io.neow3j.devpack.annotations.DisplayName;
import io.neow3j.devpack.annotations.ManifestExtra;
import io.neow3j.devpack.annotations.Permission;
import io.neow3j.devpack.annotations.Safe;
import io.neow3j.devpack.constants.NativeContract;
import io.neow3j.devpack.contracts.ContractManagement;
import io.neow3j.devpack.contracts.NeoToken;
import io.neow3j.devpack.Hash160;
import io.neow3j.devpack.Runtime;
import io.neow3j.devpack.List;
import io.neow3j.devpack.Map;
import io.neow3j.devpack.annotations.OnDeployment;
import io.neow3j.devpack.events.Event2Args;

/**
 * A smart contract for on-chain governance allowing NEO token holders to vote for council members and consensus nodes.
 */
@ManifestExtra(manifest = """
    {
        "name": "NeoGovernance",
        "description": "On-chain governance for NEO token holders to vote for council members and consensus nodes.",
        "author": "NeoDeveloper",
        "email": "contact@neo.org",
        "version": "1.0.0"
    }
""")
@Permission(nativeContract = NativeContract.ContractManagement)
@Permission(nativeContract = NativeContract.NeoToken)
public class NeoGovernance {

    // Storage keys
    private static final byte[] VOTING_PERIOD_KEY = new byte[]{0x01};
    private static final byte[] COUNCIL_MEMBERS_KEY = new byte[]{0x02};
    private static final byte[] CONSENSUS_NODES_KEY = new byte[]{0x03};
    private static final byte[] VOTES_KEY_PREFIX = new byte[]{0x04};
    private static final byte[] VOTER_BALANCE_KEY_PREFIX = new byte[]{0x05};
    private static final StorageContext ctx = Storage.getStorageContext();

    // Events
    @DisplayName("VoteCast")
    private static Event2Args<Hash160, Hash160> onVoteCast;
    @DisplayName("CouncilMemberAdded")
    private static Event2Args<Hash160, String> onCouncilMemberAdded;
    @DisplayName("ConsensusNodeAdded")
    private static Event2Args<Hash160, String> onConsensusNodeAdded;

    /**
     * Initializes the contract with default values.
     */
    @OnDeployment
    public static void deploy(Object data, boolean update) {
        if (!update) {
            // Set default voting period (e.g., 7 days in blocks)
            Storage.put(ctx, VOTING_PERIOD_KEY, 7 * 24 * 60 * 60 / 15); // Assuming 15s block time
        }
    }

    /**
     * Adds a new council member candidate.
     * @param candidate The hash of the council member candidate.
     * @param name The name of the council member candidate.
     */
    @Safe
    public static void addCouncilMember(Hash160 candidate, String name) {
        if (!Runtime.checkWitness(Runtime.getCallingScriptHash())) {
            throw new Exception("Only the contract owner can add council members.");
        }

        List<Map<String, Object>> councilMembers = getCouncilMembers();
        for (int i = 0; i < councilMembers.size(); i++) {
            if (councilMembers.get(i).get("address").equals(candidate)) {
                throw new Exception("Candidate already exists.");
            }
        }

        Map<String, Object> newMember = new Map<>();
        newMember.put("address", candidate);
        newMember.put("name", name);
        newMember.put("votes", 0);
        councilMembers.add(newMember);
        Storage.put(ctx, COUNCIL_MEMBERS_KEY, councilMembers);
        onCouncilMemberAdded.fire(candidate, name);
    }

    /**
     * Adds a new consensus node candidate.
     * @param candidate The hash of the consensus node candidate.
     * @param name The name of the consensus node candidate.
     */
    @Safe
    public static void addConsensusNode(Hash160 candidate, String name) {
        if (!Runtime.checkWitness(Runtime.getCallingScriptHash())) {
            throw new Exception("Only the contract owner can add consensus nodes.");
        }

        List<Map<String, Object>> consensusNodes = getConsensusNodes();
        for (int i = 0; i < consensusNodes.size(); i++) {
            if (consensusNodes.get(i).get("address").equals(candidate)) {
                throw new Exception("Candidate already exists.");
            }
        }

        Map<String, Object> newNode = new Map<>();
        newNode.put("address", candidate);
        newNode.put("name", name);
        newNode.put("votes", 0);
        consensusNodes.add(newNode);
        Storage.put(ctx, CONSENSUS_NODES_KEY, consensusNodes);
        onConsensusNodeAdded.fire(candidate, name);
    }

    /**
     * Casts a vote for a council member or consensus node.
     * @param candidate The hash of the candidate to vote for.
     * @param isCouncilMember True if voting for council member, false for consensus node.
     */
    public static void vote(Hash160 candidate, boolean isCouncilMember) {
        Hash160 voter = Runtime.getCallingScriptHash();
        NeoToken neo = new NeoToken();
        int balance = neo.balanceOf(voter);
        if (balance <= 0) {
            throw new Exception("Voter must hold NEO tokens.");
        }

        // Check if voter has already voted
        byte[] voterKey = concatKey(VOTER_BALANCE_KEY_PREFIX, voter.toByteArray());
        if (Storage.getBoolean(ctx, voterKey)) {
            throw new Exception("Voter has already voted.");
        }

        List<Map<String, Object>> candidates;
        if (isCouncilMember) {
            candidates = getCouncilMembers();
        } else {
            candidates = getConsensusNodes();
        }

        boolean found = false;
        for (int i = 0; i < candidates.size(); i++) {
            Map<String, Object> candidateInfo = candidates.get(i);
            if (candidateInfo.get("address").equals(candidate)) {
                int currentVotes = (int) candidateInfo.get("votes");
                candidateInfo.put("votes", currentVotes + balance);
                found = true;
                break;
            }
        }

        if (!found) {
            throw new Exception("Candidate not found.");
        }

        if (isCouncilMember) {
            Storage.put(ctx, COUNCIL_MEMBERS_KEY, candidates);
        } else {
            Storage.put(ctx, CONSENSUS_NODES_KEY, candidates);
        }

        // Mark voter as having voted
        Storage.put(ctx, voterKey, true);
        onVoteCast.fire(voter, candidate);
    }

    /**
     * Gets the list of council member candidates.
     * @return A list of council member candidates.
     */
    @Safe
    public static List<Map<String, Object>> getCouncilMembers() {
        return Storage.getList(ctx, COUNCIL_MEMBERS_KEY);
    }

    /**
     * Gets the list of consensus node candidates.
     * @return A list of consensus node candidates.
     */
    @Safe
    public static List<Map<String, Object>> getConsensusNodes() {
        return Storage.getList(ctx, CONSENSUS_NODES_KEY);
    }

    /**
     * Gets the current voting period in blocks.
     * @return The voting period in blocks.
     */
    @Safe
    public static int getVotingPeriod() {
        return Storage.getInt(ctx, VOTING_PERIOD_KEY);
    }

    /**
     * Sets the voting period in blocks.
     * @param blocks The new voting period in blocks.
     */
    @Safe
    public static void setVotingPeriod(int blocks) {
        if (!Runtime.checkWitness(Runtime.getCallingScriptHash())) {
            throw new Exception("Only the contract owner can set the voting period.");
        }
        if (blocks <= 0) {
            throw new Exception("Voting period must be positive.");
        }
        Storage.put(ctx, VOTING_PERIOD_KEY, blocks);
    }

    /**
     * Helper method to concatenate a prefix with a key.
     * @param prefix The prefix byte array.
     * @param key The key byte array.
     * @return The concatenated byte array.
     */
    private static byte[] concatKey(byte[] prefix, byte[] key) {
        byte[] result = new byte[prefix.length + key.length];
        System.arraycopy(prefix, 0, result, 0, prefix.length);
        System.arraycopy(key, 0, result, prefix.length, key.length);
        return result;
    }
}
```
