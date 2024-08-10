import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QWidget, QVBoxLayout


app = QApplication(sys.argv)

mainWindow = QMainWindow()

mainWindow.setWindowTitle("Hiển thị tên")

mainWindow.setGeometry(200,200,600,200)

central_widget = QWidget()
mainWindow.setCentralWidget(central_widget)

mainWindow.text_edit = QLineEdit()
mainWindow.display_button  = QPushButton("Hiển thị")
mainWindow.result_label = QLabel("")

layout = QVBoxLayout()

layout.addWidget(mainWindow.text_edit)
layout.addWidget(mainWindow.display_button)
layout.addWidget(mainWindow.result_label)

central_widget.setLayout(layout)

def display_text():
    entered_text = mainWindow.text_edit.text()
    mainWindow.result_label.setText(f"Tên của bạn là: {entered_text}")

mainWindow.display_button.clicked.connect(display_text)

mainWindow.show()

sys.exit(app.exec_())



