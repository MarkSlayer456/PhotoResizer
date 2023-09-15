# Photo Resizer
A simple script to mass resize photos in a directory. This program does not delete the orignals
it simply makes a new folder in the directory and stores the newly sized photos in it

## Requirements
- Python 3
- Pillow for python `pip install pillow`

## Usage
python3 main.py <width in pixels> <height in pixels> <directory with photos>

## Examples
`python3 main.py 100 100 .`

this would take every picture in the current directory and resize it! 
