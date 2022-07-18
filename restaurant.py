from tkinter import *

operador = ''
price_food = [50.50, 45.50, 62.31, 45.00, 55.00, 80.99, 20.05, 20.65]
price_beverages = [45.50, 39.99, 37.21, 51.54, 61.08, 71.10, 20.00, 31.58]



#Validar si el check o frame esta activo o no
def revise_check():
    x = 0
    for i in food_frame:
        if food_val[x].get() == 1:
            food_frame[x].config(state=NORMAL)
            #Si cuadro comida es igual a0
            if food_frame[x].get() == '0':
                food_frame[x].delete(0, END)
            food_frame[x].focus()
        else:
            food_frame[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1


    x = 0
    for i in beverages_frame:
        if beverages_val[x].get() == 1:
            beverages_frame[x].config(state=NORMAL)
            if beverages_frame[x].get() == '0':
                beverages_frame[x].delete(0, END)
            beverages_frame[x].focus()
        else:
            beverages_frame[x].config(state=DISABLED)
            beverages_text[x].set('0')
        x += 1


def total():
    sub_total_food = 0
    f = 0
    for amount in food_text:
        sub_total_food = sub_total_food + (float(amount.get()) * price_food[f])
        f += 1

    sub_total_beverages = 0
    f = 0
    for amount in beverages_text:
        sub_total_beverages = sub_total_beverages + (float(amount.get()) * price_beverages[f])
        f += 1

    sub_total = sub_total_food + sub_total_beverages
    taxs = sub_total * 0.16
    total = sub_total + taxs

    var_cost_food.set(f'${round(sub_total_food, 2)}')
    var_cost_beverages.set(f'${round(sub_total_beverages, 2)}')
    var_subtotal.set(f'${round(sub_total, 2)}')
    var_taxs.set(f'${round(taxs, 2)}')
    var_total.set(f'${round(total, 2)}')


def cal_reset():
    for text in food_text:
        text.set('0')
    for text in beverages_text:
        text.set('0')

    for c in food_frame:
        c.config(state=DISABLED)
    for c in beverages_frame:
        c.config(state=DISABLED)

    for check in food_val:
        check.set(0)
    for check in beverages_val:
        check.set(0)

    var_cost_food.set('')
    var_cost_beverages.set('')
    var_subtotal.set('')
    var_taxs.set('')
    var_total.set('')


# inicializador
app = Tk()

# Medidas de la ventana
app.geometry('1100x630+0+0')


app.title("Sistema de Facturacion")
app.config(bg='LightSkyBlue4')

# Panel superior
top_panel = Frame(app, bd=1, relief=SUNKEN)
top_panel.pack(side=TOP)

# etiqueta titulo
tag_title = Label(top_panel, text='Sistema de Cotización', fg='azure4', font=('Dosis', 58), bg='LightSkyBlue4', width=20)

tag_title.grid(row=0, column=0)

# Panel izquierdo

left_panel = Frame(app, bd=1, relief=FLAT, )
left_panel.pack(side=LEFT)

# Panel costos
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='CadetBlue3', padx=60 )
cost_panel.pack(side=BOTTOM)

# Panel comidas

food_panel = LabelFrame(left_panel, text='Comida', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='saddle brown')
food_panel.pack(side=LEFT)

# Panel de bebidas
beverages_panel = LabelFrame(left_panel, text='Bebidas', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='saddle brown')
beverages_panel.pack(side=LEFT)


# Panel derecha
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)


# Panel calculadora
button_panel = Frame(right_panel, bd=1, relief=FLAT, bg='LightSkyBlue4')
button_panel.pack()

# lista de productos
food_list = ['Hamburguesa', 'Pizza', 'Hot dog', 'Papas', 'Nuggets', 'Alitas']
beverages_list = ['Agua', 'Soda', 'Jugo', 'Coca Cola','Cerveza', 'Malteada']


#generar producto de comida en una lista
food_val = []
food_frame = []
food_text = []

