# 🛡️ Phishing URL Detector

A Python-based cybersecurity tool that analyzes URLs and identifies potential phishing indicators using multiple security checks.

## 🚀 Features

- ✅ HTTPS Verification
- ✅ IP Address Detection
- ✅ Suspicious Keyword Detection
- ✅ Risk Scoring System
- ✅ Detailed Analysis Report
- ✅ Report Export to TXT File

## 📋 How It Works

The tool analyzes a URL and checks for:

1. Whether HTTPS is being used
2. Presence of an IP address instead of a domain name
3. Suspicious phishing-related keywords such as:
   - login
   - verify
   - secure
   - update
   - bank
   - account

Based on these checks, a risk score is calculated and classified as:

- 🟢 LOW
- 🟡 MEDIUM
- 🔴 HIGH

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (Regex)
- URL Parsing (`urllib.parse`)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/dakshkumawat07/Phishing-URL-Detector.git
cd Phishing-URL-Detector
```

Run the program:

```bash
python3 phishing_detector.py
```

## 💻 Example Usage

Input:

```text
http://192.168.1.5/login/verify/account
```

Output:

```text
----- ANALYSIS REPORT -----

Risk Level: HIGH
Risk Score: 8

Reasons:
- URL is not using HTTPS
- IP address found instead of domain
- Suspicious keyword detected: login
- Suspicious keyword detected: verify
- Suspicious keyword detected: account

Report saved as report.txt
```

## 📂 Project Structure

```text
Phishing-URL-Detector/
│
├── phishing_detector.py
├── README.md
└── report.txt
```

## 🎯 Future Improvements

- Domain reputation checking
- Blacklist integration
- GUI version
- Machine Learning-based detection
- Browser extension support

## 👨‍💻 Author

Daksh Kumawat

GitHub: https://github.com/dakshkumawat07

---

⚠️ This project is intended for educational and cybersecurity learning purposes only.
