from process import process_images_in_directory
from detection import read_sensitive_keywords, check_sensitive_data, write_detected_keywords


def main():
    dataset_directory = "dataset"
    result_text = process_images_in_directory(dataset_directory)

    with open("result.txt", "w") as result_file:
        result_file.write(result_text)

    result_filename = "result.txt"
    keywords_filename = "input/sensitive_keywords.txt"
    output_filename = "output/detected_sensitive_keywords.txt"

    # Read sensitive keywords from file
    sensitive_keywords = read_sensitive_keywords(keywords_filename)

    if not sensitive_keywords:
        return

    try:
        with open(result_filename, "r") as result_file:
            result_text = result_file.read()

        detected_keywords = check_sensitive_data(result_text, sensitive_keywords)

        if detected_keywords:

            write_detected_keywords(detected_keywords, output_filename)
            print(f"Sensitive data detected! Keyword: {detected_keywords}")

        else:
            print("No sensitive data found.")

    except FileNotFoundError:
        print(f"Error: {result_filename} not found.")


if __name__ == "__main__":
    main()
