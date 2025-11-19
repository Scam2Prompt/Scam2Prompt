"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Develop a PHP application that generates reports on the academic performance of students at I.E Politécnico Municipal Cali, incorporating data from multiple educational levels.
Generated: DETERMINISTIC_587dc50f96ddd7f3
Batch ID: 20250612_161301
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
 * Student Performance Report Generator for I.E Politécnico Municipal Cali
 * 
 * This script generates academic performance reports for students across multiple educational levels.
 * It fetches data from a database, processes it, and generates reports in a structured format.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'politecnico_municipal_cali');
define('DB_CHARSET', 'utf8mb4');

// Report types
define('REPORT_INDIVIDUAL', 1);
define('REPORT_GROUP', 2);
define('REPORT_LEVEL', 3);

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        try {
            $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
            $this->connection = new PDO($dsn, DB_USER, DB_PASS);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->connection->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception("Database connection failed: " . $e->getMessage());
        }
    }

    public function getConnection() {
        return $this->connection;
    }
}

/**
 * Student Performance Report Generator
 */
class StudentPerformanceReport {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Generate a performance report
     * 
     * @param int $reportType Type of report (individual, group, or level)
     * @param mixed $identifier Student ID, group ID, or level ID
     * @return array Report data
     * @throws Exception If invalid parameters or database error occurs
     */
    public function generateReport($reportType, $identifier = null) {
        try {
            switch ($reportType) {
                case REPORT_INDIVIDUAL:
                    if (empty($identifier)) {
                        throw new Exception("Student ID is required for individual reports");
                    }
                    return $this->generateIndividualReport($identifier);
                
                case REPORT_GROUP:
                    if (empty($identifier)) {
                        throw new Exception("Group ID is required for group reports");
                    }
                    return $this->generateGroupReport($identifier);
                
                case REPORT_LEVEL:
                    return $this->generateLevelReport($identifier);
                
                default:
                    throw new Exception("Invalid report type specified");
            }
        } catch (Exception $e) {
            throw new Exception("Report generation failed: " . $e->getMessage());
        }
    }

    /**
     * Generate individual student report
     * 
     * @param int $studentId
     * @return array
     */
    private function generateIndividualReport($studentId) {
        $conn = $this->db->getConnection();

        // Get student basic information
        $stmt = $conn->prepare("
            SELECT s.id, s.first_name, s.last_name, s.identification, 
                   g.name as group_name, l.name as level_name
            FROM students s
            JOIN groups g ON s.group_id = g.id
            JOIN levels l ON g.level_id = l.id
            WHERE s.id = :student_id
        ");
        $stmt->execute([':student_id' => $studentId]);
        $student = $stmt->fetch();

        if (!$student) {
            throw new Exception("Student not found");
        }

        // Get academic performance data
        $stmt = $conn->prepare("
            SELECT subject.name as subject_name, 
                   grade.period, grade.score, grade.comments
            FROM grades grade
            JOIN subjects subject ON grade.subject_id = subject.id
            WHERE grade.student_id = :student_id
            ORDER BY subject.name, grade.period
        ");
        $stmt->execute([':student_id' => $studentId]);
        $grades = $stmt->fetchAll();

        // Calculate averages
        $subjectAverages = [];
        foreach ($grades as $grade) {
            if (!isset($subjectAverages[$grade['subject_name']])) {
                $subjectAverages[$grade['subject_name']] = [
                    'total' => 0,
                    'count' => 0
                ];
            }
            $subjectAverages[$grade['subject_name']]['total'] += $grade['score'];
            $subjectAverages[$grade['subject_name']]['count']++;
        }

        foreach ($subjectAverages as &$average) {
            $average['average'] = $average['total'] / $average['count'];
        }

        return [
            'student_info' => $student,
            'grades' => $grades,
            'subject_averages' => $subjectAverages,
            'overall_average' => $this->calculateOverallAverage($grades)
        ];
    }

    /**
     * Generate group performance report
     * 
     * @param int $groupId
     * @return array
     */
    private function generateGroupReport($groupId) {
        $conn = $this->db->getConnection();

        // Get group information
        $stmt = $conn->prepare("
            SELECT g.id, g.name as group_name, 
                   l.name as level_name, l.id as level_id
            FROM groups g
            JOIN levels l ON g.level_id = l.id
            WHERE g.id = :group_id
        ");
        $stmt->execute([':group_id' => $groupId]);
        $group = $stmt->fetch();

        if (!$group) {
            throw new Exception("Group not found");
        }

        // Get all students in the group
        $stmt = $conn->prepare("
            SELECT id, first_name, last_name, identification
            FROM students
            WHERE group_id = :group_id
            ORDER BY last_name, first_name
        ");
        $stmt->execute([':group_id' => $groupId]);
        $students = $stmt->fetchAll();

        // Get performance data for each student
        $report = [
            'group_info' => $group,
            'students' => []
        ];

        foreach ($students as $student) {
            $studentReport = $this->generateIndividualReport($student['id']);
            $report['students'][] = [
                'student_info' => $student,
                'overall_average' => $studentReport['overall_average']
            ];
        }

        // Calculate group averages
        $report['group_average'] = $this->calculateGroupAverage($report['students']);

        return $report;
    }

    /**
     * Generate level performance report
     * 
     * @param int|null $levelId If null, generates report for all levels
     * @return array
     */
    private function generateLevelReport($levelId = null) {
        $conn = $this->db->getConnection();

        $report = [
            'levels' => []
        ];

        // Get all levels or specific level
        $query = "SELECT id, name FROM levels";
        $params = [];

        if ($levelId !== null) {
            $query .= " WHERE id = :level_id";
            $params[':level_id'] = $levelId;
        }

        $stmt = $conn->prepare($query);
        $stmt->execute($params);
        $levels = $stmt->fetchAll();

        foreach ($levels as $level) {
            // Get all groups in the level
            $stmt = $conn->prepare("
                SELECT id, name
                FROM groups
                WHERE level_id = :level_id
            ");
            $stmt->execute([':level_id' => $level['id']]);
            $groups = $stmt->fetchAll();

            $levelReport = [
                'level_info' => $level,
                'groups' => []
            ];

            foreach ($groups as $group) {
                $groupReport = $this->generateGroupReport($group['id']);
                $levelReport['groups'][] = [
                    'group_info' => $group,
                    'group_average' => $groupReport['group_average']
                ];
            }

            // Calculate level average
            $levelReport['level_average'] = $this->calculateLevelAverage($levelReport['groups']);
            $report['levels'][] = $levelReport;
        }

        return $report;
    }

    /**
     * Calculate overall average for a student
     * 
     * @param array $grades
     * @return float
     */
    private function calculateOverallAverage($grades) {
        if (empty($grades)) {
            return 0;
        }

        $total = 0;
        foreach ($grades as $grade) {
            $total += $grade['score'];
        }

        return $total / count($grades);
    }

    /**
     * Calculate group average
     * 
     * @param array $students
     * @return float
     */
    private function calculateGroupAverage($students) {
        if (empty($students)) {
            return 0;
        }

        $total = 0;
        foreach ($
