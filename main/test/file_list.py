from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QAbstractItemView

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)  # Enable multiple selection

        for i in range(10):
            self.list_widget.addItem(f'Item {i}')

        layout.addWidget(self.list_widget)

        self.setLayout(layout)

        self.list_widget.itemSelectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self):
        selected_items = self.list_widget.selectedItems()
        selected_texts = [item.text() for item in selected_items]
        print('Selected items:', selected_texts)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
