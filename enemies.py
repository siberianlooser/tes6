def get_enemy(enemy_type):
    enemies = {
        "Лёва": {"health": 3, "damage": 1},
        "Сундук": {"health": 1, "damage": 3},
        "Влад": {"health": 5, "damage": 2},
        "Рома": {"health": 2, "damage": 2},
    }
    return enemies.get(enemy_type, {"health": 1, "damage": 0}) 


def get_player():
    return {"health": 3, "damage": 1}