# Instancias diferentes de um objeto com o mesmo estado
class Monostate:
    __state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj

m1 = Monostate()
print(m1.__dict__)

m2 = Monostate()
print(m2.__dict__)
# Mudanças de estados são feitas globalmente 
m1.x = "mudança 1"
m2.y = "mudança 2"
#Objetos diferentes com o mesmo estado
print(m1.__dict__)
print(m2.__dict__)

if m1 == m2:
    print("Objetos iguais")
else:
    print("Objeto m1: ", m1)
    print("Objeto m2: ", m2)
    print("Objetos diferentes com estado compartilhado, logo iguais")

