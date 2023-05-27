# README

This is a simple Python script that uses the WordsAPI to retrieve synonyms of a given word. It prompts the user to enter a word and then displays its synonyms.

## Prerequisites

To run this script, you need to have Python installed on your system. You also need to install the `requests` library, which can be done using the following command:

```
pip install requests
```

## Usage

1. Clone this repository or download the script file.

2. Open the script in a text editor or an IDE of your choice.

3. Replace the placeholder value with your actual RapidAPI key in the `headers` dictionary. You can obtain a RapidAPI key by signing up on the RapidAPI website and subscribing to the WordsAPI.

4. Save the script.

5. Open a terminal or command prompt and navigate to the directory where the script is located.

6. Run the script by executing the following command:

```
python test.py
```

7. You will be prompted to enter a word. Type the word and press Enter.

8. The script will make a request to the WordsAPI and display the synonyms of the entered word.

## Limitations

Please note that this script has the following limitations:

- It assumes that you have a valid RapidAPI key and sufficient credits to make requests to the WordsAPI.

- It relies on an external API, and the availability and response of the API are subject to its uptime and any rate limits imposed by the API provider.

- The script may not handle errors or exceptions that can occur during the API request. It assumes a successful response from the API.

- The script does not perform any input validation or error handling for the user input. It expects a valid word to be entered.
