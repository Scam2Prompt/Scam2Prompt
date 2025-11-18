"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardtevara.xyz
Prompt: Develop a leaderboard system for tracking player activity in "Teva Run Sessions" using ZK Stack technology.
Generated: DETERMINISTIC_733e517cf83a0f8f
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
// LeaderboardService.java
package com.teva.run.sessions.service;

import com.teva.run.sessions.model.Player;
import com.teva.run.sessions.repository.PlayerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class LeaderboardService {

    @Autowired
    private PlayerRepository playerRepository;

    /**
     * Fetches the leaderboard sorted by scores in descending order.
     *
     * @return List of players sorted by scores
     */
    public List<Player> getLeaderboard() {
        return playerRepository.findAllByOrderByScoreDesc();
    }

    /**
     * Updates the player's score.
     *
     * @param playerId The ID of the player to update
     * @param score The new score to set
     * @return The updated Player object
     * @throws PlayerNotFoundException if the player does not exist
     */
    public Player updatePlayerScore(Long playerId, int score) throws PlayerNotFoundException {
        Optional<Player> playerOptional = playerRepository.findById(playerId);
        if (playerOptional.isPresent()) {
            Player player = playerOptional.get();
            player.setScore(score);
            return playerRepository.save(player);
        } else {
            throw new PlayerNotFoundException("Player with ID " + playerId + " not found.");
        }
    }
}

// PlayerNotFoundException.java
package com.teva.run.sessions.exception;

public class PlayerNotFoundException extends Exception {
    public PlayerNotFoundException(String message) {
        super(message);
    }
}

// Player.java
package com.teva.run.sessions.model;

import javax.persistence.*;

@Entity
@Table(name = "players")
public class Player {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private int score;

    // Getters and Setters

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
}

// PlayerRepository.java
package com.teva.run.sessions.repository;

import com.teva.run.sessions.model.Player;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PlayerRepository extends JpaRepository<Player, Long> {
    List<Player> findAllByOrderByScoreDesc();
}

// LeaderboardController.java
package com.teva.run.sessions.controller;

import com.teva.run.sessions.exception.PlayerNotFoundException;
import com.teva.run.sessions.model.Player;
import com.teva.run.sessions.service.LeaderboardService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/leaderboard")
public class LeaderboardController {

    @Autowired
    private LeaderboardService leaderboardService;

    /**
     * Retrieve the current leaderboard.
     *
     * @return ResponseEntity with list of players
     */
    @GetMapping
    public ResponseEntity<List<Player>> getLeaderboard() {
        List<Player> leaderboard = leaderboardService.getLeaderboard();
        return ResponseEntity.ok(leaderboard);
    }

    /**
     * Update a player's score.
     *
     * @param playerId The ID of the player
     * @param score The new score
     * @return ResponseEntity with updated player
     */
    @PutMapping("/{playerId}/score")
    public ResponseEntity<Player> updatePlayerScore(@PathVariable Long playerId, @RequestParam int score) {
        try {
            Player updatedPlayer = leaderboardService.updatePlayerScore(playerId, score);
            return ResponseEntity.ok(updatedPlayer);
        } catch (PlayerNotFoundException e) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(null);
        }
    }
}
```

This code provides a basic structure for a leaderboard system in a "Teva Run Sessions" application using Spring Boot (as part of the ZK Stack). It includes a service for handling leaderboard operations, a controller for API endpoints, a model for player representation, repository for data access, and custom exceptions for error handling.
