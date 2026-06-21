from urllib.parse import urlparse
import re

def analyze_url(url):
    score = 0

    parsed = urlparse(url)

    if parsed.scheme != "https":
        score += 2

    if re.search(r'\d+\.\d+\.\d+\.\d+', parsed.netloc):
        score += 3

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

    return score

url = input("Enter URL: ")

score = analyze_url(url)

if score <= 2:
    print("Risk Level: LOW")
elif score <= 5:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: HIGH")
