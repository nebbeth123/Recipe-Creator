import tkinter as tk
import time

class Gui:
    def __init__(self):
        pass
        self.root = None

    def create_window(self):
        self.root = tk.Tk()

    def create_labels(self):
        self.instructions_text_label = tk.Label(self.root, anchor='center',
                                                height=Config.window_height,
                                                width=Config.window_width,
                                                bg=Config.instructions_bg_color,
                                                fg=Config.instructions_font_color,
                                                font="{} {}".format(Config.instructions_font,
                                                                    Config.instructions_font_size))

        self.stimulus_label = tk.Label(self.root, anchor='center',
                                       height=Config.window_height,
                                       width=Config.window_width,
                                       bg=Config.stimulus_bg_color,
                                       fg=Config.stimulus_font_color,
                                       font="{} {}".format(Config.stimulus_font,
                                                           Config.stimulus_font_size))
    def show_instructions(self):   
        pass

    def show_stimulus(self):  
        pass

    def preload_images(self):
        pass
    
