# Directory
Use these to jump to other sections.

[Introduction](#introduction)  
[Project Introduction](#project-introduction)   
[Data Formatting process](#formatting-the-data)   
[Visualizations](#visualisations)  
[Python Script](#python-script)

---

### Introduction
The purpose for this project is simple: I am bad at interviews. Questions like "How would you do this task?" or "Can 
you describe a time where you...?" always stump me. I mostly do things intuitively, so the actual process tends to 
quickly be forgotten until I have to actually do it again, where it easily comes back to me. Can I describe a time? No.
That doesn't mean there wasn't a time, nor does it mean that, if a similar task is necessary in the future, I won't be 
able to do it. I just struggle at quickly thinking of a time where I did a specific thing, and if I don't have the data
in front of me, I struggle to explain how I would go about doing various tasks with the data. This project is meant to 
show potential employers that, despite the horrid interview, I am, in fact, a highly capable individual.   

[Return to Directory](#directory)

### Project Introduction
The idea behind this project was to take some openly available data, do some stuff in some software, and make a 
visualization for it. The data I chose was from data.nasa.gov. I skimmed through the titles for various datasets until 
I stumbled upon 
["ISLSCP II Sea Surface Temperature"](https://data.nasa.gov/dataset/islscp-ii-sea-surface-temperature-f12a2). Opening 
the link, I found a few files under the "Data and Resources" section. After poking around a bit, I downloaded the top 
file, labeled "Unnamed Resource" with an icon with the word "DATA" at the top of it. Here, there was a link that took 
me to a map with various tools and windows on the left-hand side. Clicking the item with the name of the dataset, I was 
presented with three datasets: Monthly, Weekly, and another, which may represent the average temp for each month for the 
whole of the dataset timeframe. The third set wouldn't provide much information for how the temperatures changed 
throughout the years, and the Weekly set would provide more data than necessary, so the Monthly set was chosen.  

[Return to Directory](#directory)

### Formatting the Data
Extracting the .zip file gave me dozens of files with names in the format of "sst_oiv2_1d_YYYYMM00.asc". YYYY is the 
year, MM is the month, and the 00 at the end of each filename was likely the week. I had never handled .asc files 
before, so I wasn't sure what program to open them in. After opening LibreOffice Calc, I was able to open the first 
file in the directory, representing data from January 1986. Opening the file brought up a window asking me how to 
import the data, specifically what delimiters the file used. The small preview showed that data points were separated 
by spaces, so the space delimiter was checked. The file was imported into Calc.  

The first six rows were dedicated to metadata: ncols: 360, nrows: 180, xllcorner: -180, yllcorner: -90, cellsize: 1, 
NODATA_value: -99. 360 columns, 180 rows, the first cell contains the coordinate -180, 90, each cell contains 1 data 
point, and if no data is available for a point, the value is listed as -90. The actual data was in quite an interesting 
format. It's just a bunch of numbers, with many of them being -888.8. 
![img.png](Images%2Fimg.png)
Zooming out painted a better picture of what was going on.
![img_1.png](Images%2Fimg_1.png)
Every point with -888.8 was for landmass coordinates. Since the dataset is for ocean temperatures, coordinates 
corresponding to land can have absurd numbers, and using -888.8 creates a boundary between ocean and land points. The 
dataset is an ASCII art map of the world, and since longer numbers create less whitespace in a cell, higher temperatures
correspond to darker areas. Unfortunately, this data is not very usable outside of being cool, so the first step I would
have to take would be to convert this data into something usable.  

After saving the file as a .csv file, I opened it in Power BI. This is how I knew I would need to format: I couldn't 
really do anything with the data like this. I created a quick python script that looked through each column and row in 
the original file and wrote that data point in a new line in another file. The script also calculated the coordinate 
data by starting latitude and longitude at 90, -180 and subtracting 1 from latitude for each row and adding 1 to 
longitude for each column. When the data point was over land, every cell with -888.8, the value would be ignored and 
would not be added to the new .csv file. Once the program finished, I verified the resulting .csv file to ensure that 
the code worked properly.  

I then had the brilliant idea to open every .asc file in Calc and use a mouse macro to save each individually as a .csv 
file. This crashed Calc, and I had to restart my computer to reopen it. I then searched online for .asc to .csv 
converters, and found one that couldn't convert files to .csv, so I immediately gave up on that idea. I looked up how 
to open .asc files in python, thinking I would need a specific library like with csv or json files to do what I wanted. 
It turns out you can just open them. So I wrote some more code to open each .asc file and write the data into a .csv 
file. I could have probably incorporated this new code into my other code to do everything in one step, but 
rewriting my code likely would have taken longer than just adding more, and if I wanted to change something in the 
second step, I could comment out the first step and avoid having the code rerun everything.  

I then added a function that would take the YYYYMM00 part of the filename and return the year and month separately. I 
wrote the function to map the month number to a name, which probably wasn't a good idea, since later I had to create a 
new field in Tableau that took the month sting and output an int. The original reformatting code was then slightly 
reworked to take multiple .csv files and output one .csv file that contained all of the data. I couldn't open the file 
in Calc or Excel since it surpassed the row limit, so I imported it into Microsoft SQL Server Management Studio.  

And I started noticing some problems. After importing, many data points were NULL, specifically in the temp and 
latitude columns. Noe NULLs anywhere else. After looking through the code, rerunning it, changing small parts and 
rerunning again, I realized I had "Use Rich Data Type Detection" checked while importing into MSSMS. Unchecking that 
solved the NULLs problem. From there, I did a few basic SQL queries to verify that the data was what one would expect. 
Check number of rows and time to query full dataset (5,147,520 rows in 38 seconds) using basic SELECT * query, check 
for NULL values in any column, check top and bottom temperatures to make sure there weren't any absurd outliers (ocean 
temp can get below 0C due to currents, salts, and other factors, so a minimum temp of -1.8C isn't absurd), and 
checked for duplicates. The data seemed to have been properly transformed from .asc to .csv and formatted to a usable 
format.  

[Return to Directory](#directory)

### Visualisations
The visualisations for this project can be found on my 
[Tableau Public profile](https://public.tableau.com/app/profile/joshua.mcclintic/viz/OceanTempC1986-1995/Dashboard1). 
The first is a colored heat map showing ocean temps on a blue-red scale. On the right is a slider that can be used to 
filter for specific years. On the bottom left is a map showing the average global temperature for each year. On the 
right is a slider that allows for filtering through different latitudes. Finally, there is a bar chart showing the 
average global temperature for each month. This can also be filtered by year or years. The visualisations were not 
meant to be complex, just something to show cap off the project.  

[Return to Directory](#directory)

### Python Script
The script imports csv and pathlib first. From there, the `infile_path`, the directory with the asc files, and 
`outfile_path`, the path to write the new csv files, are created. Next, in a for loop, the code opens the folder by 
`infile_path`, and for each file, writes the data into a csv file, with ' ' (spaces) as the delimiter. `infile_path` 
is recreated with the folder containing the new .csv files. The function `file_dater` is defined: take the filename 
'file_name_YYYYMM00.csv', split the string by '_' ~~and return a list [YYYY, 'month_name'].~~ Function now outputs 
the list [YYYY, month] where month is numeric. This change caused some issues when reimporting the dataset into SQL, 
since the month field was automatically being assigned as NVARCHAR(50), but ensuring the field was of type INT solved 
the issue.

The filepath for the final dataset is instantiated. The final block of code converts the ASCII art .csv files into a 
usable dataset. It opens the FullDataset.csv file with `mode='w'` to create the final file. The `fieldnames` and `writer` 
variables are created to write to the new .csv file. `writer.writeheader()` is used the same as `DROP TABLE IF EXISTS` 
in SQL. The .csv file directory is opened, and, for each file: instantiate `row_id`, `latitude`, and 
`reader`. `row_id` is used to easily determine the row number code-wise. The first few rows of each file is 
unimportant. After, check the `row_id` to ensure that the row number is above where the unimportant data ends. If so, 
instantiate `longitude` and subtract 1 from `latitude`. For each point in each row, increase `longitude` by 1. If 
the data point does not represent land, add the temp, latitude and longitude, and the month and year, gotten from the 
filename.  

[Return to Directory](#directory)
