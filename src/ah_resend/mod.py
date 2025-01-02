from lib.providers.services import service
from pydantic import BaseModel, EmailStr
import resend
import os

# Get Resend API key from environment
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")

# Validate required settings
if not RESEND_API_KEY:
    raise ValueError("RESEND_API_KEY environment variable not set")

# Initialize resend
resend.api_key = RESEND_API_KEY

class EmailMessage(BaseModel):
    """Email message data model"""
    to: EmailStr
    subject: str
    body: str
    html: bool = True

@service()
async def send_email(message: EmailMessage, context=None) -> bool:
    """Send an email using Resend.com
    
    Args:
        message: EmailMessage containing to, subject, and body
        
    Returns:
        bool: True if email was sent successfully
    """
    try:
        # Create params for resend
        params = {
            "from": os.environ.get("SMTP_FROM", "MindRoot <noreply@mindroot.ai>"),
            "to": message.to,
            "subject": message.subject
        }

        # Add content based on html flag
        if message.html:
            params["html"] = message.body
        else:
            params["text"] = message.body

        # Send email
        response = resend.Emails.send(params)
        
        # Resend returns a dict with 'id' if successful
        return bool(response.get('id'))

    except Exception as e:
        print(f"Error sending email via Resend: {e}")
        return False
