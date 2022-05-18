# CREATED BY @impulsado
# veneno es antídoto

monedero = {0.01:0, 0.02:0, 0.05:0, 0.10:0,
            0.20:0, 0.50:0, 1.00:0, 2.00:0}

def pedirOpcion(opciones):
    '''
    Recibe un diccionario con pares del tipo "opcion":"descripcion"
    Devuelve la opción que selecciona el usuario
    (Tanto "opcion" como "descripcion" son de tipo texto).
    '''
    print(opciones)
    usr_opcion=input("¿QUE QUIERES HACER?: ")
    while usr_opcion not in opciones.keys():
        usr_opcion=input("¿QUE QUIERES HACER?: ")
    return usr_opcion

def pedirFloat(listaValoresOK, texto):
    '''Pide al usuario un valor numérico, opcionalmente con decimales.
    Recibe una lista con los valores admitidos.
    Si la lista está vacía, se admite cualquier valor.
    Recibe el texto que se ha de presentar al usuario al pedir un valor.
    Devuelve el valor proporcionado por el usuario.
    Mientras el valor no sea válido, vuelve a pedir.
    '''
    try:
        var = True
        if var == True:
            usr_num = float(input(texto))
            if not listaValoresOK:
                return usr_num
            if usr_num in listaValoresOK:
                return usr_num
    except:
        usr_num = float(input(texto))

def pedirEntero(texto):
    '''Pide al usuario un valor numérico entero.
    Devuelve el valor proporcionado por el usuario.
    Mientras el valor no sea válido, vuelve a pedir.
    Recibe el texto que se ha de presentar al usuario al pedir un valor.
    '''
    usr_cant = input(texto)
    
    try:
        usr_cant = int(usr_cant)
        check = True
    except ValueError:
        check = False
    
    while check == False:
        usr_cant = input(texto)
        try:
            usr_cant = int(usr_cant)
            check = True
        except ValueError:
            check = False
    
    return usr_cant

def mostrarResultadoOperacion(finalizacion):
    '''
    Recibe un mensaje que indica cómo ha terminado una operación.
    Si el mensaje es "", se dice al usuario que la operación se ha realizado correctamente.
    Si el mensaje contiene texto, es la descripción de un error y se muestra al usuario.
    No devuelve nada.
    '''
    if finalizacion == "":
        return print("OPERACION CORRECTA")
    else:
        return print("OPERACION NO VALIDA")
    pass

def guardarMonedas(tipoMoneda, cantidadMonedas):
    '''
    Actualiza la cantidad de monedas del tipo indicado
    No puede fallar. No devuelve nada.
    '''
    if tipoMoneda in monedero.keys():
        monedero[tipoMoneda] = cantidadMonedas
    return ""

def consultarSaldo(listaTiposMoneda):
    '''
    Recibe una lista con los tipos de moneda que se han de contar.
    Devuelve el importe total que suman las monedas del tipo(s) indicado(s) en la lista.
    Si la lista está vacía, se suman todos los tipos de moneda
    '''
    total = 0
    lista_contar = []
    if lista_contar == []:
        for i in monedero:
            if monedero[i] != "0":
                total = total + (i * int(monedero[i]))
        return total
    else:
        for i in range(listaTiposMoneda):
            if listaTiposMoneda[i] in monedero.keys():
                lista_contar.append(listaTiposMoneda)
            return sum(lista_contar)
    pass       

def consultarNumMonedas(tipoMoneda):
    '''Recibe un tipo de moneda.
    Devuelve el número de monedas que hay del tipo indicado.
    Si el tipoMoneda no existe, devuelve 0 monedas
    '''
    if not tipoMoneda:
        return "0"
    else:
        if tipoMoneda in monedero.keys():
            return monedero.get(tipoMoneda)

