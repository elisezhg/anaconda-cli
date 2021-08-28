@ECHO OFF
FOR /f %%p in ('where anaconda') do SET "SCRIPTPATH=%%p\..\anaconda-cli\main.py"
python %SCRIPTPATH%
