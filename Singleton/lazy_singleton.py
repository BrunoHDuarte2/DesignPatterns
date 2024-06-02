class LazySingleton(object):
    __instance = None
    # Somente inicializa a class
    def __init__(self):
        if LazySingleton.__instance != None:
            # Já existe a instancia inicial
            print(self.__instance)
        else:
            print("Ainda não criada")
    # Aqui a instancia é criada
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance
    
lazy1 = LazySingleton()
instancia = lazy1.get_instance()

lazy2 = LazySingleton()
instanci2 = lazy1.get_instance()

if  instancia == instanci2:
    print("Ambas instancias apontam para o mesmo objeto!")
else:
    print("Tá errado!")