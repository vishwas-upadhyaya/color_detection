# color_detection

## Project Overview
An application designed to detect and identify colors within an image.

## What is this Project?
This project provides a script and a Jupyter notebook to read an image, analyze its pixel values, and map those values to human-readable color names using a reference dataset.

## How it was done
Implemented in Python, it uses OpenCV for image processing and Pandas to handle the color dataset (`colo.csv`). The core logic involves capturing the RGB values of a clicked region in an image and finding the closest matching color in the dataset.

## Why it was done
To demonstrate computer vision techniques, specifically color space manipulation and mapping mathematical representations of colors to familiar names.

## Tech Stack
- Python
- OpenCV
- Pandas
- Jupyter Notebook

## Key Features
- Interactive color detection by clicking on an image.
- Mapping RGB values to specific color names.
- Uses a comprehensive CSV dataset for color reference.

## File Structure
- `color_detect.py`: Main Python script for interactive color detection.
- `color_detection.ipynb`: Jupyter notebook for demonstrating and testing the logic.
- `colo.csv`: Dataset containing color names, hex codes, and RGB values.
- `input_cat1.jpg`, `onmove.jpg`: Sample input images for testing.

## Local Setup (if applicable)
1. Clone the repository.
2. Install required dependencies: `pip install opencv-python pandas`.
3. Run the script: `python color_detect.py -i input_cat1.jpg` (or modify the script to point to a local image).