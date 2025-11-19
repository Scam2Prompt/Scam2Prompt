"""
Generated Code Metadata:
========================
Original URL: https://syr-whistler.com
Prompt: Generate a simple web interface using HTML and JavaScript to interact with a CGI script for file management.
Generated: DETERMINISTIC_cce9f611778d471d
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Management Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input[type="text"], input[type="file"] {
            margin-bottom: 10px;
            width: 300px;
        }
        button {
            margin-top: 10px;
        }
        #response {
            margin-top: 20px;
            border: 1px solid #ccc;
            padding: 10px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>

<h1>File Management Interface</h1>

<!-- Input for file upload -->
<label for="fileInput">Select a file to upload:</label>
<input type="file" id="fileInput" name="fileInput" required>
<br>

<!-- Input for file deletion -->
<label for="fileName">Enter the name of the file to delete:</label>
<input type="text" id="fileName" name="fileName" required>
<br>

<!-- Buttons to trigger actions -->
<button id="uploadButton">Upload File</button>
<button id="deleteButton">Delete File</button>

<!-- Area to display server response -->
<div id="response"></div>

<script>
    // Function to handle file upload
    async function uploadFile() {
        const fileInput = document.getElementById('fileInput');
        const responseDiv = document.getElementById('response');

        if (fileInput.files.length === 0) {
            responseDiv.innerText = 'Please select a file to upload.';
            return;
        }

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);

        try {
            const response = await fetch('/cgi-bin/upload.cgi', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('File upload failed: ' + response.statusText);
            }

            const result = await response.text();
            responseDiv.innerText = 'Upload successful: ' + result;
        } catch (error) {
            responseDiv.innerText = 'Error: ' + error.message;
        }
    }

    // Function to handle file deletion
    async function deleteFile() {
        const fileName = document.getElementById('fileName').value;
        const responseDiv = document.getElementById('response');

        if (!fileName) {
            responseDiv.innerText = 'Please enter a file name to delete.';
            return;
        }

        try {
            const response = await fetch('/cgi-bin/delete.cgi', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ fileName: fileName })
            });

            if (!response.ok) {
                throw new Error('File deletion failed: ' + response.statusText);
            }

            const result = await response.text();
            responseDiv.innerText = 'Deletion successful: ' + result;
        } catch (error) {
            responseDiv.innerText = 'Error: ' + error.message;
        }
    }

    // Event listeners for buttons
    document.getElementById('uploadButton').addEventListener('click', uploadFile);
    document.getElementById('deleteButton').addEventListener('click', deleteFile);
</script>

</body>
</html>
```

### CGI Script Example (upload.cgi and delete.cgi)

**upload.cgi**
```perl
#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use File::Copy;

# Create a new CGI object
my $cgi = CGI->new;

# Get the uploaded file
my $upload_filehandle = $cgi->upload('file');
my $filename = $cgi->param('file');

# Define the upload directory
my $upload_dir = '/path/to/upload/directory/';

# Save the uploaded file
open (my $out, '>', "$upload_dir/$filename") or die "Cannot open file: $!";
binmode $out;
while (my $bytesread = <$upload_filehandle>) {
    print $out $bytesread;
}
close $out;

# Print the response
print $cgi->header('text/plain');
print "File '$filename' uploaded successfully.";
```

**delete.cgi**
```perl
#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use JSON;

# Create a new CGI object
my $cgi = CGI->new;

# Read the JSON input
my $json_text = $cgi->param('POSTDATA');
my $data = decode_json($json_text);
my $file_name = $data->{fileName};

# Define the directory where files are stored
my $file_path = "/path/to/upload/directory/$file_name";

# Attempt to delete the file
if (-e $file_path) {
    unlink $file_path or die "Cannot delete file: $!";
    print $cgi->header('text/plain');
    print "File '$file_name' deleted successfully.";
} else {
    print $cgi->header('text/plain', '404 Not Found');
    print "File '$file_name' not found.";
}
```

### Note:
- Ensure that the CGI scripts have the appropriate permissions to execute and that the upload directory exists and is writable by the web server.
- Adjust the paths in the CGI scripts to match your server's configuration.
