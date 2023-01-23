from typing import Dict
from abstract_storage import AbstarctStorage
from exceptions import InvalidRequest, InvalidStorageName


class Request:
    def __init__(self, request: str, storages: Dict[str, AbstarctStorage]):
        splited_request = request.lower().split(' ')
        if len(splited_request) != 7:
            raise InvalidRequest

        self.amount = int(splited_request[1])
        self.product = splited_request[2]
        self.departure = splited_request[4] #откуда
        self.destination = splited_request[6] #куда

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName

