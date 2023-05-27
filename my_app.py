import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(600, 300, 300, 200)

  
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

   
        self.num1_label = QLabel("Число 1:")
        self.num1_input = QLineEdit()
        self.num2_label = QLabel("Число 2:")
        self.num2_input = QLineEdit()
        self.result_label = QLabel("Результат:")
        self.result_display = QLabel()

        self.add_button = QPushButton("Сложение")
        self.subtract_button = QPushButton("Вычитание")
        self.multiply_button = QPushButton("Умножение")
        self.divide_button = QPushButton("Деление")

      
        input_layout.addWidget(self.num1_label)
        input_layout.addWidget(self.num1_input)
        input_layout.addWidget(self.num2_label)
        input_layout.addWidget(self.num2_input)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.subtract_button)
        button_layout.addWidget(self.multiply_button)
        button_layout.addWidget(self.divide_button)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_display)

        
        self.add_button.clicked.connect(self.perform_addition)
        self.subtract_button.clicked.connect(self.perform_subtraction)
        self.multiply_button.clicked.connect(self.perform_multiplication)
        self.divide_button.clicked.connect(self.perform_division)

        self.setLayout(main_layout)

    def perform_addition(self):
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        result = num1 + num2
        self.result_display.setText(str(result))

    def perform_subtraction(self):
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        result = num1 - num2
        self.result_display.setText(str(result))

    def perform_multiplication(self):
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        result = num1 * num2
        self.result_display.setText(str(result))

    def perform_division(self):
        num1 = float(self.num1_input.text())
        num2 = float(self.num2_input.text())
        if num2 != 0:
            result = num1 / num2
            self.result_display.setText(str(result))
        else:
            self.result_display.setText("Ошибка: на ноль делить нельзя")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())
