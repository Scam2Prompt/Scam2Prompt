"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Generate a sample database schema to store information about entrepreneurs, businesses, and training courses, using Italian as the primary language.
Generated: DETERMINISTIC_1839eca183d02ad1
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Creazione dello schema del database per imprenditori, aziende e corsi di formazione

-- Tabella per gli imprenditori
CREATE TABLE imprenditori (
    id_imprenditore INT AUTO_INCREMENT PRIMARY KEY, -- Identificativo unico per l'imprenditore
    nome VARCHAR(100) NOT NULL,                    -- Nome dell'imprenditore
    cognome VARCHAR(100) NOT NULL,                 -- Cognome dell'imprenditore
    email VARCHAR(150) UNIQUE NOT NULL,            -- Email dell'imprenditore (deve essere unica)
    telefono VARCHAR(20),                          -- Numero di telefono dell'imprenditore
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Data di creazione del record
);

-- Tabella per le aziende
CREATE TABLE aziende (
    id_azienda INT AUTO_INCREMENT PRIMARY KEY,     -- Identificativo unico per l'azienda
    nome_azienda VARCHAR(150) NOT NULL,            -- Nome dell'azienda
    settore VARCHAR(100),                          -- Settore di attività dell'azienda
    partita_iva VARCHAR(20) UNIQUE NOT NULL,       -- Partita IVA dell'azienda (deve essere unica)
    id_imprenditore INT NOT NULL,                  -- Collegamento all'imprenditore proprietario
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data di creazione del record
    FOREIGN KEY (id_imprenditore) REFERENCES imprenditori(id_imprenditore) -- Relazione con la tabella imprenditori
);

-- Tabella per i corsi di formazione
CREATE TABLE corsi_formazione (
    id_corso INT AUTO_INCREMENT PRIMARY KEY,       -- Identificativo unico per il corso
    titolo VARCHAR(150) NOT NULL,                  -- Titolo del corso
    descrizione TEXT,                              -- Descrizione del corso
    data_inizio DATE NOT NULL,                     -- Data di inizio del corso
    data_fine DATE NOT NULL,                       -- Data di fine del corso
    prezzo DECIMAL(10, 2) NOT NULL,                -- Prezzo del corso
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Data di creazione del record
);

-- Tabella per la registrazione degli imprenditori ai corsi di formazione
CREATE TABLE iscrizioni_corsi (
    id_iscrizione INT AUTO_INCREMENT PRIMARY KEY,  -- Identificativo unico per l'iscrizione
    id_imprenditore INT NOT NULL,                  -- Collegamento all'imprenditore
    id_corso INT NOT NULL,                         -- Collegamento al corso di formazione
    data_iscrizione TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Data di iscrizione al corso
    FOREIGN KEY (id_imprenditore) REFERENCES imprenditori(id_imprenditore), -- Relazione con la tabella imprenditori
    FOREIGN KEY (id_corso) REFERENCES corsi_formazione(id_corso) -- Relazione con la tabella corsi_formazione
);

-- Indici per migliorare le prestazioni delle query
CREATE INDEX idx_imprenditore_email ON imprenditori(email); -- Indice sull'email degli imprenditori
CREATE INDEX idx_azienda_partita_iva ON aziende(partita_iva); -- Indice sulla partita IVA delle aziende
CREATE INDEX idx_corso_data ON corsi_formazione(data_inizio, data_fine); -- Indice sulle date dei corsi
```
