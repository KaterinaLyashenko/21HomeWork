class BaseError(Exception):
    message = "Неожиданная ошибка"

class RequestError(BaseError):
    message = "Произошла ошибка обработки запроса"

class CourierError(BaseError):
    message = "Произошла ошибка при доставке"

class NotEnoughSpace(CourierError):
    message = "Недостаточно места на складе"

class NotEnoughProduct(CourierError):
    message = "Недостаточно товара на складе"

class TooManyDifferentProduct(CourierError):
    message = "Слишком много уникальных товаров"

class InvalidRequest(RequestError):
    message = "Неправильный запрос, попробуйте снова"

class InvalidStorageName(RequestError):
    message = "Выбран несуществующий склад"


