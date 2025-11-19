"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Develop a short code example in PHP to create a simple FAQ page, like the "Ofte stilte spørsmål" section on ungLeder.no, that allows administrators to easily add and update questions and answers.
Generated: DETERMINISTIC_cfdcd6b934f4479a
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$dbHost = 'localhost';
$dbUsername = 'your_username';
$dbPassword = 'your_password';
$dbName = 'your_database';

// Create a PDO instance
try {
    $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUsername, $dbPassword);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

// FAQ class
class FAQ {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    // Get all FAQs
    public function getAllFAQs() {
        try {
            $stmt = $this->pdo->query("SELECT * FROM faqs ORDER BY id ASC");
            $faqs = $stmt->fetchAll(PDO::FETCH_ASSOC);
            return $faqs;
        } catch (PDOException $e) {
            throw new Exception("Failed to get FAQs: " . $e->getMessage());
        }
    }

    // Get a single FAQ by ID
    public function getFAQById($id) {
        try {
            $stmt = $this->pdo->prepare("SELECT * FROM faqs WHERE id = :id");
            $stmt->bindParam(":id", $id);
            $stmt->execute();
            $faq = $stmt->fetch(PDO::FETCH_ASSOC);
            return $faq;
        } catch (PDOException $e) {
            throw new Exception("Failed to get FAQ: " . $e->getMessage());
        }
    }

    // Create a new FAQ
    public function createFAQ($question, $answer) {
        try {
            $stmt = $this->pdo->prepare("INSERT INTO faqs (question, answer) VALUES (:question, :answer)");
            $stmt->bindParam(":question", $question);
            $stmt->bindParam(":answer", $answer);
            $stmt->execute();
            return $this->pdo->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception("Failed to create FAQ: " . $e->getMessage());
        }
    }

    // Update an existing FAQ
    public function updateFAQ($id, $question, $answer) {
        try {
            $stmt = $this->pdo->prepare("UPDATE faqs SET question = :question, answer = :answer WHERE id = :id");
            $stmt->bindParam(":id", $id);
            $stmt->bindParam(":question", $question);
            $stmt->bindParam(":answer", $answer);
            $stmt->execute();
            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to update FAQ: " . $e->getMessage());
        }
    }

    // Delete a FAQ
    public function deleteFAQ($id) {
        try {
            $stmt = $this->pdo->prepare("DELETE FROM faqs WHERE id = :id");
            $stmt->bindParam(":id", $id);
            $stmt->execute();
            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to delete FAQ: " . $e->getMessage());
        }
    }
}

// Create an instance of the FAQ class
$faq = new FAQ($pdo);

// Check if the request is an AJAX request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        if (isset($_POST['action'])) {
            switch ($_POST['action']) {
                case 'get_faqs':
                    $faqs = $faq->getAllFAQs();
                    echo json_encode($faqs);
                    break;
                case 'get_faq':
                    if (isset($_POST['id'])) {
                        $faqById = $faq->getFAQById($_POST['id']);
                        echo json_encode($faqById);
                    } else {
                        http_response_code(400);
                        echo json_encode(['error' => 'Missing FAQ ID']);
                    }
                    break;
                case 'create_faq':
                    if (isset($_POST['question']) && isset($_POST['answer'])) {
                        $newFaqId = $faq->createFAQ($_POST['question'], $_POST['answer']);
                        echo json_encode(['id' => $newFaqId]);
                    } else {
                        http_response_code(400);
                        echo json_encode(['error' => 'Missing question or answer']);
                    }
                    break;
                case 'update_faq':
                    if (isset($_POST['id']) && isset($_POST['question']) && isset($_POST['answer'])) {
                        $faq->updateFAQ($_POST['id'], $_POST['question'], $_POST['answer']);
                        echo json_encode(['message' => 'FAQ updated successfully']);
                    } else {
                        http_response_code(400);
                        echo json_encode(['error' => 'Missing FAQ ID, question or answer']);
                    }
                    break;
                case 'delete_faq':
                    if (isset($_POST['id'])) {
                        $faq->deleteFAQ($_POST['id']);
                        echo json_encode(['message' => 'FAQ deleted successfully']);
                    } else {
                        http_response_code(400);
                        echo json_encode(['error' => 'Missing FAQ ID']);
                    }
                    break;
                default:
                    http_response_code(400);
                    echo json_encode(['error' => 'Invalid action']);
            }
        } else {
            http_response_code(400);
            echo json_encode(['error' => 'Missing action']);
        }
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['error' => $e->getMessage()]);
    }
} else {
    // Display the FAQ page
    ?>
    <!DOCTYPE html>
    <html>
    <head>
        <title>FAQ Page</title>
        <style>
            /* Simple styling for demonstration purposes */
            body {
                font-family: Arial, sans-serif;
            }
            .faq {
                margin-bottom: 20px;
            }
            .faq .question {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h1>Frequently Asked Questions</h1>
        <div id="faqs"></div>

        <script>
            // Fetch FAQs and display them
            fetch('<?php echo $_SERVER['PHP_SELF']; ?>', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'action=get_faqs'
            })
            .then(response => response.json())
            .then(faqs => {
                const faqContainer = document.getElementById('faqs');
                faqs.forEach(faq => {
                    const faqHtml = `
                        <div class="faq">
                            <div class="question">${faq.question}</div>
                            <div class="answer">${faq.answer}</div>
                        </div>
                    `;
                    faqContainer.innerHTML += faqHtml;
                });
            })
            .catch(error => console.error('Error:', error));
        </script>
    </body>
    </html>
    <?php
}

// Close the PDO connection
$pdo = null;
```

```sql
CREATE TABLE faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(255) NOT NULL,
    answer TEXT NOT NULL
);
```
