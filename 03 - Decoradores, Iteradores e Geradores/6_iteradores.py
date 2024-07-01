def new_func():
    class MeuIterador:
        def __init__(self, numeros: list[int]):
            self.numeros = numeros
            self.contador = 0

        def __iter__(self):
            return self

        def __next__(self):
            try:
                numero = self.numeros[self.contador]
                self.contador += 1
                return numero * 2
            except IndexError as exc:
                raise StopIteration from exc


    for i in MeuIterador(numeros=[38, 13, 11]):
        print(i)

    return  # Move the return statement inside the new_func function


new_func()
