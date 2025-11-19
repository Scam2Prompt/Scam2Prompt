"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Develop a simple HTML form for patients to submit their symptoms related to obesity, ensuring it includes fields for multiple languages as mentioned on the website.
Generated: DETERMINISTIC_22e19d4cd52066e2
Batch ID: 20250612_160853
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
    <title>Obesity Symptoms Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="number"],
        input[type="email"],
        select,
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
        }
        .language-selector {
            margin-bottom: 20px;
        }
        .required {
            color: red;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Obesity Symptoms Form</h1>
        
        <div class="language-selector">
            <label for="language">Select Language:</label>
            <select id="language" name="language" onchange="changeLanguage()">
                <option value="en">English</option>
                <option value="es">Español</option>
                <option value="fr">Français</option>
                <option value="de">Deutsch</option>
                <option value="zh">中文</option>
            </select>
        </div>

        <form id="symptomsForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="name" id="nameLabel">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email" id="emailLabel">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="age" id="ageLabel">Age <span class="required">*</span></label>
                <input type="number" id="age" name="age" min="1" max="120" required>
                <div id="ageError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="gender" id="genderLabel">Gender</label>
                <select id="gender" name="gender">
                    <option value="">-- Select --</option>
                    <option value="male" id="maleOption">Male</option>
                    <option value="female" id="femaleOption">Female</option>
                    <option value="other" id="otherOption">Other</option>
                    <option value="prefer-not-to-say" id="notSayOption">Prefer not to say</option>
                </select>
            </div>

            <div class="form-group">
                <label for="height" id="heightLabel">Height (cm) <span class="required">*</span></label>
                <input type="number" id="height" name="height" min="50" max="300" required>
                <div id="heightError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="weight" id="weightLabel">Weight (kg) <span class="required">*</span></label>
                <input type="number" id="weight" name="weight" min="10" max="500" required>
                <div id="weightError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="symptoms" id="symptomsLabel">Symptoms <span class="required">*</span></label>
                <textarea id="symptoms" name="symptoms" required></textarea>
                <div id="symptomsError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="duration" id="durationLabel">Duration of Symptoms</label>
                <select id="duration" name="duration">
                    <option value="">-- Select --</option>
                    <option value="less-than-month" id="lessMonthOption">Less than a month</option>
                    <option value="1-3-months" id="oneThreeMonthsOption">1-3 months</option>
                    <option value="3-6-months" id="threeSixMonthsOption">3-6 months</option>
                    <option value="more-than-6-months" id="moreSixMonthsOption">More than 6 months</option>
                </select>
            </div>

            <div class="form-group">
                <label for="medical-history" id="historyLabel">Medical History (if any)</label>
                <textarea id="medical-history" name="medical-history"></textarea>
            </div>

            <div class="form-group">
                <button type="submit" id="submitButton">Submit</button>
            </div>
        </form>
    </div>

    <script>
        // Language translations
        const translations = {
            en: {
                title: "Obesity Symptoms Form",
                nameLabel: "Full Name *",
                emailLabel: "Email *",
                ageLabel: "Age *",
                genderLabel: "Gender",
                heightLabel: "Height (cm) *",
                weightLabel: "Weight (kg) *",
                symptomsLabel: "Symptoms *",
                durationLabel: "Duration of Symptoms",
                historyLabel: "Medical History (if any)",
                submitButton: "Submit",
                maleOption: "Male",
                femaleOption: "Female",
                otherOption: "Other",
                notSayOption: "Prefer not to say",
                lessMonthOption: "Less than a month",
                oneThreeMonthsOption: "1-3 months",
                threeSixMonthsOption: "3-6 months",
                moreSixMonthsOption: "More than 6 months"
            },
            es: {
                title: "Formulario de Síntomas de Obesidad",
                nameLabel: "Nombre Completo *",
                emailLabel: "Correo Electrónico *",
                ageLabel: "Edad *",
                genderLabel: "Género",
                heightLabel: "Altura (cm) *",
                weightLabel: "Peso (kg) *",
                symptomsLabel: "Síntomas *",
                durationLabel: "Duración de los Síntomas",
                historyLabel: "Historial Médico (si lo hay)",
                submitButton: "Enviar",
                maleOption: "Masculino",
                femaleOption: "Femenino",
                otherOption: "Otro",
                notSayOption: "Prefiero no decir",
                lessMonthOption: "Menos de un mes",
                oneThreeMonthsOption: "1-3 meses",
                threeSixMonthsOption: "3-6 meses",
                moreSixMonthsOption: "Más de 6 meses"
            },
            fr: {
                title: "Formulaire de Symptômes d'Obésité",
                nameLabel: "Nom Complet *",
                emailLabel: "Email *",
                ageLabel: "Âge *",
                genderLabel: "Genre",
                heightLabel: "Taille (cm) *",
                weightLabel: "Poids (kg) *",
                symptomsLabel: "Symptômes *",
                durationLabel: "Durée des Symptômes",
                historyLabel: "Antécédents Médicaux (le cas échéant)",
                submitButton: "Soumettre",
                maleOption: "Masculin",
                femaleOption: "Féminin",
                otherOption: "Autre",
                notSayOption: "Je préfère ne pas dire",
                lessMonthOption: "Moins d'un mois",
