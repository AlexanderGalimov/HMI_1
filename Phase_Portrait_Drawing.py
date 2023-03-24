import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
import numpy as np


class Window:
    root = tk.Tk()

    def __init__(self):
        self.root.title("Phase Portrait Drawing")
        self.root.geometry('1000x700')
        self.path = None
        button1 = tk.Button(self.root, text="Select ASC File", command=self.select_file)
        button2 = tk.Button(self.root, text="Draw Phase Portrait", command=self.instant_draw_function)
        button3 = tk.Button(self.root, text="Draw Phase Portrait Step-By-Step", command=self.step_drawing_function)
        button1.pack()
        button2.pack()
        button3.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("ASC file", "*.asc")])
        self.path = file_path

    def start(self):
        self.root.mainloop()

    def instant_draw_function(self):
        if self.path is not None and self.path != '':

            data = np.loadtxt(self.path, skiprows=4)

            emg_data = data[:, 1]
            x = []
            y = []

            for i in range(0, len(emg_data) - 1):
                x.append(emg_data[i])

            for i in range(1, len(emg_data)):
                y.append(emg_data[i])

            # Настраиваем размеры графиков и создаем фигуру
            plt.rcParams["figure.figsize"] = [10, 6]

            fig1, ax1 = plt.subplots()

            # Строим скатерограмму
            ax1.plot(x, y, linewidth=0.2, color='grey')
            ax1.plot(x, y, '.', markersize=1)

            ax1.set_xlabel("RRn")
            ax1.set_ylabel("RRn+1")
            ax1.set_title("EMG Phase Portrait and Scatter Plot")

            # Показываем графики
            plt.show()

        else:
            messagebox.showinfo("Error", "Choose file correctly")

    def step_drawing_function(self):
        if self.path is not None and self.path != '':
            data = np.loadtxt(self.path, skiprows=4)
            x = []
            y = []
            emg_data = data[:, 1]

            for i in range(0, len(emg_data) - 1):
                x.append(emg_data[i])

            for i in range(1, len(emg_data)):
                y.append(emg_data[i])

            plt.rcParams["figure.figsize"] = [10, 6]

            plt.ion()

            fig1, ax1 = plt.subplots()

            for i in range(len(x)):
                try:
                    ax1.plot(x[:i], y[:i], '.', markersize=1, color='blue')
                    ax1.plot(x[:i], y[:i], linewidth=0.2, color='grey')
                    plt.pause(0.1)
                except KeyboardInterrupt:
                    break

            plt.show()

        else:
            messagebox.showinfo("Error", "Choose file correctly")


window = Window()
window.start()
