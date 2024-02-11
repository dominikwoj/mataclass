class ExampleMetaClass(type):
    _max_class_instances = 3

    def __new__(cls, *args, **kwargs):
        if cls._max_class_instances > 0:
            cls._max_class_instances -= 1
            return super().__new__(cls, *args, **kwargs)
        raise RuntimeError(f'{cls} could have only 3 subclasess!')


class ExampleClass(metaclass=ExampleMetaClass):
    pass


class ExampleClass1(metaclass=ExampleMetaClass):
    pass


class ExampleClass2(metaclass=ExampleMetaClass):
    pass

class Ex(ExampleClass2):
    pass
