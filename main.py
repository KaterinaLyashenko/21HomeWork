from courier import Courier
from exceptions import CourierError, RequestError
from request import Request
from shop import Shop
from store import Store

"""
store = Store(items={
    "печенье": 5,
    "собака": 2,
    "картина": 10,
    "очки": 5,
    "банан": 20
})

shop = Shop(items={
    "печенье": 3,
    "собака": 1,
    "картина": 2,
    "банан": 4
})
"""

store = Store(items={})
shop = Shop(items={})

store.items = {
    "печенье": 5,
    "собака": 2,
    "картина": 10,
    "очки": 5,
    "банан": 20
}

shop.items = {
    "печенье": 3,
    "собака": 1,
    "картина": 2,
    "банан": 4
}

storages = {
    'магазинe': shop,
    'складe': store
}

def main():
    print("\nДобрый день\n")

    while True:
        for storage_name in storages:
            print(f"Сейчас в {storage_name}\n {storages[storage_name].items}")

        print('Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
              'Введите "stop" или "стоп", если хотите закончить\n')

        user_input = input()

        if user_input in ('stop', 'стоп'):
            break
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )


        try:
            courier.move()
        except CourierError as error:
            print(error)


if __name__ == '__main__':
    main()