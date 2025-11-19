"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Develop a database schema to store information about the IGEOG selection processes, including candidate lists, results, and timelines for various "Editais."
Generated: DETERMINISTIC_75feafd5a596b796
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for IGEOG selection processes

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store information about each Edital (selection process)
CREATE TABLE IF NOT EXISTS Editais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL UNIQUE,  -- Edital number (e.g., "001/2023")
    titulo TEXT NOT NULL,         -- Title/description of the selection process
    data_abertura DATE NOT NULL,  -- Opening date
    data_encerramento DATE,       -- Closing date (nullable)
    status TEXT NOT NULL CHECK(status IN ('ABERTO', 'EM_ANDAMENTO', 'CONCLUIDO', 'CANCELADO')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store candidate information
CREATE TABLE IF NOT EXISTS Candidatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,     -- Brazilian CPF (formatted or unformatted)
    email TEXT NOT NULL UNIQUE,
    telefone TEXT,
    instituicao TEXT,             -- Current institution/affiliation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store candidate applications for each Edital
CREATE TABLE IF NOT EXISTS Inscricoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    edital_id INTEGER NOT NULL,
    candidato_id INTEGER NOT NULL,
    data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('PENDENTE', 'DEFERIDA', 'INDEFERIDA', 'DESISTENTE')),
    observacoes TEXT,
    FOREIGN KEY (edital_id) REFERENCES Editais(id) ON DELETE CASCADE,
    FOREIGN KEY (candidato_id) REFERENCES Candidatos(id) ON DELETE CASCADE,
    UNIQUE(edital_id, candidato_id)  -- Prevent duplicate applications
);

-- Table to store selection process phases/timelines
CREATE TABLE IF NOT EXISTS Fases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    edital_id INTEGER NOT NULL,
    nome TEXT NOT NULL,           -- Phase name (e.g., "Inscrições", "Prova Escrita")
    descricao TEXT,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    ordem INTEGER NOT NULL,       -- Sequence of phases
    FOREIGN KEY (edital_id) REFERENCES Editais(id) ON DELETE CASCADE
);

-- Table to store results for each phase
CREATE TABLE IF NOT EXISTS Resultados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fase_id INTEGER NOT NULL,
    inscricao_id INTEGER NOT NULL,
    nota REAL,                    -- Score (if applicable)
    classificacao INTEGER,        -- Ranking position
    status TEXT NOT NULL CHECK(status IN ('APROVADO', 'REPROVADO', 'ELIMINADO', 'CLASSIFICADO')),
    observacoes TEXT,
    FOREIGN KEY (fase_id) REFERENCES Fases(id) ON DELETE CASCADE,
    FOREIGN KEY (inscricao_id) REFERENCES Inscricoes(id) ON DELETE CASCADE,
    UNIQUE(fase_id, inscricao_id)  -- One result per phase per application
);

-- Table to store documents submitted by candidates
CREATE TABLE IF NOT EXISTS Documentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inscricao_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,           -- Document type (e.g., "CV", "Diploma")
    nome_arquivo TEXT NOT NULL,   -- Original filename
    caminho_arquivo TEXT NOT NULL, -- Path to stored file
    data_upload TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('PENDENTE', 'VALIDADO', 'INVALIDO')),
    observacoes TEXT,
    FOREIGN KEY (inscricao_id) REFERENCES Inscricoes(id) ON DELETE CASCADE
);

-- Table to store notifications or communications
CREATE TABLE IF NOT EXISTS Comunicados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    edital_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    publicado_por TEXT NOT NULL,  -- Name/identifier of the publisher
    FOREIGN KEY (edital_id) REFERENCES Editais(id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when records are modified
CREATE TRIGGER IF NOT EXISTS update_edital_timestamp
AFTER UPDATE ON Editais
FOR EACH ROW
BEGIN
    UPDATE Editais SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_candidato_timestamp
AFTER UPDATE ON Candidatos
FOR EACH ROW
BEGIN
    UPDATE Candidatos SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_inscricao_timestamp
AFTER UPDATE ON Inscricoes
FOR EACH ROW
BEGIN
    UPDATE Inscricoes SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
