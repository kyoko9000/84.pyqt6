import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QStyle, QWidget, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Specific Icon Example")
        # tạo icon cho màn hình
        icon1 = self.style().standardIcon(QStyle.StandardPixmap.SP_FileDialogInfoView)
        self.setWindowIcon(icon1)

        # Tạo một nút với biểu tượng cụ thể
        button = QPushButton("Click Me")

        # 1 change icon just change text
        # icon_name = "SP_MediaPlay"  # Tên của biểu tượng bạn muốn sử dụng
        # pixmapi = getattr(QStyle.StandardPixmap, icon_name)
        # icon = self.style().standardIcon(pixmapi)

        # 2 change icon simple code
        # icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxQuestion)

        # 3 use image to make icon
        icon = QIcon('2.jpg')

        button.setIcon(icon)

        # Thiết lập layout
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
