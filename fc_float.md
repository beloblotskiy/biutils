# Introduction #

Compare two text files which contain several tab-separated columns with float numbers.

The comparison based on maximum delta between two non-precise numbers which is calculated based on FLOAT\_MAX\_PRECISION\_DIGITS constant.


## Details ##

Strings "NULL" treated as empty strings.

Process Exit code is 0 if no differences and 1 if there are some differences.

Usage: provide two command line arguments - paths for files for comparison.

### Demo ###
Suppose a.txt is a result of saving query result with "Save as..." in SQL Server Management Studio and b.txt is query result exported into tab-separated text file with sqlplus.

Compare these files (the information in both is imprecise - all these numbers are floats).

```
> python fc_float.py a.txt b.txt
Comparing a.txt and b.txt...
Float numbers in two files are identical (float precision is 15 digits).
```

a.txt
```
1.0	NULL	0.0
		123.4567
0.9	NULL	0
```

b.txt _(three columns are here but tabs mixed with spaces)_
```
0.99999999999999		-0.000000000000001
		                  123.456699999999
0.89999999999999		             0.000
```

## Unload data ##

Unload data into text files.

### Oracle ###
Save query result in tab-separated text file:

```
sqlplus user_account/password_is_here@serv_host:1521/instance @query.sql
```

```
col TAB# new_value TAB NOPRINT
select chr(9) TAB# from dual;
set colsep "&TAB"

set feedback off
set term off
set linesize 4000
--set colsep ,
--set colsep '","'
set trimspool on
set underline off
set heading off
--set headsep $
set newpage none

spool "b.txt"

select 1.0
from dual;

spool off
```

### SQL Server ###
```
SQL Server: sqlcmd -S serv_host -U user_login -P password_is_here -i query.sql -o res.txt -h-1
```

```
set nocount on;

select 1.0
```