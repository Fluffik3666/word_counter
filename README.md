# Word Counter

Simple Python utility to count words in a string with logging capabilities.

## Installation

```bash
git clone https://github.com/Elite230/word_counter.git
cd word_counter
```

## Usage

Run the counter with a string:
```bash
python run.py "your string here"
```

With custom log level:
```bash
python run.py "your string here" --log-level DEBUG
```

Available log levels:
- DEBUG
- INFO (default)
- WARNING
- ERROR
- CRITICAL

## Testing

Run tests:
```bash
python -m unittest tests.py -v
```

## Examples

Count words in simple string:
```bash
python run.py "hello world"
# Output: The number of words in the string is 2
```

Count with multiple spaces:
```bash
python run.py "hello    world   test"
# Output: The number of words in the string is 3
```

## Logging

Logs are stored in `logs/` directory with timestamp:
- Format: `word_counter_YYYYMMDD_HHMMSS.log`
- Contains both file and console output
- Configurable log level via CLI argument
```