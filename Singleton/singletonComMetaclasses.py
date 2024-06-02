class MetaclassSingleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

class Logger(metaclass=MetaclassSingleton):
    pass
logx = Logger()
print(logx)
logy = Logger()
print(logy)
        