"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create a database schema for storing information about tools and equipment, including fields for "material," "mechanism," "implemento," and "aparelho," inspired by the Geyciane Ferramentas content.
Generated: DETERMINISTIC_78a793b0088e017c
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing information about tools and equipment
CREATE DATABASE FerramentasDB;

-- Use the created database
USE FerramentasDB;

-- Create a table for storing tool categories
CREATE TABLE Categorias (
    IdCategoria INT AUTO_INCREMENT,
    NomeCategoria VARCHAR(255) NOT NULL,
    DescricaoCategoria TEXT,
    PRIMARY KEY (IdCategoria)
);

-- Create a table for storing tool materials
CREATE TABLE Materiais (
    IdMaterial INT AUTO_INCREMENT,
    NomeMaterial VARCHAR(255) NOT NULL,
    DescricaoMaterial TEXT,
    PRIMARY KEY (IdMaterial)
);

-- Create a table for storing tool mechanisms
CREATE TABLE Mecanismos (
    IdMecanismo INT AUTO_INCREMENT,
    NomeMecanismo VARCHAR(255) NOT NULL,
    DescricaoMecanismo TEXT,
    PRIMARY KEY (IdMecanismo)
);

-- Create a table for storing tools and equipment
CREATE TABLE Ferramentas (
    IdFerramenta INT AUTO_INCREMENT,
    NomeFerramenta VARCHAR(255) NOT NULL,
    MaterialId INT,
    MecanismoId INT,
    Implemento VARCHAR(255),
    Aparelho VARCHAR(255),
    IdCategoria INT,
    DescricaoFerramenta TEXT,
    PRIMARY KEY (IdFerramenta),
    FOREIGN KEY (MaterialId) REFERENCES Materiais(IdMaterial),
    FOREIGN KEY (MecanismoId) REFERENCES Mecanismos(IdMecanismo),
    FOREIGN KEY (IdCategoria) REFERENCES Categorias(IdCategoria)
);

-- Create a table for storing additional information about tools and equipment
CREATE TABLE InformacoesAdicionais (
    IdInformacao INT AUTO_INCREMENT,
    FerramentaId INT,
    Marca VARCHAR(255),
    Modelo VARCHAR(255),
    AnoFabricacao INT,
    PRIMARY KEY (IdInformacao),
    FOREIGN KEY (FerramentaId) REFERENCES Ferramentas(IdFerramenta)
);

-- Create indexes for faster queries
CREATE INDEX idx_Ferramentas_NomeFerramenta ON Ferramentas (NomeFerramenta);
CREATE INDEX idx_Ferramentas_MaterialId ON Ferramentas (MaterialId);
CREATE INDEX idx_Ferramentas_MecanismoId ON Ferramentas (MecanismoId);
CREATE INDEX idx_Ferramentas_IdCategoria ON Ferramentas (IdCategoria);

-- Example data insertion
INSERT INTO Categorias (NomeCategoria, DescricaoCategoria)
VALUES 
('Ferramentas de Corte', 'Ferramentas utilizadas para cortar materiais'),
('Ferramentas de Perfuração', 'Ferramentas utilizadas para perfurar materiais');

INSERT INTO Materiais (NomeMaterial, DescricaoMaterial)
VALUES 
('Aço', 'Material resistente e durável'),
('Alumínio', 'Material leve e resistente à corrosão');

INSERT INTO Mecanismos (NomeMecanismo, DescricaoMecanismo)
VALUES 
('Mecanismo de Corte', 'Mecanismo utilizado para cortar materiais'),
('Mecanismo de Perfuração', 'Mecanismo utilizado para perfurar materiais');

INSERT INTO Ferramentas (NomeFerramenta, MaterialId, MecanismoId, Implemento, Aparelho, IdCategoria, DescricaoFerramenta)
VALUES 
('Serra', 1, 1, 'Lâmina', 'Cabo', 1, 'Ferramenta utilizada para cortar madeira'),
('Furadeira', 2, 2, 'Broca', 'Motor', 2, 'Ferramenta utilizada para perfurar metal');

INSERT INTO InformacoesAdicionais (FerramentaId, Marca, Modelo, AnoFabricacao)
VALUES 
(1, 'Geyciane', 'Serra Geyciane', 2020),
(2, 'DeWalt', 'Furadeira DeWalt', 2019);
```