def retirarImporte(importe):
    '''Recibe el importe a extraer del monedero.
    Si no hay saldo suficiente, o no se puede sumar el importe exacto con las monedas
    disponibles, no se modifica el monedero y se devuelve
    1. un texto explicativo
    2. un diccionario vacío
    Si hay saldo suficiente, se extraen las monedas con el valor
    más alto posible que sumen el importe indicado y se devuelve
    1. Un texto vacío ""
    2. Un diccionario indicando "tipo_de_moneda : piezas_que_se_han_sacado"
    (Solo se especifican los tipos de moneda que han cambiado de cantidad)
    '''
    diccionario = {}
    if importe > consultarSaldo([]):
        return "OPERACION NO VALIDA", diccionario

    if importe <= consultarSaldo([]):
        diccionario = {}
        lista = []
        check0 = 0
        check1 = 0
        check2 = 0
        # DEFINIR ABANS
        euro2 = 0
        euro1 = 0
        euro05 = 0
        euro02 = 0
        euro01 = 0
        euro005 = 0
        euro002 = 0
        euro001 = 0

        # ESTA FUNCION DE AQUI TE DEJA EL NUMERO CON DOS DECIMALES FIJOS TIPO SI TU PONES 5 ESTA FUNCION TE LO DEJA COMO 5.00.
        importe = format(importe, '.2f')

        for i in str(importe):
            if i != '.':
                lista.append(int(i))

        while lista[0] != 0:
            if lista[0] >= 2 and monedero[2.00] != 0:
                lista[0] = lista[0] - 2
                monedero[2.00] = monedero[2.00] - 1
                euro2 += 1
                diccionario[2.00] = euro2
            elif lista[0] >= 1 and monedero[1.00] != 0:
                lista[0] = lista[0] - 1
                monedero[1.00] = monedero[1.00] - 1
                euro1 += 1
                diccionario[1.00] = euro1
            else:
                check0 = 1
                break
        while lista[1] != 0:
            if lista[1] >= 5 and monedero[0.50] != 0:
                lista[1] = lista[1] - 5
                monedero[0.50] = monedero[0.50] - 1
                euro05 += 1
                diccionario[0.50] = euro05
            elif lista[1] >= 2 and monedero[0.20] != 0:
                lista[1] = lista[1] - 2
                monedero[0.20] = monedero[0.20] - 1
                euro02 += 1
                diccionario[0.20] = euro02
            elif lista[1] >= 1 and monedero[0.10] != 0:
                lista[1] = lista[1] - 1
                monedero[0.10] = monedero[0.10] - 1
                euro01 += 1
                diccionario[0.10] = euro01
            else:
                check1 = 1
                break
        while lista[2] != 0:
            if lista[2] >= 5 and monedero[0.05] != 0:
                lista[2] = lista[2] - 5
                monedero[0.05] = monedero[0.05] - 1
                euro005 += 1
                diccionario[0.05] = euro005
            elif lista[2] >= 2 and monedero[0.02] != 0:
                lista[2] = lista[2] - 2
                monedero[0.02] = monedero[0.02] - 1
                euro002 += 1
                diccionario[0.02] = euro002
            elif lista[2] >= 1 and monedero[0.01] != 0:
                lista[2] = lista[2] - 1
                monedero[0.01] = monedero[0.01] - 1
                euro001 += 1
                diccionario[0.01] = euro001
            else:
                check2 = 1
                break
        if check0 != 0 or check1 != 0 or check2 != 0:
            diccionario = {}
            monedero[2.00] += euro2
            monedero[1.00] += euro1
            monedero[0.50] += euro05
            monedero[0.20] += euro02
            monedero[0.10] += euro01
            monedero[0.05] += euro005
            monedero[0.02] += euro002
            monedero[0.01] += euro001
            return "OPERACION NO VALIDA", diccionario
        else:
            return "", diccionario
    pass

                
def retirarMonedas(valorMoneda, cantidad):
    '''Recibe un tipo de moneda y la cantidad de monedas a retirar de ese tipo.
    Si no hay suficientes monedas del tipo indicado, se devuelve un texto explicativo
    Si hay suficientes monedas, se extrae la cantidad indicada y se devuelve un
    texto vacío ""
    '''
    if monedero[valorMoneda] < cantidad:
        return "OPERACION NO VALIDA"
    
    if monedero[valorMoneda] >= cantidad:
        monedero[valorMoneda] -= cantidad
        return ""
    pass
        

# -------------------- PROGRAMA PRINCIPAL -----------------------


opcionesMenu = {'1':'Ingresar', '2':'Retirar', '3':'Consultar', '4':'Terminar'}

terminar = False
while not terminar:
    operacion = pedirOpcion(opcionesMenu)
    if operacion == "1":
    # Guardar una cantidad de monedas o billetes
        valorMoneda = pedirFloat(list(monedero.keys()), "Indicar tipo de moneda: ")
        cantidad = pedirEntero("Indicar cantidad de monedas: ")
        guardarMonedas(valorMoneda, cantidad)
    elif operacion == "2":
        opcionesRetirar = {'1': 'Retirar importe', '2': 'Retirar número de monedas'}
        operacion = pedirOpcion(opcionesRetirar)
        if operacion == "1":
            importe = pedirFloat([], "Indicar importe a retirar: ")
            estado, queHeRetirado = retirarImporte(importe)
            mostrarResultadoOperacion(estado)
        elif operacion == "2":
            valorMoneda = pedirFloat(list(monedero.keys()), "Indicar tipo de moneda: ")
            cantidad = pedirEntero("Indicar cantidad de monedas: ")
            estado = retirarMonedas(valorMoneda, cantidad)
            mostrarResultadoOperacion(estado)
    elif operacion == "3":
        print("El saldo total es:", consultarSaldo([]))
        print("Cantidad monedas e importe total por cada tipo de moneda:")
        for tipoMoneda in monedero:
            print (f"Monedas de {tipoMoneda} €:{consultarNumMonedas(tipoMoneda)} \
            Importe total {float(tipoMoneda) * float(monedero[tipoMoneda])} €")
    elif operacion == "4":
        print("HASTA LA PROXIMA!")
        break
    else:
        pass
#instrucción para ver qué ha pasado
