# SSE Live
This Qlik Sense SSE shows how it is possible to create hypercubes on the fly completely based off live SQL queries to any ODBC data source. 
**Please note that this is a very early beta innovation project not meant for production use!**

## SSE Installation Steps
First ensure you have followed Daniel Pilla's python environment setup found [here](https://s3.amazonaws.com/dpi-sse/DPI+-+Qlik+Sense+AAI+and+Python+Environment+Setup.pdf)

1. Create a new folder called Live  ```mkdir Live ```
2. Copy the contents of the following ZIP into the folder created in step 2: [QlikSenseAAILive.zip](https://github.com/rileymd88/QlikSenseAAILive/archive/master.zip)
3. Open a command prompt and create a new virtual environment called Live  ```mkvirtualenv Live ```
4. Ensure you are in the directory of the folder created in step two and type the following command  ```setprojectdir . ```
5. Enter the following command  ```pip install -r requirements.txt ```
6. Create the analytic connection with the following properties:
 ```
Name: PythonLive
Host: localhost
Port: 50099
 ```    
7. Import the following app into Qlik Sense: [Live Native.qvf](https://github.com/rileymd88/data/raw/master/QlikSenseAAILive/Live%20Native.qvf)
8. Start the analytic connection by starting a new command prompt and entering  ```workon Live ``` and then  ```python __main__.py ```

## Setting Up The ODBC Connection Needed to Work With The Sample App
You will need to first set up the ODBC connection to use the SSE with the sample app:

1. Download the AdventureWorks2017 SQL database from here https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorks2017.bak
2. Import the SQL database using SQL Server Management Studio https://stackoverflow.com/questions/1535914/import-bak-file-to-a-database-in-sql-server
3. Create an ODBC Connection:

Once the ODBC connection is created the sample app which you can download [here](https://s3.amazonaws.com/dpi-sse/DPI+-+Qlik+Sense+AAI+and+Python+Environment+Setup.pdf) should work after starting the analytic connection

![1](https://raw.githubusercontent.com/rileymd88/data/master/QlikSenseAAILive/odbc1.png)
![2](https://raw.githubusercontent.com/rileymd88/data/master/QlikSenseAAILive/odbc2.png)
![3](https://raw.githubusercontent.com/rileymd88/data/master/QlikSenseAAILive/odbc3.png)
![4](https://raw.githubusercontent.com/rileymd88/data/master/QlikSenseAAILive/odbc4.png)

## Formula Parameters
It is of course possible to use this SSE with any ODBC connection, you simply need to change the formulas/variables in the app:
![Formula](https://raw.githubusercontent.com/rileymd88/data/master/QlikSenseAAILive/formula.png)

* **SQL Statement:** This should be an SQL query
* **Column From SQL:** This is the column number you want to have returned from the SQL query table result (starts at 0 for the first column)
* **pyodbc Connection String:** This is the connection string needed to connect to the specific ODBC database. pyodbc simply forwards the connection string to the specific driver for each ODBC connection. For more information on connection string formats you can refer to the link here: https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-databases
* **Index Field Name:** This is the dummy index field name as a string. The dummy index field is needed in order for the pick functions to work properly and should be auto-generated in the script