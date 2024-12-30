"""OTP Email Verification Script using Gmail's SMTP Server."""

import smtplib
import random
import sys

def generate_otp(num_digits):
    """
    Generate an OTP with the given number of digits.

    Args:
        num_digits (int): Number of OTP digits.
    Returns:
        str: Generated OTP as a string.
    """
    return str(random.randint(10**(num_digits - 1), (10**num_digits) - 1))

def send_otp_email(sender_email, app_password, recipient_email, otp, subject):
    """
    Send an OTP email via Gmail SMTP.

    Args:
        sender_email (str): Sender's email.
        app_password (str): App password for Gmail.
        recipient_email (str): Recipient's email.
        otp (str): OTP to send.
        subject (str): Email subject.
    """
    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp_server:
            smtp_server.starttls()  # Enable encryption
            print("Logging in...")
            smtp_server.login(sender_email, app_password)
            message = f"Subject: {subject}\n\nYour OTP is: {otp}"
            smtp_server.sendmail(sender_email, recipient_email, message)
        print("Email sent successfully!")
    except smtplib.SMTPException as error:
        print(f"Failed to send email: {error}")
        sys.exit(1)

def verify_otp(generated_otp):
    """
    Prompt user for OTP and verify it.

    Args:
        generated_otp (str): Generated OTP for verification.
    """
    entered_otp = input("Enter the OTP: ").strip()
    if entered_otp == generated_otp:
        print("OTP Verified!")
    else:
        print("Invalid OTP.")

def main():
    """Generate, send, and verify OTP."""
    sender_email = "vijaybhosale1932@gmail.com"  # Sender's Gmail address
    app_password = "wmgm trdp jvwd ypld"  # App-specific password

    try:
        # Get OTP length and validate
        num_digits = int(input("Enter OTP length (4-10): ").strip())
        if not 4 <= num_digits <= 10:
            print("OTP length must be between 4 and 10.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Enter a valid number.")
        sys.exit(1)

    # Get email details
    email_subject = input("Enter email subject: ").strip()
    recipient_email = input("Enter recipient's email: ").strip()

    print("Generating OTP...")
    otp = generate_otp(num_digits)  # Generate OTP
    print("OTP generated.")

    send_otp_email(sender_email, app_password, recipient_email, otp, email_subject)  # Send OTP
    verify_otp(otp)  # Verify OTP

if __name__ == "__main__":
    main()
