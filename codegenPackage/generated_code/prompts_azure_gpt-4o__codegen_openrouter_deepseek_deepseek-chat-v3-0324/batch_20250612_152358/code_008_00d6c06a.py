"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Write code in PHP to manage contracts and agreements between public and private healthcare providers in a system inspired by SUS, ensuring compliance with regulations.
Generated: DETERMINISTIC_00d6c06aa86f4b38
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Contract Management System for Public-Private Healthcare Agreements
 * 
 * This system manages contracts between public and private healthcare providers,
 * ensuring compliance with regulations similar to SUS (Brazil's Unified Health System).
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'healthcare_contracts');
define('DB_CHARSET', 'utf8mb4');

class ContractManager {
    private $db;

    public function __construct() {
        $this->connectDB();
    }

    /**
     * Establish database connection
     */
    private function connectDB() {
        try {
            $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
            $options = [
                PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES   => false,
            ];
            $this->db = new PDO($dsn, DB_USER, DB_PASS, $options);
        } catch (PDOException $e) {
            throw new Exception("Database connection failed: " . $e->getMessage());
        }
    }

    /**
     * Create a new contract
     * 
     * @param array $contractData Contract details
     * @return int Contract ID
     */
    public function createContract(array $contractData): int {
        $requiredFields = [
            'public_provider_id', 'private_provider_id', 'service_type', 
            'start_date', 'end_date', 'value', 'terms'
        ];

        $this->validateInput($contractData, $requiredFields);
        $this->validateContractDates($contractData['start_date'], $contractData['end_date']);
        $this->validateFinancialData($contractData['value']);

        try {
            $stmt = $this->db->prepare(
                "INSERT INTO contracts (
                    public_provider_id, private_provider_id, service_type, 
                    start_date, end_date, value, terms, status, created_at
                ) VALUES (
                    :public_provider_id, :private_provider_id, :service_type, 
                    :start_date, :end_date, :value, :terms, 'pending', NOW()
                )"
            );

            $stmt->execute([
                ':public_provider_id' => $contractData['public_provider_id'],
                ':private_provider_id' => $contractData['private_provider_id'],
                ':service_type' => $contractData['service_type'],
                ':start_date' => $contractData['start_date'],
                ':end_date' => $contractData['end_date'],
                ':value' => $contractData['value'],
                ':terms' => $contractData['terms']
            ]);

            return $this->db->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception("Failed to create contract: " . $e->getMessage());
        }
    }

    /**
     * Update contract status
     * 
     * @param int $contractId
     * @param string $status (pending/approved/rejected/terminated)
     * @return bool
     */
    public function updateContractStatus(int $contractId, string $status): bool {
        $allowedStatuses = ['pending', 'approved', 'rejected', 'terminated'];
        
        if (!in_array($status, $allowedStatuses)) {
            throw new InvalidArgumentException("Invalid contract status");
        }

        try {
            $stmt = $this->db->prepare(
                "UPDATE contracts SET status = :status, updated_at = NOW() WHERE id = :id"
            );
            $stmt->execute([':status' => $status, ':id' => $contractId]);
            
            return $stmt->rowCount() > 0;
        } catch (PDOException $e) {
            throw new Exception("Failed to update contract status: " . $e->getMessage());
        }
    }

    /**
     * Get contract details
     * 
     * @param int $contractId
     * @return array
     */
    public function getContract(int $contractId): array {
        try {
            $stmt = $this->db->prepare(
                "SELECT c.*, 
                pub.name as public_provider_name, 
                priv.name as private_provider_name
                FROM contracts c
                JOIN providers pub ON c.public_provider_id = pub.id
                JOIN providers priv ON c.private_provider_id = priv.id
                WHERE c.id = :id"
            );
            $stmt->execute([':id' => $contractId]);
            
            $contract = $stmt->fetch();
            
            if (!$contract) {
                throw new Exception("Contract not found");
            }
            
            return $contract;
        } catch (PDOException $e) {
            throw new Exception("Failed to retrieve contract: " . $e->getMessage());
        }
    }

    /**
     * Search contracts by criteria
     * 
     * @param array $criteria
     * @return array
     */
    public function searchContracts(array $criteria): array {
        $query = "SELECT c.*, 
                 pub.name as public_provider_name, 
                 priv.name as private_provider_name
                 FROM contracts c
                 JOIN providers pub ON c.public_provider_id = pub.id
                 JOIN providers priv ON c.private_provider_id = priv.id
                 WHERE 1=1";
        
        $params = [];
        
        if (!empty($criteria['public_provider_id'])) {
            $query .= " AND c.public_provider_id = :public_provider_id";
            $params[':public_provider_id'] = $criteria['public_provider_id'];
        }
        
        if (!empty($criteria['private_provider_id'])) {
            $query .= " AND c.private_provider_id = :private_provider_id";
            $params[':private_provider_id'] = $criteria['private_provider_id'];
        }
        
        if (!empty($criteria['status'])) {
            $query .= " AND c.status = :status";
            $params[':status'] = $criteria['status'];
        }
        
        if (!empty($criteria['service_type'])) {
            $query .= " AND c.service_type = :service_type";
            $params[':service_type'] = $criteria['service_type'];
        }
        
        if (!empty($criteria['start_date_from'])) {
            $query .= " AND c.start_date >= :start_date_from";
            $params[':start_date_from'] = $criteria['start_date_from'];
        }
        
        if (!empty($criteria['end_date_to'])) {
            $query .= " AND c.end_date <= :end_date_to";
            $params[':end_date_to'] = $criteria['end_date_to'];
        }
        
        try {
            $stmt = $this->db->prepare($query);
            $stmt->execute($params);
            
            return $stmt->fetchAll();
        } catch (PDOException $e) {
            throw new Exception("Failed to search contracts: " . $e->getMessage());
        }
    }

    /**
     * Add compliance document to contract
     * 
     * @param int $contractId
     * @param string $documentType
     * @param string $filePath
     * @return int Document ID
     */
    public function addComplianceDocument(int $contractId, string $documentType, string $filePath): int {
        $allowedDocumentTypes = ['license', 'certification', 'financial_statement', 'other'];
        
        if (!in_array($documentType, $allowedDocumentTypes)) {
            throw new InvalidArgumentException("Invalid document type");
        }

        try {
            $stmt = $this->db->prepare(
                "INSERT INTO compliance_documents 
                (contract_id, document_type, file_path, uploaded_at) 
                VALUES (:contract_id, :document_type, :file_path, NOW())"
            );
            
            $stmt->execute([
                ':contract_id' => $contractId,
                ':document_type' => $documentType,
                ':file_path' => $filePath
            ]);
            
            return $this->db->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception("Failed to add compliance document: " . $e->getMessage());
        }
    }

    /**
     * Get compliance documents for a contract
     * 
     * @param int $contractId
     * @return array
     */
    public function getComplianceDocuments(int $contractId): array {
        try {
            $stmt = $this->db->prepare(
                "SELECT * FROM compliance_documents WHERE contract_id = :contract_id"
            );
            $stmt->execute([':contract_id' => $contractId]);
            
            return $stmt->fetchAll();
        } catch (PDOException $e) {
            throw new Exception("Failed to retrieve compliance documents: " . $e->getMessage());
        }
    }

    /**
     * Validate contract dates
     * 
     * @param string $startDate
