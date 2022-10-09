from Pyqt5.QtCore import Qt
from Pyqt5.QtWidgets import QAppLication, QWidget, QPushButton, QLabel, \
    QListWidget, QLineEdit, QtextEdit, QInputDialog, \
        QHBoxLayout, QVBoxLayout, QFormLayout

import json

app = QAppLication([])
main_win = QWidget()
main_win.setWindowTitle("Розумні нотатки")
main_win.resize(900, 600)

list_notes  = QListWidget()
list_notes_label = QLabel("Список нотаток: ")

button_note_create = QPushButton("Створити нотатку")
button_note_del = QPushButton("Видалити нотатку")
button_note_save = QPushButton("Зберегти нотатку")

field_tag = QLineEdit('')
field_tag.setPlaceholderText("Введіть тег...")
field_text = QtextEdit()

button_tag_add = QPushButton("Додати до нотатки")
button_note_del = QPushButton("Видалити тег")
button_note_search = QPushButton("Шукати по тегові")

list_tags = QListWidget()
list_tags_label = QLabel("Список тегів")

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_notes_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_note_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_note_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)

main_win.setLayout(layout_notes)
main_win.show()
app.exec_()