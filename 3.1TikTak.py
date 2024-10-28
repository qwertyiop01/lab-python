import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt5.QtWidgets import QMessageBox, QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.score=0
        self.choice_dialog = None

    def work(self):
            if self.sender() == self.value_x and self.value_x.isChecked():
                QMessageBox.information(self, 'Выбор', 'Вы выбрали X!')
            elif self.sender() == self.value_o and self.value_o.isChecked():
                QMessageBox.information(self, 'Выбор', 'Вы выбрали O!')

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Крестики-нолики')

        self.value_x = QRadioButton ("x", self)
        self.value_x.setChecked(True)
        self.value_x.setGeometry(230,20,100,30)
        #self.value_x.toggled.connect(self.work)

        self.value_o = QRadioButton("o", self)
        self.value_o.setGeometry (270,20,100,30)
        #self.value_o.toggled.connect(self.work)

        self.play_field()
    
    def play_field(self):
        field = QGridLayout()
        self.setLayout(field)
        self.slots = []
        for i in range (3):
            slot_row=[]
            for j in range (3):
                self.slot = QPushButton(" ", self)
                self.slot.setFixedSize(30,30)
                self.slot.clicked.connect(self.make_play)
                field.addWidget(self.slot,i,j)
                slot_row.append(self.slot)
            self.slots.append(slot_row)
            #print (self.slots)
    
    def make_play(self):
        sender = self.sender()  
        value = "x" if self.value_x.isChecked() else "o"
    
        #if sender.text() in ("x", "o"):
        #    QMessageBox.information(self, "Error" ,"Эта ячейка занята!")
        #else:
            #sender.text() not in ("x", "o")
        sender.setText(value)
        sender.setEnabled(False)
        self.score+=1
        self.value_x.setChecked(value == "o") 
        self.value_o.setChecked(value == "x")
    
        if self.check_winner(): 
            QMessageBox.information(self, 'Победа!', f'Выиграл {value}!')
            self.choise()

        elif self.score == 9:  # Проверка на ничью
            self.loss()
         

    def check_winner(self):
        
        for row in range(3):
            if (self.slots[row][0].text() == self.slots[row][1].text() == self.slots[row][2].text() and
                self.slots[row][0].text() != " "):
                return True

        for col in range(3):
            if (self.slots[0][col].text() == self.slots[1][col].text() == self.slots[2][col].text() and
                self.slots[0][col].text() != " "):
                return True 

        if (self.slots[0][0].text() == self.slots[1][1].text() == self.slots[2][2].text() and
            self.slots[0][0].text() != " "):
            return True

        if (self.slots[0][2].text() == self.slots[1][1].text() == self.slots[2][0].text() and
            self.slots[0][2].text() != " "):
            return True

        return False

    def loss(self):
        QMessageBox.information(self, 'Ничья!', 'Как-нибудь у вас получится!')
        self.choise()
    
    def choise(self):
        if self.choice_dialog is not None:
            return
        
        self.choice_dialog = QWidget()  
        self.choice_dialog.setGeometry(300, 300, 300, 200)
        self.choice_dialog.setWindowTitle('Хотите ли вы продолжить игру?')

        button_1 = QPushButton("Да", self.choice_dialog)
        button_1.move(90, 40)
        button_1.clicked.connect(self.reset_game)

        button_2 = QPushButton("Нет", self.choice_dialog)
        button_2.move(90, 80)
        button_2.clicked.connect(self.choice_dialog.close) 
        button_2.clicked.connect(lambda: self.set_choice_dialog(None))

        self.choice_dialog.show()  

    def reset_game(self): 
        if self.choice_dialog is not None:
            self.choice_dialog.close()
            self.choice_dialog = None

        for row in range(3):
            for col in range(3):
                self.slots[row][col].setText(" ")
                self.slots[row][col].setEnabled(True)
        
        self.score = 0
        self.value_x.setChecked(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())