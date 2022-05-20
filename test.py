import tkinter as tk
from ic import ICChip
import ic74259


if __name__ == '__main__':
    try:
        width = 500
        height = 500
        root = tk.Tk()
        root.title(ic74259.title)
        root.configure(background="black")
        root.geometry(f'{width}x{height}+100+100')
        root.maxsize(width, height)
        root.minsize(width, height)

        canvas = tk.Canvas(root, width=width, height=height, bg='#444444')
        canvas.pack()
        canvas.update()

        chip = ICChip(pins=ic74259.pins, logic=ic74259.logic, canvas=canvas, color="pink3")
        canvas.pack()
        canvas.update()
        
        root.mainloop()

    except KeyboardInterrupt as ki:
        print(ki.args)
    except Exception as e:
        print(e.args)
