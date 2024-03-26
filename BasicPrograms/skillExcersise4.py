#program 1
import random
import string

def random_color_hex():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_alphabetical_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def random_between(min_value, max_value):
    return random.randint(min_value, max_value)

def random_multiple_of_seven():
    return random.randint(0, 10) * 7

# Example usage:
print("Random Color Hex:", random_color_hex())
print("Random Alphabetical String:", random_alphabetical_string(8))
print("Random Value between 5 and 15:", random_between(5, 15))
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_seven())


#program 2
import random
from datetime import datetime, timedelta

random_int_excluding_six = random.randrange(6)

random_int_excluding_ten = random.randrange(5, 10)

random_int_with_step_of_three = random.randrange(0, 10, 3)

def random_date(start_date, end_date):
    time_difference = end_date - start_date
    random_days = random.randrange(time_difference.days)
    return start_date + timedelta(days=random_days)

print("Random Integer between 0 and 6-excluding 6:", random_int_excluding_six)
print("Random Integer between 5 and 10-excluding 10:", random_int_excluding_ten)
print("Random Integer between 0 and 10 with step 3:", random_int_with_step_of_three)
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
print("Random Date between {} and {}: {}".format(start_date, end_date, random_date(start_date, end_date)))


#program 3
import pandas as pd
import matplotlib.pyplot as plt

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df

def generate_graph(data_frame):
    x_values = data_frame['REGNUM']
    y_columns = data_frame.columns[1:]
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, column in enumerate(y_columns):
        y_values = data_frame[column]
        plt.plot(x_values, y_values, marker='o', linestyle='-', label=column, color=colors[i])

    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('CSV Data Plot')
    plt.grid(True)
    plt.legend()
    plt.savefig("a1.png")
    plt.show()

if __name__ == "__main__":
    file_path = "TRY1.csv"
    data_frame = read_csv_file(file_path)
    generate_graph(data_frame)
