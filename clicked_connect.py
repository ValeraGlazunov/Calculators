from modules.lists import list_numButtons, list_num_functions,list_Symbols_Button,list_sym_functions

for num in range(10):
    list_numButtons[num].clicked.connect(list_num_functions[num])
for sym in range(3,7):
    list_Symbols_Button[sym].clicked.connect(list_sym_functions[sym-3])
list_Symbols_Button[7].clicked.connect(list_sym_functions[4])
