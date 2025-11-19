"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: "Design a system diagram using Moodle's Lambda theme and plugins, incorporating features like image handling and text addition in patent drawings."
Generated: DETERMINISTIC_ae82d88343b1b19c
Batch ID: 20250622_210122
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
 * Moodle system diagram plugin for Lambda theme.
 * Handles patent drawing features including image upload and text addition.
 */

defined('MOODLE_INTERNAL') || die();

require_once($CFG->libdir.'/filelib.php');
require_once($CFG->libdir.'/formslib.php');

class patent_drawing {
    /**
     * @var int The course module ID
     */
    private $cmid;

    /**
     * @var int The course ID
     */
    private $courseid;

    /**
     * @var context The context object
     */
    private $context;

    /**
     * @var array The drawing data
     */
    private $drawingdata;

    /**
     * Constructor
     * @param int $cmid The course module ID
     * @param int $courseid The course ID
     */
    public function __construct($cmid, $courseid) {
        $this->cmid = $cmid;
        $this->courseid = $courseid;
        $this->context = context_module::instance($cmid);
    }

    /**
     * Save drawing data
     * @param array $data The drawing data to save
     * @return bool True if successful
     */
    public function save_drawing($data) {
        global $DB, $USER;

        try {
            $record = new stdClass();
            $record->userid = $USER->id;
            $record->courseid = $this->courseid;
            $record->cmid = $this->cmid;
            $record->drawingdata = json_encode($data);
            $record->timecreated = time();
            $record->timemodified = time();

            if ($existing = $DB->get_record('patent_drawings', ['userid' => $USER->id, 'cmid' => $this->cmid])) {
                $record->id = $existing->id;
                return $DB->update_record('patent_drawings', $record);
            } else {
                return $DB->insert_record('patent_drawings', $record, false);
            }
        } catch (Exception $e) {
            debugging('Error saving patent drawing: ' . $e->getMessage(), DEBUG_DEVELOPER);
            return false;
        }
    }

    /**
     * Get drawing data
     * @return array|null The drawing data or null if not found
     */
    public function get_drawing() {
        global $DB, $USER;

        try {
            if ($record = $DB->get_record('patent_drawings', ['userid' => $USER->id, 'cmid' => $this->cmid])) {
                return json_decode($record->drawingdata, true);
            }
            return null;
        } catch (Exception $e) {
            debugging('Error retrieving patent drawing: ' . $e->getMessage(), DEBUG_DEVELOPER);
            return null;
        }
    }

    /**
     * Handle file upload
     * @param string $filearea The file area
     * @param int $draftitemid The draft item ID
     * @return bool True if successful
     */
    public function handle_file_upload($filearea, $draftitemid) {
        global $USER;

        try {
            file_save_draft_area_files(
                $draftitemid,
                $this->context->id,
                'mod_patentdrawing',
                $filearea,
                0,
                ['subdirs' => 0, 'maxfiles' => 1]
            );
            return true;
        } catch (Exception $e) {
            debugging('Error uploading file: ' . $e->getMessage(), DEBUG_DEVELOPER);
            return false;
        }
    }

    /**
     * Get file URL
     * @param string $filearea The file area
     * @return moodle_url|null The file URL or null if not found
     */
    public function get_file_url($filearea) {
        $fs = get_file_storage();
        $files = $fs->get_area_files(
            $this->context->id,
            'mod_patentdrawing',
            $filearea,
            0,
            'itemid, filepath, filename',
            false
        );

        if ($file = reset($files)) {
            return moodle_url::make_pluginfile_url(
                $file->get_contextid(),
                $file->get_component(),
                $file->get_filearea(),
                $file->get_itemid(),
                $file->get_filepath(),
                $file->get_filename()
            );
        }
        return null;
    }
}

class patent_drawing_form extends moodleform {
    public function definition() {
        global $CFG;

        $mform = $this->_form;

        // Drawing title
        $mform->addElement('text', 'title', get_string('title', 'mod_patentdrawing'));
        $mform->setType('title', PARAM_TEXT);
        $mform->addRule('title', get_string('required'), 'required', null, 'client');

        // Drawing description
        $mform->addElement('editor', 'description', get_string('description', 'mod_patentdrawing'));
        $mform->setType('description', PARAM_RAW);

        // Image upload
        $mform->addElement('filemanager', 'drawing_image', get_string('drawingimage', 'mod_patentdrawing'), null,
            ['accepted_types' => ['image'], 'maxfiles' => 1]);

        // Text elements
        $mform->addElement('textarea', 'drawing_text', get_string('drawingtext', 'mod_patentdrawing'));
        $mform->setType('drawing_text', PARAM_RAW);

        // Submit button
        $this->add_action_buttons();
    }
}

function patent_drawing_pluginfile($course, $cm, $context, $filearea, $args, $forcedownload, array $options=[]) {
    if ($context->contextlevel != CONTEXT_MODULE) {
        return false;
    }

    require_login($course, true, $cm);

    $fs = get_file_storage();
    $relativepath = implode('/', $args);
    $fullpath = "/$context->id/mod_patentdrawing/$filearea/0/$relativepath";
    
    if (!$file = $fs->get_file_by_hash(sha1($fullpath)) or $file->is_directory()) {
        return false;
    }

    send_stored_file($file, 0, 0, $forcedownload, $options);
}
```
