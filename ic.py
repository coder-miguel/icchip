from tkinter import Canvas
from functools import partial


class Pin:
    LEFT = True
    RIGHT = False
    INPUT = True
    OUTPUT = False
    ON = True
    OFF = False

    def __init__(self, name: str, tag: str, input=True, left=True):
        self.name = name
        self.tag = tag
        self.input = input
        self.left = left


class ICChip:
    def __init__(self):
        print('ICChip: Bad initialization.')
        exit()

    def __init__(self, pins: list[Pin] = [], logic=None, canvas: Canvas = None, xpos: int = 30, ypos: int = 15, pin_w: int = 100, pin_h: int = 40, v_pad: int = 15, h_pad: int = 100, color: str = "#223355"):
        if not canvas:
            print('ICChip: No Canvas.')
            exit()
        self.pins = {}
        self._canvas = canvas
        top = ypos
        right = xpos + pin_w + h_pad
        left = xpos
        self._canvas.create_rectangle(
            left + int(pin_w/2),
            top,
            left + pin_w + h_pad + int(pin_w/2),
            top + (((len(pins)/2)) * (pin_h + v_pad)) + v_pad, fill=color)
        i_left = 0
        i_right = 0
        for pin in pins:
            if pin.left:
                icpin = ICChip._icpin(pin.name, pin.tag, pin.input,
                                      left,
                                      pin_h*i_left+top+v_pad*(i_left+1),
                                      pin_w,
                                      pin_h,
                                      self._canvas)
                icpin.draw()
                i_left += 1
            else:
                icpin = ICChip._icpin(pin.name, pin.tag, pin.input,
                                      right,
                                      pin_h*i_right+top+v_pad*(i_right+1),
                                      pin_w,
                                      pin_h,
                                      self._canvas)
                icpin.draw()
                i_right += 1

            self.pins[pin.tag] = icpin
            self._canvas.tag_bind(pin.tag, "<Button-1>",
                                  partial(self._pushed, icpin))
            self.logic = partial(logic, self)

    class _icpin:
        state = False

        def __init__(self):
            self.label = "Error"
            self.tag = "error"
            self.input = Pin.ON
            self.x = -1
            self.y = -1
            self.w = -1
            self.h = -1
            self.canvas = None

        def __init__(self, label, tag, input, x, y, w, h, canvas: Canvas):
            self.label = label
            self.tag = tag
            self.input = input
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.canvas = canvas
            self.state = Pin.OFF
            self.color = "silver" if self.input else "dim gray"

        def off(self):
            self.state = Pin.OFF
            self.color = "silver" if self.input else "dim gray"
            self.draw()

        def on(self):
            self.state = Pin.ON
            self.color = "gold" if self.input else "red3"
            self.draw()

        def toggle(self):
            if self.state:
                self.off()
            else:
                self.on()

        def draw(self):
            self.canvas.delete(self.tag)
            self.canvas.create_rectangle(
                self.x,
                self.y,
                self.x + self.w,
                self.y + self.h,
                fill=self.color, tags=self.tag)
            font_size = int(self.h/3) if (self.h *
                                          2) < self.w else int(self.w/(2 * 3))
            self.canvas.create_text(
                self.x + int(self.w/2),
                self.y + int(self.h/2),
                text=self.label, font=("", font_size), tags=self.tag)

    def _pushed(self, the_pin: _icpin, *args):
        if the_pin.input:
            the_pin.toggle()
            self.logic(the_pin, args)

    def logic(self, *args):
        '''
        Arguments:
        self:ICChip - Instance of the current chip with a Dictionary of pins
        *args - Arguments passed from event that triggered this method
        
        ICChip Properties:
            pins:dict[_icpin] - A Dictionary of pins indexed by Tag (not by Label)
            
        Pin Properties:
            state:bool - True if HIGH, False if LOW
            on:method - turns the pin HIGH
            off:method - turns the pin LOW
            toggle:method - toggles pin from HIGH to LOW or LOW to HIGH
        '''
        pass
