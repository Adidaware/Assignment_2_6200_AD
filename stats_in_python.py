""" Calculate Mathematical Functions using sys.argv[] to input file from the user """
import sys
import math

def calculate_statistics(data_list, col_index, file_name):
    """
    Calculate statistics for a given column in a file.

    Parameters:
    data_list: List of data points from the specified column.
    col_index: Index of the column to analyze.
    file_name: Name of the input file.

    Returns:
    A dictionary containing the calculated statistics.
    """

    stats = {
        'count': len(data_list),
        'valid_num': 0,
        'average': 'N/A',
        'variance': 'N/A',
        'std_dev': 'N/A',
        'median': 'N/A',
        'maximum': 'N/A',
        'minimum': 'N/A'
    }

    numeric_data = []

    # Calculating statistics if numeric_data is not empty:
    if data_list:
        numeric_data = []
        for i, x_num in enumerate(data_list):
            try:
                if x_num.lower() != 'nan':
                    numeric_value = float(x_num)
                    numeric_data.append(numeric_value)
                    stats['valid_num'] += 1
            except ValueError:
                print(f"Skipping line number {i+1}: could not convert string to float: '{x_num}'\n")
        if numeric_data:
            stats['average'] = sum(numeric_data) / len(numeric_data)
            stats['variance'] = round\
            (sum((x-stats['average']) ** 2 for x in numeric_data)/(stats['valid_num']-1), 3)
            stats['std_dev'] = round(math.sqrt(stats['variance']), 3)
            s_data = sorted(numeric_data)
            stats['median'] = (s_data[len(s_data)//2]+s_data[-(len(s_data)//2+1)])/2\
                if len(s_data) % 2 == 0 else s_data[len(s_data) // 2]
            stats['maximum'] = max(numeric_data)
            stats['minimum'] = min(numeric_data)
        else:
            print\
            (f"Exiting: There is no valid number(s) in column {col_index} in file: {file_name}")
    else:
        print\
        (f"Exiting: There is no valid 'list index' in {col_index} in line 1 in file: {file_name}")

    return stats

def main():
    """
    Main function to process command-line arguments and call the calculate_statistics function.
    """
    if len(sys.argv) != 3:
        print("Usage: python stats_in_python.py <filename> <column_index>")
        sys.exit(1)

    file_name = sys.argv[1]
    col_index = int(sys.argv[2])

    try:
        data_list = []
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                columns = line.strip().split('\t')
                if len(columns) > col_index:
                    data_list.append(columns[col_index])

        statistics_result = calculate_statistics(data_list, col_index, file_name)

        if statistics_result['valid_num'] == 0:
            print(f"Error: No numeric data found in column {col_index}.")
            sys.exit(2)

        # Printing the values:
        print(f"    Column: {col_index}\n")
        print(f"        Count = {statistics_result['count']}")
        print(f"        ValidNum = {statistics_result['valid_num']}")
        print(f"        Average = {statistics_result['average']}")
        print(f"        Maximum = {statistics_result['maximum']}")
        print(f"        Minimum = {statistics_result['minimum']}")
        print(f"        Variance = {statistics_result['variance']}")
        print(f"        Std Dev = {statistics_result['std_dev']}")
        print(f"        Median = {statistics_result['median']}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except ValueError:
        print\
        ("Error: Please make sure the column index is an integer and the file contains valid data.")

if __name__ == "__main__":
    main()
