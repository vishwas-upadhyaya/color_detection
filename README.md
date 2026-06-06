# Real-Time Interactive Color Detection with OpenCV

## Project Overview
This repository contains a high-precision, interactive **Color Detection** application designed to identify exact color names and their RGB values from any image. By combining low-level image processing with a comprehensive color dataset, the project provides a seamless "point-and-click" interface for digital color identification.

## What is this Project?
The application serves as a digital color-picker with several advanced features:
- **Interactive Identification:** Users can double-click anywhere on an image to instantly retrieve the color name and its RGB components.
- **Dynamic Dataset Matching:** Cross-references pixel data against a dataset of over 800+ named colors.
- **Adaptive UI:** Automatically adjusts the visibility of text overlays based on the brightness of the detected color to ensure readability.

## How it was done (Deep Technical Details)
- **Computer Vision Framework:** Built using **OpenCV** (`cv2`) for image rendering, window management, and event handling.
- **Interactive Event Pipeline:**
    - **Event Capture:** Utilizes `cv2.setMouseCallback` with the `EVENT_LBUTTONDBLCLK` flag to capture precise (x, y) coordinates of user clicks.
    - **Pixel Extraction:** Directly accesses the image's NumPy array at the clicked coordinates to extract **BGR** (Blue, Green, Red) values.
- **Color Matching Algorithm:**
    - **Distance Metric:** Implements a **Manhattan distance** calculation to find the closest match in the color space:
      $Distance = |R - R_{dataset}| + |G - G_{dataset}| + |B - B_{dataset}|$
    - **Efficiency:** Iterates through a pre-loaded Pandas DataFrame containing 865 color records to find the global minimum distance.
- **User Interface Implementation:**
    - **Dynamic Overlays:** Uses `cv2.rectangle` to create a live color swatch and `cv2.putText` to display metadata (Color Name, R, G, B).
    - **Adaptive Contrast:** Includes logic to switch text color between black and white based on the sum of RGB values ($R+G+B \geq 600$), ensuring the information is always legible against different backgrounds.

## Why it was done
- To explore the integration of interactive event handling with real-time image processing in OpenCV.
- To implement a practical tool for designers and developers to identify colors in digital assets.
- To demonstrate proficiency in NumPy array manipulation and Pandas-based data matching.

## Tech Stack
- **Language:** Python
- **Computer Vision:** OpenCV (`cv2`)
- **Data Engineering:** Pandas, NumPy
- **Dataset:** `colo.csv` (865 named colors with Hex and RGB values)

## Key Features
- **Instant Response:** Sub-millisecond color matching.
- **Broad Coverage:** Supports a wide array of specific color names beyond standard primaries.
- **User-Friendly:** Simple, intuitive interaction via window-based GUI.

## File Structure
- `color_detect.py`: The main entry point for the interactive application.
- `color_detection.ipynb`: Research notebook documenting the algorithm development and data exploration.
- `colo.csv`: The core dataset for color name mapping.
- `input_cat1.jpg` & `onmove.jpg`: Sample images for testing.

## Local Setup
1.  **Clone the repository:**
    ```bash
    git clone [repository-url]
    ```
2.  **Install dependencies:**
    ```bash
    pip install opencv-python pandas numpy
    ```
3.  **Run the application:**
    ```bash
    python color_detect.py
    ```
4.  **How to use:** Double-click on any part of the image to see the color name and values. Press 'ESC' to exit.
