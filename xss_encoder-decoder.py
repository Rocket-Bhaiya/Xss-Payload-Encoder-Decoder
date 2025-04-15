#!/usr/bin/env python3
"""
XSS Payload Encoder/Decoder
A simple CLI tool to encode and decode XSS payloads
"""

import html
import urllib.parse
import sys
import re

def encode_html(payload):
    """Encode HTML entities in a string"""
    return html.escape(payload)

def decode_html(payload):
    """Decode HTML entities in a string"""
    return html.unescape(payload)

def encode_js(payload):
    """Encode a string as JavaScript escape sequences"""
    result = ""
    for char in payload:
        code = ord(char)
        if char == '"' or char == "'" or char == "\\" or code < 32 or code > 126:
            result += f"\\x{code:02x}"
        else:
            result += char
    return result

def encode_url(payload):
    """Encode a string for URL parameters"""
    return urllib.parse.quote(payload)

def decode_url(payload):
    """Decode a URL-encoded string"""
    return urllib.parse.unquote(payload)

def show_menu():
    """Display the menu of available operations"""
    print("\n===== XSS Payload Encoder/Decoder =====")
    print("1. Encode HTML")
    print("2. Decode HTML")
    print("3. Encode JS")
    print("4. Encode URL")
    print("5. Decode URL")
    print("0. Exit")
    return input("Select an option (0-5): ")

def get_payload():
    """Get the payload from the user"""
    print("\nEnter the payload to process (press Ctrl+D or enter 'EOF' on a new line to finish):")
    lines = []
    try:
        while True:
            line = input()
            if line == 'EOF':
                break
            lines.append(line)
    except EOFError:
        pass
    
    return '\n'.join(lines)

def main():
    """Main function to run the CLI"""
    while True:
        choice = show_menu()
        
        if choice == '0':
            print("Exiting. Goodbye!")
            sys.exit(0)
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid option. Please try again.")
            continue
            
        payload = get_payload()
        result = ""
        
        if choice == '1':
            result = encode_html(payload)
            print("\nHTML Encoded Result:")
        elif choice == '2':
            result = decode_html(payload)
            print("\nHTML Decoded Result:")
        elif choice == '3':
            result = encode_js(payload)
            print("\nJavaScript Escape Encoded Result:")
        elif choice == '4':
            result = encode_url(payload)
            print("\nURL Encoded Result:")
        elif choice == '5':
            result = decode_url(payload)
            print("\nURL Decoded Result:")
            
        print(result)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting due to user interrupt. Goodbye!")
        sys.exit(0)