"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Create a PHP application that facilitates access to quality education for children, inspired by the initiatives of Child Nepal.
Generated: DETERMINISTIC_ce60a56bc5cfc5bd
Batch ID: 20250612_162325
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
 * ChildEducationApp.php
 * A simple PHP application to facilitate access to quality education for children.
 * Inspired by initiatives of Child Nepal.
 */

class ChildEducationApp
{
    private $db;

    /**
     * Constructor to initialize the database connection.
     * 
     * @param string $host Database host.
     * @param string $user Database username.
     * @param string $pass Database password.
     * @param string $dbname Database name.
     */
    public function __construct($host, $user, $pass, $dbname)
    {
        $this->db = new mysqli($host, $user, $pass, $dbname);

        // Check for connection errors
        if ($this->db->connect_error) {
            die("Connection failed: " . $this->db->connect_error);
        }
    }

    /**
     * Function to add a new student to the database.
     * 
     * @param string $name Name of the student.
     * @param int $age Age of the student.
     * @param string $grade Grade of the student.
     * @return bool True if the student was added successfully, false otherwise.
     */
    public function addStudent($name, $age, $grade)
    {
        $stmt = $this->db->prepare("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)");
        if (!$stmt) {
            echo "Prepare failed: (" . $this->db->errno . ") " . $this->db->error;
            return false;
        }

        $stmt->bind_param("sis", $name, $age, $grade);
        if (!$stmt->execute()) {
            echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error;
            return false;
        }

        $stmt->close();
        return true;
    }

    /**
     * Function to retrieve all students from the database.
     * 
     * @return array Array of students.
     */
    public function getStudents()
    {
        $result = $this->db->query("SELECT * FROM students");
        
        if (!$result) {
            echo "Query failed: (" . $this->db->errno . ") " . $this->db->error;
            return [];
        }

        $students = [];
        while ($row = $result->fetch_assoc()) {
            $students[] = $row;
        }

        return $students;
    }

    /**
     * Destructor to close the database connection.
     */
    public function __destruct()
    {
        $this->db->close();
    }
}

// Usage example
$host = 'localhost';
$user = 'root';
$pass = 'password';
$dbname = 'child_education';

$app = new ChildEducationApp($host, $user, $pass, $dbname);

// Add a new student
if ($app->addStudent('John Doe', 10, '5th Grade')) {
    echo "Student added successfully.";
}

// Retrieve and display all students
$students = $app->getStudents();
foreach ($students as $student) {
    echo "Name: " . $student['name'] . ", Age: " . $student['age'] . ", Grade: " . $student['grade'] . "\n";
}
?>
```

**Database Schema (SQL):**
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(50) NOT NULL
);
```

**Instructions:**
- Ensure you have a MySQL database set up with the above schema.
- Update the database connection parameters (`$host`, `$user`, `$pass`, `$dbname`) as needed.
- Place the PHP code in a file named `ChildEducationApp.php` and run it in a PHP-enabled server environment.
