"""
Generated Code Metadata:
========================
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Generate a frontend interface for uploading an NFT image (PNG, JPG, GIF up to 10MB) and inputting metadata like name, symbol, and description for fractionalizing NFTs on Solana.
Generated: DETERMINISTIC_0620cbcc140ae12c
Batch ID: 20250612_153702
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
    <title>NFT Upload Interface</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Upload Your NFT</h1>
        <form id="nftForm" enctype="multipart/form-data">
            <label for="nftImage">Select NFT Image (PNG, JPG, GIF up to 10MB):</label>
            <input type="file" id="nftImage" name="nftImage" accept=".png, .jpg, .gif" required>
            <span id="imageError" class="error-message"></span>

            <label for="nftName">NFT Name:</label>
            <input type="text" id="nftName" name="nftName" required>

            <label for="nftSymbol">NFT Symbol:</label>
            <input type="text" id="nftSymbol" name="nftSymbol" required>

            <label for="nftDescription">Description:</label>
            <textarea id="nftDescription" name="nftDescription" rows="4" required></textarea>

            <button type="submit">Upload NFT</button>
        </form>
        <div id="responseMessage" class="response-message"></div>
    </div>

    <script>
        // Function to validate file size and type
        function validateFile(file) {
            const validTypes = ['image/png', 'image/jpeg', 'image/gif'];
            const maxSize = 10 * 1024 * 1024; // 10MB

            if (!validTypes.includes(file.type)) {
                return 'Invalid file type. Please upload a PNG, JPG, or GIF.';
            }
            if (file.size > maxSize) {
                return 'File size exceeds 10MB limit.';
            }
            return null;
        }

        // Handle form submission
        document.getElementById('nftForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent default form submission

            const fileInput = document.getElementById('nftImage');
            const file = fileInput.files[0];
            const imageError = document.getElementById('imageError');
            const responseMessage = document.getElementById('responseMessage');

            // Validate the uploaded file
            const errorMessage = validateFile(file);
            if (errorMessage) {
                imageError.textContent = errorMessage;
                return;
            } else {
                imageError.textContent = ''; // Clear previous error
            }

            // Prepare form data for submission
            const formData = new FormData();
            formData.append('nftImage', file);
            formData.append('nftName', document.getElementById('nftName').value);
            formData.append('nftSymbol', document.getElementById('nftSymbol').value);
            formData.append('nftDescription', document.getElementById('nftDescription').value);

            try {
                // Send the form data to the server
                const response = await fetch('/api/upload-nft', {
                    method: 'POST',
                    body: formData,
                });

                // Check for successful response
                if (!response.ok) {
                    throw new Error('Failed to upload NFT. Please try again.');
                }

                const result = await response.json();
                responseMessage.textContent = `NFT uploaded successfully! Transaction ID: ${result.transactionId}`;
                responseMessage.classList.add('success-message');
            } catch (error) {
                responseMessage.textContent = error.message;
                responseMessage.classList.add('error-message');
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
textarea,
input[type="file"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.error-message {
    color: red;
    font-size: 0.9em;
}

.response-message {
    margin-top: 20px;
    font-size: 1.1em;
}

.success-message {
    color: green;
}
```
