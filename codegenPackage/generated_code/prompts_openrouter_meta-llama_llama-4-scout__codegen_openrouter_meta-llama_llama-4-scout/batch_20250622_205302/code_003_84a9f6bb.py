"""
Generated Code Metadata:
========================
Original URL: https://questsmisten.pw
Prompt: Design a database schema for storing quest information in a multiplayer game.
Generated: DETERMINISTIC_84a9f6bbc9c08c1d
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the multiplayer game
CREATE DATABASE multiplayer_game;

-- Use the database
USE multiplayer_game;

-- Create a table for quests
CREATE TABLE quests (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  reward INT,
  experience_reward INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for quest objectives
CREATE TABLE quest_objectives (
  id INT AUTO_INCREMENT,
  quest_id INT NOT NULL,
  objective_type ENUM('kill', 'collect', 'talk') NOT NULL,
  target VARCHAR(255) NOT NULL,
  quantity INT NOT NULL,
  completed INT DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (quest_id) REFERENCES quests(id) ON DELETE CASCADE
);

-- Create a table for player quests
CREATE TABLE player_quests (
  id INT AUTO_INCREMENT,
  player_id INT NOT NULL,
  quest_id INT NOT NULL,
  status ENUM('pending', 'in_progress', 'completed') NOT NULL DEFAULT 'pending',
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (quest_id) REFERENCES quests(id) ON DELETE CASCADE
);

-- Create a table for quest rewards
CREATE TABLE quest_rewards (
  id INT AUTO_INCREMENT,
  quest_id INT NOT NULL,
  reward_type ENUM('item', 'gold', 'experience') NOT NULL,
  reward_value VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (quest_id) REFERENCES quests(id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_quest_objectives_quest_id ON quest_objectives (quest_id);
CREATE INDEX idx_player_quests_quest_id ON player_quests (quest_id);
CREATE INDEX idx_quest_rewards_quest_id ON quest_rewards (quest_id);

-- Example data
INSERT INTO quests (name, description, reward, experience_reward)
VALUES 
  ('The Lost City', 'Find the lost city deep in the jungle.', 1000, 500),
  ('The Dark Lord', 'Defeat the dark lord and save the kingdom.', 5000, 2000);

INSERT INTO quest_objectives (quest_id, objective_type, target, quantity)
VALUES 
  (1, 'kill', 'Jungle Monster', 10),
  (1, 'collect', 'Ancient Artifact', 5),
  (2, 'talk', 'Village Elder', 1);

INSERT INTO quest_rewards (quest_id, reward_type, reward_value)
VALUES 
  (1, 'item', 'Magic Sword'),
  (1, 'gold', '1000'),
  (2, 'experience', '5000');
```
