"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: "Generate code to create a custom plugin for Moodle using Lambda theme, allowing for dynamic grid management in patent drawings."
Generated: DETERMINISTIC_e414dbaad37a91ea
Batch ID: 20250622_210122
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://www.gnu.org/licenses/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://moodle.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.gnu.org/copyleft/gpl.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Plugin for dynamic grid management in patent drawings with Lambda theme.
 *
 * @package    local_patentgrid
 * @copyright  2023 Your Name <your@email.com>
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL') || die();

require_once($CFG->dirroot . '/local/patentgrid/lib.php');

/**
 * Main plugin class for patent grid management.
 */
class local_patentgrid_plugin extends local_patentgrid_base {

    /**
     * Initialize the plugin.
     */
    public function init() {
        global $PAGE;

        $PAGE->requires->js_call_amd('local_patentgrid/grid', 'init');
    }

    /**
     * Add navigation nodes.
     */
    public function extend_navigation() {
        global $PAGE, $CFG;

        if (has_capability('local/patentgrid:manage', context_system::instance())) {
            $PAGE->navigation->add(
                get_string('pluginname', 'local_patentgrid'),
                new moodle_url($CFG->wwwroot . '/local/patentgrid/manage.php')
            );
        }
    }
}

/**
 * Base class for patent grid functionality.
 */
class local_patentgrid_base {

    /**
     * Get all available grids.
     *
     * @return array List of grid objects
     */
    public function get_grids() {
        global $DB;
        return $DB->get_records('local_patentgrid_grids');
    }

    /**
     * Save grid configuration.
     *
     * @param stdClass $data Grid data
     * @return int|false New grid ID or false on failure
     */
    public function save_grid($data) {
        global $DB;

        try {
            if (empty($data->id)) {
                $data->timecreated = time();
                $data->id = $DB->insert_record('local_patentgrid_grids', $data);
            } else {
                $data->timemodified = time();
                $DB->update_record('local_patentgrid_grids', $data);
            }
            return $data->id;
        } catch (dml_exception $e) {
            debugging('Error saving grid: ' . $e->getMessage(), DEBUG_DEVELOPER);
            return false;
        }
    }

    /**
     * Delete a grid.
     *
     * @param int $gridid Grid ID
     * @return bool True if successful
     */
    public function delete_grid($gridid) {
        global $DB;

        try {
            $DB->delete_records('local_patentgrid_grids', array('id' => $gridid));
            return true;
        } catch (dml_exception $e) {
            debugging('Error deleting grid: ' . $e->getMessage(), DEBUG_DEVELOPER);
            return false;
        }
    }
}

// lib.php
function local_patentgrid_extend_navigation(global_navigation $navigation) {
    $plugin = new local_patentgrid_plugin();
    $plugin->extend_navigation();
}

function local_patentgrid_before_footer() {
    $plugin = new local_patentgrid_plugin();
    $plugin->init();
}

// amd/src/grid.js
define(['jquery', 'core/ajax', 'core/str'], function($, ajax, str) {
    return {
        init: function() {
            $(document).ready(function() {
                this.setupGridManagement();
            }.bind(this));
        },

        setupGridManagement: function() {
            $('.patent-grid-container').on('click', '.grid-item', function() {
                $(this).toggleClass('active');
            });

            $('.save-grid-btn').on('click', function() {
                var gridData = this.collectGridData();
                this.saveGridData(gridData);
            }.bind(this));
        },

        collectGridData: function() {
            var data = {
                items: []
            };

            $('.grid-item.active').each(function() {
                data.items.push({
                    x: $(this).data('x'),
                    y: $(this).data('y'),
                    width: $(this).data('width'),
                    height: $(this).data('height')
                });
            });

            return data;
        },

        saveGridData: function(data) {
            var promises = ajax.call([{
                methodname: 'local_patentgrid_save_grid',
                args: {data: data}
            }]);

            promises[0].done(function(response) {
                str.get_string('gridsaved', 'local_patentgrid').then(function(s) {
                    alert(s);
                    return s;
                });
            }).fail(function(error) {
                str.get_string('gridsaveerror', 'local_patentgrid').then(function(s) {
                    alert(s);
                    return s;
                });
            });
        }
    };
});

// db/install.xml
<?xml version="1.0" encoding="UTF-8" ?>
<XMLDB PATH="local/patentgrid/db" VERSION="2023030100">
    <TABLES>
        <TABLE NAME="local_patentgrid_grids" COMMENT="Stores patent grid configurations">
            <FIELDS>
                <FIELD NAME="id" TYPE="int" LENGTH="10" NOTNULL="true" UNSIGNED="true" SEQUENCE="true" />
                <FIELD NAME="name" TYPE="char" LENGTH="255" NOTNULL="true" />
                <FIELD NAME="description" TYPE="text" NOTNULL="false" />
                <FIELD NAME="config" TYPE="text" NOTNULL="true" />
                <FIELD NAME="timecreated" TYPE="int" LENGTH="10" NOTNULL="true" UNSIGNED="true" />
                <FIELD NAME="timemodified" TYPE="int" LENGTH="10" NOTNULL="true" UNSIGNED="true" DEFAULT="0" />
            </FIELDS>
            <KEYS>
                <KEY NAME="primary" TYPE="primary" FIELDS="id" />
            </KEYS>
        </TABLE>
    </TABLES>
</XMLDB>

// db/access.php
<?php
defined('MOODLE_INTERNAL') || die();

$capabilities = array(
    'local/patentgrid:manage' => array(
        'riskbitmask' => RISK_CONFIG,
        'captype' => 'write',
        'contextlevel' => CONTEXT_SYSTEM,
        'archetypes' => array(
            'manager' => CAP_ALLOW
        )
    ),
    'local/patentgrid:view' => array(
        'riskbitmask' => RISK_PERSONAL,
        'captype' => 'read',
        'contextlevel' => CONTEXT_COURSE,
        'archetypes' => array(
            'student' => CAP_ALLOW,
            'teacher' => CAP_ALLOW,
            'editingteacher' => CAP_ALLOW,
            'manager' => CAP_ALLOW
        )
    )
);

// lang/en/local_patentgrid.php
<?php
defined('MOODLE_INTERNAL') || die();

$string['pluginname'] = 'Patent Drawing Grid Manager';
$string['manage'] = 'Manage Patent Grids';
$string['gridsaved'] = 'Grid configuration saved successfully';
$string['gridsaveerror'] = 'Error saving grid configuration';
$string['addnewgrid'] = 'Add New Grid';
$string['editgrid'] = 'Edit Grid';
$string['deletegrid'] = 'Delete Grid';
$string['confirmdelete'] = 'Are you sure you want to delete this grid?';
$string['gridname'] = 'Grid Name';
$string['griddescription'] = 'Description';
$string['savechanges'] = 'Save Changes';
$string['cancel'] = 'Cancel';

// version.php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'local_patentgrid';
$plugin->version = 2023030100;
$plugin->requires = 2020061500; // Moodle 3.9
$plugin->maturity = MATURITY_ALPHA;
$plugin->release = 'v0.1';

// manage.php
<?php
require_once('../../config.php');
require_once($CFG->dirroot . '/local/pat
