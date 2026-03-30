import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

# ----------------------------
# Folder setup
# ----------------------------
BASE_DIR = "data"
SUBFOLDERS = ["policies", "manuals", "faqs", "notes"]

for folder in SUBFOLDERS:
    os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

# ----------------------------
# PDF utility
# ----------------------------
styles = getSampleStyleSheet()
title_style = styles["Title"]
heading_style = styles["Heading2"]
body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=11,
    leading=16,
    alignment=TA_LEFT,
    spaceAfter=8,
)

def create_pdf(filepath, title, sections):
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    story = []

    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))

    for section_title, section_body in sections:
        story.append(Paragraph(section_title, heading_style))
        for para in section_body:
            story.append(Paragraph(para, body_style))
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 10))

    doc.build(story)
    print(f"Created: {filepath}")

def create_txt(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {filepath}")

# ----------------------------
# POLICY PDFs
# ----------------------------

create_pdf(
    "data/policies/employee_handbook.pdf",
    "Employee Handbook",
    [
        ("1. Working Hours", [
            "Standard office hours are from 9:30 AM to 6:30 PM, Monday to Friday.",
            "Employees are expected to log attendance daily through the HRMS portal.",
            "Flexible timing may be approved by reporting managers depending on team requirements."
        ]),
        ("2. Code of Conduct", [
            "Employees must maintain professionalism, respect colleagues, and follow company ethics.",
            "Harassment, discrimination, and workplace misconduct are strictly prohibited.",
            "Violations may lead to disciplinary action including written warning or termination."
        ]),
        ("3. Probation Period", [
            "All new employees undergo a probation period of 6 months from the date of joining.",
            "Probation may be extended based on performance, attendance, or business requirements."
        ]),
        ("4. Resignation and Exit", [
            "Employees must serve a notice period of 30 days unless otherwise specified in the employment contract.",
            "All company assets such as laptop, ID card, and access devices must be returned before final settlement."
        ]),
    ]
)

create_pdf(
    "data/policies/leave_policy.pdf",
    "Leave Policy",
    [
        ("1. Leave Types", [
            "Employees are eligible for 12 Casual Leaves, 10 Sick Leaves, and 15 Earned Leaves per calendar year.",
            "Casual leave is intended for short personal absences and should generally be planned in advance."
        ]),
        ("2. Leave Approval", [
            "All leaves must be applied through the leave management portal and approved by the reporting manager.",
            "Emergency leave should be informed through email or phone as early as possible."
        ]),
        ("3. Carry Forward Rules", [
            "A maximum of 10 earned leaves may be carried forward to the next year.",
            "Unused casual leave and sick leave lapse at the end of the calendar year."
        ]),
        ("4. Half-Day Leave", [
            "Half-day leave can be availed only with manager approval and should be marked in the HRMS system."
        ]),
    ]
)

create_pdf(
    "data/policies/attendance_policy.pdf",
    "Attendance Policy",
    [
        ("1. Daily Attendance", [
            "Employees must log in and log out through the attendance system every working day.",
            "Three late logins in a month may be treated as one half-day leave unless approved."
        ]),
        ("2. Missing Attendance", [
            "Employees must regularize missing attendance entries within 3 working days.",
            "Unregularized attendance gaps may be treated as leave without pay."
        ]),
    ]
)

create_pdf(
    "data/policies/remote_work_policy.pdf",
    "Remote Work Policy",
    [
        ("1. Work From Home Eligibility", [
            "Employees may work remotely based on team policy, business requirements, and manager approval.",
            "Remote work is subject to maintaining productivity, communication, and data security."
        ]),
        ("2. Remote Work Requirements", [
            "Employees must ensure stable internet, VPN access, and availability during core working hours.",
            "Sensitive company data must only be accessed through approved secure systems."
        ]),
    ]
)

create_pdf(
    "data/policies/benefits_policy.pdf",
    "Benefits Policy",
    [
        ("1. Insurance", [
            "Employees are covered under the company-provided health insurance policy from the date of confirmation.",
            "Dependent coverage may be available based on grade and policy terms."
        ]),
        ("2. Allowances", [
            "Internet reimbursement up to INR 1,000 per month is available for eligible employees.",
            "Meal cards and travel allowances are governed by grade-specific policy."
        ]),
    ]
)

create_pdf(
    "data/policies/it_security_policy.pdf",
    "IT Security Policy",
    [
        ("1. Password Policy", [
            "Passwords must be at least 12 characters long and include uppercase, lowercase, numbers, and symbols.",
            "Passwords must not be shared with anyone, including team members or vendors."
        ]),
        ("2. Device Security", [
            "All company laptops must be protected with screen lock and full-disk encryption.",
            "Employees must report lost or stolen devices to IT Security immediately."
        ]),
        ("3. Phishing Awareness", [
            "Employees must not click suspicious links or download attachments from unknown sources.",
            "Potential phishing emails should be reported to the IT helpdesk."
        ]),
    ]
)

create_pdf(
    "data/policies/holiday_calendar_2026.pdf",
    "Holiday Calendar 2026",
    [
        ("Declared Holidays", [
            "January 1 - New Year's Day",
            "January 26 - Republic Day",
            "March 25 - Ugadi",
            "August 15 - Independence Day",
            "October 2 - Gandhi Jayanti",
            "December 25 - Christmas"
        ]),
    ]
)

# ----------------------------
# MANUAL PDFs
# ----------------------------

create_pdf(
    "data/manuals/laptop_setup.pdf",
    "Laptop Setup Guide",
    [
        ("1. Initial Login", [
            "Power on the laptop and log in using the credentials shared by the IT team.",
            "Change your temporary password at first login."
        ]),
        ("2. Required Applications", [
            "Install Chrome, Microsoft Office, VPN client, Slack or Teams, and endpoint security tools.",
            "Do not uninstall preloaded security software."
        ]),
        ("3. Security Setup", [
            "Enable automatic updates and configure screen lock timeout.",
            "Ensure antivirus definitions are updated before using the device for office work."
        ]),
    ]
)

create_pdf(
    "data/manuals/vpn_guide.pdf",
    "VPN Guide",
    [
        ("1. Install VPN Client", [
            "Download the approved VPN client from the internal IT portal.",
            "Install the application using admin privileges if prompted."
        ]),
        ("2. Connect to VPN", [
            "Launch the VPN client and enter your company email ID.",
            "Use multi-factor authentication to complete login."
        ]),
        ("3. Troubleshooting", [
            "If connection fails, verify your internet connection and retry after restarting the VPN client.",
            "Raise a helpdesk ticket if the issue persists beyond 15 minutes."
        ]),
    ]
)

create_pdf(
    "data/manuals/password_reset_guide.pdf",
    "Password Reset Guide",
    [
        ("1. Self-Service Reset", [
            "Visit the internal identity portal and click on 'Forgot Password'.",
            "Complete OTP or MFA verification to continue."
        ]),
        ("2. Password Rules", [
            "New passwords must not match the last 5 passwords used.",
            "Passwords should be updated every 90 days."
        ]),
    ]
)

create_pdf(
    "data/manuals/email_setup_guide.pdf",
    "Email Setup Guide",
    [
        ("1. Outlook Setup", [
            "Open Outlook and sign in using your company email ID and password.",
            "Approve multi-factor authentication when prompted."
        ]),
        ("2. Mobile Email Setup", [
            "Use the Outlook mobile app for secure access to company mail.",
            "Do not configure company email in unsupported third-party apps."
        ]),
    ]
)

create_pdf(
    "data/manuals/leave_portal_guide.pdf",
    "Leave Portal Guide",
    [
        ("1. Apply for Leave", [
            "Log in to the HRMS portal and navigate to Leave Management.",
            "Select leave type, date range, and provide reason if required."
        ]),
        ("2. View Balance", [
            "Current leave balances are visible under the Leave Summary section."
        ]),
    ]
)

create_pdf(
    "data/manuals/payroll_portal_guide.pdf",
    "Payroll Portal Guide",
    [
        ("1. Access Payslips", [
            "Log in to the payroll portal using your employee credentials.",
            "Navigate to the Payslips section and select the relevant month."
        ]),
        ("2. Tax Documents", [
            "Form 16 and annual tax statements are available after the end of the financial year."
        ]),
    ]
)

create_pdf(
    "data/manuals/onboarding_checklist.pdf",
    "Onboarding Checklist",
    [
        ("1. Before Joining", [
            "Complete document submission, background verification, and bank details upload."
        ]),
        ("2. First Day Tasks", [
            "Activate laptop, set up email, join communication channels, and attend induction sessions."
        ]),
        ("3. First Week Tasks", [
            "Meet your reporting manager, complete mandatory trainings, and review team documentation."
        ]),
    ]
)

# ----------------------------
# FAQ PDFs
# ----------------------------

create_pdf(
    "data/faqs/employee_faq.pdf",
    "Employee FAQ",
    [
        ("Frequently Asked Questions", [
            "Q: How many casual leaves do I get? A: Employees receive 12 casual leaves per year.",
            "Q: Can I work from home? A: Work from home depends on team policy and manager approval.",
            "Q: How do I apply for leave? A: Leave can be applied through the HRMS leave portal.",
            "Q: When is salary credited? A: Salary is generally credited on the last working day of the month.",
            "Q: How do I access payslips? A: Payslips are available in the payroll portal."
        ]),
    ]
)

create_pdf(
    "data/faqs/it_support_faq.pdf",
    "IT Support FAQ",
    [
        ("Frequently Asked Questions", [
            "Q: How do I connect to VPN? A: Install the approved VPN client and log in with MFA.",
            "Q: How do I reset my password? A: Use the self-service identity portal.",
            "Q: What should I do if my laptop is slow? A: Restart the device and ensure updates are installed before raising a ticket.",
            "Q: How do I request software access? A: Raise a helpdesk ticket with manager approval if required.",
            "Q: What should I do if I suspect phishing? A: Report the email to the IT helpdesk immediately."
        ]),
    ]
)

# ----------------------------
# NOTES / TXT FILES
# ----------------------------

create_txt(
    "data/notes/meeting_notes.txt",
    """Team Meeting Notes - March 2026

1. HRMS leave workflow will be updated next quarter.
2. VPN timeout issue was reported by multiple employees.
3. IT team plans to publish a revised laptop troubleshooting guide.
4. Salary slips are now available through the payroll portal.
5. New joiners must complete onboarding within the first 5 working days.
"""
)

create_txt(
    "data/notes/faq_notes.txt",
    """Internal FAQ Notes

- Employees often ask about leave carry forward limits.
- VPN installation is the most common IT support request.
- Many new joiners need help with payroll portal access.
- Password reset should be routed through self-service before IT escalation.
"""
)

create_txt(
    "data/notes/team_decisions.txt",
    """Team Decisions

- Hybrid work schedule will continue for eligible teams.
- Employees must use company-approved VPN while working remotely.
- Updated security training will be mandatory for all employees.
"""
)

print("\nAll sample documents generated successfully.")