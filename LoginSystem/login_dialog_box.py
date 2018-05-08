from PYQT.PROJECTS.LoginSystem.editor import *
from validate_email import validate_email

from PYTHON_MODULES.PYQT.PROJECTS.LoginSystem.user_registration import *


class LoginDialogBox(QDialog):
    def __init__(self, parent=None):
        super(LoginDialogBox, self).__init__(parent)
        self.parent = parent
        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle("Login")
        self.move_to_center("")
        self.font = QFont("Arial", 15)

        '''Create the username label.'''
        self.username_label = QLabel("Username: ", self)
        self.username_label.setFont(self.font)
        self.username_label.move(0, 25)

        '''Create the username text box.'''
        self.username_textbox = QLineEdit(self)
        self.username_textbox.move(200, 30)

        '''Create the password label.'''
        self.password_label = QLabel("Password: ", self)
        self.password_label.setFont(self.font)
        self.password_label.move(0, 75)

        '''Create the password text box.'''
        self.password_textbox = QLineEdit(self)
        self.password_textbox.move(200, 80)
        self.password_textbox.setEchoMode(QLineEdit.Password)

        '''Create login button.'''
        self.login_button = QPushButton("Login", self)
        self.login_button.move(self.frameSize().width() / 2 + 50,
                               self.frameSize().height() / 2)
        self.login_button.clicked.connect(self.analyze)

        '''Create Sign-up button'''
        self.sign_up_button = QPushButton("Sign Up", self)
        self.sign_up_button.move(self.frameSize().width() / 2 - 100,
                                 self.frameSize().height() / 2)
        self.sign_up_button.clicked.connect(self.new_user)

        self.invalid_credentials = None

        self.setWindowModality(Qt.ApplicationModal)

        self.show()

        if self.exec():
            pass

    """
    Allows the window to close properly when instructed to by the user.
    """

    def closeEvent(self, event):
        event.accept()

    """
    Moves the current window to the center of the screen.
    """

    def move_to_center(self, screen):
        if screen == "":
            screen = self
        resolution = QDesktopWidget().screenGeometry()
        screen.move(resolution.width() / 2 - screen.frameSize().width() / 2,
                    resolution.height() / 2 - screen.frameSize().height() / 2)

    """
    Reads in the username and password from the login page and reads a text file determining whether or
    not the user has "registered" with the application before. The entered username must be a CNU email or the user will
    be asked to enter a valid email address. 
    """

    def analyze(self):
        if self.username_textbox.text() == "" or self.password_textbox.text() == "":
            self.invalid_info_entered("no username or password")
        else:
            if validate_email(self.username_textbox.text()):
                cnu_email = self.username_textbox.text()[-7:]
                if cnu_email == "cnu.edu":
                    with open("login_info.txt", 'r') as file_being_read:
                        for line in file_being_read:
                            if line == self.username_textbox.text() + " " + self.password_textbox.text():
                                self.hide()
                                self.editor = Editor(self)
                                if self.invalid_credentials is not None:
                                    self.invalid_credentials.clear()
                            else:
                                self.invalid_info_entered("password")
                else:
                    self.invalid_info_entered("email")
            else:
                self.invalid_info_entered("email")

    """
    Only activated when an email or password is incorrect.
    
    Determines the portion of the login information that is incorrect and displays an error. 
    
    :param
    """

    def invalid_info_entered(self, type_of_error):
        if self.invalid_credentials is not None:
            self.invalid_credentials.clear()
        else:
            self.invalid_credentials = QLabel("", self)

        font = QFont("Arial", 7)
        if type_of_error == "email":
            self.invalid_credentials.setText("Please enter an existing CNU email address")
            self.invalid_credentials.move(200, 55)
        elif type_of_error == "password":
            self.invalid_credentials.setText("Incorrect username and password combination")
            self.invalid_credentials.move(200, 120)
        else:
            self.invalid_credentials.setText("Please enter a valid email address and password")
            self.invalid_credentials.move(200, 55)

        self.invalid_credentials.setStyleSheet("color: red")
        self.invalid_credentials.setFont(font)
        self.invalid_credentials.show()

    """
    Creates a NewUser() object which allows the user to "sign-up" for the application.
    """

    def new_user(self):
        self.hide()
        self.new_user = NewUser(self)
