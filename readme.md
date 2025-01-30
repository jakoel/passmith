# PassSmith

## Description
PassSmith Tool is a Python script designed to generate custom wordlists for security testing purposes and employee education. It creates permutations and combinations of user-provided personal information to produce a comprehensive list of potential passwords.

## Features
- Interactive input for personal information
- Generates permutations and combinations of input data
- Applies various case modifications (lowercase, uppercase, title case)
- Adds common number suffixes/prefixes
- Saves the generated wordlist to a text file

## Usage
1. Edit 'extensions' list with your favorite prefixes and postfixes
2. Run `python passmith.py`
3. Enter requested personal information when prompted
4. The wordlist will be saved as `[First_Name]_words_list.txt`

## Important Notes
- This tool is intended for ethical security testing and password strength assessment only.
- Always obtain proper authorization before using generated wordlists for any security testing.
- The quality and effectiveness of the generated wordlist depend on the accuracy and completeness of the input information.
- The script may generate a large number of words, which could result in a sizable output file.

## Limitations
- The maximum complexity for permutations is set to 3 fields to manage computational resources.
- The script does not include advanced password creation rules or patterns.

## Future Improvements
- Add support for custom rules and patterns
- Implement more sophisticated permutation algorithms
- Include options for importing existing wordlists
- Add progress indicators for large dictionary generations

## Disclaimer
This tool is provided for educational and ethical testing purposes only. The authors and contributors are not responsible for any misuse or illegal activities conducted with this tool.
