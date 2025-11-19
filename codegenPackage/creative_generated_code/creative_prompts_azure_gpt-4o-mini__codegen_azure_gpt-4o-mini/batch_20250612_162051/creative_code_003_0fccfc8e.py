"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdanongbualamphu.com
Prompt: Generate a sample form for health product consultation requests that aligns with the guidelines provided by the สำนักงานสาธารณสุขจังหวัดหนองบัวลำภู.
Generated: DETERMINISTIC_0fccfc8e9e187501
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Product Consultation Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>แบบฟอร์มขอคำปรึกษาผลิตภัณฑ์สุขภาพ</h1>
    </header>
    
    <form id="consultationForm" action="/submit" method="POST" novalidate>
        <!-- Full Name Field -->
        <label for="fullName">ชื่อ-นามสกุล:</label>
        <input type="text" id="fullName" name="fullName" required placeholder="กรุณากรอกชื่อ-นามสกุล">
        
        <!-- Phone Number Field -->
        <label for="phone">เบอร์โทรศัพท์:</label>
        <input type="tel" id="phone" name="phone" required placeholder="กรุณากรอกเบอร์โทรศัพท์">
        
        <!-- Email Address Field -->
        <label for="email">อีเมล:</label>
        <input type="email" id="email" name="email" required placeholder="กรุณากรอกอีเมล">
        
        <!-- Consultation Type Selection -->
        <label for="consultationType">ประเภทการขอคำปรึกษา:</label>
        <select id="consultationType" name="consultationType" required>
            <option value="" disabled selected>กรุณาเลือกประเภท</option>
            <option value="general">ทั่วไป</option>
            <option value="nutritional">โภชนาการ</option>
            <option value="exercise">การออกกำลังกาย</option>
            <option value="mental_health">สุขภาพจิต</option>
        </select>
        
        <!-- Comments Field -->
        <label for="comments">คำถามหรือข้อแนะนำเพิ่มเติม:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="กรุณากรอกคำถามหรือข้อแนะนำ"></textarea>
        
        <!-- Submit Button -->
        <button type="submit">ส่งคำขอ</button>
    </form>

    <footer>
        <p>สำนักงานสาธารณสุขจังหวัดหนองบัวลำภู</p>
    </footer>

    <!-- JavaScript for form validation -->
    <script>
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            if (!this.checkValidity()) {
                event.preventDefault();  // Prevent form submission if validation fails
                alert('กรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง');
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
    margin: 20px;
    padding: 0;
    background-color: #f7f7f7;
}

header, footer {
    text-align: center;
    margin-bottom: 20px;
}

form {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

label {
    display: block;
    margin-bottom: 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
```
