"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguclash.ru
Prompt: Provide code examples for integrating the referral tracking feature of PenguClash.ru into a leaderboard system for Pengu Clash using PHP.
Generated: DETERMINISTIC_55cf77bcfe5b94ff
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Class Leaderboard
 * Handles the leaderboard system for Pengu Clash, including referral tracking.
 */
class Leaderboard {
    private $db; // Database connection

    /**
     * Constructor to initialize the database connection.
     * 
     * @param PDO $db Database connection instance
     */
    public function __construct(PDO $db) {
        $this->db = $db;
    }

    /**
     * Fetches the leaderboard with referral tracking.
     * 
     * @return array List of players with their scores and referral counts
     * @throws Exception If the database query fails
     */
    public function getLeaderboard() {
        try {
            $query = "
                SELECT p.id, p.username, p.score, COUNT(r.referrer_id) as referral_count 
                FROM players p
                LEFT JOIN referrals r ON p.id = r.referred_player_id
                GROUP BY p.id
                ORDER BY p.score DESC
            ";

            $stmt = $this->db->prepare($query);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
            
        } catch (PDOException $e) {
            throw new Exception("Failed to fetch leaderboard: " . $e->getMessage());
        }
    }

    /**
     * Adds a referral for a player.
     * 
     * @param int $referrerId The ID of the referrer
     * @param int $referredPlayerId The ID of the new player being referred
     * @return bool True on success, False on failure
     * @throws Exception If the database query fails
     */
    public function addReferral($referrerId, $referredPlayerId) {
        try {
            $query = "INSERT INTO referrals (referrer_id, referred_player_id) VALUES (:referrer_id, :referred_player_id)";
            $stmt = $this->db->prepare($query);
            $stmt->bindParam(':referrer_id', $referrerId);
            $stmt->bindParam(':referred_player_id', $referredPlayerId);
            return $stmt->execute();
            
        } catch (PDOException $e) {
            throw new Exception("Failed to add referral: " . $e->getMessage());
        }
    }

    /**
     * Updates the score of a player.
     * 
     * @param int $playerId The ID of the player
     * @param int $newScore The new score to set
     * @return bool True on success, False on failure
     * @throws Exception If the database query fails
     */
    public function updateScore($playerId, $newScore) {
        try {
            $query = "UPDATE players SET score = :score WHERE id = :id";
            $stmt = $this->db->prepare($query);
            $stmt->bindParam(':score', $newScore);
            $stmt->bindParam(':id', $playerId);
            return $stmt->execute();
            
        } catch (PDOException $e) {
            throw new Exception("Failed to update score: " . $e->getMessage());
        }
    }
}

// Usage example:
// Assuming you have a valid PDO connection $pdo
try {
    $leaderboard = new Leaderboard($pdo);
    $topPlayers = $leaderboard->getLeaderboard();
    print_r($topPlayers); // Display the leaderboard

    // Example of adding a referral
    $leaderboard->addReferral(1, 2); // Player 1 refers Player 2

    // Example of updating a score
    $leaderboard->updateScore(2, 1500); // Update Player 2's score to 1500

} catch (Exception $e) {
    echo "Error: " . $e->getMessage(); // Handle exceptions
}
?>
```
