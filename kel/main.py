import logging
logging.basicConfig(
    filename = 'app.log',
    level = logging.INFO,
    format = '%(asctime)s-%(levelname)s -%(message)s',
    encoding='utf-8'

)

def get_user():
    logging.info('Начелась опросник')
    try:
        age_input = input('Введите ваш возраст: ')
        age = int(age_input)
        logging.info(f'Пользователь ввел возраст: {age}')
    except ValueError:
        logging.error(f'Ошибка при вводе возраста: {age_input}')
        print('Пожалуйста, введите корректное число для возраста.')
  

if __name__ == '__main__':
    logging.info('Программа запущена')
    get_user()
    logging.info('Программа завершена')