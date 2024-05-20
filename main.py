import pandas as pd


def calculate_difference(csv_file, limit, output_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Calculate the difference between 'Size' and 'Allocated'
    df['Difference'] = df['Size'] - df['Allocated']

    # Convert limit from MB or GB to bytes
    if 'MB' in limit:
        limit = float(limit.replace('MB', '')) * 1024 * 1024
    elif 'GB' in limit:
        limit = float(limit.replace('GB', '')) * 1024 * 1024 * 1024
    else:
        print("Invalid limit unit. Please use MB or GB.")
        return

    # Filter the data where the difference is less than the limit
    filtered_df = df[df['Difference'] < limit]

    # Sort the data by the difference in descending order
    sorted_df = filtered_df.sort_values(by='Difference', ascending=False)

    # Write the sorted file names to a text file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        for file_name in sorted_df['File Name']:
            f.write(file_name + '\n')


# Example usage:
calculate_difference('csv_file.csv', 'limitMB', 'output_file.txt')
