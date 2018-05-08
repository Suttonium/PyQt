from PYTHON_MODULES.PYQT.PROJECTS.LoginSystem.email_file_dialog import *

class Editor(QMainWindow):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.parent = parent
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowTitle("Editor")

        '''Coding the main menu.'''
        self.main_menu = self.menuBar()

        '''Coding the options within the main menu.'''
        self.file_main_menu_option = self.main_menu.addMenu("&File")  # file
        self.edit_main_menu_option = self.main_menu.addMenu("&Edit")  # edit
        self.view_main_menu_option = self.main_menu.addMenu("&View")  # view

        self.create_blank_text_editor()
        self.add_file_sub_menus()
        self.move_to_center("")

        self.show()

    """
    Coding the options under the File secondary menu.
    """

    def add_file_sub_menus(self):
        self.file_actions = []

        '''Actions to create an option for a new file.'''
        self.new_file_action = QAction("&New...", self)
        self.new_file_action.setShortcut("Ctrl+N")
        self.new_file_action.setStatusTip("New File")
        self.new_file_action.triggered.connect(self.create_blank_text_editor)
        self.file_actions.append(self.new_file_action)

        '''Actions to open a file.'''
        self.open_file_action = QAction("&Open...", self)
        self.open_file_action.setShortcut("Ctrl+O")
        self.open_file_action.setStatusTip("Open File")
        self.open_file_action.triggered.connect(self.open_file)
        self.file_actions.append(self.open_file_action)

        '''Actions to save a file'''
        self.save_file_action = QAction("&Save...", self)
        self.save_file_action.setShortcut("Ctrl+S")
        self.save_file_action.setStatusTip("Save File")
        self.save_file_action.triggered.connect(self.save_file)
        self.file_actions.append(self.save_file_action)

        '''Add action to email file'''
        self.email_file_action = QAction("&Share", self)
        self.email_file_action.setStatusTip("Email Your Current File")
        self.file_actions.append(self.email_file_action)
        self.email_file_action.triggered.connect(self.email_file)

        for action in self.file_actions:
            self.file_main_menu_option.addAction(action)

    def email_file(self):
        self.hide()
        self.email_dialog = Email(self)

    """
    creates a new text editor with zero input
    """

    def create_blank_text_editor(self):
        self.text_editor = QTextEdit()
        self.text_editor.clear()
        self.setCentralWidget(self.text_editor)

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
    Saves the current state of the text editor to a file and location of the user's choice.
    """

    def save_file(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        try:
            file = open(name, 'w')
            text = self.text_editor.toPlainText()
            file.write(text)
            file.close()
        except:
            pass

    """
    Open's a user-specified file from the computer.
    """

    def open_file(self):
        try:
            name = QFileDialog.getOpenFileName(self, "Open File")
            file = open(name, 'r')
            self.create_blank_text_editor()
            with file:
                text = file.read()
                self.text_editor.setText(text)
        except:
            pass

    """
    Returns the current character length of the text editor.
    """

    def get_editor_character_length(self):
        my_text = self.text_editor.toPlainText()
        return len(my_text)

    def closeEvent(self, event):
        event.accept()
