# BookBot

A Python command-line tool for analyzing text files and generating detailed statistics about word counts and character frequency distributions.

## Features

- **Word Count Analysis**: Get the total number of words in any text file
- **Character Frequency Analysis**: See how often each alphabetic character appears
- **Sorted Results**: Character counts are automatically sorted from most to least frequent
- **Clean Report Format**: Easy-to-read output with clear sections

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tyrannikal/bookbot.git
cd bookbot
```

2. Ensure you have Python 3 installed:
```bash
python3 --version
```

No additional dependencies are required - BookBot uses only Python standard library modules.

## Usage

Run BookBot by providing the path to a text file you want to analyze:

```bash
python3 main.py <path_to_book>
```

### Example

Analyze one of the included sample books:

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output

```
============= BOOKBOT =============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20818
h: 19725
...
============== END ================
```

## Project Structure

```
bookbot/
├── main.py              # Entry point and report generation
├── stats.py             # Text analysis functions
├── books/               # Sample text files
│   ├── frankenstein.txt
│   ├── prideandprejudice.txt
│   └── mobydick.txt
└── README.md
```

## How It Works

1. **Text Reading**: Opens and reads the specified text file
2. **Word Counting**: Splits the text into words and counts them
3. **Character Analysis**: Iterates through each character, converts to lowercase, and tallies alphabetic characters only
4. **Report Generation**: Sorts characters by frequency and generates a formatted report

## Sample Books

This repository includes three classic literature texts for testing:
- **Frankenstein** by Mary Shelley
- **Pride and Prejudice** by Jane Austen
- **Moby Dick** by Herman Melville

You can analyze any text file by providing its path as an argument.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available for educational purposes.
