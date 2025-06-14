🛡️ SOC Phishing Playbook 🎣

![alt text](https://img.shields.io/badge/Language-Python-blue.svg)


![alt text](https://img.shields.io/badge/Document-LaTeX-00A0A0.svg)


![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)


![alt text](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

A comprehensive, actionable Security Operations Center (SOC) playbook designed to detect, analyze, and respond to phishing attacks effectively. This repository contains the full playbook in PDF and LaTeX formats, along with a custom Python script for automated email analysis.

Project Objective

To design a comprehensive Security Operations Center (SOC) playbook to detect, analyze, and respond to phishing attacks. The playbook must include actionable steps, detection tools, and a custom Python script to identify phishing emails.

✨ Key Features

📖 Comprehensive Guide: A step-by-step document covering the entire incident response lifecycle, from preparation to post-incident improvement.

⚙️ Actionable Steps: The playbook is not just theoretical. It includes clear, actionable Standard Operating Procedures (SOPs) for SOC analysts and CSIRT teams.

🐍 Automated Detection Script: A Python script that analyzes raw email files (.eml) for common phishing red flags and provides a risk score.

📊 Clear Workflow: Includes a visual flow diagram to illustrate the decision-making process during an incident.

👥 Built for Teams: Defines roles and responsibilities for various stakeholders, including technical teams, management, and legal departments, ensuring seamless coordination.

📚 Playbook Structure

The playbook is organized into distinct phases to guide a security team through a phishing incident in a structured manner.

Section #	Title	Description
1-2	Introduction & Overview	Sets the stage, defining the purpose, scope, and types of phishing attacks.
3	Preparation Phase	Proactive steps: tool configuration, training, and playbook maintenance.
4	Detection & Analysis	How to identify potential threats using tools and IOCs.
5	Phishing Detection Code	The core Python script with example phishing and benign emails for testing.
6-7	Containment & Eradication	Immediate actions to stop the attack and remove its artifacts.
8	Post-Incident & Improvement	The crucial "lessons learned" phase to strengthen security posture.
9-10	Coordination & Flow Diagram	Communication protocols and a high-level visual workflow.
Appendix	SOPs	Detailed checklists for executing the response process.
🚀 The Python Detector Script

A key deliverable of this project is phishing_detector.py, a simple yet effective tool for a first-pass analysis of suspicious emails.

How it Works

The script parses a raw email source and checks for common phishing indicators:

Sender Mismatch: Compares From:, Reply-To:, and Return-Path: headers.

Urgency Keywords: Scans the subject line for words like "urgent," "action required," "suspension."

Generic Greetings: Detects impersonal greetings like "Dear user."

Presence of Links: Flags emails containing hyperlinks, a primary vector for phishing.

How to Use

Save the raw source of a suspicious email as a .eml file (e.g., suspicious_email.eml).

Run the script from your terminal, piping the email content into it.

# Example with a phishing email
python phishing_detector.py < phishing_email.eml

# Expected Output:
# {
#     'risk_score': 70,
#     'verdict': 'High Risk (Likely Phishing)',
#     'details': [
#         "Risk (+25): 'From' address (...) does not match 'Reply-To' (...).",
#         "Risk (+20): Subject line contains urgency keyword(s). ...",
#         "Risk (+15): Email uses a generic greeting.",
#         "Risk (+10): Email contains 1 link(s). ..."
#     ]
# }

# Example with a benign email
python phishing_detector.py < benign_email.eml

# Expected Output:
# {
#     'risk_score': 10,
#     'verdict': 'Low Risk (Likely Benign)',
#     'details': [
#         "Risk (+10): Email contains 1 link(s). ..."
#     ]
# }
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
deliverables

This repository contains:

📄 SOC_Phishing_Playbook.pdf: The final, compiled playbook ready for use.

✍️ SOC_Phishing_Playbook.tex: The full LaTeX source code for the playbook.

🐍 phishing_detector.py: The Python script for email analysis.

📧 phishing_email.eml: An example of a malicious email for testing the script.

✉️ benign_email.eml: An example of a safe email for testing the script.
