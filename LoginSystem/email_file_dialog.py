import smtplib
from email.mime.text import MIMEText
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

"""
Creates a dialog box for the user to email a specified file.
"""


class Email(QDialog):
    def __init__(self, parent=None):
        super(Email, self).__init__(parent)
        self.parent = parent
        self.setGeometry(50, 50, 700, 500)
        self.width = self.frameSize().width()
        self.height = self.frameSize().height()
        self.setWindowTitle("Email")
        self.move_to_center("")
        self.font = QFont("Arial", 7)

        '''Create email label'''
        self.user_email = QLabel("Email Address: ", self)
        self.user_email.setFont(self.font)
        self.user_email.move(5, 15)

        '''Create user email textbox'''
        self.user_email_textbox = QLineEdit(self)
        self.user_email_textbox.setFixedWidth(self.width - 325)
        self.user_email_textbox.move(90, 10)

        '''Create user password label'''
        self.user_password_label = QLabel("Password: ", self)
        self.user_password_label.setFont(self.font)
        self.user_password_label.move(470, 15)

        '''Create user password textbox'''
        self.user_password_textbox = QLineEdit(self)
        self.user_password_textbox.move(535, 10)
        self.user_password_textbox.setFixedWidth(160)
        self.user_password_textbox.setEchoMode(QLineEdit.Password)

        '''Create recipient label'''
        self.recipient_email = QLabel("Recipient: ", self)
        self.recipient_email.setFont(self.font)
        self.recipient_email.move(5, 45)

        '''Create recipient textbox'''
        self.recipient_email_textbox = QLineEdit(self)
        self.recipient_email_textbox.setFixedWidth(self.width - 95)
        self.recipient_email_textbox.move(90, 40)

        '''Create subject label'''
        self.subject_label = QLabel("Subject: ", self)
        self.subject_label.setFont(self.font)
        self.subject_label.move(5, 75)

        '''Create subject textbox'''
        self.subject_textbox = QLineEdit(self)
        self.subject_textbox.setFixedWidth(self.width - 95)
        self.subject_textbox.move(90, 70)

        '''Create text editor for email'''
        self.email_editor = QTextEdit(self)
        self.email_editor.clear()
        self.email_editor.setFixedWidth(self.width - 10)
        self.email_editor.setFixedHeight(self.height - 130)
        self.email_editor.move(5, 95)

        '''Create button to send email'''
        self.email_button = QPushButton("Send", self)
        self.email_button.move(300, self.height - 30)
        self.email_button.clicked.connect(self.send_email)

        self.show()

        if self.exec():
            pass

    def send_email(self):
        TO = self.recipient_email_textbox.text()
        SUBJECT = self.subject_textbox.text()
        TEXT = self.email_editor.toPlainText()
        SENDER = self.user_email_textbox.text()
        SENDER_PASSWORD = self.user_password_textbox.text()
        SERVER = smtplib.SMTP("smtp.gmail.com", 587)
        SERVER.ehlo()
        SERVER.starttls()
        SERVER.login(SENDER, SENDER_PASSWORD)

        BODY = "\r\n".join([
            "To: %s" % TO,
            "From: %s" % SENDER,
            "Subject: %s" % SUBJECT,
            "",
            TEXT
        ])

        try:
            SERVER.sendmail(SENDER, [TO], BODY)
        except:
            print("Error sending email")

        self.user_email_textbox.clear()
        self.user_password_textbox.clear()
        self.recipient_email_textbox.clear()
        self.subject_textbox.clear()
        self.email_editor.clear()
        SERVER.quit()

    """
    Allows the window to close when specified.
    """

    def closeEvent(self, event):
        self.parent.show()
        event.accept()

    """
    Moves the window to the center of the screen.
    """

    def move_to_center(self, screen):
        if screen == "":
            screen = self
        resolution = QDesktopWidget().screenGeometry()
        screen.move(resolution.width() / 2 - screen.frameSize().width() / 2,
                    resolution.height() / 2 - screen.frameSize().height() / 2)
