import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем словарь для кодирования категориальных значений
encode_dict = {value: [1] if value == 'robot' else [0] for value in data['whoAmI']}

# Создаем список столбцов для нового DataFrame
columns = ['robot', 'human']

# Создаем новый DataFrame с кодированными значениями
encoded_data = pd.DataFrame(encode_dict, columns=columns)

encoded_data.head()