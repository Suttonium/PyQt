from PYQT.PROJECTS.LoginSystem.editor import *
from PYQT.PROJECTS.LoginSystem.login_dialog_box import *

from PYTHON_MODULES.PYQT.PROJECTS.LoginSystem.user_registration import *

"""
PROBLEMS TO FIX:
1) disable save if nothing in text editor
2) Need to check if the email already exists when registering 
3) add multiple recipients for email
"""

"""
Main class which starts the application by loading the login screen. 
"""


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.login_dialog_box = LoginDialogBox()


def main():
    application, GUI = QApplication(sys.argv), Main()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
