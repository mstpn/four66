from datetime import datetime
from typing import List
class TodoList:
    def __init__(self) -> None:
        self.list: List[Item] = []
    def is_list_empty(self) -> bool:
        return len(self.list) == 0
    def add_item(self) -> None:
        self.list.append(Item(input('\nAdd a new item:\ntitle: '), int(input('priority (Number 1 - 3 (Low -> High)): ')), input('description: '), datetime.strptime(input('date (YYYY-MM-DD): '), "%Y-%m-%d")))
    def print_list(self) -> None:
        print("\nYour Todo List:")
        for count, item in enumerate(self.list):
            print('Item ' + str(count) +':')
            item.print_item()
            print('_______________________\n')
    def modify_item(self) -> None:
        self.print_list()
        item = self.list[int(input("\nWhich item do you want to modify (Item #): "))]
        param = int(input(f"\n{item.title}\nWhich field do you want to modify (1: Title, 2: Description, 3: Priority, 4: Date): "))
        item.title = input("title: ") if param == 1 else item.title
        item.desc = input("description: ") if param == 2 else item.desc
        item.priority = int(input("priority (Nubmer 1 - 3 (Low -> High)): ")) if param == 3 else item.priority
        item.date = datetime.strptime(input('date (YYYY-MM-DD): '), "%Y-%m-%d") if param == 4 else item.date
    def remove_item(self) -> None:
        self.list.pop(int(input(f"{self.print_list()}\nWhich item do you want to remove (Item #): ")))
    def order_items(self) -> None:
        if len(self.list) >= 2:
            choice = input("Do you want to order items by date or priority (d: date, p: priority): ")
            if choice == 'd':
                self.order_date()
            elif choice == 'p':
                self.order_priority()
        else:
            print("Single item list... Nothing to sort!")
    def order_date(self) -> None:
        self.list.sort(key=lambda item: item.date)
    def order_priority(self) -> None:
        self.list.sort(key=lambda item: item.priority)
class Item:
    def __init__(self, title: str, priority: int, desc: str, date: datetime) -> None:
        self.title = title
        self.priority = priority
        self.desc = desc
        self.date = date
    def print_item(self) -> None:
        print(f'{self.title}\nD: {self.desc}\nP: {self.priority}\nT: {self.date}')
def get_commands() -> str:
    return '\nCommands:\n\tp:\tprint list\n\ta:\tadd item\n\tr:\tremove item\n\tm:\tmodify item\n\to:\torder list\n\tc:\tshow commands\n\tq:\tquit\n'
def choice_handler(choice: str) -> bool:
    if choice == 'a': l.add_item()
    elif choice == 'c': print(get_commands())
    elif choice == 'p': l.print_list() if not l.is_list_empty() else print("List empty... Nothing to print!")
    elif choice == 'r': l.remove_item() if not l.is_list_empty() else print("List empty... Nothing to remove!")
    elif choice == 'm': l.modify_item() if not l.is_list_empty() else print("List empty... Nothing to modify!")
    elif choice == 'o': l.order_items() if not l.is_list_empty() else print("List empty... Nothing to sort!")
    elif choice == 'q': return False
    return True
if __name__ == '__main__':
    print("\n---Todo List---\n", get_commands())
    l = TodoList()
    run = True
    while run:
        try:
            run = choice_handler(input('> '))
        except:
            print("\nInvalid input... Returning to menu") 
