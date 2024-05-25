from abc import ABC, abstractmethod

class QueueBehaviour(ABC):
    @abstractmethod
    def enqueue(self, person):
        pass
    
    @abstractmethod
    def dequeue(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass

class MarketBehaviour(ABC):
    @abstractmethod
    def accept_order(self, order):
        pass
    
    @abstractmethod
    def process_order(self):
        pass
    
    @abstractmethod
    def complete_order(self):
        pass

class UpdateBehaviour(ABC):
    @abstractmethod
    def update(self):
        pass




class Market(QueueBehaviour, MarketBehaviour, UpdateBehaviour):
    def __init__(self):
        self.queue = []
        self.orders = []
        self.completed_orders = []
    
    # Реализация методов QueueBehaviour
    def enqueue(self, person):
        self.queue.append(person)
        print(f'{person} добавлен в очередь.')
    
    def dequeue(self):
        if not self.is_empty():
            person = self.queue.pop(0)
            print(f'{person} удален из очереди.')
            return person
        else:
            print('Очередь пуста.')
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    # Реализация методов MarketBehaviour
    def accept_order(self, order):
        self.orders.append(order)
        print(f'Заказ {order} принят.')
    
    def process_order(self):
        if self.orders:
            order = self.orders.pop(0)
            print(f'Заказ {order} обрабатывается.')
            return order
        else:
            print('Нет заказов для обработки.')
            return None
    
    def complete_order(self):
        if self.orders:
            order = self.process_order()
            self.completed_orders.append(order)
            print(f'Заказ {order} завершен.')
        else:
            print('Нет заказов для завершения.')
    
    # Реализация метода UpdateBehaviour
    def update(self):
        print('Обновление состояния магазина...')
        if not self.is_empty():
            person = self.dequeue()
            if self.orders:
                self.process_order()
                self.complete_order()
            else:
                print(f'{person} ожидает обработки заказа.')
        else:
            print('Очередь пуста. Нет людей для обслуживания.')




if __name__ == "__main__":
    market = Market()

    # Добавление людей в очередь
    market.enqueue("Человек 1")
    market.enqueue("Человек 2")

    # Принятие заказов
    market.accept_order("Заказ 1")
    market.accept_order("Заказ 2")

    # Обновление состояния магазина
    market.update()
    market.update()
    market.update()
