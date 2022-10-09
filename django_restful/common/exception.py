# * coding:utf-8 *


from pathlib import Path

from ruamel.yaml import YAML


class ExceptionLoader(type):
    fileName = "exceptions.yml"

    def __new__(cls, *args, **kwargs):
        instance = type.__new__(cls, *args, **kwargs)
        instance._except_mapping = ExceptionLoader.load()
        return instance

    @staticmethod
    def load():
        p = Path(__file__).parent.joinpath(Path(ExceptionLoader.fileName))
        yaml = YAML(typ="safe")
        return yaml.load(p)


class BaseError(Exception, metaclass=ExceptionLoader):
    def __init__(self, code, message=None):
        self.code = code
        self.message = message if message else self._except_mapping[self.code]
        super().__init__(self.code, self.message)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(code={self.code},message={self.message})"


class DjangoError(BaseError):
    @property
    def body(self):
        return {
            "detail": {
                "type": "Bad Request",
                "code": self.code,
                "message": self.message,
            }
        }


class InternalError(BaseError):
    @property
    def body(self):
        return {
            "detail": {
                "type": "internal error",
                "code": self.code,
                "message": self.message,
            }
        }
