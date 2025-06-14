import email
import re

def analyze_email(raw_email_string):
    risk_score = 0
    analysis_details = []

    msg = email.message_from_string(raw_email_string)

    from_address = msg.get('From', '').lower()
    reply_to = msg.get('Reply-To', from_address).lower()
    return_path = msg.get('Return-Path', from_address).lower()

    if from_address != reply_to and 'no-reply' not in reply_to:
        risk_score += 25
        analysis_details.append(f"Risk (+25): 'From' address ({from_address}) does not match 'Reply-To' ({reply_to}).")

    subject = msg.get('Subject', '')
    urgent_keywords = ['urgent', 'verify', 'suspension', 'action required', 'password', 'invoice', 'security alert']
    if any(keyword in subject.lower() for keyword in urgent_keywords):
        risk_score += 20
        analysis_details.append(f"Risk (+20): Subject line contains urgency keyword(s). Subject: '{subject}'")

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if "text/plain" in content_type or "text/html" in content_type:
                try:
                    body += part.get_payload(decode=True).decode()
                except:
                    continue
    else:
        try:
            body = msg.get_payload(decode=True).decode()
        except:
            body = ""

    generic_greetings = ['dear customer', 'dear user', 'dear account holder']
    if any(greeting in body.lower() for greeting in generic_greetings):
        risk_score += 15
        analysis_details.append("Risk (+15): Email uses a generic greeting.")

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
    if urls:
        risk_score += 10
        analysis_details.append(f"Risk (+10): Email contains {len(urls)} link(s). First link: {urls[0][:50]}...")

    verdict = "Low Risk (Likely Benign)"
    if risk_score >= 50:
        verdict = "High Risk (Likely Phishing)"
    elif risk_score >= 25:
        verdict = "Medium Risk (Suspicious)"

    return {
        'risk_score': risk_score,
        'verdict': verdict,
        'details': analysis_details
    }

print("Enter the email details for analysis:")
from_input = input("From: ")
reply_to_input = input("Reply-To (leave blank to match From): ")
return_path_input = input("Return-Path (leave blank to match From): ")
subject_input = input("Subject: ")
print("Enter the body of the email (press ENTER twice to finish):")

body_lines = []
while True:
    line = input()
    if line == "":
        break
    body_lines.append(line)
body_input = "\n".join(body_lines)

raw_email = f"""From: {from_input}
Reply-To: {reply_to_input or from_input}
Return-Path: {return_path_input or from_input}
Subject: {subject_input}
Content-Type: text/plain

{body_input}
"""

result = analyze_email(raw_email)

print("\n--- Analysis Report ---")
print(f"Risk Score: {result['risk_score']}")
print(f"Verdict: {result['verdict']}")
print("Details:")
for detail in result['details']:
    print(f" - {detail}")
