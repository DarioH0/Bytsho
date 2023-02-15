import os

def process_file(file_name):
    file_base, file_ext = os.path.splitext(file_name)
    if file_ext != '.bytsho':
        print('Starting binary compression...')

        with open(file_name, 'rb') as f:
            content = f.read()

        binary_content = ''.join(format(byte, '08b') for byte in content)
        count = 0

        while True:
            new_content = binary_content.replace('10', '1').replace('01', '0')
            if new_content == binary_content:
                break
            binary_content = new_content
            count += 1

        with open(file_base + '.bytsho', 'w') as f:
            f.write(binary_content[-1] + '\n')
            f.write(str(count) + '\n')
            f.write(file_name + '\n')

    else:
        print('reverse process coming soon :(')

file_name = input('File: ')
process_file(file_name)

