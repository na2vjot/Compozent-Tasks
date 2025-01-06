#C- File Handling

def count_words(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input:
            content = input.read()

        words = content.split()
        word_count = len(words)

        with open(output_file_path, 'w') as output:
            output.write(f'The file "{input_file_path}" contains {word_count} words.')

        print(f"Word count successfully written to {output_file_path}.")

    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = 'D:\My Data\Desktop\Compozent\Python Tasks\File Handling\input.txt'  
output_file = 'output.txt'  
count_words(input_file, output_file)
