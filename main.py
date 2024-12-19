from main_functions import *
from functions_for_work import *
from menu_interface import *

def main():

    # Инициализация начального состояния
    state = {
        'array1': [],
        'array2': [],
        'menu_choice': '',
        'task_choice': '',
        'is_task_selected': False,
        'is_info_input': False,
        'is_algoritm_done': False,
        'result': None
    }
    # Словарь для выбора пунктов меню
    choice_handlers = {
        1: handle_task_selection,
        2: handle_data_input,
        3: handle_algorithm_execution,
        4: handle_result_display,
        5: handle_exit
    }


    while True:
        show_menu()
        menu_choice = input("\nВыберите пункт для дальнейшей работы: ")
        if is_int(menu_choice):
            menu_choice = int(menu_choice)
            state = choice_handlers.get(menu_choice, lambda state: state)(state)

def handle_task_selection(state):
    show_tasks()
    choice_task = input("\nВведите номер выбранной задачи: ")
    #возвращаем новый state
    return {**state, 'task_choice': int(choice_task), 'is_task_selected': True} if is_int(choice_task) else state

def handle_data_input(state):

    # Словарь обработчиков для ввода данных в зависимости от выбранной задачи
    data_input_handlers = {
        1: input_big_numbers_mas,
        2: input_numbers_mas_for_compare,
        3: input_points_array
    }
    array1, array2 = data_input_handlers.get(state['task_choice'], lambda x, y: (x, y))(state['array1'], state['array2'])
    return {**state, 'array1': array1, 'array2': array2, 'is_info_input': True} if state['is_task_selected'] else (
        print("\nСначала выберите задание\n")
    )

def handle_algorithm_execution(state):

    # Словарь обработчиков для выполнения алгоритма в зависимости от выбранной задачи
    algorithm_handlers = {
        1: sum_or_dif_of_array,
        2: count_same_numbers,
        3: find_points_bigger_distance
    }
    result = algorithm_handlers.get(state['task_choice'], lambda x, y: None)(state['array1'], state['array2'])
    return {**state, 'result': result, 'is_algoritm_done': True} if state['is_task_selected'] and state['is_info_input'] else (
        print("\nСначала введите данные для выполнения алгоритма\n")
    )

def handle_result_display(state):
    if state['is_algoritm_done']:

        # Словарь обработчиков для отображения результата в зависимости от выбранной задачи
        result_display_handlers = {
            1: lambda result: f"\nРезультат работы алгоритма по сложению/вычитанию массивов: {result}",
            2: lambda result: f"\nКоличество общих чисел у двух массивов: {result}",
            3: lambda result: f"\nСписок точек, удовлетворяющих условию: {result}"
        }
        print(result_display_handlers.get(state['task_choice'], lambda result: "Неизвестная задача")(state['result']))
    else:
        print("\nСначала выполните алгоритм\n")
    return state

def handle_exit():
    print("\nЗавершение работы\n")
    exit()

if __name__ == "__main__":
    main()
