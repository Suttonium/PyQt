from PYQT.PROJECTS.LoginSystem.login_dialog_box import *
from validate_email import validate_email

from PYTHON_MODULES.PYQT.PROJECTS.LoginSystem.main import *


class NewUser(QDialog):
    def __init__(self, parent=None):
        super(NewUser, self).__init__(parent)
        self.parent = parent
        self.resolution = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle("New User Information")
        self.move_to_center("")
        self.font = QFont("Arial", 10)

        '''Create new user label'''
        self.new_username_label = QLabel("Username: ", self)
        self.new_username_label.setFont(self.font)
        self.new_username_label.move(20, 20)

        '''Create new user textbox'''
        self.new_username_textbox = QLineEdit(self)
        self.new_username_textbox.move(160, 20)

        '''Create new user password label'''
        self.new_user_password = QLabel("Password: ", self)
        self.new_user_password.setFont(self.font)
        self.new_user_password.move(20, 60)

        '''Create new user password textbox'''
        self.new_user_password_textbox = QLineEdit(self)
        self.new_user_password_textbox.move(160, 60)
        self.new_user_password_textbox.setEchoMode(QLineEdit.Password)

        '''Create confirm password label'''
        self.confirm_password_label = QLabel("Confirm password: ", self)
        self.confirm_password_label.setFont(self.font)
        self.confirm_password_label.move(20, 100)

        '''Create confirm password textbox'''
        self.confirm_password_textbox = QLineEdit(self)
        self.confirm_password_textbox.move(160, 100)
        self.confirm_password_textbox.setEchoMode(QLineEdit.Password)

        '''Create button that verifies credentials and registers the user if correct information is entered'''
        self.register_button = QPushButton("Register", self)
        self.register_button.move(self.frameSize().width() / 2 - 100,
                                  self.frameSize().height() / 2)
        self.register_button.clicked.connect(self.new_user_validate_credentials)

        self.invalid_credentials_label = None

        self.setWindowModality(Qt.ApplicationModal)
        self.show()

        if self.exec():
            pass

    """
    Allows the window to close properly when instructed to by the user.
    """

    def closeEvent(self, event):
        self.parent.show()
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

    def new_user_validate_credentials(self):
        if self.new_username_textbox.text() == "" or self.new_user_password_textbox.text() == "" or \
                        self.confirm_password_textbox.text() == "":
            self.invalid_credentials("no username or password")
        else:
            if validate_email(self.new_username_textbox.text()):
                cnu_email = self.new_username_textbox.text()[-7:]
                if cnu_email == "cnu.edu":
                    if self.new_user_password_textbox.text() == self.confirm_password_textbox.text():
                        with open("login_info.txt", 'a') as info:  # appends to the file
                            string = self.new_username_textbox.text() + " " + self.new_user_password_textbox.text()
                            info.write("\n" + string)
                            self.close()
                    else:
                        self.invalid_credentials("password")
                else:
                    self.invalid_credentials("email")
            else:
                self.invalid_credentials("email")

    def invalid_credentials(self, type_of_error):
        if self.invalid_credentials_label is not None:
            self.invalid_credentials_label.clear()
        else:
            self.invalid_credentials_label = QLabel("", self)

        font = QFont("Arial", 7)
        if type_of_error == "email":
            self.invalid_credentials_label.setText("Please enter an existing CNU email address.")
            self.invalid_credentials_label.move(160, 43)
        elif type_of_error == "password":
            self.invalid_credentials_label.setText("The entered passwords do not match.")
            self.invalid_credentials_label.move(160, 125)
        else:
            self.invalid_credentials_label.setText("Please remember to fill in all entries.")
            self.invalid_credentials_label.move(160, 125)

        self.invalid_credentials_label.setStyleSheet("color: red")
        self.invalid_credentials_label.setFont(font)
        self.invalid_credentials_label.show()
