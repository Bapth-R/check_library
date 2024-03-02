# Requirements Checker

This is a Python 3 program that checks if the libraries in the requirements file are up to date.

## Usage

This script is uploaded to the https://pypi.org website at the URL: https://pypi.org/project/check-library. To use this script and check/update your libraries, you need to install the pip library using the following command: `pip3 install check-library`.

After installation, run the following command to execute the script and get help:

```shell
check-library --help
```
It will provide you with all the necessary specifications:

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
You can use the script with no options. It will take the `requirements.txt` file at the same location as your current path, check the libraries, and create another file `requirements-output.txt` as the updated version.

- `check-library -p Lib/requirements.txt` or `check-library --path Lib/requirements.txt`   
In this example, it will take the `requirements.txt` file located in Lib/, check the libraries, and create another file `requirements-output.txt` at the same location as your current path with the default name (requirements-output.txt).

- `check-library -p Lib/requirements.txt -o updated_requirements.txt`   
In this example, it will take the `requirements.txt` file located in Lib/, check the libraries, and create another file `updated_requirements.txt` as the updated version at the same location as your current path.


- `check-library -p Lib/requirements.txt -v -f`      
These two new options allow the script:
  - -v: Verbose (default: False). To set it as True, simply add -v at the end of your queries.
  - -f: Erases the input file to include new libraries inside.

