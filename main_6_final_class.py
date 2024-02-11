class Final(type):
    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, Final):
                raise TypeError("type '{0}' could not be base class - it's marked as final class".format(b.__name__))
        return type.__new__(cls, name, bases, dict(classdict))


class ExampleClass(metaclass=Final):
    pass


class SecondClass(ExampleClass):
    pass