#Se hace un recorrido para crear los checkbuttons de las listas
account = 0
for food in food_list:

    #Crear el check
    food_val.append('') #Se agrega un elemento vacio
    food_val[account] = IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=('Dosis',16, 'bold'),onvalue=1, offvalue=0, variable=food_val[account], command=revise_check)
    food.grid(row=account, column=0, stick=W)

    #Se crea el cuadro de entrada

    food_frame.append('')
    food_text.append('')
    food_text[account] = StringVar()
    food_text[account].set('0')
    food_frame[account] = Entry(food_panel, font=('Dosis', 16, 'bold'), bd=1, width=6, state=DISABLED, textvariable=food_text[account])

    food_frame[account].grid(row=account, column=1)

    account += 1

#Crear una lista comida
beverages_val = []
beverages_frame = []
beverages_text = []

#Se hace un recorrido para agregar el checkbutton a cada bebida
account = 0
for beverages in beverages_list:
    # Crear el check
    beverages_val.append('') #Se agrega un elemento vacio
    beverages_val[account] = IntVar()
    beverages = Checkbutton(beverages_panel, text=beverages.title(), font=('Dosis',16, 'bold'),onvalue=1, offvalue=0, variable=beverages_val[account], command=revise_check)
    beverages.grid(row=account, column=0, stick=W)

    # Se crea el frame de entrada
    beverages_frame.append('')
    beverages_text.append('')
    beverages_text[account] = StringVar()
    beverages_text[account].set('0')
    beverages_frame[account] = Entry(beverages_panel, font=('Dosis', 16, 'bold'), bd=1, width=6, state=DISABLED, textvariable=beverages_text[account])

    beverages_frame[account].grid(row=account, column=1)
    account += 1



#Se generan las variables locales
    var_cost_food = StringVar()
    var_cost_beverages = StringVar()
    var_cost_desserts = StringVar()
    var_subtotal = StringVar()
    var_taxs = StringVar()
    var_total = StringVar()

# Etiquetas costo y entradas
tag_cost_food = Label(cost_panel, text='Costo Comida', font=('Dosis', 12, 'bold'), bg='CadetBlue3', fg='white')
tag_cost_food.grid(row=0, column=0)

text_cost_food = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_cost_food)
text_cost_food.grid(row=0, column=1, padx=41)

tag_cost_beverages = Label(cost_panel, text='Costo Bebida', font=('Dosis', 12, 'bold'), bg='CadetBlue3', fg='white')
tag_cost_beverages.grid(row=1, column=0)

text_cost_beverages = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_cost_beverages)
text_cost_beverages.grid(row=1, column=1, padx=41)




#Se agran los elementos para que aparezcan los calculos realizados

tag_subtotal = Label(cost_panel, text='Subtotal', font=('Dosis', 12, 'bold'), bg='CadetBlue3', fg='white')
tag_subtotal.grid(row=0, column=2)

text_subtotal = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3)

tag_taxs = Label(cost_panel, text='Impuestos', font=('Dosis', 12, 'bold'), bg='CadetBlue3', fg='white')
tag_taxs.grid(row=1, column=2, padx=30)

text_taxs = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_taxs)
text_taxs.grid(row=1, column=3)

tag_total = Label(cost_panel, text='Total', font=('Dosis', 12, 'bold'), bg='CadetBlue3', fg='white')
tag_total.grid(row=2, column=2, padx=30)

text_total = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
text_total.grid(row=2, column=3, padx=30)

# Botones se crea una lista para poder hacer recorridos

buttons = ['total', 'Borrar']
columns = 0
buttons_create = []

for button in buttons:
    button = Button(button_panel, text= button.title(), font=('Dosis', 14, 'bold'), fg='white', bg='CadetBlue3', bd=1, width=7 )

    buttons_create.append(button)
    #Traemos el buton y agregamos la variable columns
    button.grid(row=0, column=columns)
    columns += 1

buttons_create[0].config(command=total)
buttons_create[1].config(command=cal_reset)





app.mainloop()