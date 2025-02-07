import os
import scenes
import battle

result = 0

def center_in_terminal(any_string):
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size[0]
    input_length = len(any_string)
    empty_space_required = int((terminal_width - input_length)/2)
    empty_space = " " * empty_space_required
    print(empty_space + any_string)

os.system('cls' if os.name == 'nt' else 'clear')

logo = """
████████ ███████ ███████  ██████         ██   ██  █████  ██████  ██      ██ ██   ██ ██      █████  ████████  █████  ██   ██ ██    ██      ██ ██    ██ ████████ 
   ██    ██      ██      ██       ██     ██  ██  ██   ██ ██   ██ ██      ██ ██  ██  ██     ██   ██    ██    ██   ██ ██  ██  ██    ██      ██ ██    ██    ██    
   ██    █████   ███████ ███████         █████   ███████ ██████  ██      ██ █████   ██     ███████    ██    ███████ █████   ██    ██      ██ ██    ██    ██    
   ██    ██           ██ ██    ██ ██     ██  ██  ██   ██ ██   ██ ██      ██ ██  ██  ██     ██   ██    ██    ██   ██ ██  ██  ██    ██ ██   ██ ██    ██    ██    
   ██    ███████ ███████  ██████         ██   ██ ██   ██ ██   ██ ███████ ██ ██   ██ ██     ██   ██    ██    ██   ██ ██   ██  ██████   █████   ██████     ██    
                                                                                                                                                               
                                                                                                                                                               
"""

glava1 = """
 ██████  ██       █████  ██    ██  █████       ██ 
██       ██      ██   ██ ██    ██ ██   ██     ███ 
██   ███ ██      ███████ ██    ██ ███████      ██ 
██    ██ ██      ██   ██  ██  ██  ██   ██      ██ 
 ██████  ███████ ██   ██   ████   ██   ██      ██ 
                                                  
                                                  
"""

glava3 = """
 ██████  ██       █████  ██    ██  █████      ██████  
██       ██      ██   ██ ██    ██ ██   ██          ██ 
██   ███ ██      ███████ ██    ██ ███████      █████  
██    ██ ██      ██   ██  ██  ██  ██   ██     ██      
 ██████  ███████ ██   ██   ████   ██   ██     ███████ 
                                                      
                                                      
"""

glava4 = """
 ██████  ██       █████  ██    ██  █████      ██████  
██       ██      ██   ██ ██    ██ ██   ██          ██ 
██   ███ ██      ███████ ██    ██ ███████      █████  
██    ██ ██      ██   ██  ██  ██  ██   ██          ██ 
 ██████  ███████ ██   ██   ████   ██   ██     ██████  
                                                      
                                                      
"""

glava5 = """
 ██████  ██       █████  ██    ██  █████      ██   ██ 
██       ██      ██   ██ ██    ██ ██   ██     ██   ██ 
██   ███ ██      ███████ ██    ██ ███████     ███████ 
██    ██ ██      ██   ██  ██  ██  ██   ██          ██ 
 ██████  ███████ ██   ██   ████   ██   ██          ██ 
                                                      
                                                                                              
"""

glava6 = """
 ██████  ██       █████  ██    ██  █████      ███████ 
██       ██      ██   ██ ██    ██ ██   ██     ██      
██   ███ ██      ███████ ██    ██ ███████     ███████ 
██    ██ ██      ██   ██  ██  ██  ██   ██          ██ 
 ██████  ███████ ██   ██   ████   ██   ██     ███████ 
                                                      
                                                      
"""

fight_logo = """
███████ ██  ██████  ██   ██ ████████ ██ 
██      ██ ██       ██   ██    ██    ██ 
█████   ██ ██   ███ ███████    ██    ██ 
██      ██ ██    ██ ██   ██    ██       
██      ██  ██████  ██   ██    ██    ██ 
                                        
                                        
"""


print(logo)
print(center_in_terminal("The Elder Scrolls 6: Карлики Атакуют"))

print(glava1)
scenes.scene1()

print(glava3)
scenes.scene3()
enemy_type = 'Лёва'
print(fight_logo)
battle.fight(enemy_type)
from battle import result
if battle.result == 'win':
    from battle import choice_final
    if battle.choice_final == 1:
        scenes.scene3_kill()
    elif battle.choice_final == 2:
        scenes.scene3_spare()
    else:
        print('a?')
elif battle.result == 'lose':
    scenes.lose()
else:
    print('как?')

print(glava4)
scenes.scene4()
print(fight_logo)
battle.fight('Сундук')
from battle import result
if battle.result == 'win':
    from battle import choice_final
    if battle.choice_final == 1:
        scenes.scene5()
    elif battle.choice_final == 2:
        scenes.scene5()
    else:
        print('a?')
elif battle.result == 'lose':
    scenes.lose()
else:
    print('как?')

print(glava6)
scenes.scene6()
print(fight_logo)
battle.fight('Влад')
from battle import result
if battle.result == 'win':
    from battle import choice_final
    if battle.choice_final == 1:
        scenes.scene6_kill()
    elif battle.choice_final == 2:
        scenes.scene6_spare()
    else:
        print('a?')
elif battle.result == 'lose':
    scenes.lose()
else:
    print('как?')

print(fight_logo)
battle.fight('Рома')
from battle import result
if battle.result == 'win':
    from battle import choice_final
    if battle.choice_final == 1:
        scenes.scene6_spare_kill()
    elif battle.choice_final == 2:
        scenes.scene6_spare_spare()
    else:
        print('a?')
elif battle.result == 'lose':
    scenes.lose()
else:
    print('как?')