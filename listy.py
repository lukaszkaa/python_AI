



def dodj_do_listy(v_element, v_lista):
    v_lista.append(v_element)
    
def usun_z_listy(v_element, v_lista):
    for it in v_lista:
        if it == v_element:
            v_lista.remove(v_element)


def dlugosc_listy(v_lista):
    return len(v_lista)

def popraw_wielkosc_liter(v_lista):
    for it in v_lista:
        if type(it) is str:
            pozycja = v_lista.index(it)
            v_lista[pozycja] = it.upper()



global lista 
lista = []

dodj_do_listy(1,lista)
dodj_do_listy(12,lista)
dodj_do_listy(13,lista)
dodj_do_listy('sdasdasdasd',lista)

usun_z_listy(12,lista)

popraw_wielkosc_liter(lista)

print(lista[:1])

print(lista)


popraw_wielkosc_liter(v_lista=lista)