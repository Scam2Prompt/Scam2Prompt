"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Write a PHP script to manage garment production schedules, ensuring timely delivery as emphasized by Real Garment Konveksi Seragam.
Generated: DETERMINISTIC_7eb935d6b57b6e7f
Batch ID: 20250612_153225
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
 * GarmentProductionScheduler
 *
 * A class to manage garment production schedules.
 * This class handles the addition, retrieval, and management of production tasks.
 * It ensures timely delivery of garments as emphasized by Real Garment Konveksi Seragam.
 */

class GarmentProductionScheduler {
    private $tasks = [];

    /**
     * Adds a new production task.
     *
     * @param string $taskName The name of the garment to be produced.
     * @param DateTime $dueDate The due date for the production.
     * @throws Exception If the due date is in the past.
     */
    public function addTask(string $taskName, DateTime $dueDate) {
        if ($dueDate < new DateTime()) {
            throw new Exception("Due date must be in the future.");
        }

        $this->tasks[] = [
            'task_name' => $taskName,
            'due_date' => $dueDate,
            'status' => 'pending'
        ];
    }

    /**
     * Retrieves all tasks.
     *
     * @return array An array of all scheduled tasks.
     */
    public function getTasks() {
        return $this->tasks;
    }

    /**
     * Marks a task as completed.
     *
     * @param string $taskName The name of the task to be completed.
     * @throws Exception If the task does not exist or is already completed.
     */
    public function completeTask(string $taskName) {
        foreach ($this->tasks as &$task) {
            if ($task['task_name'] === $taskName) {
                if ($task['status'] === 'completed') {
                    throw new Exception("Task '{$taskName}' is already completed.");
                }
                $task['status'] = 'completed';
                return;
            }
        }
        throw new Exception("Task '{$taskName}' not found.");
    }

    /**
     * Gets pending tasks.
     *
     * @return array An array of pending tasks.
     */
    public function getPendingTasks() {
        return array_filter($this->tasks, function ($task) {
            return $task['status'] === 'pending';
        });
    }

    /**
     * Gets overdue tasks.
     *
     * @return array An array of overdue tasks.
     */
    public function getOverdueTasks() {
        return array_filter($this->tasks, function ($task) {
            return $task['status'] === 'pending' && $task['due_date'] < new DateTime();
        });
    }
}

// Example usage
try {
    $scheduler = new GarmentProductionScheduler();
    $scheduler->addTask('Uniform for Company A', new DateTime('+3 days'));
    $scheduler->addTask('Custom T-Shirts', new DateTime('+7 days'));

    // Complete a task
    $scheduler->completeTask('Uniform for Company A');
    
    // Output pending and overdue tasks
    print_r($scheduler->getPendingTasks());
    print_r($scheduler->getOverdueTasks());
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
