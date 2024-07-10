import sys
import zmq
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal

class SubscriberThread(QThread):
    new_message = pyqtSignal(str)

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect("tcp://localhost:5555")
        socket.setsockopt_string(zmq.SUBSCRIBE, "")

        while True:
            message = socket.recv_string()
            self.new_message.emit(message)

class SubscriberApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.subscriber_thread = SubscriberThread()
        self.subscriber_thread.new_message.connect(self.display_message)
        self.subscriber_thread.start()

    def initUI(self):
        self.setWindowTitle('Subscriber')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.layout.addWidget(self.text_edit)

        self.clear_button = QPushButton('Clear', self)
        self.clear_button.clicked.connect(self.text_edit.clear)
        self.layout.addWidget(self.clear_button)

        self.setLayout(self.layout)

    def display_message(self, message):
        self.text_edit.append(message)

def main():
    app = QApplication(sys.argv)
    subscriber_app = SubscriberApp()
    subscriber_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
