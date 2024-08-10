import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QWidget, QVBoxLayout

app = QApplication(sys.argv)

mainWindow = QMainWindow()

mainWindow.setWindowTitle("Quản lý thông tin các nhân")

mainWindow.setGeometry(200,200,600,200)

central_widget = QWidget()
mainWindow.setCentralWidget(central_widget)

mainWindow.lblHoTen = QLabel("Họ và tên: ")
mainWindow.text_edit_HoTen = QLineEdit()
mainWindow.lblSdt = QLabel("Số điện thoại: ")
mainWindow.text_edit_Sdt = QLineEdit()
mainWindow.result_label = QLabel("")

mainWindow.display_btton_Luu = QPushButton("Lưu Thông tin")
mainWindow.display_btton_Xoa = QPushButton("Xóa Thông tin")

layout = QVBoxLayout()

def display_text():
    entered_text_hoten = mainWindow.text_edit_HoTen.text()
    mainWindow.result_label.setText(f"Tên của bạn là: {entered_text_hoten}")

    entered_text_Sdt = mainWindow.text_edit_Sdt.text()
    mainWindow.result_label.setText(f"Số điện thoại của bạn là: {entered_text_Sdt}")

mainWindow.display_btton_Luu.clicked.connect(display_text)

mainWindow.show()

sys.exit(app.exec_())
