from tkinter import Button, Label, Message
import random
import settings
import ctypes
import sys 

class Cell:
    all = []
    cell_count = settings.cell_count
    cell_count_label_object = None
    cell_instruction_label_obj = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            bg='purple',
            fg='black'
        )
        btn.bind('<Button-1>', self.left_click_actions) # left click
        btn.bind('<Button-3>', self.right_click_actions)  # right click
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='blue',
            text=f"Cells Left:{Cell.cell_count}",
            font=("Arial", 30, "bold")
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def create_instruction_label(location):
        lbl2 = Message(
            location,
            bg='black',
            fg='red',
            text='Instructions: Left click to select space, Right click to mark possible mine.',
            font=("Times", 20, "bold italic")
        )
        Cell.cell_instruction_label_obj = lbl2

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if mines count = cells left count, Player won
            if Cell.cell_count == settings.mines_count:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations!! You won!!', 'Game over!', 0)
                sys.exit()

        # cancel left and right click events if cell opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>') 

    def get_cell_by_axis(self, x, y):
        # return a cell object based on x, y value
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell 

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
    
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # replace text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                        text=f"Cells Left:{Cell.cell_count}"
                )
            # if mine candidate, config bg color too SytemButtonFace 

            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )

        # mark the cell as opened (use as last line of method)
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine!', 'Game over!!', 0)
        sys.exit()
    
    
    def right_click_actions(self, event):
        if not self.is_mine_candidate:
           self.cell_btn_object.configure(
               bg='orange'
           )
           self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='purple'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.mines_count 
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"