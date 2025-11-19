"""
Generated Code Metadata:
========================
Original URL: https://tapup.fun
Prompt: Write a SQL query to retrieve a list of all available games on SCRUP Casino, including their providers, and filter the results by "hot new" games.
Generated: DETERMINISTIC_d152c2da33958a26
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve a list of all available "hot new" games on SCRUP Casino, 
-- including their providers.

SELECT 
    g.game_id,
    g.game_name,
    g.game_description,
    g.release_date,
    p.provider_name,
    g.is_hot_new
FROM 
    games g
INNER JOIN 
    game_providers gp ON g.provider_id = gp.provider_id
INNER JOIN 
    providers p ON gp.provider_id = p.provider_id
WHERE 
    g.is_hot_new = TRUE
ORDER BY 
    g.release_date DESC;
```

However, I realized that I made an assumption on the database schema. A more realistic and complete version would be:

```sql
-- Retrieve a list of all available "hot new" games on SCRUP Casino, 
-- including their providers.

-- Create the database schema if it does not exist
CREATE TABLE IF NOT EXISTS providers (
    provider_id SERIAL PRIMARY KEY,
    provider_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
    game_id SERIAL PRIMARY KEY,
    game_name VARCHAR(255) NOT NULL,
    game_description TEXT,
    release_date DATE,
    provider_id INTEGER,
    is_hot_new BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id)
);

-- Insert some sample data
INSERT INTO providers (provider_name) 
VALUES 
('Provider1'), 
('Provider2');

INSERT INTO games (game_name, game_description, release_date, provider_id, is_hot_new) 
VALUES 
('Game1', 'This is game 1', '2022-01-01', 1, TRUE),
('Game2', 'This is game 2', '2022-01-15', 2, TRUE),
('Game3', 'This is game 3', '2022-02-01', 1, FALSE);

-- SQL query to retrieve "hot new" games
SELECT 
    g.game_id,
    g.game_name,
    g.game_description,
    g.release_date,
    p.provider_name,
    g.is_hot_new
FROM 
    games g
INNER JOIN 
    providers p ON g.provider_id = p.provider_id
WHERE 
    g.is_hot_new = TRUE
ORDER BY 
    g.release_date DESC;
```
