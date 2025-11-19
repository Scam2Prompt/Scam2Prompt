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
-- Database schema for entrepreneurs, businesses, and training courses (Italian language)
CREATE TABLE imprenditori (
    id_imprenditore SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    data_nascita DATE,
    codice_fiscale VARCHAR(16) UNIQUE,
    data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    indirizzo TEXT,
    citta VARCHAR(50),
    provincia VARCHAR(2),
    cap VARCHAR(5),
    paese VARCHAR(50)
);

CREATE TABLE settori (
    id_settore SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descrizione TEXT
);

CREATE TABLE aziende (
    id_azienda SERIAL PRIMARY KEY,
    id_imprenditore INTEGER REFERENCES imprenditori(id_imprenditore),
    nome VARCHAR(100) NOT NULL,
    partita_iva VARCHAR(11) UNIQUE NOT NULL,
    indirizzo_sede TEXT,
    citta VARCHAR(50),
    provincia VARCHAR(2),
    cap VARCHAR(5),
    telefono VARCHAR(20),
    email VARCHAR(100),
    sito_web VARCHAR(100),
    data_fondazione DATE,
    id_settore INTEGER REFERENCES settori(id_settore),
    descrizione TEXT,
    data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE corsi_formazione (
    id_corso SERIAL PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    descrizione TEXT,
    durata_ore INTEGER,
    livello VARCHAR(50),
    categoria VARCHAR(50),
    costo DECIMAL(10,2),
    data_inizio DATE,
    data_fine DATE,
    luogo_svolgimento VARCHAR(100),
    posti_disponibili INTEGER,
    requisiti TEXT,
    programma TEXT,
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE docenti (
    id_docente SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    competenze TEXT,
    bio TEXT,
    data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE corsi_docenti (
    id_corso INTEGER REFERENCES corsi_formazione(id_corso),
    id_docente INTEGER REFERENCES docenti(id_docente),
    PRIMARY KEY (id_corso, id_docente)
);

CREATE TABLE iscrizioni_corsi (
    id_iscrizione SERIAL PRIMARY KEY,
    id_imprenditore INTEGER REFERENCES imprenditori(id_imprenditore),
    id_corso INTEGER REFERENCES corsi_formazione(id_corso),
    data_iscrizione TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stato_pagamento VARCHAR(20) DEFAULT 'in attesa',
    metodo_pagamento VARCHAR(30),
    importo_pagato DECIMAL(10,2),
    data_pagamento TIMESTAMP,
    certificato_ottenuto BOOLEAN DEFAULT FALSE,
    valutazione INTEGER CHECK (valutazione BETWEEN 1 AND 5)
);

CREATE TABLE eventi (
    id_evento SERIAL PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    descrizione TEXT,
    data_evento TIMESTAMP NOT NULL,
    luogo VARCHAR(100),
    posti_disponibili INTEGER,
    costo_partecipazione DECIMAL(10,2),
    organizzatore VARCHAR(100),
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE partecipazioni_eventi (
    id_partecipazione SERIAL PRIMARY KEY,
    id_imprenditore INTEGER REFERENCES imprenditori(id_imprenditore),
    id_evento INTEGER REFERENCES eventi(id_evento),
    data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stato_pagamento VARCHAR(20) DEFAULT 'in attesa',
    partecipazione_confermata BOOLEAN DEFAULT FALSE
);

-- Indexes for performance optimization
CREATE INDEX idx_imprenditori_email ON imprenditori(email);
CREATE INDEX idx_aziende_partita_iva ON aziende(partita_iva);
CREATE INDEX idx_corsi_formazione_data ON corsi_formazione(data_inizio, data_fine);
CREATE INDEX idx_iscrizioni_corsi_imprenditore ON iscrizioni_corsi(id_imprenditore);
CREATE INDEX idx_iscrizioni_corsi_corso ON iscrizioni_corsi(id_corso);
```
