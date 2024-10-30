from flask import Flask, request, render_template
import csv
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

def form_action():
    if request.method == "POST":
        recipient_email = "lexrunit@gmail.com" 
        sender_email = "lexrunit@gmail.com"
        if "send-message" in request.form:
            name = request.form["name"]
            email = request.form["email"]
            message = request.form["message"]

            subject = "Incoming Message"
            body = f"""
            Name: {name} \n \n 

            Email: {email} \n \n 

            Message: {message}
            """
        elif "subscribe" in request.form:
            email = request.form["email"]
            subject = "New subscriber"
            body = f"""
            Subscribers_Email: {email}
            """
        send_email(sender_email, recipient_email, subject, body)

def send_email(sender_email, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login("lexrunit@gmail.com", "grux wghi ekqv zfzd")
        smtp.send_message(msg)