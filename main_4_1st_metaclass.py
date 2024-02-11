class ExampleMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("I'm creating new class: ", cls)
        return super().__new__(cls, *args, **kwargs)


class ExampleClass(metaclass=ExampleMetaClass):
    pass
