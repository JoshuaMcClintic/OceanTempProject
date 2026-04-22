import csv
from pathlib import Path

# Define Input and Output paths for converting .asc files to .csv files
infile_path = Path('C:\\filepath')
outfile_path = Path('C:\\filepath')


# For each .asc file, open and read it, using spaces as delimiter; Write info to .csv file
for file in infile_path.iterdir():
    with open(f'{file}', mode='r') as f_in, open(f'{outfile_path}\\{file.name[:-4]}.csv', mode='w', newline='') as f_out:
        reader = csv.reader(f_in, delimiter=' ')
        writer = csv.writer(f_out)
        writer.writerows(reader)


# Define input path for final file
infile_path = Path('C:\\filepath')


# Works only for files of name_format file_name_YYYYMMWW.abc where YYYY is 4-digit year, MM is 2-digit month, WW is
# 2-digit week.
# This was changed so each month would be numeric
def file_dater(filename):
    filename_split = filename.split('_')
    year = filename_split[-1][:4]
    month = filename_split[-1][4:8]
    month = int(month[0:2])
    # print(filename, year, month)
    return [month, year]


# Define output path for final file
full_file = 'C:\\filepath'


# Code to take multiple ASCII art .csv files and convert into workable data format in single .csv file
with open(f'{full_file}\\FullDataset.csv', mode='w', newline='') as f:
    fieldnames = ['temperatureC', 'latitude', 'longitude', 'month', 'year']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for file in infile_path.iterdir():
        with open(f'{file}', mode='r') as g:
            row_id = 0
            latitude = 90
            reader = csv.reader(g)
            for row in reader:
                row_id += 1
                if row_id >= 7:
                    longitude = -180
                    latitude -= 1
                    for temp in row:
                        longitude += 1
                        if float(temp) > -800:
                            writer.writerow(
                                {
                                    'temperatureC': float(temp),
                                    'latitude': latitude, 'longitude': longitude,
                                    'month': file_dater(file.name)[0], 'year': file_dater(file.name)[1]
                                })

