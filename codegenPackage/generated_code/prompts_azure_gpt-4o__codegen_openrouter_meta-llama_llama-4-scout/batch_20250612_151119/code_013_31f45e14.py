"""
Generated Code Metadata:
========================
Original URL: https://www.cc-community.net
Prompt: Write code to implement a bug tracker system for a XenForo-based forum, inspired by the CC-Community Board's "Bugtracker" section.
Generated: DETERMINISTIC_31f45e148ee0a724
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// BugTracker.php

class BugTracker {
    /**
     * @var XenForo_db
     */
    protected $db;

    public function __construct(XenForo_db $db) {
        $this->db = $db;
    }

    /**
     * Create bug report
     *
     * @param array $data
     * @return int
     */
    public function createBugReport(array $data) {
        if (empty($data['title']) || empty($data['description'])) {
            throw new Exception('Title and description are required');
        }

        $bugReport = array(
            'title' => $data['title'],
            'description' => $data['description'],
            'reporter_id' => XenForo_Visitor::getUserId(),
            'report_date' => XenForo_Application::$time,
            'status' => 'open'
        );

        $this->db->beginTransaction();

        try {
            $bugReportId = $this->db->insert('bug_tracker_reports', $bugReport);
            $this->db->commit();
            return $bugReportId;
        } catch (Exception $e) {
            $this->db->rollback();
            throw $e;
        }
    }

    /**
     * Get all bug reports
     *
     * @param array $conditions
     * @param array $options
     * @return array
     */
    public function getBugReports(array $conditions = array(), array $options = array()) {
        $db = $this->db;

        $query = $db->limit($db->prepareQuery("
            SELECT *
            FROM bug_tracker_reports
            WHERE 1=1
        "), $options['limit'], $options['offset']);

        if (!empty($conditions['status'])) {
            $query->where('status', $conditions['status']);
        }

        return $query->fetchAll();
    }

    /**
     * Update bug report
     *
     * @param int $bugReportId
     * @param array $data
     * @return bool
     */
    public function updateBugReport($bugReportId, array $data) {
        if (empty($bugReportId)) {
            throw new Exception('Bug report ID is required');
        }

        $this->db->beginTransaction();

        try {
            $this->db->update('bug_tracker_reports', $data, 'report_id = ' . intval($bugReportId));
            $this->db->commit();
            return true;
        } catch (Exception $e) {
            $this->db->rollback();
            throw $e;
        }
    }

    /**
     * Delete bug report
     *
     * @param int $bugReportId
     * @return bool
     */
    public function deleteBugReport($bugReportId) {
        if (empty($bugReportId)) {
            throw new Exception('Bug report ID is required');
        }

        $this->db->beginTransaction();

        try {
            $this->db->delete('bug_tracker_reports', 'report_id = ' . intval($bugReportId));
            $this->db->commit();
            return true;
        } catch (Exception $e) {
            $this->db->rollback();
            throw $e;
        }
    }
}

// BugTrackerAdmin.php

class BugTrackerAdmin extends BugTracker {
    /**
     * Get all bug report comments
     *
     * @param int $bugReportId
     * @return array
     */
    public function getBugReportComments($bugReportId) {
        if (empty($bugReportId)) {
            throw new Exception('Bug report ID is required');
        }

        return $this->db->fetchAll("
            SELECT *
            FROM bug_tracker_comments
            WHERE report_id = ?
            ORDER BY comment_date ASC
        ", array($bugReportId));
    }

    /**
     * Add bug report comment
     *
     * @param int $bugReportId
     * @param array $data
     * @return int
     */
    public function addBugReportComment($bugReportId, array $data) {
        if (empty($bugReportId)) {
            throw new Exception('Bug report ID is required');
        }

        if (empty($data['comment'])) {
            throw new Exception('Comment is required');
        }

        $comment = array(
            'report_id' => $bugReportId,
            'comment' => $data['comment'],
            'commenter_id' => XenForo_Visitor::getUserId(),
            'comment_date' => XenForo_Application::$time
        );

        $this->db->beginTransaction();

        try {
            $commentId = $this->db->insert('bug_tracker_comments', $comment);
            $this->db->commit();
            return $commentId;
        } catch (Exception $e) {
            $this->db->rollback();
            throw $e;
        }
    }
}

// Install code

$structure = new XenForo_DataStructure_Exporter();
$structure->exportTable('bug_tracker_reports', array(
    'report_id' => array('type' => 'int', 'auto_increment' => true),
    'title' => array('type' => 'varchar', 'length' => 100),
    'description' => array('type' => 'text'),
    'reporter_id' => array('type' => 'int'),
    'report_date' => array('type' => 'int'),
    'status' => array('type' => 'varchar', 'length' => 50)
));

$structure->exportTable('bug_tracker_comments', array(
    'comment_id' => array('type' => 'int', 'auto_increment' => true),
    'report_id' => array('type' => 'int'),
    'comment' => array('type' => 'text'),
    'commenter_id' => array('type' => 'int'),
    'comment_date' => array('type' => 'int')
));

$structure->apply();

// Example usage:

$bugTracker = new BugTracker($db);
$bugReportId = $bugTracker->createBugReport(array(
    'title' => 'Test bug report',
    'description' => 'This is a test bug report.'
));

$bugReport = $bugTracker->getBugReports(array('report_id' => $bugReportId));
print_r($bugReport);

$bugTrackerAdmin = new BugTrackerAdmin($db);
$commentId = $bugTrackerAdmin->addBugReportComment($bugReportId, array(
    'comment' => 'This is a test comment.'
));

$comments = $bugTrackerAdmin->getBugReportComments($bugReportId);
print_r($comments);
```
