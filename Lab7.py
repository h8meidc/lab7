def Print (teams):

    for i in teams:

        print("Очки ", i, " - ", teams[i])

def add(teams, key, points):
    #teams.update({key:points})
    teams[key] = points

    print("Додано", key, ".")

def Del(teams, key):
    if key in teams:
        del teams[key]

        print("Видалено", key, ".")
    else:
        print("Команда відсутня.")

def print_sort(teams):

    teams = {k: teams[k] for k in sorted(teams)}

    print("Відсортований словник: ")

    for i in teams:

        print("Очки ", i, " - ", teams[i])
        
def findplace(teams):
    sorted_teams = sorted(teams.items(), reverse=True)
    print("First place: ", sorted_teams[0])
    print("Second place: ", sorted_teams[1])
    print("Third place: ", sorted_teams[2])
    
teams = {"Team1": 100,"Team2": 32,"Team3": 15,"Team4": 42,"Team5": 14,
         "Team6": 67,"Team7": 35,"Team8": 54,"Team9": 90,"Team0": 67}
act=1
while act!=6:
    print("Оберіть дію: \n"
      "1 - Виведення на екран всіх значень словника\n"
      "2 - Додавання нового запису до словника\n"
      "3 - Видалення запису зі словника\n"
      "4 - Перегляд словника з відсортованими ключами\n"
      "5 - Знайти 1, 2 та 3 місце серед команд\n"
      "6 - Завершити роботу програми")
    act=int(input(" "))
    if act==1:
        Print (teams)
    
    elif act==2:
        key=input("Введіть назву команди: ")
        points=int(input("Введіть кількість очок команди: "))
        while points<0:
            print("Очки не можуть буду від'ємні.")
            points=int(input("Введіть кількість очок команди: "))
        add(teams, key, points)
    elif act==3:
        key=input("Введіть назву команди: ")
        Del(teams, key)
    elif act==4:
        print_sort(teams)
    elif act==5:
        findplace(teams)
    elif act==6:
        print("Програма завершена.")
    else:
        print("Обрано невірну дію.")