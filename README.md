# img-scanner

This Python project is an image scanner that performs sensitive keyword scanning on visual files and reports the detected data.

## Installation

1. If Python is not installed, [Download and Install Python](https://www.python.org/downloads/).
2. Install the required libraries by running the following command in your terminal/cmd:
    ```
    pip install opencv-python pytesseract
    ```

## Usage

1. To process visual files in the `dataset` directory:
    ```bash
    python main.py
    ```

2. To check the results using sensitive keywords from the `input/sensitive_keywords.txt` file:
    ```bash
    python main.py
    ```

## Project Structure

- `dataset/`: Directory containing image files.
- `input/sensitive_keywords.txt`: File containing sensitive keywords.
- `output/detected_sensitive_keywords.txt`: File reporting detected sensitive keywords.
- `process.py`: Python module performing image processing operations.
- `detection.py`: Python module performing sensitive keyword scanning operations.
- `main.py`: Main execution file of the project.

## Development

- While working on the project, you can modify the image processing and sensitive keyword scanning algorithms by editing the `process.py` and `detection.py` files.
- If needed, you can expand the project by adding new features.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

