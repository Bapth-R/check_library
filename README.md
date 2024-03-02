# Requirements Checker

This is a python3 program that checks if the libraries in the requirements file are up to date.

## Usage

This script is uploaded on the https://pypi.org website at the url : https://pypi.org/project/check-library. 
To use this script and check and update your libraries, you are to install the pip library using this command : `pip3 install check-library`.

After this installation, you will have to run this command to execute the scirpt and get the help:
```shell
check-library --help
```
It will give you all specification needed : 

```txt
usage: check_library [-h] [-p FILE] [-v] [-f]

Check if the libraries in the requirements.txt file are up to date

optional arguments:
  -h, --help              show this help message and exit
  -p FILE, --path FILE    Path of the requirements file
  -o FILE, --output FILE  Output path of the new requirements file
  -v, --verbose           Display additional information
  -f, --force             Overwrite the requirements file
```

- `check-library`   
We can see that we can use the script with no option. It will take the `requirements.txt` at the same location as your current path, check the libraries and create an other file `requirements-output.txt` which will be the older file updated.

- `check-library -p Lib/requirements.txt` or `check-library --path Lib/requirements.txt`   
It will take the `requirements.txt` at the same location Lib/, check the libraries and create an other file `requirements-output.txt` which will be the older file updated at the same location as your current path with the default name(requirements-output.txt).

- `check-library -p Lib/requirements.txt -o updated_requirements.txt`   
It will take the `requirements.txt` at the same location Lib/, check the libraries and create an other file `requirements-updated_requirements.txt` which will be the older file updated at the same location as your current path with the `updated_requirements.txt`.

- `check-library -p Lib/requirements.txt -v -f`      
Thoses 2 news options allowig the scrit:
    - -v : The verbose (default) False. To set it as True, just put the -v at the end of yours queries.
    - -f : It will erase the input file to put new libraries inside. 


