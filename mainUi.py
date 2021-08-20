from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sys
from richUtils import richPresence
from urllib.parse import urlparse


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def validString(st):
    if len(st) >= 2:
        return True
    return False


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi("Main.ui", self)  # Load the .ui file
        self.buttonUpdate.clicked.connect(self.buttonUpdatePressed)
        self.show()  # Show the GUI

    def buttonUpdatePressed(self):
        # This is executed when the button is pressed
        # Terminate the process
        # proc.terminate()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Empty Field(s)")
        msg.setWindowTitle("Error")
        if not validString(self.textDetail.text()) or not validString(
            self.textStat.text()
        ):
            msg.setInformativeText(
                "Make sure that atleast the Details and stat are filled"
            )
            msg.exec_()
        elif not validString(self.textLabel.text()) and validString(
            self.textUrl.text()
        ):
            msg.setInformativeText("Please enter a label")
            msg.exec_()

        elif validString(self.textLabel.text()) and not is_url(self.textUrl.text()):
            msg.setInformativeText("please enter a valid url ")
            msg.exec_()
            self.textUrl.setText("https://")
        else:
            args = [self.textDetail.text(), self.textStat.text()]
            if validString(self.textLabel.text()):
                args = args + [self.textLabel.text(), self.textUrl.text()]
            richPresence(args)


app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication

window = Ui()  # Create an instance of our class
app.exec_()  # Start the application

window.textDetail.setText("Text Changed")
window.update()
