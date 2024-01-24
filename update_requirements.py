# To get an updated requirements.txt file, 
# pip freeze > requirements_not_updated.in
# python update_requirements.py
# pip install -r requirements.txt


# update_requirements.py

def update_requirements(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = [line.strip() for line in infile if 'file://' not in line]

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(lines))

if __name__ == '__main__':
    input_file = 'requirements_not_updated.in'
    output_file = 'requirements.txt'
    update_requirements(input_file, output_file)
