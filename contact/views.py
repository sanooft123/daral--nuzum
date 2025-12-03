from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

@api_view(["POST"])
def contact_message(request):
    name = request.data.get("name")
    company = request.data.get("company")
    phone = request.data.get("phone")
    email = request.data.get("email")
    subject = request.data.get("subject")
    message = request.data.get("message")

    email_body = f"""
Name: {name}
Company: {company}
Phone: {phone}
Email: {email}

Message:
{message}
"""

    send_mail(
        subject=f"Contact Form: {subject}",
        message=email_body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECEIVER_EMAIL],
    )

    return Response({"success": True, "message": "Message sent successfully!"})
