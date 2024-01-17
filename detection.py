def read_sensitive_keywords(filename):
    try:
        with open(filename, "r") as keywords_file:
            keywords = [line.strip() for line in keywords_file.readlines()]
        return keywords
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []


def check_sensitive_data(result_text, sensitive_keywords):
    detected_keywords = []

    for keyword in sensitive_keywords:
        if keyword.lower() in result_text.lower():
            detected_keywords.append(keyword)

    return detected_keywords


def write_detected_keywords(detected_keywords, output_filename):
    try:
        with open(output_filename, "w") as output_file:
            for keyword in detected_keywords:
                output_file.write(f"{keyword}\n")
        print(f"Detected sensitive keywords written to {output_filename}")
    except IOError as e:
        print(f"Error writing to {output_filename}: {e}")
