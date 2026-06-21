from urllib.parse import urlparse
import re

def analyze_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)

    # Check HTTPS
    if parsed.scheme != "https":
        score += 2
        reasons.append("URL is not using HTTPS")

    # Check for IP address
    if re.search(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
        score += 3
        reasons.append("IP address found instead of domain")

    # Check suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "bank",
        "account"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Suspicious keyword detected: {word}")

    return score, reasons


# User Input
url = input("Enter URL: ")

# Analyze URL
score, reasons = analyze_url(url)

# Determine Risk Level
if score <= 2:
    risk = "LOW"
elif score <= 5:
    risk = "MEDIUM"
else:
    risk = "HIGH"

# Display Results
print("\n----- ANALYSIS REPORT -----")
print(f"Risk Level: {risk}")
print(f"Risk Score: {score}")

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)

# Save Report
with open("report.txt", "w") as file:
    file.write("PHISHING URL DETECTOR REPORT\n")
    file.write("===========================\n")
    file.write(f"URL: {url}\n")
    file.write(f"Risk Level: {risk}\n")
    file.write(f"Risk Score: {score}\n\n")

    if reasons:
        file.write("Reasons:\n")
        for reason in reasons:
            file.write(f"- {reason}\n")

print("\nReport saved as report.txt")
