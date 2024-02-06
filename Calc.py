import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry('350x450')
        master.resizable(False, False)
        
        self.equation = tk.StringVar()
        self.equation.set('')
        
        # Entry widget to display the equation
        self.entry = tk.Entry(master, textvariable=self.equation, font=('Arial', 18), bd=5, relief=tk.SOLID, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='ew', padx=10, pady=10)
        
        # Buttons for numbers and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('%', 5, 3)
        ]
        
        for label, row, col in buttons:
            btn = tk.Button(master, text=label, font=('Arial', 16), width=5, height=2, bd=3, relief=tk.RAISED,
                            command=lambda label=label: self.button_click(label))
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # Bind Enter key to evaluate equation
        master.bind('<Return>', lambda event: self.button_click('='))
    
    def button_click(self, label):
        if label == '=':
            try:
                self.solve()
            except Exception as e:
                self.equation.set('Error')
        elif label == 'C':
            self.equation.set('')
        else:
            self.equation.set(self.equation.get() + label)
            
    def solve(self):
        #Replace 'x' with '*'
        expression = self.equation.get().replace('x', '*')
        result = eval(expression)
        self.equation.set(result)
        

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()