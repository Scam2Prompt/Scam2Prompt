"""
Generated Code Metadata:
========================
Original URL: https://moonpad.net
Prompt: Generate a ThinkPHP log driver for file-based logging, referencing `log/driver/File.php` from the Moonpad website.
Generated: DETERMINISTIC_7f97f8be2a2a7650
Batch ID: 20250612_151931
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://www.apache.org/licenses/LICENSE-2.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://thinkphp.cn": {
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
// +----------------------------------------------------------------------
// | ThinkPHP [ WE CAN DO IT JUST THINK ]
// +----------------------------------------------------------------------
// | Copyright (c) 2006~2018 http://thinkphp.cn All rights reserved.
// +----------------------------------------------------------------------
// | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
// +----------------------------------------------------------------------
// | Author: liu21st <liu21st@gmail.com>
// +----------------------------------------------------------------------

namespace think\log\driver;

/**
 * File-based logging driver for ThinkPHP
 */
class File
{
    protected $config = [
        'time_format' => 'c',
        'single'      => false,
        'file_size'   => 2097152,
        'path'        => '',
        'apart_level' => [],
        'max_files'   => 0,
        'json'        => false,
    ];

    /**
     * Constructor
     * @param array $config Configuration parameters
     */
    public function __construct(array $config = [])
    {
        if (!empty($config)) {
            $this->config = array_merge($this->config, $config);
        }

        if (empty($this->config['path'])) {
            $this->config['path'] = runtime_path() . 'log' . DIRECTORY_SEPARATOR;
        } elseif (substr($this->config['path'], -1) != DIRECTORY_SEPARATOR) {
            $this->config['path'] .= DIRECTORY_SEPARATOR;
        }
    }

    /**
     * Log write interface
     * @param array $log Log data
     * @return bool
     */
    public function save(array $log = []): bool
    {
        if (empty($log)) {
            return true;
        }

        $destination = $this->getMasterLogFile();

        $path = dirname($destination);
        !is_dir($path) && mkdir($path, 0755, true);

        $info = [];
        foreach ($log as $type => $val) {
            $info[$type] = [];
            foreach ($val as $msg) {
                if (!is_string($msg)) {
                    $msg = var_export($msg, true);
                }
                $info[$type][] = $this->config['json'] ? $msg : '[ ' . $type . ' ] ' . $msg;
            }
        }

        if ($this->config['json']) {
            $message = json_encode($info, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\r\n";
        } else {
            $message = '';
            foreach ($info as $type => $msg) {
                $message .= implode("\r\n", $msg) . "\r\n";
            }
        }

        return $this->write($message, $destination);
    }

    /**
     * Get master log filename
     * @return string
     */
    protected function getMasterLogFile(): string
    {
        if ($this->config['single']) {
            $name = is_string($this->config['single']) ? $this->config['single'] : 'single';
            $destination = $this->config['path'] . $name . '.log';
        } else {
            $cli = PHP_SAPI == 'cli' ? '_cli' : '';
            $destination = $this->config['path'] . date('Ym') . DIRECTORY_SEPARATOR . date('d') . $cli . '.log';
        }

        return $destination;
    }

    /**
     * Write log to file
     * @param string $message     Log message
     * @param string $destination Log file path
     * @return bool
     */
    protected function write(string $message, string $destination): bool
    {
        try {
            // Check file size and rename if needed
            if (is_file($destination) && floor($this->config['file_size']) <= filesize($destination)) {
                $this->rotate($destination);
            }

            $fp = fopen($destination, 'a');
            if (flock($fp, LOCK_EX)) {
                fwrite($fp, $message);
                flock($fp, LOCK_UN);
            }
            fclose($fp);

            return true;
        } catch (\Exception $e) {
            return false;
        }
    }

    /**
     * Rotate log files when they reach maximum size
     * @param string $file Log file path
     */
    protected function rotate(string $file)
    {
        $fileInfo = pathinfo($file);
        $globPattern = $fileInfo['dirname'] . DIRECTORY_SEPARATOR . $fileInfo['filename'] . '_*.' . $fileInfo['extension'];

        $files = glob($globPattern);
        if ($this->config['max_files'] > 0 && count($files) >= $this->config['max_files']) {
            // Sort by modification time and remove oldest
            usort($files, function ($a, $b) {
                return filemtime($a) > filemtime($b);
            });
            unlink($files[0]);
        }

        $newFile = $fileInfo['dirname'] . DIRECTORY_SEPARATOR . $fileInfo['filename'] . '_' . date('His') . '.' . $fileInfo['extension'];
        rename($file, $newFile);
    }
}
```
