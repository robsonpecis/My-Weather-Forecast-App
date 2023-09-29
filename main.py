import requests
from  tkinter import *
from tkinter import ttk
from token_api import api_key

city_name = ''
def get_wheater():
    city_name = get_city.get()
    request_wheater = requests(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')

    print(request_wheater)


# Creat the window
window = Tk()
window.geometry('400x200')

get_city = StringVar(window)
get_city.set('')


# List of states and cities
options_state = [
    'Default',
    'Estado1',
    'Estado2'
]

options_city = ['']

state1 = [
    'Default',
    'Rio de Janeiro',
    'Esatdo1, cidade2',
]

state2 = [
    'Default',
    'Estado2, Cidade1',
    'Esatdo2, cidade2',
]

# Function to bind the comboboxs
def pick_state(e):
    if state_combobox.get() == 'Estado1':
        city_combobox.config(value=state1)
        city_combobox.current(0)
    if state_combobox.get() == 'Estado2':
        city_combobox.config(value=state2)
        city_combobox.current(0)


# Edit the windows title
window.title('Previsão do Tempo')

# Head
head = Label(window, text='Previsão do Tempo')
head.grid(column=2, row=0)

# Combobox heads
text_dropdown_state = Label(window, text='Estado:')
text_dropdown_state.grid(column=1, row=1)

text_dropdown_city = Label(window, text='Cidade:')
text_dropdown_city.grid(column=3, row=1)

# Dropdown States
state_combobox = ttk.Combobox(window, values=options_state)
state_combobox.current(0)
state_combobox.grid(column=1, row=2)

# Bind the combobox
state_combobox.bind('<<ComboboxSelected>>', pick_state)

# Combobox City
city_combobox = ttk.Combobox(window, textvariable=city_name, values=[''])
city_combobox.current(0)
city_combobox.grid(column=3, row=2)

# Send the value to a var

# Button to shearch
button = Button(window, text='Pesquisar', command=get_wheater)
button.grid(column=2, row=3)

window.mainloop() # Keep the window open
# End of the window code
