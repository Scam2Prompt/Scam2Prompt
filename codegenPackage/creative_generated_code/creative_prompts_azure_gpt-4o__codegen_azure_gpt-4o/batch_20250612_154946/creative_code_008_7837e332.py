"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Write a Python script to detect and open downloaded files from The Prepper Codex using Adobe Reader or a ZIP extractor like WinZip.
Generated: DETERMINISTIC_7837e33280264301
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import zipfile

def detect_and_open_files(download_dir, file_prefix, pdf_reader_path, zip_extractor_path):
    """
    Detects files downloaded from 'The Prepper Codex' in the specified directory
    and opens them using Adobe Reader for PDFs or WinZip for ZIP files.

    Parameters:
        download_dir (str): The directory where files are downloaded.
        file_prefix (str): The prefix used to identify files from 'The Prepper Codex'.
        pdf_reader_path (str): Path to the Adobe Reader executable.
        zip_extractor_path (str): Path to the WinZip executable.
    """
    try:
        # Ensure the provided directory exists
        if not os.path.isdir(download_dir):
            raise FileNotFoundError(f"The directory '{download_dir}' does not exist.")

        # Iterate through files in the directory
        for filename in os.listdir(download_dir):
            if filename.startswith(file_prefix):
                file_path = os.path.join(download_dir, filename)

                if filename.endswith(".pdf"):
                    # Open PDF files with Adobe Reader
                    subprocess.run([pdf_reader_path, file_path], check=True)
                    print(f"Opened PDF file: {file_path}")
                elif filename.endswith(".zip"):
                    # Extract and open ZIP files using WinZip
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        extracted_dir = os.path.join(download_dir, "extracted_files")
                        os.makedirs(extracted_dir, exist_ok=True)
                        zip_ref.extractall(extracted_dir)
                        print(f"Extracted ZIP file: {file_path} to {extracted_dir}")
                    subprocess.run([zip_extractor_path, extracted_dir], check=True)
                else:
                    print(f"Skipped unsupported file type: {filename}")
    except FileNotFoundError as fnf_err:
        print(f"Error: {fnf_err}")
    except zipfile.BadZipFile as bz_err:
        print(f"Error: Failed to open ZIP file. {bz_err}")
    except subprocess.CalledProcessError as sp_err:
        print(f"Error: Failed to open file with the external application. {sp_err}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == '__main__':
    # Configuration for the script
    download_directory = r"C:\Users\YourUsername\Downloads"  # Example download directory
    prepper_codex_prefix = "The_Prepper_Codex"               # Prefix to identify files
    adobe_reader_exe_path = r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
    winzip_exe_path = r"C:\Program Files\WinZip\WINZIP64.EXE"

    # Call the function with provided configuration
    detect_and_open_files(download_directory, prepper_codex_prefix, adobe_reader_exe_path, winzip_exe_path)
```
