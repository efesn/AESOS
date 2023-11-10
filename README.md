# Automated Error Searcher on StackOverFlow(AESOS)

The goal of the Automated Error Searcher on StackOverFlow (AESOS) is to save time for
programmers by quickly and efficiently finding solutions to programming errors on StackOverFlow.
By automating the search process, programmers can avoid the time-consuming task of manually
searching for solutions to their errors on the internet.

AESOS will automatically detect errors from given code file (might be any programming language),
open a browser and search for related pages on stackoverflow by using Stack Exchange API
including syntax errors, runtime errors, logical errors etc.

<img src="https://imgur.com/3u5gZuP.png" width="600" height="500">

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)


## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/efesn/AESOS.git
2. Navigate to the project directory:
   ```bash
    cd AESOS
3. Install the required dependencies:
   ```bash
    pip install -r requirements.txt

## Configuration
Just put your main file path to line 52 of app.py

## Usage
1. Ensure that you have Python installed on your system.

2. Run the app.py script:
   ```bash
   python app.py
This will execute AESOS, which will detect errors in the provided file and open a browser to search for related solutions on StackOverflow.

