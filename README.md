# Codeforces C++ Template Generator

This repository contains a Python script to generate a simple C++ template for competitive programming tasks, specifically for Codeforces problems. The template includes basic I/O management and utility functions to streamline problem-solving.

## Description

The script creates a new .cpp file with boilerplate code that:

Sets up fast input/output

Provides common type aliases (e.g., ll, pii, vi)

**Allows reading from in.txt and writing to out.txt** if arguments are passed during execution

## Usage

### Generating a C++ Template

Run the Python script to generate a new .cpp file:

```
$ python3 main.py
Enter the task name: A_plus_B
File 'A_plus_B.cpp' was successfully created!
```

This will create a file named hello_cf.cpp with the C++ template.

Example Compilation and Execution

After generating the C++ file, compile and run it with the following commands:

## Compile the C++ file

```
$ g++ -o hello_cf hello_cf.cpp -std=c++17
```


## Run the executable

```
$ ./hello_cf < in.txt > out.txt

-o A_plus_B specifies the output executable name.

-std=c++17 ensures compatibility with C++17.
```

Input is read from in.txt and output is written to out.txt.

## How It Works

File Redirection: If the C++ program is run with command-line arguments (e.g., ./A_plus_B 1), the program redirects input from in.txt and output to out.txt.

Without Arguments: Standard input and output are used (ideal for local testing).

## Why Use This?

Saves time by automating the creation of a consistent starting point for each problem.

Includes fast I/O setup, common types, and utility functions.

## Requirements

Python 3.x

```
g++ (GNU C++ Compiler)
```

Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features!

License

This project is licensed under the MIT License.
