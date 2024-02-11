from functools import partial


class MetaClass(type):
    __prohibited_methods__ = ['get_name']

    def __new__(self, name, base, ns):
        def alert_function(f_name):
            raise RuntimeError(f'Method {f_name} is prohibited in this class!')

        for key, val in ns.items():
            if key in self.__prohibited_methods__:
                ns[key] = partial(alert_function, f_name=key)

        return type.__new__(self, name, base, ns)


class ExampleClass(metaclass=MetaClass):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


ex = ExampleClass('name')
ex.get_name()
