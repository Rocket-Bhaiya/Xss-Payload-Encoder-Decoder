# XSS Payload Encoder/Decoder

A simple command-line tool for encoding and decoding XSS (Cross-Site Scripting) payloads.

## Features

- HTML Entity Encoding and Decoding (e.g., `<` to `&lt;`)
- JavaScript Escape Encoding (e.g., `"` to `\x22`)
- URL Encoding and Decoding (e.g., `<script>` to `%3Cscript%3E`)
- Interactive CLI menu for easy use

## Installation

No additional dependencies are required. The tool uses only built-in Python libraries.

```bash
# Clone or download the repository
# Make the script executable
chmod +x xss_encoder-decoder.py
```

## Usage

Run the script from the command line:

```bash
./xss_encoder-decoder.py
```

### Menu Options

1. **Encode HTML** - Convert special characters to HTML entities
2. **Decode HTML** - Convert HTML entities back to characters
3. **Encode JS** - Convert characters to JavaScript escape sequences
4. **Encode URL** - URL-encode a string
5. **Decode URL** - URL-decode a string
0. **Exit** - Quit the application

### Input Method

When prompted, enter your payload. You can enter multi-line input.
To finish input, press `Ctrl+D` or type `EOF` on a new line.

## Examples

### HTML Encoding

Input:
```
<script>alert('XSS')</script>
```

Output:
```
&lt;script&gt;alert(&#x27;XSS&#x27;)&lt;/script&gt;
```

### JavaScript Escape Encoding

Input:
```
<script>alert("XSS")</script>
```

Output:
```
\x3cscript\x3ealert(\x22XSS\x22)\x3c/script\x3e
```

### URL Encoding

Input:
```
<script>alert(1)</script>
```

Output:
```
%3Cscript%3Ealert%281%29%3C/script%3E
```

## Why This Tool?

This tool is useful for security professionals, penetration testers, and developers who need to quickly transform XSS payloads for testing web application security.

## License

Open source - feel free to modify and distribute.