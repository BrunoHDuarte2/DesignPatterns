# O construtor aponta sempre para o mesmo local onde foi endereçado a primeira instancia do objeto Singleton
class Singleton(object):
    # Cria o novo objeto 
    def __new__(cls):
        # Se não há atributos = não existe instancia ainda -> Logo cria esse objeto!
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
first_instance = Singleton()
second_instance = Singleton()
if first_instance == second_instance:
    print("Ambas instancias apontam para o mesmo objeto!")
else:
    print("Tá errado!")