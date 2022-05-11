# Fourth revision.

import tkinter

class ChangeCounterGUI:
     def __init__(self):

          # Create the main window, set-up necessary parameters.
          self.main_window = tkinter.Tk()
          self.main_window.title('Change Counter')
          self.main_window.geometry('400x200')

          # Create frames (text, quaters, dimes, nickels, pennies,and compute).
          self.text_frame = tkinter.Frame()
          self.dollars_frame = tkinter.Frame()
          self.halfdollars_frame = tkinter.Frame()
          self.quarters_frame = tkinter.Frame()
          self.dimes_frame = tkinter.Frame()
          self.nickels_frame = tkinter.Frame()
          self.pennies_frame = tkinter.Frame()
          self.compute_frame = tkinter.Frame()


          # Create the text-widget for the text_frame.
          self.text_label = tkinter.Label(self.text_frame, text='Enter the number of each coin type and hit, Compute:')
          # Pack the text_frame widget.
          self.text_label.pack(side='top')


          # Create the widget for the dollars frame, 
          self.dollars_label = tkinter.Label(self.dollars_frame, text='Dollars:')
          self.dollars_entry = tkinter.Entry(self.dollars_frame, width=10)
          self.dollarsvalue_label = tkinter.Label(self.dollars_frame, text='Dollar value: $')
          self.dollarsvalue = tkinter.StringVar()
          self.dollarsmoney_label = tkinter.Label(self.dollars_frame, textvariable=self.dollarsvalue)
          # Pack the dollars frame's widgets.
          self.dollars_label.pack(side='left')
          self.dollars_entry.pack(side='left')
          self.dollarsvalue_label.pack(side='left')
          self.dollarsmoney_label.pack(side='left')


          # Create a widgets for the half-dollars frame, I use 'hd' instead of half-dollars for short.
          self.hd_label = tkinter.Label(self.halfdollars_frame, text='Half-Dollars:')
          self.hd_entry = tkinter.Entry(self.halfdollars_frame, width=10)
          self.hdvalue_label = tkinter.Label(self.halfdollars_frame, text='Half-Dollar value: $')
          self.hdvalue = tkinter.StringVar()
          self.hdmoney_label = tkinter.Label(self.halfdollars_frame, textvariable=self.hdvalue)
          # Pack the hals-dollars frame's widgets.
          self.hd_label.pack(side='left')
          self.hd_entry.pack(side='left')
          self.hdvalue_label.pack(side='left')
          self.hdmoney_label.pack(side='left')
          
          # Create the widget for the quarters frame.
          self.quarters_label = tkinter.Label(self.quarters_frame, text='Quarters:')
          self.quarters_entry = tkinter.Entry(self.quarters_frame, width=10)
          self.qvalue_label = tkinter.Label(self.quarters_frame, text='Quater value: $')
          self.qvalue = tkinter.StringVar()
          self.quatersmoney_label = tkinter.Label(self.quarters_frame, textvariable=self.qvalue)
          # Pack the quaters frame's widgets.
          self.quarters_label.pack(side='left')
          self.quarters_entry.pack(side='left')
          self.qvalue_label.pack(side='left')
          self.quatersmoney_label.pack(side='left')


          # Create a widgets for the dimes frame, I use 'd' instead of dimes for short.
          self.d_label = tkinter.Label(self.dimes_frame, text='Dimes:')
          self.d_entry = tkinter.Entry(self.dimes_frame, width=10)
          self.dvalue_label = tkinter.Label(self.dimes_frame, text='Dime value: $')
          self.dvalue = tkinter.StringVar()
          self.dmoney_label = tkinter.Label(self.dimes_frame, textvariable=self.dvalue)
          # Pack the dimes frame's widgets.
          self.d_label.pack(side='left')
          self.d_entry.pack(side='left')
          self.dvalue_label.pack(side='left')
          self.dmoney_label.pack(side='left')


          # Create a widgets for the nickels frame, I use 'n' instead of nickels for short.
          self.n_label = tkinter.Label(self.nickels_frame, text='Nickels:')
          self.n_entry = tkinter.Entry(self.nickels_frame, width=10)
          self.nvalue_label = tkinter.Label(self.nickels_frame, text='Nickel value: $')
          self.nvalue = tkinter.StringVar()
          self.nmoney_label = tkinter.Label(self.nickels_frame, textvariable=self.nvalue)
          # Pack the nickels frame's widgets.
          self.n_label.pack(side='left')
          self.n_entry.pack(side='left')
          self.nvalue_label.pack(side='left')
          self.nmoney_label.pack(side='left')


          # Create a widgets for the pennies frame, I use 'p' instead of pennies for short.
          self.p_label = tkinter.Label(self.pennies_frame, text='Pennies:')
          self.p_entry = tkinter.Entry(self.pennies_frame, width=10)
          self.pvalue_label = tkinter.Label(self.pennies_frame, text='Penny value: $')
          self.pvalue = tkinter.StringVar()
          self.pmoney_label = tkinter.Label(self.pennies_frame, textvariable=self.pvalue)
          # Pack the nickels frame's widgets.
          self.p_label.pack(side='left')
          self.p_entry.pack(side='left')
          self.pvalue_label.pack(side='left')
          self.pmoney_label.pack(side='left')
  

          # Create the button widgets for the bottom frame.
          self.compute_button = tkinter.Button(self.compute_frame, text='Compute', command=self.compute)
          self.total_label = tkinter.Label(self.compute_frame, text='Total Change value: $')
          self.totalvalue = tkinter.StringVar()
          self.totalmoney_label = tkinter.Label(self.compute_frame, textvariable=self.totalvalue)
          # Pack the buttons.
          self.compute_button.pack(side='left')
          self.total_label.pack(side='left')
          self.totalmoney_label.pack(side='left')

          # Pack the frames.
          self.text_frame.pack()
          self.dollars_frame.pack()
          self.halfdollars_frame.pack()
          self.quarters_frame.pack()
          self.dimes_frame.pack()
          self.nickels_frame.pack()
          self.pennies_frame.pack()
          self.compute_frame.pack()

          # Enter the tkinter main loop.
          tkinter.mainloop()

     # The convert method is a callback function for the Calculate button.
     def compute(self):

          # Get the number of different coints from the user.
          dollars = int(self.dollars_entry.get())
          if dollars < 0:
              raise ValueError('Negative values not allowed!')
          halfdollars = int(self.hd_entry.get())
          if halfdollars < 0:
              raise ValueError('Negative values not allowed!')
          quarters = int(self.quarters_entry.get())
          if quarters < 0:
              raise ValueError('Negative values not allowed!')
          dimes = int(self.d_entry.get())
          if dimes < 0:
              raise ValueError('Negative values not allowed!')
          nickels = int(self.n_entry.get())
          if nickels < 0:
              raise ValueError('Negative values not allowed!')
          pennies = int(self.p_entry.get())
          if pennies < 0:
              raise ValueError('Negative values not allowed!')
          
          # Convert number of coints in $ value.
          dollarsvalue = (round(dollars * 1.00,2))
          hdvalue = (round(halfdollars * 0.50,2))
          qvalue = (round(quarters * 0.25,2))
          dvalue = (round(dimes * 0.10,2))
          nvalue = (round(nickels * 0.05,2))
          pvalue = (round(pennies * 0.01,2))
          totalvalue = (round(dollarsvalue + hdvalue + qvalue + dvalue + nvalue + pvalue,2))
          # Convert $ value to a string and store it in the StringVar object.
          self.dollarsvalue.set(dollarsvalue)
          self.hdvalue.set(hdvalue)
          self.qvalue.set(qvalue)
          self.dvalue.set(dvalue)
          self.nvalue.set(nvalue)
          self.pvalue.set(pvalue)
          self.totalvalue.set(totalvalue)
          

ChangeCounterGUI()
