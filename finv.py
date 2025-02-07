import smayk
import nazor
import scenes
import items
scenes.print_inventory()
def inenit():
    print(scenes.inventory)
    index = int(input("Введите индекс элемента, который хотите выбрать (от 0 до {}): ".format(len(scenes.inventory)-1)))
    if 0 <= index < len(scenes.inventory):
        print("Выбранный элемент:", scenes.inventory[index])
        if scenes.inventory[index] == "Нажор":
            return scenes.inventory[index]
        elif scenes.inventory[index] == "Смайк":
            return items.smayk()
    else:
        print("Неверный индекс!")