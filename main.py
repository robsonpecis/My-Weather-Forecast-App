import requests
from  tkinter import *
from tkinter import ttk
from token_api import api_key


def get_wheater(city, token):
    city = get_city.get()
    request_wheater = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&lang=pt_br')
    request_dic = request_wheater.json()
    weather = request_dic['weather'][0]['description']
    temp = request_dic['main']['temp'] - 273.15
    sens_temp = request_dic['main']['feels_like'] - 273.15

    exibition = f'''
    Clima: {weather}
    Temperatura: {temp:.0f}ºC
    Sensação termica: {sens_temp:.0f}ºC'''

    text_exibition['text'] = exibition


def get_state():
    request_states = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome')
    request_states_dic = request_states.json()

    acronym = []
    state =['-- Selecionar --']
    for indice, n in enumerate(request_states_dic):
        acronym.append(request_states_dic[indice]['sigla'])
        state.append(request_states_dic[indice]['nome'])

    return state, acronym

def get_cities(uf):
    request_cities = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos?orderBy=nome')
    request_cities_dic = request_cities.json()

    cities = ['-- Selecionar --']
    for indice, n in enumerate(request_cities_dic):
        cities.append(request_cities_dic[indice]['nome'])
    
    return cities

# Creat the window
window = Tk()
window.geometry('400x200')

city_name = ''
get_city = StringVar(window)
get_city.set('')


# List of states and cities
states_and_ufs = get_state()
options_state = states_and_ufs[0]
options_uf = states_and_ufs[1]


options_city = []
city_list = []

for indice, state in enumerate(options_state):
    options_city.append(get_cities(options_uf[indice - 1]))

# Function to bind the comboboxs
def pick_state(e):
    for indice, state in enumerate(options_state):
        if state_combobox.get() == state:
            city_combobox.config(value=options_city[indice])
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
city_combobox = ttk.Combobox(window, textvariable=get_city, values=[''])
city_combobox.current(0)
city_combobox.grid(column=3, row=2)

# Send the value to a var

# Button to shearch
button = Button(window, text='Pesquisar', command=lambda: get_wheater(city_name, api_key))
button.grid(column=2, row=3)

text_exibition = Label(window, text='')
text_exibition.grid(column=2, row=4)

window.mainloop() # Keep the window open
# End of the window code
