from ic import ICChip, Pin

title = 'SN74259 - 8bit Addressable Register'

pins = [
    #   Label   Tag    Input        Left
    Pin('ADR0', 'A0',  Pin.INPUT,   Pin.LEFT),
    Pin('ADR1', 'A1',  Pin.INPUT,   Pin.LEFT),
    Pin('ADR2', 'A2',  Pin.INPUT,   Pin.LEFT),
    Pin('OUT0', 'Q0',  Pin.OUTPUT,  Pin.LEFT),
    Pin('OUT1', 'Q1',  Pin.OUTPUT,  Pin.LEFT),
    Pin('OUT2', 'Q2',  Pin.OUTPUT,  Pin.LEFT),
    Pin('OUT3', 'Q3',  Pin.OUTPUT,  Pin.LEFT),
    Pin('GND',  'GN',  Pin.INPUT,   Pin.LEFT),
    Pin('VCC',  '5V',  Pin.INPUT,   Pin.RIGHT),
    Pin('CLR',  'CL',  Pin.INPUT,   Pin.RIGHT),
    Pin('ENAB', 'EN',  Pin.INPUT,   Pin.RIGHT),
    Pin('DATA', 'D0',  Pin.INPUT,   Pin.RIGHT),
    Pin('OUT7', 'Q7',  Pin.OUTPUT,  Pin.RIGHT),
    Pin('OUT6', 'Q6',  Pin.OUTPUT,  Pin.RIGHT),
    Pin('OUT5', 'Q5',  Pin.OUTPUT,  Pin.RIGHT),
    Pin('OUT4', 'Q4',  Pin.OUTPUT,  Pin.RIGHT),
]

def logic(self:ICChip, *args):
    '''
    Arguments:
    self:ICChip - Instance of the current chip with a Dictionary of pins
    *args - Arguments passed from event that triggered this method
    
    ICChip Properties:
        pins:dict[_icpin] - A Dictionary of Pins indexed by Tag (not by Label)
        
    Pin Properties:
        state:bool - True if HIGH, False if LOW
        on:method - turns the pin HIGH
        off:method - turns the pin LOW
        toggle:method - toggles pin from HIGH to LOW or LOW to HIGH
    '''
    
    print(f'Pressed {args[0].tag}, {args[1][0]}')
    
    EN = self.pins["EN"].state
    CL = self.pins["CL"].state
    VCC = self.pins["5V"].state
    GND = self.pins["GN"].state

    if not CL or not VCC or not GND:
        for pin in self.pins.values():
            if not pin.input:
                pin.off()

    if EN and VCC and GND:
        A0 = self.pins["A0"].state
        A1 = self.pins["A1"].state
        A2 = self.pins["A2"].state
        D0 = self.pins["D0"].state
        sel = 0
        if A0:
            sel += 1
        if A1:
            sel += 2
        if A2:
            sel += 4

        key = f'Q{sel}'
        pin = self.pins[key]

        if D0:
            pin.on()
        else:
            pin.off()
